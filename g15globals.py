# Gnome15 - Suite of tools for the Logitech G series keyboards and headsets
#  Copyright (C) 2010 Brett Smith <tanktarta@blueyonder.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import xdg.BaseDirectory

name = "gnome15"
version = "0.9.8"

package_dir = os.path.abspath(os.path.dirname(__file__))
image_dir = os.path.join(package_dir, "..", "..", "data", "images")
dev = False
if os.path.exists(image_dir):
    dev = True
    ui_dir = os.path.realpath(os.path.join(package_dir, "..", "..", "data", "ui"))
    font_dir = os.path.realpath(os.path.join(package_dir, "..", "..", "data", "fonts"))
    icons_dir = os.path.realpath(os.path.join(package_dir, "..", "..", "data", "icons"))
    ukeys_dir = os.path.realpath(os.path.join(package_dir, "..", "..", "data", "ukeys"))
    plugin_dir = os.path.realpath(os.path.join(package_dir, "..", "plugins"))
    scripts_dir = os.path.realpath(os.path.join(package_dir, "..", "scripts"))
    themes_dir = os.path.realpath(os.path.join(package_dir, "..", "..", "data", "themes"))
    i18n_dir = os.path.realpath(os.path.join(package_dir, "..", "i18n"))
else:
    image_dir = "/usr/share/gnome15/images"
    ui_dir = "/usr/share/gnome15/ui"
    font_dir = "/usr/share/gnome15"
    plugin_dir = "/usr/share/gnome15/plugins"
    themes_dir = "/usr/share/gnome15/themes"
    ukeys_dir = "/usr/share/gnome15/ukeys"
    i18n_dir = "/usr/share/gnome15/i18n"
    icons_dir = "/usr/share/icons"
    scripts_dir = "/usr/bin"

user_config_dir = os.path.join(xdg.BaseDirectory.xdg_config_home, "gnome15")
user_data_dir = os.path.join(xdg.BaseDirectory.xdg_data_home, "gnome15")
user_cache_dir = os.path.join(xdg.BaseDirectory.xdg_cache_home, "gnome15")

# Differs from distro to distro, so it can changed as a ./configure option
# by setting the FIXED_SIZE_FONT environment variable.
fixed_size_font_name = "Fixed"
