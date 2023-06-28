#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path
from lib.dom import DOM
from lib.page import CT_PageBlock

from lib.res import Res

xml = Path(__file__).parent / 'files' / 'test3_unzip_files' / 'Doc_0' / 'DocumentRes.xml'

def test():
    res = Res(xml)
    res.show()

def test_res_content():
    dom = DOM(xml)
    dom_content = dom.query('CompositeGraphicUnits.CompositeGraphicUnit.Content')
    content = CT_PageBlock(dom_content)
    content.show()
