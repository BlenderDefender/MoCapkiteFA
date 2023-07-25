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
    AddonPreferences,
    Context,
    UILayout
)
from bpy.props import (
    BoolProperty,
    IntProperty,

)

# updater ops import, all setup in this file
from . import addon_updater_ops


class MOCAPKITEFA_APT_Preferences(AddonPreferences):
    bl_idname = __package__

    # addon updater preferences

    auto_check_update: BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=True,
    )
    updater_intrval_months: IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0
    )
    updater_intrval_days: IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
        max=31
    )
    updater_intrval_hours: IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
    )
    updater_intrval_minutes: IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )

    def draw(self, context: 'Context'):
        layout: UILayout = self.layout

        layout.operator("wm.url_open", text="Checkout Gumroad for other addons and more...",
                        icon='FUND').url = "https://gumroad.com/blenderdefender"

        # updater draw function
        addon_updater_ops.update_settings_ui(self, context)


classes = (
    MOCAPKITEFA_APT_Preferences,
)


def register(bl_info):
    # addon updater code and configurations
    # in case of broken version, try to register the updater first
    # so that users can revert back to a working version
    addon_updater_ops.register(bl_info)

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    addon_updater_ops.unregister()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
