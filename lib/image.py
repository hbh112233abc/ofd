#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .color import CT_Color

class Border(Model):
    AttrLineWidth:Optional[NonNegativeFloat] = 0.353
    AttrHorizonalCornerRadius:Optional[NonNegativeFloat] = 0
    AttrVerticalCornerRadius:Optional[NonNegativeFloat] = 0
    AttrDashOffset:Optional[NonNegativeFloat] = 0
    AttrDasPattern:Optional[ST_Array] = None
    DomBorderColor:CT_Color = None

class CT_Image(Model):
    AttrResourceID: ST_RefID = 0
    AttrSubstitution:Optional[ST_RefID] = None
    AttrImageMask:Optional[ST_RefID] = None
    DomBorder:
