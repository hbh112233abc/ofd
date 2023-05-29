#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from lib.model  import DOMModel

from lib.ofd import DocBody

def test_docbody():
    body = DocBody()
    breakpoint()
    s = body.tostring()
    print(s)
    assert "ofd:" in s
