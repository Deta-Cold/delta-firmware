VOL_MOUNT = -v $(shell pwd):/release
IMAGETAG  = detahard-udev-build-env

all: .package

.package: .docker-image detahard.rules
	$(info Packaging ...)
	docker run -t $(VOL_MOUNT) $(IMAGETAG) /release/release.sh

detahard.rules:
	cp ../51-detahard.rules detahard.rules

.docker-image:
	$(info Preparing docker image ...)
	docker build -t $(IMAGETAG) .

shell: .docker-image
	docker run -i -t $(VOL_MOUNT) $(IMAGETAG) /bin/bash
