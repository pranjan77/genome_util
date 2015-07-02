
MODULE = core_genome_util
MODULE_CAPS = KBaseCoreGenomeUtil

SPEC_FILE = KBaseCoreGenomeUtil.spec

#End of user defined variables

GITCOMMIT := $(shell git rev-parse --short HEAD)
TAGS := $(shell git tag --contains $(GITCOMMIT))

TOP_DIR = $(shell python -c "import os.path as p; print p.abspath('../..')")

TOP_DIR_NAME = $(shell basename $(TOP_DIR))

DIR = $(shell pwd)

LIB_DIR = lib

LBIN_DIR = bin

EXECUTABLE_SCRIPT_NAME = run_$(MODULE_CAPS).sh


default: compile-kb-module build-executable-script-python

compile-kb-module:
	kb-mobu compile $(SPEC_FILE) \
		--out $(LIB_DIR) \
		--pyclname biokbase.$(MODULE).$(MODULE_CAPS)Client \
		--pysrvname biokbase.$(MODULE).$(MODULE_CAPS) \
		--pyimplname biokbase.$(MODULE).$(MODULE_CAPS)Impl;

# NOTE: script generation and wrapping in various languages should be
# handled in a kb-mobu tool, but for now we just generate the
# script within this makefile
build-executable-script-python: setup-local-dev-kb-py-libs
	mkdir -p $(LBIN_DIR)
	echo '#!/bin/bash' > $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	echo 'export PYTHONPATH="$(DIR)/$(LIB_DIR)"' >> $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	echo 'python $(DIR)/lib/biokbase/$(MODULE)/$(MODULE_CAPS).py $$1 $$2 $$3' \
		>> $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
	chmod +x $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME)
ifeq ($(TOP_DIR_NAME), dev_container)
	cp $(LBIN_DIR)/$(EXECUTABLE_SCRIPT_NAME) $(TOP_DIR)/bin/.
endif


setup-local-dev-kb-py-libs:
	touch lib/biokbase/__init__.py
	touch lib/biokbase/$(MODULE)/__init__.py
	rsync -vrh ../kbapi_common/lib/biokbase/* lib/biokbase/.
	rsync -vrh ../auth/lib/biokbase/* lib/biokbase/.
	#	--exclude TestMathClient.pl --exclude TestPerlServer.sh \
	#	--exclude *.bak* --exclude AuthConstants.pm


clean:
	rm -rfv $(LBIN_DIR)



# below are targets for deploying in a KBase environment - note that these
# are hacked together to get things working for now, and should be refactored if
# this example is going to be copied into a production service
ifeq ($(TOP_DIR_NAME), dev_container)
include $(TOP_DIR)/tools/Makefile.common
include $(TOP_DIR)/tools/Makefile.common.rules

DEPLOY_RUNTIME ?= /kb/runtime
TARGET ?= /kb/deployment
#SERVICE_DIR ?= $(TARGET)/services/$(MODULE)

deploy: deploy-scripts

deploy-scripts: deploy-libs deploy-executable-script

deploy-service: deploy-libs deploy-executable-script deploy-service-scripts deploy-cfg

deploy-libs:
	@echo "Deploying libs to target: $(TARGET)"
	#rsync -vrh lib/* $(TARGET)/lib/. \
	#	--exclude TestMathClient.pl --exclude TestPerlServer.sh \
	#	--exclude *.bak* --exclude AuthConstants.pm

deploy-executable-script:
	@echo "Installing executable scripts to target: $(TARGET)/bin"
	echo '#!/bin/bash' > $(TARGET)/bin/$(EXECUTABLE_SCRIPT_NAME)
	#echo 'export KB_RUNTIME=$(DEPLOY_RUNTIME)' >> $(TARGET)/bin/$(EXECUTABLE_SCRIPT_NAME)
	#echo 'export PATH=$(TARGET)/bin:$(DEPLOY_RUNTIME)/bin:$$PATH' >> $(TARGET)/bin/$(EXECUTABLE_SCRIPT_NAME)
	#echo 'export PERL5LIB=$(TARGET)/lib' >> $(TARGET)/bin/$(EXECUTABLE_SCRIPT_NAME)
	echo 'python $(TARGET)/lib/Bio/KBase/$(MODULE)/$(MODULE_CAPS)Server.pm $$1 $$2 $$3' \
		>> $(TARGET)/bin/$(EXECUTABLE_SCRIPT_NAME)
	chmod +x $(TARGET)/bin/$(EXECUTABLE_SCRIPT_NAME)

deploy-service-scripts:


endif
