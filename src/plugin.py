# Copyright (C) 2018-2026 by xcentaurix
# License: GNU General Public License v3.0 (see LICENSE file for details)


import os
from .Version import VERSION
from .FileUtils import copyFile
from .Debug import logger


def Plugins(**__):
    logger.info("+++ Version: %s starts...", VERSION)
    if not os.path.exists("/bin/ubuntu"):
        copyFile(
            "/usr/lib/enigma2/python/Plugins/SystemPlugins/UbuntuCockpit/root/enter_chroot",
            "/bin/ubuntu"
        )
    descriptors = []
    return descriptors
