#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path

from lib.ofd import OFD

def test_ofd():
    ofd_file = Path.cwd() / 'tests' / 'files' / 'test3_unzip_files' / 'OFD.xml'
    ofd = OFD(ofd_file)
    ofd.show()
    assert ofd is not None
    documents = ofd.documents()
    assert len(documents) > 0
    print(documents)
