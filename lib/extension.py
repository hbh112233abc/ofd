#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from typing import Any
from .classes import *

class Property(Model):
    AttrName:str = ""
    AttrType:Optional[str] = ""
    Text:Optional[str] = ""

class CT_Extension(Model):
    AttrAppName:str = ""
    AttrRefId: ST_RefID = 0
    AttrCompany:Optional[str] = None
    AttrAppVersion:Optional[str] = None
    AttrDate:Optional[datetime] = None
    DomsProperty:List[Property] = None
    DomsData:List[Any] = None
    DomsExtendData: List[ST_Loc] = None


class Extensions(Model):
    NodesExtensions:List[Extension] = None
