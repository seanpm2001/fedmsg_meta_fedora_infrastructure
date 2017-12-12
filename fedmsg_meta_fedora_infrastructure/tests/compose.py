# This file is part of fedmsg.
# Copyright (C) 2013 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for compose messages """

from fedmsg.tests.test_meta import Base

from .common import add_doc

## LEGACY 'BRANCHED' MESSAGES


class TestLegacyPreArchComposeBranchedComplete(Base):
    """ This tests Branched compose complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.complete"
    expected_subti = "18 compose completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedStart(Base):
    """ This tests Branched compose start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.start"
    expected_subti = "18 compose started"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedMashStart(Base):
    """ This tests Branched mash start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.mash.start"
    expected_subti = "18 compose started mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedMashComplete(Base):
    """ This tests Branched mash complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.mash.complete"
    expected_subti = "18 compose finished mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedPungifyStart(Base):
    """ This tests Branched pungify start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.pungify.start"
    expected_subti = "started building boot.iso for 18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedPungifyComplete(Base):
    """ This tests Branched pungify complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.pungify.complete"
    expected_subti = "finished building boot.iso for 18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedRsyncStart(Base):
    """ This tests Branched rsync start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.rsync.start"
    expected_subti = "started rsyncing 18 compose"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "18",
        },
    }


class TestLegacyPreArchComposeBranchedRsyncComplete(Base):
    """ This tests Branched rsync complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.rsync.complete"
    expected_subti = \
        "finished rsync of 18 compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "18",
        },
    }

## LEGACY RAWHIDE MESSAGES


class TestLegacyPreArchComposeRawhideComplete(Base):
    """ This tests Rawhide compose complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestLegacyPreArchComposeRawhideStart(Base):
    """ This tests Rawhide compose start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.start"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyPreArchComposeRawhideMashStart(Base):
    """ This tests Rawhide mash start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.mash.start"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyPreArchComposeRawhideMashComplete(Base):
    """ This tests Rawhide mash complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.mash.complete"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestLegacyPreArchComposeRawhideRsyncStart(Base):
    """ This tests Rawhide rsync start messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.start"
    expected_subti = "started rsyncing rawhide compose"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyPreArchComposeRawhideRsyncComplete(Base):
    """ This tests Rawhide rsync complete messages from before the
    'arch' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }

class TestLegacyPreShortComposeRawhideStart(Base):
    """ This tests Rawhide compose start messages from before the
    'short' key was added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.start"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestLegacyPreCidComposeRawhideRsyncStart(Base):
    """ This tests Rawhide rsync start messages from before the
    'short'  and 'compose_id' keys were added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.start"
    expected_subti = "started rsyncing rawhide compose"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestLegacyPreCidComposeRawhideRsyncComplete(Base):
    """ This tests Rawhide rsync complete messages from before the
    'short'  and 'compose_id' keys were added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestLegacyPreCidComposeRawhideComplete(Base):
    """ This tests Rawhide compose complete messages from before the
    'short'  and 'compose_id' keys were added to the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose completed"
    expected_objects = set(['rawhide/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestLegacyPreShortComposeRawhideRsyncStart(Base):
    """ This tests Rawhide rsync start messages from before the
    'short'key was added to the fedmsg, but after 'compose_id' was.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.start"
    expected_subti = "started rsyncing rawhide compose"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512395453.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171204.n.0",
        },
    }


class TestLegacyPreShortComposeRawhideRsyncComplete(Base):
    """ This tests Rawhide rsync complete messages from before the
    'short'key was added to the fedmsg, but after 'compose_id' was.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512313750.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171203.n.0",
        },
    }


