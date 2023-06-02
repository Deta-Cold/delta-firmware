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

# usage examples
# read entire bootloader: ./mem_read.py 8000000 8000
# read initial stack pointer: ./mem_read.py 8000000 4
# an entire bootloader can be later disassembled with:
# arm-none-eabi-objdump -D -b binary -m arm -M force-thumb memory.dat
# note that in order for this to work, your detahard device must
# be running a firmware that was built with debug link enabled


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

    arg1 = int(sys.argv[1], 16)
    arg2 = int(sys.argv[2], 16)
    step = 0x400 if arg2 >= 0x400 else arg2

    f = open("memory.dat", "wb")

    for addr in range(arg1, arg1 + arg2, step):
        mem = debug.memory_read(addr, step)
        f.write(mem)

    f.close()


if __name__ == "__main__":
    main()
