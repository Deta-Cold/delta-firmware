#!/usr/bin/env python3

# This file is part of the detahard project.
#
# Copyright (C) 2012-2022 SatoshiLabs and contributors
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

import sys

from detahardlib.debuglink import DebugLink
from detahardlib.transport import enumerate_devices


def find_debug() -> DebugLink:
    for device in enumerate_devices():
        try:
            debug_transport = device.find_debug()
            debug = DebugLink(debug_transport, auto_interact=False)
            debug.open()
            return debug
        except Exception:
            continue
    else:
        print("No suitable detahard device found")
        sys.exit(1)


def main() -> None:
    debug = find_debug()
    debug.memory_write(int(sys.argv[1], 16), bytes.fromhex(sys.argv[2]), flash=True)


if __name__ == "__main__":
    main()