class TestLegacyPreShortComposeRawhideComplete(Base):
    """ This tests Rawhide compose complete messages from before the
    'short'key was added to the fedmsg, but after 'compose_id' was.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose completed"
    expected_objects = set(['rawhide/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    msg = {
        "i": 1,
        "timestamp": 1512398352.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171204.n.0",
        },
    }


class TestLegacyModularComposeRawhideComplete(Base):
    """ This tests compose complete messages for Rawhide modular composes.
    These were replaced by the 'bikeshed' composes in 2017-11.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "Modular-Rawhide compose completed"
    expected_objects = set(['rawhide/primary'])
    expected_link = \
        "https://kojipkgs.fedoraproject.org/compose/Fedora-Modular-Rawhide-20170821.n.0"
    msg = {
        "i": 1,
        "msg": {
            "arch": "",
            "branch": "Modular-Rawhide",
            "compose_id": "Fedora-Modular-Rawhide-20170821.n.0",
            "log": "done"
        },
        "msg_id": "2017-857e93ea-3d46-4d8c-abc6-d50faeae313c",
        "timestamp": 1503339696.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
    }

## SECONDARY ARCH 'BRANCHED' MESSAGES


class TestSecondaryArchComposeBranchedComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **finished composing**
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.complete"
    expected_subti = "18 compose (arm) completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
        "development/18"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **started composing**
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.start"
    expected_subti = "18 compose (arm) started"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedMashStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **started mashing**
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.mash.start"
    expected_subti = "18 compose (arm) started mashing"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedMashComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **finished mashing**
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.mash.complete"
    expected_subti = "18 compose (arm) finished mashing"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedPungifyStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    started the `pungify <https://fedorahosted.org/pungi/>`_ process for
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.pungify.start"
    expected_subti = "started building boot.iso for 18 (arm)"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedPungifyComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    completed the `pungify <https://fedorahosted.org/pungi/>`_ process for
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.pungify.complete"
    expected_subti = "finished building boot.iso for 18 (arm)"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedRsyncStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **started rsyncing**
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.rsync.start"
    expected_subti = "started rsyncing 18 compose (arm)"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedRsyncComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **finished rsyncing**
    a secondary arch compose for a Branched release. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    # no need to include both this and the primary arch test in the docs
    nodoc = True
    expected_title = "compose.branched.rsync.complete"
    expected_subti = \
        "finished rsync of 18 compose (arm)"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
        "development/18"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "arm",
        },
    }

## SECONDARY ARCH RAWHIDE MESSAGES


class TestLegacySecondaryArchComposeRawhideComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **finished**
    a Rawhide secondary arch compose. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose (arm) completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
        "development/rawhide"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestLegacySecondaryArchComposeRawhideStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **started**
    a Rawhide secondary arch compose. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    expected_title = "compose.rawhide.start"
    expected_subti = "rawhide compose (arm) started"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestLegacySecondaryArchComposeRawhideMashStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **started mashing**
    a Rawhide secondary arch compose. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    expected_title = "compose.rawhide.mash.start"
    expected_subti = "rawhide compose (arm) started mashing"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestLegacySecondaryArchComposeRawhideMashComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **finished mashing**
    a Rawhide secondary arch compose. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    expected_title = "compose.rawhide.mash.complete"
    expected_subti = "rawhide compose (arm) finished mashing"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestLegacySecondaryArchComposeRawhideRsyncStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **started rsyncing**
    a Rawhide secondary arch compose. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    expected_title = "compose.rawhide.rsync.start"
    expected_subti = "started rsyncing rawhide compose (arm)"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestLegacySecondaryArchComposeRawhideRsyncComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had
    **finished rsyncing**
    a Rawhide secondary arch compose. Since the Pungi 4
    migration, all arches are included in the same compose process.
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = \
        "finished rsync of rawhide compose (arm)"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
        "development/rawhide"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "arm",
        },
    }

## OLD (BUT NOT LEGACY) 'BRANCHED' MESSAGES


class TestComposeBranchedComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **finished composing**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, instead the topic for messages
    related to Branched composes will include the release number (e.g.
    'compose.27.complete').
    """
    expected_title = "compose.branched.complete"
    expected_subti = "18 compose completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **began composing**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, instead the topic for messages
    related to Branched composes will include the release number (e.g.
    'compose.27.start').
    """
    expected_title = "compose.branched.start"
    expected_subti = "18 compose started"
    expected_link = "https://dl.fedoraproject.org/pub/fedora/linux/development/18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedMashStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **began mashing**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no mash-related
    messages published by the current compose process.
    """
    expected_title = "compose.branched.mash.start"
    expected_subti = "18 compose started mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedMashComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **finished mashing**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no mash-related
    messages published by the current compose process.
    """
    expected_title = "compose.branched.mash.complete"
    expected_subti = "18 compose finished mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedPungifyStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **started to pungify**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no pungify
    messages published by the current compose process.
    """
    expected_title = "compose.branched.pungify.start"
    expected_subti = "started building boot.iso for 18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedPungifyComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **finished pungifying**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no pungify
    messages published by the current compose process.
    """
    expected_title = "compose.branched.pungify.complete"
    expected_subti = "finished building boot.iso for 18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedRsyncStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **began syncing out (publishing, effectively)**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, instead the topic for messages
    related to Branched composes will include the release number (e.g.
    'compose.27.rsync.start').
    """
    expected_title = "compose.branched.rsync.start"
    expected_subti = "started rsyncing 18 compose"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "18",
            "arch": "",
        },
    }


class TestComposeBranchedRsyncComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **finished syncing out (publishing, effectively)**
    whatever the current branched distribution version was. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, instead the topic for messages
    related to Branched composes will include the release number (e.g.
    'compose.27.rsync.complete').
    """
    expected_title = "compose.branched.rsync.complete"
    expected_subti = \
        "finished rsync of 18 compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "18",
            "arch": "",
        },
    }

## OLD (BUT NOT LEGACY) RAWHIDE MESSAGES


class TestComposeRawhideMashStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **started mashing**
    the rawhide compose. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no mash-related
    messages published by the current compose process.
    """
    expected_title = "compose.rawhide.mash.start"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideMashComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **finished mashing**
    the rawhide compose. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no mash-related
    messages published by the current compose process.
    """
    expected_title = "compose.rawhide.mash.complete"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhidePungifyStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **started creating a boot.iso**
    for the rawhide compose. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no pungify
    messages published by the current compose process.
    """
    expected_title = "compose.rawhide.pungify.start"
    expected_subti = "started building boot.iso for rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.pungify.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhidePungifyComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they
    **finished creating a boot.iso**
    for the rawhide compose. They were published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary). Messages
    with this topic are not currently published, and there are no pungify
    messages published by the current compose process.
    """
    expected_title = "compose.rawhide.pungify.complete"
    expected_subti = "finished building boot.iso for rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }

## CURRENT RAWHIDE MESSAGES


class TestComposeRawhideStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **started** the rawhide compose.
    """
    expected_title = "compose.rawhide.start"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171215.n.0",
            "short": "Fedora",
        },
    }


class TestComposeRawhideRsyncStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **started syncing out**
    a completed rawhide compose.
    """
    expected_title = "compose.rawhide.rsync.start"
    expected_subti = "started rsyncing rawhide compose"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512395453.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171215.n.0",
            "short": "Fedora",
        },
    }


class TestComposeRawhideRsyncComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished syncing out**
    a completed rawhide compose.
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512313750.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171215.n.0",
            "short": "Fedora",
        },
    }


class TestComposeRawhideComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished**
    a rawhide compose.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose completed"
    expected_objects = set(['rawhide/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
    msg = {
        "i": 1,
        "timestamp": 1512398352.0,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
            "compose_id": "Fedora-Rawhide-20171215.n.0",
            "short": "Fedora",
        },
    }

## CURRENT MODULAR BIKESHED COMPOSE MESSAGES


class TestComposeBikeshedStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **started** a 'bikeshed' compose
    (basically like a Rawhide compose, but for modular).
    """
    expected_title = "compose.bikeshed.start"
    expected_subti = "bikeshed compose started"
    expected_objects = set(['bikeshed/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512756914.0,
        "msg_id": "2017-7e497c3e-14b6-497f-a016-79cf9b591585",
        "topic": "org.fedoraproject.prod.compose.bikeshed.start",
        "msg": {
            "log": "start",
            "branch": "bikeshed",
            "arch": "",
            "short": "Fedora-Modular",
        },
    }


class TestComposeBikeshedComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished** a 'bikeshed' compose
    (basically like a Rawhide compose, but for modular).
    """
    expected_title = "compose.bikeshed.complete"
    expected_subti = "bikeshed compose completed"
    expected_objects = set(['bikeshed/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512756914.0,
        "topic": "org.fedoraproject.prod.compose.bikeshed.complete",
        "msg": {
            "log": "done",
            "branch": "bikeshed",
            "arch": "",
            "compose_id": "Fedora-Modular-Bikeshed-20171208.n.0",
            "short": "Fedora-Modular",
        },
    }

## LEGACY MODULAR BIKESHED COMPOSE MESSAGES


class TestLegacyPre201712ComposeBikeshedComplete(Base):
    """ This tests bikeshed messages from before the fixes in 2017-12,
    which added the 'short' key, changed the 'branch' value from
    'Modular-Bikeshed' to 'bikeshed', and ensured the compose_id was
    present for post-compose-complete messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.bikeshed.complete"
    expected_subti = "Modular-Bikeshed compose completed"
    expected_objects = set(['bikeshed/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512411407.0,
        "msg_id": "2017-7973eb0b-0715-40c2-9903-01c31dd25e06",
        "topic": "org.fedoraproject.prod.compose.bikeshed.complete",
        "msg": {
            "log": "done",
            "branch": "Modular-Bikeshed",
            "arch": "",
            "compose_id": "",
        },
    }

## CURRENT NUMERIC COMPOSE MESSAGES


class TestComposeNumericStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **started** a compose for a
    numbered release. This could be a Branched compose, or a post-release
    two-week Atomic, Docker, or Cloud compose: the 'short' and 'compose_id'
    values can be used to differentiate. The message topic obviously differs
    based on the release, this one is only an example.
    """
    expected_title = "compose.28.start"
    expected_subti = "28 compose started"
    expected_objects = set(['28/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.28.start",
        "msg": {
            "log": "start",
            "branch": "28",
            "arch": "",
            "compose_id": "Fedora-28-20171215.n.0",
            "short": "Fedora",
        },
    }


class TestComposeNumericRsyncStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **started syncing out** a compose for
    a numbered release. This could be a Branched compose, or a post-release
    two-week Atomic, Docker, or Cloud compose: the 'short' and 'compose_id'
    values can be used to differentiate. The message topic obviously differs
    based on the release, this one is only an example.
    """
    expected_title = "compose.28.rsync.start"
    expected_subti = "started rsyncing 28 compose"
    expected_objects = set(['28/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512395453.0,
        "topic": "org.fedoraproject.prod.compose.28.rsync.start",
        "msg": {
            "log": "start",
            "branch": "28",
            "arch": "",
            "compose_id": "Fedora-Atomic-28-20171215.n.0",
            "short": "Fedora-Atomic",
        },
    }


class TestComposeNumericRsyncComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished syncing out** a compose
    for a numbered release. This could be a Branched compose, or a post-release
    two-week Atomic, Docker, or Cloud compose: the 'short' and 'compose_id'
    values can be used to differentiate. The message topic obviously differs
    based on the release, this one is only an example.
    """
    expected_title = "compose.28.rsync.complete"
    expected_subti = "finished rsync of 28 compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/28"
    expected_objects = set(['28/primary'])
    msg = {
        "i": 1,
        "timestamp": 1512313750.0,
        "topic": "org.fedoraproject.prod.compose.28.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "28",
            "arch": "",
            "compose_id": "Fedora-Cloud-28-20171215.n.0",
            "short": "Fedora-Cloud",
        },
    }


class TestComposeNumericComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished** a compose for a
    numbered release. This could be a Branched compose, or a post-release
    two-week Atomic, Docker, or Cloud compose: the 'short' and 'compose_id'
    values can be used to differentiate. The message topic obviously differs
    based on the release, this one is only an example.
    """
    expected_title = "compose.28.complete"
    expected_subti = "28 compose completed"
    expected_objects = set(['28/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/28"
    msg = {
        "i": 1,
        "timestamp": 1512398352.0,
        "topic": "org.fedoraproject.prod.compose.28.complete",
        "msg": {
            "log": "done",
            "branch": "28",
            "arch": "",
            "compose_id": "Fedora-Docker-28-20171215.n.0",
            "short": "Fedora-Docker",
        },
    }


class TestComposeNumericModularComplete(Base):
    """This is just an additional test for current numeric Modular
    compose messages, as we don't have enough tests for all shortnames
    above. Note, it may be the case that none of these ever actually
    exist - F27 modular composes were stopped just before the 2017-12
    changes that would have produced this form of message, and we may
    roll modular deliverables into the main compose process before 28
    branches. But let's test this format just in case.
    """
    # no need to doc this, previous class is the doc
    nodoc = True
    expected_title = "compose.28.complete"
    expected_subti = "28 compose completed"
    expected_objects = set(['28/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/28"
    msg = {
        "i": 1,
        "timestamp": 1512398352.0,
        "topic": "org.fedoraproject.prod.compose.28.complete",
        "msg": {
            "log": "done",
            "branch": "28",
            "arch": "",
            "compose_id": "Fedora-Modular-28-20171215.n.0",
            "short": "Fedora-Modular",
        },
    }

## LEGACY NUMERIC COMPOSE MESSAGES


class TestLegacyPre201712ComposeNumericComplete(Base):
    """ This tests numeric messages from before the fixes in 2017-12,
    which added the 'short' key and ensured the compose_id was present
    for post-compose-complete messages.

    Note there are no secondary arch messages of this type; we switched
    to numeric messages with the Pungi 4 migration, which also ended
    separate secondary arch composes.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.23.complete"
    expected_subti = "23 compose completed"
    expected_objects = set(['23/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    msg = {
        "i": 1,
        "timestamp": 1464301992.0,
        "msg_id": "2016-d6086626-88c3-41e0-8904-449c372fc33d",
        "topic": "org.fedoraproject.prod.compose.23.complete",
        "msg": {
            "log": "done",
            "branch": "23",
            "arch": "",
        },
    }


class TestLegacyPre201712ComposeNumericModularComplete(Base):
    """ This tests numeric messages for modular composes from before
    the fixes in 2017-12, which added the 'short' key, and changed the
    'branch' value from 'Modular-NN' to 'NN'.

    For the historical record, the 'compose_id' value in these fedmsgs
    is often a lie: these messages would be sent out even when the
    pungi compose failed, and in those cases, the 'compose_id' would
    in fact be the ID of the previous successful compose, not the ID
    of the failed compose that actually triggered the fedmsg.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.27.complete"
    expected_subti = "Modular-27 compose completed"
    expected_objects = set(['27/primary'])
    expected_link = \
        "https://kojipkgs.fedoraproject.org/compose/Fedora-Modular-27-20171123.n.1"
    msg = {
        "i": 1,
        "timestamp": 1511450794.0,
        "msg_id": "2017-ab0bc502-29d3-47b7-bd54-c71b50dcbd76",
        "topic": "org.fedoraproject.prod.compose.27.complete",
        "msg": {
            "log": "done",
            "branch": "Modular-27",
            "arch": "",
            "compose_id": "Fedora-Modular-27-20171123.n.1",
        },
    }

## OLD MAKE-UPDATES PROCESS MESSAGES


class TestComposeMakeUpdatesStarted(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had **started** the make-updates
    process (which was how we did periodic re-spins of our cloud, atomic, and
    docker images during the Fedora 21, 22 and 23 cycles). From Fedora 24
    onwards, these re-spins are produced with Pungi 4 like all other forms of
    compose, and emit the standard compose messages with the release number
    in the topic (e.g. compose.24.start or compose.28.start).
    Here's an example of a message from Fedora 23:
    """
    expected_title = "compose.23.make-updates.start"
    expected_subti = \
        "started a run of F23 make-updates"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            "log": "start"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.make-updates.start"
    }


class TestComposeCloudImgBuildComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had **finished** the cloud image
    build phase of the make-updates process (which was how we did periodic
    re-spins of our cloud, atomic, and docker images during the Fedora 21,
    22 and 23 cycles). From Fedora 24 onwards, these re-spins are produced
    with Pungi 4 like all other forms of compose, and emit the standard
    compose messages with the release number in the topic (e.g.
    compose.24.start or compose.28.start). Here's an example of a message from
    Fedora 23:
    """
    expected_title = "compose.23.cloudimg-build.done"
    expected_subti = \
        "the cloudimg-build phase of a F23 make-updates run completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            "log": "done"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.cloudimg-build.done"
    }


class TestComposeMashAtomicComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had **started** the Atomic mash
    phase of the make-updates process (which was how we did periodic
    re-spins of our cloud, atomic, and docker images during the Fedora 21,
    22 and 23 cycles). From Fedora 24 onwards, these re-spins are produced
    with Pungi 4 like all other forms of compose, and emit the standard
    compose messages with the release number in the topic (e.g.
    compose.24.start or compose.28.start). Here's an example of a message from
    Fedora 23:
    """
    # yes, 'stop'
    expected_title = "compose.23.mash-atomic.stop"
    expected_subti = \
        "the mash-atomic phase of a F23 make-updates run completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            # yes, really 'start', this is what real messages looked like
            "log": "start"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.mash-atomic.stop"
    }


class TestComposeAtomicLoraxComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had **finished** the Atomic lorax
    phase of the make-updates process (which was how we did periodic
    re-spins of our cloud, atomic, and docker images during the Fedora 21,
    22 and 23 cycles). From Fedora 24 onwards, these re-spins are produced
    with Pungi 4 like all other forms of compose, and emit the standard
    compose messages with the release number in the topic (e.g.
    compose.24.start or compose.28.start). Here's an example of a message from
    Fedora 23:
    """
    expected_title = "compose.23.atomic-lorax.done"
    expected_subti = \
        "the atomic-lorax phase of a F23 make-updates run completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            "log": "done"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.atomic-lorax.done"
    }


class TestComposeCloudImgChecksumStarted(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had **started** the Cloud image
    checksum phase of the make-updates process (which was how we did periodic
    re-spins of our cloud, atomic, and docker images during the Fedora 21,
    22 and 23 cycles). From Fedora 24 onwards, these re-spins are produced
    with Pungi 4 like all other forms of compose, and emit the standard
    compose messages with the release number in the topic (e.g.
    compose.24.start or compose.28.start). Here's an example of a message from
    Fedora 23:
    """
    expected_title = "compose.23.cloudimg-checksum.start"
    expected_subti = \
        "started the cloudimg-checksum phase of a F23 make-updates run"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            "log": "start"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.cloudimg-checksum.start"
    }


class TestComposeCloudImgStagingComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    used to produce these messages when they had **finished** the Cloud image
    staging phase of the make-updates process (which was how we did periodic
    re-spins of our cloud, atomic, and docker images during the Fedora 21,
    22 and 23 cycles). From Fedora 24 onwards, these re-spins are produced
    with Pungi 4 like all other forms of compose, and emit the standard
    compose messages with the release number in the topic (e.g.
    compose.24.start or compose.28.start). Here's an example of a message from
    Fedora 23:
    """
    expected_title = "compose.23.cloudimg-staging.done"
    expected_subti = \
        "the cloudimg-staging phase of a F23 make-updates run completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            "log": "start"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.cloudimg-staging.done"
    }

## MISCELLANEOUS MESSAGES


class TestComposeEPELBetaComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished composing** the EPEL beta.
    """
    expected_title = "compose.epelbeta.complete"
    expected_subti = "epelbeta compose completed"
    expected_link = "https://dl.fedoraproject.org/pub/epel/beta/7/"
    expected_objects = set(['epelbeta/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.epelbeta.complete",
        "msg": {
            "log": "done",
        },
    }

add_doc(locals())
