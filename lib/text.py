#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from enum import IntEnum
from typing import Optional

from lib.color import CT_Color
from .classes import *


class Direction(IntEnum):
    D0 = 0
    D90 = 90
    D180 = 180
    D270 = 270


class Weight(IntEnum):
    W100 = 100
    W200 = 200
    W300 = 300
    W400 = 400
    W500 = 500
    W600 = 600
    W700 = 700
    W800 = 800
    W900 = 900


class TextCode(Model):
    Text:str = ''
    AttrX:float = 0.0
    AttrY:float = 0.0
    AttrDeltaX:ST_Array = Field(default_factory=lambda:[])
    AttrDeltaY:ST_Array = Field(default_factory=lambda:[])

class CT_CGTransform(Model):
    AttrCodePosition:int = 0
    # select ↓
    AttrCodeCount:Optional[int] = 0
    AttrGlyphCount:Optional[int] = 0
    DomGlyphs:ST_Array = Field(default_factory=lambda:[])

class CGTransform(CT_CGTransform):pass

class CT_Text(Model):
    AttrID:str = ''
    AttrBoundary:CT_Box = Field(default_factory=lambda:CT_Box())
    AttrFont:ST_RefID = ''
    AttrSize:float = 0.0
    AttrStroke:Optional[bool] = False
    AttrFill:Optional[bool] = True
    AttrHScale:Optional[float] = 1.0
    AttrReadDirection:Optional[Direction] = Direction.D0
    AttrCharDirection:Optional[Direction] = Direction.D0
    AttrWeight:Optional[Weight] = 400
    AttrItalic:Optional[bool] = False
    DomFillColor:Optional[CT_Color] = Field(default_factory=lambda:CT_Color())
    DomStrokeColor:Optional[CT_Color] = Field(default_factory=lambda:CT_Color())
    NodesTextCode:List[TextCode] = Field(default_factory=lambda:[])
    NodesCGTransform:List[CGTransform] = Field(default_factory=lambda:[])
