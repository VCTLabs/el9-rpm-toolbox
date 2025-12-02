#!/bin/bash

OUTPUT=${1:-mirrors-list.txt}
MIRROR_URL=https://mirrors.rockylinux.org/mirrormanager/mirrors/Rocky/9.6/x86_64
COUNTRY=US
MASTER_MIRROR=dl.rockylinux.org
REPO_CONFIG=/etc/yum.repos.d/rocky.repo

dnf install -y python3-pip
pip install html2text

## get list of mirrors

# published as html table with row per mirror
# look for 'US' label (except master mirror, already in repo config)
# then pick https link out of 4th column
curl -s $MIRROR_URL |
    html2text --no-wrap-links -b 0  |
    grep -w $COUNTRY |
    grep -v $MASTER_MIRROR |
    cut -d '|' -f 4- |
    grep -o 'https://[[:alnum:]./]*' > $OUTPUT

## update dnf repo config

cp $REPO_CONFIG $REPO_CONFIG.bak$$

# switch from mirrorlist to explicit baseurl entries
sed -i "s/^mirrorlist/#mirrorlist/" $REPO_CONFIG
sed -i "s/^#baseurl/baseurl/" $REPO_CONFIG

# add mirrors as fallbacks
for MIRROR in `cat $OUTPUT` ; do
    # for each original baseurl entry, duplicate line and substitute in this specific mirror
    sed -i "/$MASTER_MIRROR/ p; s|https\?://$MASTER_MIRROR/.contentdir|$MIRROR|;" $REPO_CONFIG
done

## dnf refresh after changing conf

dnf clean all
dnf check-update
