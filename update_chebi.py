#!/usr/bin/env python

from khemia.net import khFTP as FTP

ftp = FTP('ftp://ftp.ebi.ac.uk/pub/databases/chebi/SDF')
ftp.set_local_dir('data/ChEBI')

ftp.download('ChEBI_complete.sdf.gz')
ftp.download('ChEBI_complete_3star.sdf.gz')
ftp.download('ChEBI_lite.sdf.gz')
ftp.download('ChEBI_lite_3star.sdf.gz')
