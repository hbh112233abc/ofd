#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from pathlib import Path
from lxml import etree


ofd_file = Path.cwd() / 'tests' / 'files' / 'test3_unzip_files' / 'OFD.xml'
def test_find():
    parse = etree.XMLParser(ns_clean=True)
    et = etree.parse(ofd_file,parse)
    root = et.getroot()
    print(root)
    cd = root.find("ModDate")
    assert cd.text == "2022-08-19"
    doc_root = root.findtext("DocRoot")
    assert doc_root == "Doc_0/Document.xml"
    custom_datas = root.find("CustomDatas")
    cds = custom_datas.findall("CustomData")
    assert isinstance(cds,list)
    assert len(cds)  == 2
