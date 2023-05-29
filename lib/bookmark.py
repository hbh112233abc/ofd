#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .action import CT_Dest

class CT_Bookmark(Model):
    AttrName:str = ""
    DomDest:CT_Dest = None

class Bookmark(CT_Bookmark):pass
