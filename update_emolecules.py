#!/usr/bin/env python

from mysync import MyHTTP

http = MyHTTP('http://downloads.emolecules.com/free/2019-03-01')
http.set_local_dir('data/eMolecules/free/2019-03-01')

http.download('version.smi.gz')
