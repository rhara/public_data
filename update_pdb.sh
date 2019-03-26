#!/bin/bash

SERVER=ftp.pdbj.org::ftp_data
PORT=873
MIRRORDIR=$PWD/data/PDB

rsync -rlptivz --delete --port=$PORT ${SERVER}/structures/divided/pdb/ $MIRRORDIR/
