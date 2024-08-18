# ##### BEGIN GPL LICENSE BLOCK #####
#    Copyright (C) <2020>  <Blender Defender, CG Matter>
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

import bpy
from bpy.types import (
    Context,
    Operator
)


# The following Operator does the pre-alignment (Minimal changes needed)
class MOCAPKITEFA_OT_pre_align(Operator):
    """Adds a camera and pre aligns it and the Active Object"""
    bl_idname = "mocapkitefa.pre_alignment"
    bl_label = "Pre-Align"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context: 'Context'):
        return context.active_object is not None

    def execute(self, context: 'Context'):

        context.scene.frame_set(1)
        for obj in context.selected_objects:
            obj.name = "Head"
            obj.data.name = "Head"
            bpy.ops.transform.rotate(
                value=1.5708, orient_axis='X', orient_type='GLOBAL', constraint_axis=(True, False, False))

        bpy.ops.object.camera_add(location=(0, 0, 5), rotation=(0, 0, 0))
        bpy.ops.view3d.object_as_camera()
        for obj in context.selected_objects:
            obj.name = "TopCamMoCap"
            obj.data.name = "TopCamMoCap"
        bpy.ops.object.transform_apply()
        bpy.data.objects['TopCamMoCap'].select_set(False)

        context.area.ui_type = 'CLIP_EDITOR'
        bpy.ops.clip.select_all(action='SELECT')
        bpy.ops.clip.track_to_empty()
        context.area.ui_type = 'VIEW_3D'

        return {'FINISHED'}


# The following Operator set's up the motion Capture
class MOCAPKITEFA_OT_facial_mocap(Operator):
    """Setup Motion Capture (Needs Tracker Setup + Active Object)"""
    bl_idname = "mocapkitefa.facial_mocap"
    bl_label = "Set Up Facial Motion Capture"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context: 'Context'):
        return context.active_object is not None

    def execute(self, context: 'Context'):

        tracker_count = 1

        # rename trackers
        face_trackers = bpy.data.collections.new('FaceTrackers')
        context.scene.collection.children.link(face_trackers)
        for trackers in bpy.data.objects:
            if trackers.type != 'EMPTY':
                continue

            tracker_count = tracker_count + 1
            face_trackers.objects.link(trackers)

        if face_trackers:
            for i, object in enumerate(face_trackers.objects):
                object.name = f"Tracker{i + 1}"

        # face mesh setup
        context.scene.frame_set(1)
        bpy.ops.object.transform_apply()

        # trackers with depth
        for value in range(1, tracker_count):
            select_name = f"Tracker{value}"
            ob = bpy.data.objects[select_name]
            context.view_layer.objects.active = ob
            context.object.constraints["Follow Track"].depth_object = bpy.data.objects["Head"]

        # add armatures to trackers
        for value in range(1, tracker_count):
            select_name = f"Tracker{value}"
            ob = bpy.data.objects[select_name]
            context.view_layer.objects.active = ob
            bpy.ops.object.armature_add(
                enter_editmode=False, location=ob.matrix_world.translation)

        # select armatures
        for object in bpy.data.objects:
            if object.type != 'ARMATURE':
                continue

            object.select_set(state=True)

        # join armatures in correct order
        context.view_layer.objects.active = ob = bpy.data.objects['Armature']
        bpy.ops.object.join()
        bpy.ops.object.transform_apply()

        # rename bones in armature
        for value in range(1, tracker_count):
            bone_name = "Bone." + "0" * \
                (2 - len(str(value - 1))) + str(value - 1)
            if value == 1:
                bone_name = "Bone"

            bone = bpy.data.objects['Armature'].data.bones.get(bone_name)
            bpy.data.objects['Armature'].data.bones[bone_name].name = f'Bone{value}'

        # parent face to bones
        bpy.data.objects['Head'].select_set(True)
        bpy.data.objects['Armature'].select_set(True)
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')

        # parent bones to trackers
        bpy.ops.object.posemode_toggle()
        for value in range(1, tracker_count):
            tracker_name = f"Tracker{value}"
            bone_name = f"Bone{value}"
            bone = bpy.data.objects['Armature'].data.bones.get(bone_name)
            bpy.data.objects['Armature'].data.bones.active = bone
            bpy.ops.pose.constraint_add(type='COPY_LOCATION')
            context.object.pose.bones[bone_name].constraints["Copy Location"].use_z = False
            context.object.pose.bones[bone_name].constraints["Copy Location"].target = bpy.data.objects[tracker_name]
            bone.select = False

        return {'FINISHED'}


classes = (
    MOCAPKITEFA_OT_pre_align,
    MOCAPKITEFA_OT_facial_mocap,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
