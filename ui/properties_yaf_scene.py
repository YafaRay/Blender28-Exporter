# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import bpy
from ..ot import yafaray_presets
from bl_ui.properties_scene import SceneButtonsPanel
from bpy.types import Panel, Menu

class YAFA_V3_PT_color_management(SceneButtonsPanel, Panel):
    bl_label = "Color Management"
    COMPAT_ENGINES = {'YAFA_V3_RENDER'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        col = layout.column()
        col.label(text="Display:")
        col.prop(scene.display_settings, "display_device")

        if scene.display_settings.display_device == "sRGB":
            pass
        elif scene.display_settings.display_device == "None":
            row = layout.row(align=True)
            row.prop(scene, "gs_gamma", text = "Display device output gamma")
        elif scene.display_settings.display_device == "XYZ":
            row = layout.row(align=True)
            row.label(text="YafaRay 'XYZ' support is experimental and may not give the expected results", icon="ERROR")
        else:
            row = layout.row(align=True)
            row.label(text="YafaRay doesn't support '" + scene.display_settings.display_device + "', assuming sRGB", icon="ERROR")

        col = layout.column()
        col.separator()
        col.label(text="Render:")
        col.template_colormanaged_view_settings(scene, "view_settings")


classes = (
    YAFA_V3_PT_color_management,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

        
if __name__ == "__main__":  # only for live edit.
    import bpy
    bpy.utils.register_module(__name__)
