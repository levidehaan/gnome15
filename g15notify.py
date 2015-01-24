# Gnome15 - Suite of tools for the Logitech G series keyboards and headsets
#  Copyright (C) 2011 Brett Smith <tanktarta@blueyonder.co.uk>
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

'''
Notifications
'''
import dbus
import g15globals

# Logging
import logging

logger = logging.getLogger(__name__)

_session_bus = dbus.SessionBus()


class NotifyMessage():
    def __init__(self):
        self.id = 0

    def close(self):
        logger.info("Closing notification %s", str(self.id))
        _get_obj().CloseNotification(self.id)

    def handle_reply(self, e):
        self.id = int(e)
        logger.debug("Got message ID %d", self.id)

    def handle_error(self, e):
        logger.error("Error getting notification message ID. %s", str(e))


def _get_obj():
    return _session_bus.get_object("org.freedesktop.Notifications", '/org/freedesktop/Notifications')


def notify(summary, body, icon="", actions=[], hints={}, timeout=10.0, replaces=0):
    actions_array = dbus.Array(actions, signature='s')
    hints_dict = dbus.Dictionary(hints, signature='sv')
    msg = NotifyMessage()
    _get_obj().Notify(g15globals.name,
                      replaces,
                      icon,
                      summary,
                      body,
                      actions_array,
                      hints_dict,
                      int(timeout * 1000),
                      dbus_interface='org.freedesktop.Notifications',
                      reply_handler=msg.handle_reply,
                      error_handler=msg.handle_error)
    return msg