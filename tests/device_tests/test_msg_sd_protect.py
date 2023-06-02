# This file is part of the detahard project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from detahardlib import debuglink, device
from detahardlib.debuglink import detahardClientDebugLink as Client
from detahardlib.exceptions import detahardFailure
from detahardlib.messages import SdProtectOperationType as Op

from ..common import MNEMONIC12

pytestmark = [pytest.mark.skip_t1, pytest.mark.sd_card]


def test_enable_disable(client: Client):
    assert client.features.sd_protection is False
    # Disabling SD protection should fail
    with pytest.raises(detahardFailure):
        device.sd_protect(client, Op.DISABLE)

    # Enable SD protection
    device.sd_protect(client, Op.ENABLE)
    assert client.features.sd_protection is True

    # Enabling SD protection should fail
    with pytest.raises(detahardFailure):
        device.sd_protect(client, Op.ENABLE)
    assert client.features.sd_protection is True

    # Disable SD protection
    device.sd_protect(client, Op.DISABLE)
    assert client.features.sd_protection is False


def test_refresh(client: Client):
    assert client.features.sd_protection is False
    # Enable SD protection
    device.sd_protect(client, Op.ENABLE)
    assert client.features.sd_protection is True

    # Refresh SD protection
    device.sd_protect(client, Op.REFRESH)
    assert client.features.sd_protection is True

    # Disable SD protection
    device.sd_protect(client, Op.DISABLE)
    assert client.features.sd_protection is False

    # Refreshing SD protection should fail
    with pytest.raises(detahardFailure):
        device.sd_protect(client, Op.REFRESH)
    assert client.features.sd_protection is False


def test_wipe(client: Client):
    # Enable SD protection
    device.sd_protect(client, Op.ENABLE)
    assert client.features.sd_protection is True

    # Wipe device (this wipes internal storage)
    device.wipe(client)
    assert client.features.sd_protection is False

    # Restore device to working status
    debuglink.load_device(
        client, mnemonic=MNEMONIC12, pin=None, passphrase_protection=False, label="test"
    )
    assert client.features.sd_protection is False

    # Enable SD protection
    device.sd_protect(client, Op.ENABLE)
    assert client.features.sd_protection is True

    # Refresh SD protection
    device.sd_protect(client, Op.REFRESH)
