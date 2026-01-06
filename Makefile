# Prepare variables
ifeq ($(TMP),)
TMP := $(CURDIR)/tmp
endif

ifndef NAME
$(error NAME is not set)
endif

VERSION = $(shell grep ^Version specs/$(NAME).spec | sed 's/.* //')

# Define special targets
all: packages

# Temporary directory, include .fmf to prevent exploring tests there
tmp:
	mkdir -p $(TMP)/.fmf

# RPM packaging
tarball: tmp
	dnf -y builddep --spec specs/$(NAME).spec
	mkdir -p $(TMP)/SOURCES
	cp specs/*.patch $(TMP)/SOURCES/
	spectool --define '_topdir $(TMP)' -g -R specs/$(NAME).spec
version:
	@echo "$(VERSION)"
rpm: tarball
	rpmbuild --define '_topdir $(TMP)' -bb specs/$(NAME).spec
srpm: tarball
	rpmbuild --define '_topdir $(TMP)' -bs specs/$(NAME).spec
packages: rpm srpm

clean:
	rm -f *.spec
	rm -rf $(TMP)
