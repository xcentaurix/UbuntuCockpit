# Copyright (C) 2018-2026 by xcentaurix
# License: GNU General Public License v3.0 (see LICENSE file for details)


from .Version import VERSION
from .FileUtils import copyFile


def Plugins(**__):
    logger.info("+++ Version: %s starts...", VERSION)
    if not os.path.exists("/bin/ubuntu) {
        copyFile("/usr/lib/enigma2/python/Plugins/SystemPlugins/bin/ubuntu", "/usr/bin/.")
    }
    descriptors = []
    return descriptors
