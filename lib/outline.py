#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from typing import List, Optional

from .classes import *
from .model import DOMModel
from .action import Action


class CT_OutlineElem(DOMModel):
    AttrTitle:str = ''
    AttrCount:Optional[int] = 0
    AttrExpanded:Optional[bool] = True
    DomsActions:Optional[List[Action]] = None
    DomsOutlineElem:Optional[List["CT_OutlineElem"]]= None


class OutlineElem(CT_OutlineElem):pass
