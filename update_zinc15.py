#!/usr/bin/env python

from khemia.net import khHTTP as HTTP
import os, itertools, re

http = HTTP('http://files.docking.org/2D')

http.set_local_dir('data/ZINC15')

ss = ['ABCDEFGHIJK', 'ABCDEFGHIJK', 'ABCDE', 'ABCD']
bases = [''.join(it) for it in itertools.product(*ss)]
heads = sorted(set([it[:2] for it in bases]))

for base in bases:
    head = base[:2]
    http.download(f'{head}/{base}.smi')
