FRONT_TAG ?= defendid:dev

.PHONY: build-front
build-front:
	cd front
	docker build -t $(FRONT_TAG) .
