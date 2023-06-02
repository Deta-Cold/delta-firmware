//
// Created by Dusan Klinec on 10/05/2018.
//

#ifndef detahard_CRYPTO_MONERO_H
#define detahard_CRYPTO_MONERO_H

#if !USE_MONERO
#error "Compile with -DUSE_MONERO=1"
#endif

#if !USE_KECCAK
#error "Compile with -DUSE_KECCAK=1"
#endif

#include "base58.h"
#include "serialize.h"
#include "xmr.h"

#endif  // detahard_CRYPTO_MONERO_H
