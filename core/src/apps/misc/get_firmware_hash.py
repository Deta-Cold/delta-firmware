from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from detahard.messages import GetFirmwareHash, FirmwareHash
    from detahard.wire import Context
    from detahard.ui.layouts.common import ProgressLayout

_progress_obj: ProgressLayout | None = None


async def get_firmware_hash(ctx: Context, msg: GetFirmwareHash) -> FirmwareHash:
    from detahard.messages import FirmwareHash
    from detahard.utils import firmware_hash
    from detahard.ui.layouts.progress import progress
    from detahard import wire, workflow

    workflow.close_others()
    global _progress_obj
    _progress_obj = progress()

    try:
        hash = firmware_hash(msg.challenge, _render_progress)
    except ValueError as e:
        raise wire.DataError(str(e))
    finally:
        _progress_obj = None

    return FirmwareHash(hash=hash)


def _render_progress(progress: int, total: int) -> None:
    global _progress_obj
    if _progress_obj is not None:
        _progress_obj.report(1000 * progress // total)
