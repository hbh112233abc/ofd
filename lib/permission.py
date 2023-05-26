#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from datetime import datetime

from .classes import *

class Print(DOMModel):
    AttrPrintable:bool = True
    AttrCopies:Optional[int] = -1


class ValidPeriod(DOMModel):
    AttrStartDate:Optional[datetime] = None
    AttrEndDate:Optional[datetime] = None


class CT_Permission(DOMModel):
    DomEdit:Optional[bool] = True
    DomAnnot:Optional[bool] = True
    DomExport:Optional[bool] = True
    DomSignature:Optional[bool] = True
    DomWatermark:Optional[bool] = True
    DomPrintScreen:Optional[bool] = True
    DomPrint:Optional[Print] = None
    DomValidPeriod:Optional[ValidPeriod] = None
