#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from pathlib import Path
from lib.document import Document

def test_document():
    file = Path.cwd() / 'tests' / 'files' / 'test3_unzip_files' / 'Doc_0' / 'Document.xml'
    res = Document(file)
    print(res)
    assert res is not None
