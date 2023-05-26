#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path

import lxml.etree import ET
from lib.ofd import OFD

from lib.zip import extract
from lib.classes import *

# docNS that have to be part of every ofd file
FILE_DOC_NS = {"ofd": "http://www.ofdspec.org/2016"}

class Reader:
    def __init__(self,ofd_file:str) -> None:
        self.ofd_file = Path(ofd_file)
        if not self.ofd_file.exists():
            raise FileNotFoundError("ofd file %s not found" % ofd_file)
        self.ofd_path = extract(self.ofd_file)

        self.OFD = OFD(self.ofd_path / 'OFD.xml')
        self.Documents = []
        for doc_body in self.OFD.DocBodies:
            doc_xml = self.ofd_path / doc_body.DocRoot
            self.Documents.append(Document(doc_xml))
