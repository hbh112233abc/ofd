#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from typing import List, Optional

from .classes import *
from .model import Model
from .action import Actions

class CT_OutlineElem(Model):
    AttrTitle:str = ''
    AttrCount:Optional[int] = 0
    AttrExpanded:Optional[bool] = True
    DomActions:Optional[Actions] = None
    NodesOutlineElem:Optional[List["CT_OutlineElem"]]= None


class OutlineElem(CT_OutlineElem):pass
