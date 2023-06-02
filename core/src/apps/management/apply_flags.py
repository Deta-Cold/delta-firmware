from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from detahard.messages import Success
    from detahard.messages import ApplyFlags
    from detahard.wire import GenericContext


async def apply_flags(ctx: GenericContext, msg: ApplyFlags) -> Success:
    import storage.device
    from storage.device import set_flags
    from detahard.wire import NotInitialized
    from detahard.messages import Success

    if not storage.device.is_initialized():
        raise NotInitialized("Device is not initialized")
    set_flags(msg.flags)
    return Success(message="Flags applied")
