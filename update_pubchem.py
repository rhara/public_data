#!/usr/bin/env python

from mysync import MyFTP

ftp = MyFTP('ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF')
ftp.set_local_dir('data/pubchem')
ls = ftp.get_file_list()

import re

pat = re.compile('^Compound_([0-9]+)_([0-9]+)\.sdf\.gz$')
for name in ls:
    m = pat.match(name)
    if m is None:
        continue
    a = int(m.group(1))
    b = int(m.group(2))
    if a < 75950000:
        print(f'{name} skip')
        continue
    mode = 'binary' if name.endswith('.sdf.gz') else 'text'
    ftp.download(name, mode=mode)
