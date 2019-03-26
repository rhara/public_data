#!/usr/bin/env python

from mysync import MyFTP

ftp = MyFTP('ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF')
ftp.set_local_dir('data/pubchem')
ls = ftp.get_file_list()
for name in ls:
    mode = 'binary' if name.endswith('.sdf.gz') else 'text'
    ftp.download(name, mode=mode)
