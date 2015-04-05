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
#
# Copyright 2004 (C) GIANTS Software GmbH, Confidential, All Rights Reserved.

bl_info = {
    "name": "GIANTS I3D Exporter Tools",
    "author": "GIANTS Software",
    "blender": ( 2, 7, 0 ),
    "version": ( 5, 5, 0 ),
    "location": "GIANTS I3D",
    "description": "GIANTS Utilities and Exporter",
    "warning": "",
    "wiki_url": "http://gdn.giants-software.com",
    "tracker_url": "http://gdn.giants-software.com",
    "category": "Game Engine"}


if "bpy" in locals():
    import imp
    imp.reload( i3d_UIexport )
else:
    from . import i3d_UIexport

import bpy

#-------------------------------------------------------------------------------
#   I3D Menu Class
#-------------------------------------------------------------------------------
class I3D_Menu( bpy.types.Menu ):
    bl_label = "GIANTS I3D"
    bl_idname = "i3d_menu"

    def draw( self, context ):
        layout = self.layout
        layout.label( text = "v 5.5.0" )
        layout.operator( "i3d.menu_export" )
        
#-------------------------------------------------------------------------------
#   I3D Menu Draw 
#-------------------------------------------------------------------------------
def draw_I3D_Menu( self, context ):
    self.layout.menu( I3D_Menu.bl_idname )

#-------------------------------------------------------------------------------
#   Register
#-------------------------------------------------------------------------------
def register():
    i3d_UIexport.register()  
    bpy.utils.register_class( I3D_Menu )
    bpy.types.INFO_HT_header.append( draw_I3D_Menu )

def unregister():
    i3d_UIexport.unregister()
    bpy.utils.unregister_class( I3D_Menu )
    bpy.types.INFO_HT_header.remove( draw_I3D_Menu )

if __name__ == "__main__":
    register()
#-------------------------------------------------------------------------------