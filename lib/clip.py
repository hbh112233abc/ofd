#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .graph import CT_Path
from .text import CT_Text

class Area(Model):
    AttrDrawParam:Optional[ST_RefID] = None
    AttrCTM:Optional[ST_Array] = None
    DomPath:CT_Path = None
    DomText:CT_Text = None

class CT_Clip(Model):
    DomsArea:List[Area] = Field(default_factory=lambda:[],min_items=1)

class Clip(CT_Clip):pass
