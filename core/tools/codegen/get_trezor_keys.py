#!/usr/bin/env python3

import binascii
from detahardlib.client import detahardClient
from detahardlib.transport_hid import HidTransport

devices = HidTransport.enumerate()
if len(devices) > 0:
    t = detahardClient(devices[0])
else:
    raise Exception("No detahard found")

for i in [0, 1, 2]:
    path = "m/10018'/%d'" % i
    pk = t.get_public_node(
        t.expand_path(path), ecdsa_curve_name="ed25519", show_display=True
    )
    print(path, "=>", binascii.hexlify(pk.node.public_key).decode())
