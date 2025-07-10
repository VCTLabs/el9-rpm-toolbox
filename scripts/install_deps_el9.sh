#!/usr/bin/env bash
#

set -e
set -o pipefail
set -x

dnf install -y 'dnf-command(config-manager)'
dnf config-manager --set-enabled crb
dnf install -y dnf-utils epel-release
dnf search --refresh epel
dnf install -y sudo git make wget rpm-build rpm-devel rpmlint rpmdevtools python3-pip
