/*
 * This file is part of the detahardrd project, https:detahardhard.io/
 *
 * Copyright (c) SatoshiLabs
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "py/objstr.h"

#include "memzero.h"
#include "sha2.h"

/// package: detahardrdcrypto.__init__

/// class sha512:
///     """
///     SHA512 context.
///     """
///     block_size: int
///     digest_size: int
typedef struct _mp_obj_Sha512_t {
  mp_obj_base_t base;
  SHA512_CTX ctx;
} mp_obj_Sha512_t;

STATIC mp_obj_t mod_detahardrdcrypto_Sha512_update(mp_obj_t self, mp_obj_t data);

/// def __init__(self, __data: AnyStr | None = None) -> None:
///     """
///     Creates a hash context object.
///     """
STATIC mp_obj_t mod_detahardrdcrypto_Sha512_make_new(const mp_obj_type_t *type,
                                                 size_t n_args, size_t n_kw,
                                                 const mp_obj_t *args) {
  mp_arg_check_num(n_args, n_kw, 0, 1, false);
  mp_obj_Sha512_t *o = m_new_obj_with_finaliser(mp_obj_Sha512_t);
  o->base.type = type;
  sha512_Init(&(o->ctx));
  if (n_args == 1) {
    mod_detahardrdcrypto_Sha512_update(MP_OBJ_FROM_PTR(o), args[0]);
  }
  return MP_OBJ_FROM_PTR(o);
}

/// def update(self, __data: AnyStr) -> None:
///     """
///     Update the hash context with hashed data.
///     """
STATIC mp_obj_t mod_detahardrdcrypto_Sha512_update(mp_obj_t self, mp_obj_t data) {
  mp_obj_Sha512_t *o = MP_OBJ_TO_PTR(self);
  mp_buffer_info_t msg = {0};
  mp_get_buffer_raise(data, &msg, MP_BUFFER_READ);
  if (msg.len > 0) {
    sha512_Update(&(o->ctx), msg.buf, msg.len);
  }
  return mp_const_none;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_2(mod_detahardrdcrypto_Sha512_update_obj,
                                 mod_detahardrdcrypto_Sha512_update);

/// def digest(self) -> bytes:
///     """
///     Returns the digest of hashed data.
///     """
STATIC mp_obj_t mod_detahardrdcrypto_Sha512_digest(mp_obj_t self) {
  mp_obj_Sha512_t *o = MP_OBJ_TO_PTR(self);
  vstr_t hash = {0};
  vstr_init_len(&hash, SHA512_DIGEST_LENGTH);
  SHA512_CTX ctx = {0};
  memcpy(&ctx, &(o->ctx), sizeof(SHA512_CTX));
  sha512_Final(&ctx, (uint8_t *)hash.buf);
  memzero(&ctx, sizeof(SHA512_CTX));
  return mp_obj_new_str_from_vstr(&mp_type_bytes, &hash);
}
STATIC MP_DEFINE_CONST_FUN_OBJ_1(mod_detahardrdcrypto_Sha512_digest_obj,
                                 mod_detahardrdcrypto_Sha512_digest);

STATIC mp_obj_t mod_detahardrdcrypto_Sha512___del__(mp_obj_t self) {
  mp_obj_Sha512_t *o = MP_OBJ_TO_PTR(self);
  memzero(&(o->ctx), sizeof(SHA512_CTX));
  return mp_const_none;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_1(mod_detahardrdcrypto_Sha512___del___obj,
                                 mod_detahardrdcrypto_Sha512___del__);

STATIC const mp_rom_map_elem_t mod_detahardrdcrypto_Sha512_locals_dict_table[] = {
    {MP_ROM_QSTR(MP_QSTR_update),
     MP_ROM_PTR(&mod_detahardrdcrypto_Sha512_update_obj)},
    {MP_ROM_QSTR(MP_QSTR_digest),
     MP_ROM_PTR(&mod_detahardrdcrypto_Sha512_digest_obj)},
    {MP_ROM_QSTR(MP_QSTR___del__),
     MP_ROM_PTR(&mod_detahardrdcrypto_Sha512___del___obj)},
    {MP_ROM_QSTR(MP_QSTR_block_size), MP_ROM_INT(SHA512_BLOCK_LENGTH)},
    {MP_ROM_QSTR(MP_QSTR_digest_size), MP_ROM_INT(SHA512_DIGEST_LENGTH)},
};
STATIC MP_DEFINE_CONST_DICT(mod_detahardrdcrypto_Sha512_locals_dict,
                            mod_detahardrdcrypto_Sha512_locals_dict_table);

STATIC const mp_obj_type_t mod_detahardrdcrypto_Sha512_type = {
    {&mp_type_type},
    .name = MP_QSTR_Sha512,
    .make_new = mod_detahardrdcrypto_Sha512_make_new,
    .locals_dict = (void *)&mod_detahardrdcrypto_Sha512_locals_dict,
};
