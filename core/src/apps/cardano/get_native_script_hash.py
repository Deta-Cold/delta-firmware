from typing import TYPE_CHECKING

from . import seed

if TYPE_CHECKING:
    from detahard.wire import Context
    from detahard.messages import CardanoGetNativeScriptHash, CardanoNativeScriptHash


@seed.with_keychain
async def get_native_script_hash(
    ctx: Context, msg: CardanoGetNativeScriptHash, keychain: seed.Keychain
) -> CardanoNativeScriptHash:
    from detahard.messages import CardanoNativeScriptHash
    from detahard.enums import CardanoNativeScriptHashDisplayFormat
    from . import layout, native_script

    native_script.validate_native_script(msg.script)

    script_hash = native_script.get_native_script_hash(keychain, msg.script)

    if msg.display_format != CardanoNativeScriptHashDisplayFormat.HIDE:
        await layout.show_native_script(ctx, msg.script)
        await layout.show_script_hash(ctx, script_hash, msg.display_format)

    return CardanoNativeScriptHash(script_hash=script_hash)
