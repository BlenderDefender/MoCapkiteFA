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
    Menu,
    UILayout
)

from .operators import (
    MOCAPKITEFA_OT_facial_mocap,
    MOCAPKITEFA_OT_pre_align
)


# The following menu appears in the "Add" menu and contains the "MOCAPKITEFA_OT_facial_mocap" Operator
class MOCAPKITEFA_MT_main_menu(Menu):
    bl_idname = 'mocapkitefa.menu'
    bl_label = 'Motion Capture'

    def draw(self, context: 'Context'):
        layout: UILayout = self.layout
        layout.operator(MOCAPKITEFA_OT_pre_align.bl_idname, icon='PLUS')
        layout.operator(MOCAPKITEFA_OT_facial_mocap.bl_idname, icon='SHADERFX')


def menu_func(self, context: 'Context'):
    self.layout.menu(MOCAPKITEFA_MT_main_menu.bl_idname)


classes = (
    MOCAPKITEFA_MT_main_menu,

)


def register():
    bpy.types.VIEW3D_MT_add.append(menu_func)

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    bpy.types.VIEW3D_MT_add.remove(menu_func)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
