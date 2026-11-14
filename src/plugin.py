# Copyright (C) 2018-2026 by xcentaurix
# License: GNU General Public License v3.0


import os
from .Version import VERSION
from .Debug import logger


ENTER_CHROOT = "/usr/lib/enigma2/python/Plugins/SystemPlugins/UbuntuCockpit/root/enter_chroot"


def Plugins(**__):
    logger.info("  +++ Version: %s starts...", VERSION)
    # The ubuntu command is a link to the script of the plugin, which finds the Ubuntu itself (ubuntucockpit.cfg). It is made here,
    # at every start, and not by the installation scripts: they cannot rely on the disk being there (an image installation), and
    # this also replaces a copy or a link that an earlier version made.
    if not (os.path.islink("/bin/ubuntu") and os.readlink("/bin/ubuntu") == ENTER_CHROOT):
        try:
            if os.path.lexists("/bin/ubuntu"):
                os.remove("/bin/ubuntu")
            os.chmod(ENTER_CHROOT, 0o755)
            os.symlink(ENTER_CHROOT, "/bin/ubuntu")
        except OSError as e:
            logger.error("cannot link /bin/ubuntu: %s", e)
    descriptors = []
    return descriptors
