#!/usr/bin/env python

"""
For Clean-Lead-Like and Standard-All-Purchasable
"""

from khemia.net import khHTTP as HTTP
import re

pat = re.compile('([0-9]+)_(.)([0-9]+)\.([0-9]+)\.sdf\.gz')
def name_key(a):
    m1 = pat.match(a)
    assert m1
    return (int(m1.group(1)), m1.group(2), int(m1.group(3)), int(m1.group(4)))


### Clean-Lead-Like

http = HTTP('http://zinc.docking.org/db/bysubset/11')
http.set_local_dir('data/ZINC12/Clean-Lead-Like')
http.download('usual.sdf.csh')

names = []
for line in open('data/ZINC12/Clean-Lead-Like/usual.sdf.csh', 'rt'):
    line = line.strip()
    if line.endswith('sdf.gz'):
        names.append(line)
names.sort(key=name_key)

for name in names:
    http.download(name)


### Standard-All-Purchasable

http = HTTP('http://zinc.docking.org/db/bysubset/6')
http.set_local_dir('data/ZINC12/Standard-All-Purchasable')
http.download('usual.sdf.csh')

names = []
for line in open('data/ZINC12/Standard-All-Purchasable/usual.sdf.csh', 'rt'):
    line = line.strip()
    if line.endswith('sdf.gz'):
        names.append(line)
names.sort(key=name_key)

for name in names:
    http.download(name)

