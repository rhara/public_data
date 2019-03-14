#!/bin/bash

SERVER=ftp.pdbj.org::ftp_data
PORT=873
MIRRORDIR=/home/rhara/github.com/public_data/data/PDB

rsync -rlptivz --delete --port=$PORT ${SERVER}/structures/divided/pdb/ $MIRRORDIR/
