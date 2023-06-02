NAME  = bootloader-unaligned

OBJS += startup.o
OBJS += bootloader.o
OBJS += usb.o

# Overrides from libdetahard.
# Objects ending with 'small.o' are built with -Os to make the bootloader smaller.
CFLAGS += -DFONT_SKIP_FIXED=1
OBJS += ../buttons.small.o
OBJS += ../common.small.o
OBJS += ../flash.small.o
OBJS += ../fw_signatures.small.o
OBJS += ../gen/bitmaps.small.o
OBJS += ../gen/fonts.small.o
OBJS += ../layout.small.o
OBJS += ../memory.small.o
OBJS += ../oled.small.o
OBJS += ../random_delays.small.o
OBJS += ../rng.small.o
OBJS += ../setup.small.o
OBJS += ../supervise.small.o
OBJS += ../timer.small.o
OBJS += ../usb21_standard.small.o
OBJS += ../usb_standard.small.o
OBJS += ../util.small.o
OBJS += ../webusb.small.o
OBJS += ../winusb.small.o

# Overrides from detahard-crypto
CFLAGS += -DUSE_PRECOMPUTED_CP=0
CFLAGS += -DUSE_PRECOMPUTED_IV=0
OBJS += ../vendor/detahard-crypto/bignum.small.o
OBJS += ../vendor/detahard-crypto/ecdsa.small.o
OBJS += ../vendor/detahard-crypto/hmac_drbg.small.o
OBJS += ../vendor/detahard-crypto/memzero.small.o
OBJS += ../vendor/detahard-crypto/secp256k1.small.o
OBJS += ../vendor/detahard-crypto/sha2.small.o

OPTFLAGS ?= -Os

include ../Makefile.include

# Remove libdetahard from linking since we specified the small versions
LDLIBS := $(filter-out -ldetahard,$(LDLIBS))

bootloader.bin: $(NAME).bin
	./firmware_align.py $< $@

all: bootloader.bin
