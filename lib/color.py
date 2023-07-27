#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from enum import IntEnum
from typing import Optional

from pydantic import NonNegativeInt,NonNegativeFloat

from .classes import *


class BitsPerComponent(IntEnum):
    BPC1 = 1
    BPC2 = 2
    BPC4 = 4
    BPC8 = 8
    BPC16 = 16

class ColorSpaceType(str,Enum):
    GRAY = "GRAY"
    RGB = "RGB"
    CMYK = "CMYK"

class Palette(Model):
    NodesCV:ST_Array = []

class CT_ColorSpace(Model):
    AttrType:ColorSpaceType = ColorSpaceType.RGB
    AttrBitsPerComponent:Optional[BitsPerComponent] = BitsPerComponent.BPC8
    AttrProfile:Optional[ST_Loc] = ''
    DomPalette:Optional[Palette] = None

class ReflectMethod(str,Enum):
    Normal = "Normal"
    Column = "Column"
    Row = "Row"
    RowAndColumn = "RowAndColumn"

class RelativeTo(str,Enum):
    Page = "Page"
    Object = "Object"

class CellContent(Model):
    NodesPageBlock:Optional["CT_PageBlock"] = None
    AttrThumbnail:Optional[ST_RefID] = None

class CT_Pattern(Model):
    AttrWidth:float = 0.0
    AttrHeight:float = 0.0
    AttrXStep:Optional[float] = 0.0
    AttrYStep:Optional[float] = 0.0
    AttrReflectMethod:Optional[ReflectMethod] = "Normal"
    AttrRelativeTo:Optional[RelativeTo] = "Object"
    AttrCTM:Optional[ST_Array] = None
    NodesCellContent:List["CT_PageBlock"] = None

class MapType(str,Enum):
    Direct = "Direct"
    Repeat = "Repeat"
    Reflect = "Reflect"

class Extend(IntEnum):
    E0 = 0
    E1 = 1
    E2 = 2
    E3 = 3

class Segment(Model):
    DomColor:"CT_Color" = None
    AttrPosition:Optional[float] = Field(None,ge=0,le=1)

class Shd(Model):
    AttrStartPoint:ST_Pos = Field(default_factory=lambda:[0,0])
    AttrEndPoint:ST_Pos = Field(default_factory=lambda:[0,0])
    NodesSegment:List[Segment] = Field(default_factory=lambda:[],min_items=2)
    AttrMapType:Optional[MapType] = "Direct"
    AttrMapUnit:Optional[float] = None
    AttrExtend:Optional[Extend] = 0

class CT_AxialShd(Shd):pass

class CT_RadialShd(Model):
    AttrEndRadius:NonNegativeInt = 0
    AttrStartRadius:Optional[NonNegativeInt] = 0
    AttrEccentricity:Optional[float] = Field(0,ge=0,lt=1.0)
    AttrAngle:Optional[float] = Field(0,ge=0,le=360)

class Point(Model):
    AttrX:NonNegativeFloat = 0.0
    AttrY:NonNegativeFloat = 0.0
    AttrEdgeFlag:Optional[NonNegativeInt] = None
    DomColor:"CT_Color" = None

class CT_GouraudShd(Model):
    AttrExtend:Optional[int] = Field(0,ge=0,le=1)
    NodesPoint:List[Point] = Field([],min_items=3)
    DomBackColor:"CT_Color" = None

class CT_LaGouraudShd(Model):
    AttrVerticesPerRow:NonNegativeInt = 0
    AttrExtend:Optional[int] = Field(0,ge=0,le=1)
    NodesPoint:List[Point] = Field([],min_items=4)
    DomBackColor:"CT_Color" = None

class CT_Color(Model):
    AttrValue:Optional[ST_Array] = None
    AttrIndex:Optional[NonNegativeInt] = None
    AttrColorSpace:Optional[ST_RefID] = None
    AttrAlpha:Optional[int] = Field(255,ge=0,le=255)
    DomPattern:Optional[CT_Pattern] = None
    DomAxialShd:Optional[CT_AxialShd] = None
    DomRadialShd:Optional[CT_RadialShd] = None
    DomGouraudShd:Optional[CT_GouraudShd] = None
    DomLaGouraudShd:Optional[CT_LaGouraudShd] = None
