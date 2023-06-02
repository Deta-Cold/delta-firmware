/*
 * This file is part of the detahard project, https://detahard.io/
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

#ifndef _FONTS_H
#define _FONTS_H

#include "fonts/font_bitmap.h"

#if defined detahard_MODEL_T
#define detahard_FONT_BPP 4
#elif defined detahard_MODEL_1
#define detahard_FONT_BPP 1
#elif defined detahard_MODEL_R
#define detahard_FONT_BPP 1
#else
#error Unknown detahard model
#endif

#define COMPOSE(font_name, suffix) font_name##suffix
#define FONT_DEFINE(s, suffix) COMPOSE(s, suffix)

#ifdef detahard_FONT_NORMAL_ENABLE
#define FONT_NORMAL (-1)
#include detahard_FONT_NORMAL_INCLUDE
#define FONT_NORMAL_DATA detahard_FONT_NORMAL_ENABLE
#define FONT_NORMAL_HEIGHT FONT_DEFINE(detahard_FONT_NORMAL_ENABLE, _HEIGHT)
#define FONT_NORMAL_MAX_HEIGHT \
  FONT_DEFINE(detahard_FONT_NORMAL_ENABLE, _MAX_HEIGHT)
#define FONT_NORMAL_BASELINE FONT_DEFINE(detahard_FONT_NORMAL_ENABLE, _BASELINE)
#endif

#ifdef detahard_FONT_DEMIBOLD_ENABLE
#include detahard_FONT_DEMIBOLD_INCLUDE
#define FONT_DEMIBOLD (-5)
#define FONT_DEMIBOLD_DATA detahard_FONT_DEMIBOLD_ENABLE
#define FONT_DEMIBOLD_HEIGHT FONT_DEFINE(detahard_FONT_DEMIBOLD_ENABLE, _HEIGHT)
#define FONT_DEMIBOLD_MAX_HEIGHT \
  FONT_DEFINE(detahard_FONT_DEMIBOLD_ENABLE, _MAX_HEIGHT)
#define FONT_DEMIBOLD_BASELINE \
  FONT_DEFINE(detahard_FONT_DEMIBOLD_ENABLE, _BASELINE)
#endif

#ifdef detahard_FONT_MONO_ENABLE
#include detahard_FONT_MONO_INCLUDE
#define FONT_MONO (-3)
#define FONT_MONO_DATA detahard_FONT_MONO_ENABLE
#define FONT_MONO_HEIGHT FONT_DEFINE(detahard_FONT_MONO_ENABLE, _HEIGHT)
#define FONT_MONO_MAX_HEIGHT FONT_DEFINE(detahard_FONT_MONO_ENABLE, _MAX_HEIGHT)
#define FONT_MONO_BASELINE FONT_DEFINE(detahard_FONT_MONO_ENABLE, _BASELINE)
#endif

#ifdef detahard_FONT_BOLD_ENABLE
#include detahard_FONT_BOLD_INCLUDE
#define FONT_BOLD (-2)
#define FONT_BOLD_DATA detahard_FONT_BOLD_ENABLE
#define FONT_BOLD_HEIGHT FONT_DEFINE(detahard_FONT_BOLD_ENABLE, _HEIGHT)
#define FONT_BOLD_MAX_HEIGHT FONT_DEFINE(detahard_FONT_BOLD_ENABLE, _MAX_HEIGHT)
#define FONT_BOLD_BASELINE FONT_DEFINE(detahard_FONT_BOLD_ENABLE, _BASELINE)
#endif

#define MAX_FONT_H(A, B) ((A) > (B) ? (A) : (B))

#define FONT_MAX_HEIGHT_1 0
#ifdef detahard_FONT_NORMAL_ENABLE
#define FONT_MAX_HEIGHT_2 MAX_FONT_H(FONT_NORMAL_MAX_HEIGHT, FONT_MAX_HEIGHT_1)
#else
#define FONT_MAX_HEIGHT_2 FONT_MAX_HEIGHT_1
#endif

#ifdef detahard_FONT_BOLD_ENABLE
#define FONT_MAX_HEIGHT_3 MAX_FONT_H(FONT_BOLD_MAX_HEIGHT, FONT_MAX_HEIGHT_2)
#else
#define FONT_MAX_HEIGHT_3 FONT_MAX_HEIGHT_2
#endif

#ifdef detahard_FONT_DEMIBOLD_ENABLE
#define FONT_MAX_HEIGHT_4 \
  MAX_FONT_H(FONT_DEMIBOLD_MAX_HEIGHT, FONT_MAX_HEIGHT_3)
#else
#define FONT_MAX_HEIGHT_4 FONT_MAX_HEIGHT_3
#endif

#ifdef detahard_FONT_MONO_ENABLE
#define FONT_MAX_HEIGHT MAX_FONT_H(FONT_MONO_MAX_HEIGHT, FONT_MAX_HEIGHT_4)
#else
#define FONT_MAX_HEIGHT FONT_MAX_HEIGHT_4
#endif

int font_height(int font);
int font_max_height(int font);
int font_baseline(int font);
const uint8_t *font_get_glyph(int font, uint8_t c);

#endif  //_FONTS_H
