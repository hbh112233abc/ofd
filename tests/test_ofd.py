#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path
from lib.ofd import OFD,DocBody
from lxml import etree

def test_ofd_encode():
    ofd_file = Path.cwd() / 'tests' / 'files' / 'test3_unzip_files' / 'OFD.xml'
    ofd = OFD(ofd_file)
    print(ofd)
    assert ofd is not None

def test_ofd_encode():
    ofd = OFD()
    ofd.AttrVersion = "1.1"
    ofd.AttrDocType = "OFD"
    body = DocBody()
    ofd.NodesDocBodies = [body]
    print(ofd.encode())
    print(etree.tostring(ofd.encode()))
    breakpoint()
    assert ofd is not None
