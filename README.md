# Description

These 3 python files let you install an exporter script for your Blender (>=2.7.0) to save your models as i3d file for the game Farming Simulator.

# Installation

0) If you never opened Blender before, do it now, open the User Preferences dialog in the File menue, just click Save User Settings at the bottom left and close Blender (to create some directories).
1-Windows) Open the (file) Explorer and type "%APPDATA%" in your address bar
1-Mac) Open a terminal and create a symlink to your (hidden) Library folder (ln -s ~/Library ~/LibraryLink). Then jump in there and go to "Application Support"
2) Optional: create a temporary shortcut to this directory on your desktop (for step 6)
3) Change your directory further to Blender/2.7X/scripts/addons (where X is the thrid number of your Blender version)
4) Create a folder "io_export_i3d" in addons
5) Put all 3 python files (__init__.py, i3d_IOexport.py and i3d_UIexport.py) from this GitHub page in there
6) Open Blender, open up the User Preferences dialog again, change to the Add-ons tab and click Install from File at the bottom. Browse to your io_export_i3d directory and select __init__.py to install
7) Select Game Engine as Category on the right and check GIANTS I3D Exporter Tools from the list
8) Save your user settings

Now you should have the option under File/Export to export your model as GIANTS I3D (.i3d)

# Licence

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Copyright 2004 (C) GIANTS Software GmbH, Confidential, All Rights Reserved.
