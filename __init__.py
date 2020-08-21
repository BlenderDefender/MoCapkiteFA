# ##### BEGIN GPL LICENSE BLOCK #####
#    Copyright (C) <2020>  <CG Matter, Blender Defender>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Face Motion Capture",
    "author": "CG Matter, Blender Defender",
    "version": (1, 0),
    "blender": (2, 82, 0),
    "location": "View3D > Add > Motion Capture > Set up Facial Motion Capture",
    "description": "Turns your Trackers and your head into facial motion capture!",
    "warning": "You might run in trouble with translated Blender versions. Use English version!",
    "wiki_url": "https://github.com/BlenderDefender/MoCapkiteFA#mocapkitefa",
    "tracker_url": "https://github.com/BlenderDefender/MoCapkiteFA/issues",
    "category": "Animation"}


import bpy

# updater ops import, all setup in this file
from . import addon_updater_ops


#The following Operator does the pre-alignment (Minimal changes needed)
class MOCAPKITEFA_OT_pre_align(bpy.types.Operator):
    """Adds a camera and pre aligns it and the Active Object"""
    bl_idname = "mocapkitefa.pre_alignment"
    bl_label = "Pre-Align"
    bl_options = {'REGISTER'}

    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    
    def execute(self, context):
        
        bpy.context.scene.frame_set(1)
        for obj in bpy.context.selected_objects:
            obj.name = "Head"
            obj.data.name = "Head"
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', constraint_axis=(True, False, False))
        
        bpy.ops.object.camera_add(location=(0, 0, 5), rotation=(0, 0, 0))
        bpy.ops.view3d.object_as_camera()
        for obj in bpy.context.selected_objects:
            obj.name = "TopCamMoCap"
            obj.data.name = "TopCamMoCap"
        bpy.ops.object.transform_apply()
        bpy.data.objects['TopCamMoCap'].select_set(False)
        
        bpy.context.area.ui_type = 'CLIP_EDITOR'
        bpy.ops.clip.select_all(action='SELECT')
        bpy.ops.clip.track_to_empty()
        bpy.context.area.ui_type = 'VIEW_3D'
        

        
        return {'FINISHED'}


#The following Operator set's up the motion Capture
class MOCAPKITEFA_OT_facial_mocap(bpy.types.Operator):
    """Setup Motion Capture (Needs Tracker Setup + Active Object)"""
    bl_idname = "mocapkitefa.facial_mocap"
    bl_label = "Set Up Facial Motion Capture"
    bl_options = {'REGISTER'}
    

    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        
        iter = 1
        
        
        #rename trackers
        FaceTrackers = bpy.data.collections.new('FaceTrackers')
        bpy.context.scene.collection.children.link(FaceTrackers)
        for trackers in bpy.data.objects:
           if trackers.type != 'EMPTY':
               continue
           else:
               iter = iter + 1
               FaceTrackers.objects.link(trackers)
        if FaceTrackers:
            for i, o in enumerate(FaceTrackers.objects):
                o.name = "Tracker%d" % (i+1) 

        #face mesh setup
        bpy.context.scene.frame_set(1)
        bpy.ops.object.transform_apply()

        #trackers with depth
        for value in range(1,iter):
            selectname = "Tracker" + str(value)
            ob = bpy.data.objects[selectname]
            bpy.context.view_layer.objects.active = ob
            bpy.context.object.constraints["Follow Track"].depth_object = bpy.data.objects["Head"]

        #add armatures to trackers
        for value in range(1,iter):
            selectname = "Tracker" + str(value)
            ob = bpy.data.objects[selectname]
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.armature_add(enter_editmode=False, location=ob.matrix_world.translation)

        #select armatures
        for bones in bpy.data.objects:
           if bones.type != 'ARMATURE':
               continue
           else:
               bones.select_set(state=True)    

        #join armatures in correct order
        bpy.context.view_layer.objects.active = ob = bpy.data.objects['Armature']
        bpy.ops.object.join()
        bpy.ops.object.transform_apply()    

        #rename bones in armature
        for value in range(1,iter):
            if value == 1:
                bonename = "Bone"
            elif value > 1 and value < 11:
                bonename = "Bone.00" + str(value-1)
            elif value >= 11:
                bonename = "Bone.0" + str(value-1)      
            bone = bpy.data.objects['Armature'].data.bones.get(bonename)
            bpy.data.objects['Armature'].data.bones[bonename].name = 'Bone' + str(value)

        #parent face to bones
        bpy.data.objects['Head'].select_set(True)
        bpy.data.objects['Armature'].select_set(True)
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')

        #parent bones to trackers
        bpy.ops.object.posemode_toggle()
        for value in range(1,iter):
            trackname = "Tracker" + str(value)
            bonename = "Bone" + str(value)
            bone = bpy.data.objects['Armature'].data.bones.get(bonename)
            bpy.data.objects['Armature'].data.bones.active = bone
            bpy.ops.pose.constraint_add(type='COPY_LOCATION')
            bpy.context.object.pose.bones[bonename].constraints["Copy Location"].use_z = False
            bpy.context.object.pose.bones[bonename].constraints["Copy Location"].target = bpy.data.objects[trackname]
            bone.select = False
            
        return {'FINISHED'}


