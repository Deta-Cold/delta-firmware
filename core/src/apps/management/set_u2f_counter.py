from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from detahard.messages import SetU2FCounter, Success
    from detahard.wire import Context


async def set_u2f_counter(ctx: Context, msg: SetU2FCounter) -> Success:
    import storage.device as storage_device
    from detahard import wire
    from detahard.enums import ButtonRequestType
    from detahard.messages import Success
    from detahard.ui.layouts import confirm_action

    if not storage_device.is_initialized():
        raise wire.NotInitialized("Device is not initialized")
    if msg.u2f_counter is None:
        raise wire.ProcessError("No value provided")

    await confirm_action(
        ctx,
        "set_u2f_counter",
        "Set U2F counter",
        description="Do you really want to set the U2F counter to {}?",
        description_param=str(msg.u2f_counter),
        br_code=ButtonRequestType.ProtectCall,
    )

    storage_device.set_u2f_counter(msg.u2f_counter)

    return Success(message="U2F counter set")
