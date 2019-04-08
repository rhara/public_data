#!/usr/bin/env python

from khemia.net import khFTP as FTP
import os

ftp = FTP('ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF')
ftp.set_local_dir('data/pubchem')
ls = ftp.get_file_list()

D_remote = {name: size for name, size in ls}
D_remote_names = set(D_remote.keys())

D_local = {name:os.stat(f'{ftp.local_dir}/{name}').st_size for name in os.listdir(ftp.local_dir)}
D_local_names = set(D_local.keys())

for name in D_local_names - D_remote_names:
    os.unlink(f'{ftp.local_dir}/{name}')

targets = D_remote_names - D_local_names

in_both = D_remote_names.intersection(D_local_names)
for name in in_both:
    if D_local[name] != D_remote[name]:
        targets.add(name)
print(len(targets), 'files will be downloaded')

for name in sorted(targets):
    ftp.download(name)
