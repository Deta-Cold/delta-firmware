from typing import *
from detahardcrypto.bip32 import HDNode


# extmod/moddetahardcrypto/moddetahardcrypto-cardano.h
def derive_icarus(
    mnemonic: str,
    passphrase: str,
    detahard_derivation: bool,
    callback: Callable[[int, int], None] | None = None,
) -> bytes:
    """
    Derives a Cardano master secret from a mnemonic and passphrase using the
    Icarus derivation scheme.
    If `detahard_derivation` is True, the Icarus-detahard variant is used (see
    CIP-3).
    """


# extmod/moddetahardcrypto/moddetahardcrypto-cardano.h
def from_secret(secret: bytes) -> HDNode:
    """
    Creates a Cardano HD node from a master secret.
    """


# extmod/moddetahardcrypto/moddetahardcrypto-cardano.h
def from_seed_slip23(seed: bytes) -> HDNode:
   """
   Creates a Cardano HD node from a seed via SLIP-23 derivation.
   """


# extmod/moddetahardcrypto/moddetahardcrypto-cardano.h
def from_seed_ledger(seed: bytes) -> HDNode:
    """
    Creates a Cardano HD node from a seed via Ledger derivation.
    """
