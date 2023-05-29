#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .model import Model

class CharsetEnum(str,Enum):
    symbol = 'symbol'
    prc = 'prc'
    big5 = 'big5'
    unicode = 'unicode'

class CT_Font(Model):
    AttrID:str = ''
    AttrFontName:str = ''
    AttrFamilyName:Optional[str] = None
    AttrCharset:Optional[CharsetEnum] = CharsetEnum.unicode
    AttrItalic:Optional[bool] = False
    AttrBold:Optional[bool] = False
    AttrSerif:Optional[bool] = False
    AttrFixedWidth:Optional[bool] = False

    DomFontFile:ST_Loc = None
