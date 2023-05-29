#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .color import CT_Color
from .model import Model
from .action import Action

class JoinEnum(str,Enum):
    Miter = "Miter"
    Round = "Round"
    Bevel = "Bevel"

class CapEnum(str,Enum):
    Butt = "Butt"
    Round = "Round"
    Square = "Square"

class CT_GraphicUnit(Model):
    AttrBoundary:ST_Box = None
    AttrName:Optional[str] = ""
    AttrVisible:Optional[bool] = True
    AttrCTM:Optional[ST_Array] = None
    AttrDrawParam:Optional[ST_RefID] = None
    AttrLineWidth:Optional[NonNegativeFloat] = 0.353
    AttrJoin:Optional[JoinEnum] = JoinEnum.Miter
    AttrCap:Optional[CapEnum] = CapEnum.Butt
    AttrDasOffset:Optional[NonNegativeFloat] = 0
    AttrDashPattern:Optional[ST_Array] = None
    AttrAlpha:Optional[int] = Field(255,ge=0,le=255)
    DomsActions: Optional[List[Action]] = None
    DomsClips: Optional[List["Clip"]] = None


class CT_DrawParam(Model):
    AttrRlative:Optional[ST_RefID] = None
    AttrLineWidth:Optional[NonNegativeFloat] = 0.353
    AttrJoin:Optional[JoinEnum] = JoinEnum.Miter
    AttrCap:Optional[CapEnum] = CapEnum.Butt
    AttrDasOffset:Optional[NonNegativeFloat] = 0
    AttrDashPattern:Optional[ST_Array] = None
    AttrMiterLimit:Optional[NonNegativeFloat] = 3.528
    DomFillColor:Optional[CT_Color] = None
    DomStrokeColor:Optional[CT_Color] = None
