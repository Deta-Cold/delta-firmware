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

from dataclasses import dataclass
from typing import Collection, Optional, Tuple

from . import mapping

UsbId = Tuple[int, int]

VENDORS = ("bitcoindetahard.com", "detahard.io")


@dataclass(eq=True, frozen=True)
class detahardModel:
    name: str
    minimum_version: Tuple[int, int, int]
    vendors: Collection[str]
    usb_ids: Collection[UsbId]
    default_mapping: mapping.ProtobufMapping


detahard_ONE = detahardModel(
    name="1",
    minimum_version=(1, 8, 0),
    vendors=VENDORS,
    usb_ids=((0x534C, 0x0001),),
    default_mapping=mapping.DEFAULT_MAPPING,
)

detahard_T = detahardModel(
    name="T",
    minimum_version=(2, 1, 0),
    vendors=VENDORS,
    usb_ids=((0x1209, 0x53C1), (0x1209, 0x53C0)),
    default_mapping=mapping.DEFAULT_MAPPING,
)

detahard_R = detahardModel(
    name="R",
    minimum_version=(2, 1, 0),
    vendors=VENDORS,
    usb_ids=((0x1209, 0x53C1), (0x1209, 0x53C0)),
    default_mapping=mapping.DEFAULT_MAPPING,
)

detahardS = {detahard_ONE, detahard_T, detahard_R}


def by_name(name: Optional[str]) -> Optional[detahardModel]:
    if name is None:
        return detahard_ONE
    for model in detahardS:
        if model.name == name:
            return model
    return None
