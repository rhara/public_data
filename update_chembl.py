#!/usr/bin/env python

from mysync import MyFTP

ftp = MyFTP('ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_24_1')
ftp.set_local_dir('data/ChEMBL/ChEMBLdb/24_1')
ftp.download('LICENSE', mode='text')
ftp.download('REQUIRED.ATTRIBUTION', mode='text')
ftp.download('checksums.txt', mode='text')
ftp.download('chembl_24_1_schema_documentation.html', mode='text')
ftp.download('chembl_24_1.fps.gz')
ftp.download('chembl_24_1_bio.fa.gz')
ftp.download('chembl_24_1_release_notes.txt', mode='text')
ftp.download('README', mode='text')
ftp.download('chembl_24_1_monomer_library.xml', mode='text')
ftp.download('chembl_24_1_chemreps.txt.gz')
ftp.download('chembl_24_1.sdf.gz')
ftp.download('chembl_24_1_schema_documentation.txt', mode='text')
ftp.download('chembl_24_1.fa.gz')
ftp.download('chembl_24_1_schema.png')
ftp.download('chembl_uniprot_mapping.txt', mode='text')

ftp = MyFTP('ftp://ftp.ebi.ac.uk/pub/databases/chembl/GPCRSARfari/releases/3.00')
ftp.set_local_dir('data/ChEMBL/GPCRSARfari/3.00')
ftp.download('gs_bioactivity.txt.gz')
ftp.download('gs_compound.sdf.gz')
ftp.download('gs_compound.txt.gz')
ftp.download('gs_protein.txt.gz')
ftp.download('gs_sequence.fa.gz')

ftp = MyFTP('ftp://ftp.ebi.ac.uk/pub/databases/chembl/KinaseSARfari/releases/5.01')
ftp.set_local_dir('data/ChEMBL/KinaseSARfari/5.01')
ftp.download('README', mode='text')
ftp.download('ks_aln.txt.gz')
ftp.download('ks_bioactivity.txt.gz')
ftp.download('ks_compound.sdf.gz')
ftp.download('ks_compound.txt.gz')
ftp.download('ks_protein.txt.gz')
ftp.download('ks_sequence.fa.gz')

ftp = MyFTP('ftp://ftp.ebi.ac.uk/pub/databases/chembl/MalariaData/releases/mmv_3')
ftp.set_local_dir('data/ChEMBL/MalariaData/mmv_3')
ftp.download('MMV_3_release_notes.txt', mode='text')
ftp.download('MalariaData_bioactivity.txt.gz')
ftp.download('MalariaData_compound.sdf.gz')

ftp = MyFTP('ftp://ftp.ebi.ac.uk/pub/databases/chembl/SureChEMBL/data')
ftp.set_local_dir('data/ChEMBL/SureChEMBL')
ftp.download('SureChEMBL_20141001_1.sdf.gz')
ftp.download('SureChEMBL_20141001_2.sdf.gz')
ftp.download('SureChEMBL_20150101_3.sdf.gz')
ftp.download('SureChEMBL_20150401_4.sdf.gz')
ftp.download('SureChEMBL_20150701_5.sdf.gz')
ftp.download('SureChEMBL_20151001_6.sdf.gz')
ftp.download('SureChEMBL_20160101_7.sdf.gz')
ftp.download('SureChEMBL_20160401_8.sdf.gz')
ftp.download('SureChEMBL_20160701_9.sdf.gz')
ftp.download('SureChEMBL_20161001_10.sdf.gz')
ftp.download('SureChEMBL_20170101_11.sdf.gz')
ftp.download('SureChEMBL_20170401_12.sdf.gz')
ftp.download('SureChEMBL_20170701_13.sdf.gz')
ftp.download('SureChEMBL_20171001_14.sdf.gz')
ftp.download('SureChEMBL_20180101_15.sdf.gz')
ftp.download('SureChEMBL_20180401_16.sdf.gz')
ftp.download('SureChEMBL_20180701_17.sdf.gz')
