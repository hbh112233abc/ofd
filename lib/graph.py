#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from lib.model import TAG_PREFIX
from .classes import *
from .color import CT_Color
from .page import CT_PageBlock

class RuleEnum(str,Enum):
    NonZero = "NonZero"
    EvenOdd = "EvenOdd"

class CT_Path(Model):
    AttrID:str = ''
    AttrBoundary:CT_Box = Field(default_factory=lambda:CT_Box())
    AttrStroke:Optional[bool] = True
    AttrFill:Optional[bool] = False
    AttrRule:Optional[RuleEnum] = RuleEnum.NonZero # NonZero or EvenOdd
    DomAbbreviatedData:List[str] = Field(default_factory=lambda:[])
    DomFillColor:CT_Color = Field(default_factory=lambda:ColorRGB(255, 255, 255))
    DomStrokeColor:CT_Color = Field(default_factory=lambda:ColorRGB(0, 0, 0))

class Path(CT_Path):
    pass

class Move(Model):
    AttrPoint1:ST_Pos = None

class Line(Model):
    AttrPoint1:ST_Pos = None

class QuadraticBezier(Model):
    AttrPoint1:ST_Pos = None
    AttrPoint2:ST_Pos = None

class CubicBezier(Model):
    AttrPoint1:Optional[ST_Pos] = None
    AttrPoint2:Optional[ST_Pos] = None
    AttrPoint3:ST_Pos = None

class Arc(Model):
    AttrSweepDirection:bool = None
    AttrLargeArc:bool = None
    AttrRotationAngle:float = None
    AttrEllipseSize:ST_Array = None
    AttrEndPoint:ST_Pos = None

class Close(Model):pass


class Area(Model):
    AttrStart:ST_Pos = None
    NodesPath:List[Union[Move,Line,QuadraticBezier,CubicBezier,Arc,Close]] = Field(default_factory=lambda:[],min_items=1)

    def paths(self):
        if not self.__children__.get('paths'):
            self.__children__['paths'] = []
            for child in self.dom:
                tag = child.tag.strip(TAG_PREFIX)
                path = eval(tag)(child)
                self.__children__['paths'].append(path)
        return self.__children__['paths']

class CT_Region(Model):
    NodesArea: List[Area] = Field(default_factory=lambda:[],min_items=1)

class CT_VectorG(Model):
    AttrWidth:float = 0.0
    AttrHeight:float = 0.0
    DomThumbnail:ST_RefID = None
    DomSubstitution:ST_RefID = None
    DomContent:CT_PageBlock = None
