REPO_ROOT := $(abspath ../..)
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: default
default: milestone-build-whl

#-----------------------------------------------------------------------------
.PHONY: camgen 
camgen: echo-camgen
	python3 ./src/camgen.py

.PHONY: echo-camgen
echo-camgen:
	@echo "Executing camgen..."
