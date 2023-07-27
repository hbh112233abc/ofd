#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path

from lib.page import *
from lib.dom import DOM

xml = Path(__file__).parent / 'files' / 'test3_unzip_files' / 'Doc_0' / 'Pages' / 'Page_0' / 'Content.xml'
root = DOM(xml)

def test_page():
    page = Page(xml)
    print(page)
    assert page is not None

def test_content():
    content_dom = root.query('Content')
    print(content_dom)
    content = Content(content_dom)
    print(content)

def test_layer():
    layer_dom = root.query('Content.Layer')
    layer = Layer(layer_dom)
    print(layer)
    print(layer.CompositeObject)