#The following menu appears in the "Add" menu and contains the "MOCAPKITEFA_OT_facial_mocap" Operator
class MOCAPKITEFA_MT_main_menu(bpy.types.Menu):
    bl_idname = 'mocapkitefa.menu'
    bl_label = 'Motion Capture'

    def draw(self, context):
        layout = self.layout
        layout.operator(MOCAPKITEFA_OT_pre_align.bl_idname, icon = 'PLUS')
        layout.operator(MOCAPKITEFA_OT_facial_mocap.bl_idname, icon = 'SHADERFX')
        


def menu_func(self, context):
    self.layout.menu(MOCAPKITEFA_MT_main_menu.bl_idname)


class MOCAPKITEFA_APT_Preferences(bpy.types.AddonPreferences):
	bl_idname = __package__

	# addon updater preferences

	auto_check_update = bpy.props.BoolProperty(
		name="Auto-check for Update",
		description="If enabled, auto-check for updates using an interval",
		default=True,
		)
	updater_intrval_months = bpy.props.IntProperty(
		name='Months',
		description="Number of months between checking for updates",
		default=0,
		min=0
		)
	updater_intrval_days = bpy.props.IntProperty(
		name='Days',
		description="Number of days between checking for updates",
		default=7,
		min=0,
		max=31
		)
	updater_intrval_hours = bpy.props.IntProperty(
		name='Hours',
		description="Number of hours between checking for updates",
		default=0,
		min=0,
		max=23
		)
	updater_intrval_minutes = bpy.props.IntProperty(
		name='Minutes',
		description="Number of minutes between checking for updates",
		default=0,
		min=0,
		max=59
		)

	def draw(self, context):
		layout = self.layout
		# col = layout.column() # works best if a column, or even just self.layout
		mainrow = layout.row()
		col = mainrow.column()

        layout.operator("wm.url_open", text="Checkout Gumroad for other addons and more...", icon='FUND').url="https://gumroad.com/blenderdefender"


		# updater draw function
		# could also pass in col as third arg
		addon_updater_ops.update_settings_ui(self, context)

		# Alternate draw function, which is more condensed and can be
		# placed within an existing draw function. Only contains:
		#   1) check for update/update now buttons
		#   2) toggle for auto-check (interval will be equal to what is set above)
		# addon_updater_ops.update_settings_ui_condensed(self, context, col)

		# Adding another column to help show the above condensed ui as one column
		# col = mainrow.column()
		# col.scale_y = 2
		# col.operator("wm.url_open","Open webpage ").url=addon_updater_ops.updater.website


classes = (
	MOCAPKITEFA_OT_pre_align,
	MOCAPKITEFA_OT_facial_mocap,
	MOCAPKITEFA_MT_main_menu,
	MOCAPKITEFA_APT_Preferences,
	
)


def register():
	# addon updater code and configurations
	# in case of broken version, try to register the updater first
	# so that users can revert back to a working version
	addon_updater_ops.register(bl_info)

	bpy.types.VIEW3D_MT_add.append(menu_func)

	# register the example panel, to show updater buttons
	for cls in classes:
		addon_updater_ops.make_annotations(cls) # to avoid blender 2.8 warnings
		bpy.utils.register_class(cls)


def unregister():
	# addon updater unregister
	addon_updater_ops.unregister()

	bpy.types.VIEW3D_MT_add.remove(menu_func)

	# register the example panel, to show updater buttons
	for cls in reversed(classes):
		bpy.utils.unregister_class(cls)
