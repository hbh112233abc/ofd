#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

import pytest
from lib.classes import ColorRGB,CT_Path

def test_CT_Path():
    ctp = CT_Path()
    assert ctp.ID == ''
    assert isinstance(ctp.FillColor,ColorRGB)
    assert isinstance(ctp.StrokeColor,ColorRGB)
    ctp.Stroke = 'true'
    assert ctp.Stroke == True
    ctp.Stroke = 'false'
    assert ctp.Stroke == False

    with pytest.raises(ValueError):
        ctp.Stroke = 'hhh'
    with pytest.raises(ValueError):
        ctp.Rule = 'aaa'
