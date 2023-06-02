from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from detahard.messages import GetNonce, Nonce
    from detahard.wire import Context


async def get_nonce(ctx: Context, msg: GetNonce) -> Nonce:
    from storage import cache
    from detahard.crypto import random
    from detahard.messages import Nonce

    nonce = random.bytes(32)
    cache.set(cache.APP_COMMON_NONCE, nonce)
    return Nonce(nonce=nonce)
