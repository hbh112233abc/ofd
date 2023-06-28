#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path

from lib.document import Document

xml = Path(__file__).parent / 'files' / 'test3_unzip_files' / 'Doc_0' / 'Document.xml'

def test_document():
    doc = Document(xml)
    pages = doc.pages()
    assert len(pages) > 0
    print(doc)
