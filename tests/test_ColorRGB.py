#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

import pytest
from lib.classes import ColorRGB

def test_init_rgb():
    c = ColorRGB(0, 0, 0)
    assert str(c) == '0 0 0'
    with pytest.raises(ValueError):
        ColorRGB(256, 0, 0)
    with pytest.raises(ValueError):
        ColorRGB(0, 256, 0)
    with pytest.raises(ValueError):
        ColorRGB(0, 0, 256)
    with pytest.raises(ValueError):
        ColorRGB(-1, 0, 0)
    with pytest.raises(ValueError):
        ColorRGB(0, -1, 0)
    with pytest.raises(ValueError):
        ColorRGB(0, 0, -1)

def test_init_str():
    c = ColorRGB("100 50 255")
    assert str(c) == "100 50 255"
    with pytest.raises(ValueError):
        ColorRGB("100 50 255 110")
    with pytest.raises(ValueError):
        ColorRGB("100 50")
    with pytest.raises(ValueError):
        ColorRGB("100 50 25a")
    with pytest.raises(ValueError):
        ColorRGB("100 50 256")
