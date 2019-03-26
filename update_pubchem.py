#!/usr/bin/env python

from mysync import MyFTP

ftp = MyFTP('ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF')
ftp.set_local_dir('data/pubchem')
ls = ftp.get_file_list()
for name in ls:
    # if name.startswith('Compound_00'):
    #     continue
    # if name.startswith('Compound_01'):
    #     continue
    # if name.startswith('Compound_02'):
    #     continue
    # if name.startswith('Compound_030'):
    #     continue
    # if name.startswith('Compound_031'):
    #     continue
    # if name.startswith('Compound_032'):
    #     continue
    # if name.startswith('Compound_033'):
    #     continue
    # if name.startswith('Compound_034'):
    #     continue
    # if name.startswith('Compound_035'):
    #     continue
    # if name.startswith('Compound_036'):
    #     continue
    mode = 'binary' if name.endswith('.sdf.gz') else 'text'
    ftp.download(name, mode=mode)
