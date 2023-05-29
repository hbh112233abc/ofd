#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *

class CT_Attachment(Model):
    AttrID:int = 0
    AttrName:str = ''
    AttrFormat:Optional[str] = None
    AttrCreationDate:Optional[Datetime] = None
    AttrModeDate:Optional[Datetime] = None
    AttrSize:Optional[float] = None
    AttrVisiable:Optional[bool] = None
    AttrUsage:Optional[str] = None
    DomFileLoc:Optional[ST_Loc] = None

class Attachment(CT_Attachment):pass

class Attachments(Model):
    NodesAttachment:List[Attachment] = None
