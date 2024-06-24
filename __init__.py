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

from . import (
    menus,
    operators,
    prefs,
)

bl_info = {
    "name": "MoCapkiteFA - Face Motion Capture",
    "author": "Blender Defender, CG Matter",
    "version": (1, 0, 2),
    "blender": (2, 82, 0),
    "location": "View3D > Add > Motion Capture > Set up Facial Motion Capture",
    "description": "Turns your Trackers and your head into facial motion capture!",
    "warning": "You might run in trouble with translated Blender versions. Use English version!",
    "doc_url": "https://github.com/BlenderDefender/MoCapkiteFA#mocapkitefa",
    "tracker_url": "https://github.com/BlenderDefender/MoCapkiteFA/issues",
    "endpoint_url": "https://raw.githubusercontent.com/BlenderDefender/BlenderDefender/updater_endpoints/MOCAPKITEFA.json",
    "category": "Animation"
}


def register():
    if bpy.app.version < (4, 2):
        prefs.register_legacy(bl_info)
    else:
        prefs.register()
    operators.register()
    menus.register()


def unregister():
    prefs.unregister()
    menus.unregister()
    operators.unregister()
