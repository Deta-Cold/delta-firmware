from typing import *


# extmod/moddetahardcrypto/moddetahardcrypto-crc.h
def crc32(data: bytes, crc: int = 0) -> int:
    """
    Computes a CRC32 checksum of `data`.
    """
