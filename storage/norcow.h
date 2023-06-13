/*
 * This file is part of the detahard project, https://detahard.io/
 
 */

#ifndef __NORCOW_H__
#define __NORCOW_H__

#include <stdint.h>
#include "secbool.h"

/*
 * Storage parameters
 */

#include "norcow_config.h"

/*
 * Initialize storage
 */
void norcow_init(uint32_t *norcow_version);

/*
 * Wipe the storage
 */
void norcow_wipe(void);

/*
 * Looks for the given key, returns status of the operation
 */
secbool norcow_get(uint16_t key, const void **val, uint16_t *len);

/*
 * Reads the next entry in the storage starting at offset. Returns secfalse if
 * there is none.
 */
secbool norcow_get_next(uint32_t *offset, uint16_t *key, const void **val,
                        uint16_t *len);

/*
 * Sets the given key, returns status of the operation. If NULL is passed
 * as val, then norcow_set allocates a new key of size len. The value should
 * then be written using norcow_update_bytes().
 */
secbool norcow_set(uint16_t key, const void *val, uint16_t len);
secbool norcow_set_ex(uint16_t key, const void *val, uint16_t len,
                      secbool *found);

/*
 * Deletes the given key, returns status of the operation.
 */
secbool norcow_delete(uint16_t key);

/*
 * Update a word in flash in the given key at the given offset.
 * Note that you can only change bits from 1 to 0.
 */
secbool norcow_update_word(uint16_t key, uint16_t offset, uint32_t value);

/*
 * Update the value of the given key starting at the given offset.
 * Note that you can only change bits from 1 to 0.
 */
secbool norcow_update_bytes(const uint16_t key, const uint16_t offset,
                            const uint8_t *data, const uint16_t len);

/*
 * Complete storage version upgrade
 */
secbool norcow_upgrade_finish(void);

#endif
