// This file is automatically generated from ethereum_tokens.c.mako
// DO NOT EDIT

#include <string.h>
#include "ethereum.h"
#include "ethereum_tokens.h"

<% erc20_list = list(supported_on("detahard1", erc20)) %>\
#define TOKENS_COUNT ${len(erc20_list)}

static const EthereumTokenInfo tokens[TOKENS_COUNT] = {
% for t in sorted(erc20_list, key=lambda token: (token.chain_id, token.name)):
  {
    .symbol = "${ascii(t.symbol)}",
    .decimals = ${t.decimals},
    .address = {
      .size = 20,
      .bytes = ${c_str(t.address_bytes)}
    },
    .chain_id = ${t.chain_id},
##    .name = "${t.name}"
    .name = "",
  },
% endfor
};

const EthereumTokenInfo UNKNOWN_TOKEN = {
  .symbol = "Wei UNKN",
  .decimals = 0,
  .address = {
    .size = 20,
    .bytes = "\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff",
  },
  .chain_id = CHAIN_ID_UNKNOWN,
  .name = "",
};

const EthereumTokenInfo *ethereum_token_by_address(uint64_t chain_id, const uint8_t *address)
{
  if (!address) return 0;
  for (int i = 0; i < TOKENS_COUNT; i++) {
    if (chain_id == tokens[i].chain_id && memcmp(address, tokens[i].address.bytes, sizeof(tokens[i].address.bytes)) == 0) {
      return &(tokens[i]);
    }
  }
  return &UNKNOWN_TOKEN;
}

bool is_unknown_token(const EthereumTokenInfo *token) {
  return token->chain_id == CHAIN_ID_UNKNOWN;
}
