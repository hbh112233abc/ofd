#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .color import CT_ColorSpace
from .draw import CT_DrawParam
from .font import CT_Font
from .graph import CT_VectorG

class ColorSpace(CT_ColorSpace):pass

class DrawParam(CT_DrawParam):pass

class Font(CT_Font):pass

class CT_MultiMedia(Model):
    AttrType:str = ""
    DomMediaFile:ST_Loc = ""
    # select ↓
    AttrFormat:Optional[str] = ""

class MultiMedias(CT_MultiMedia):pass


class DocumentRes(Model):
    AttrBaseLoc:ST_Loc = ""
    NodesMultiMedias:List[CT_MultiMedia] = None

class PublicRes(Model):
    AttrBaseLoc:ST_Loc = ""
    NodesFonts:List[CT_Font] = Field(default_factory=lambda:[])


class CompositeGraphicUnit(CT_VectorG):pass

class Res(Model):
    AttrBaseLoc:ST_Loc = ""
    DomsColorSpaces: Optional[List[ColorSpace]] = None
    DomsDrawParams: Optional[List[DrawParam]] = None
    DomsFonts: Optional[List[Font]] = None
    DomsMultiMediass: Optional[List[MultiMedias]] = None
    DomsCompositeGraphicUnits: Optional[List[CompositeGraphicUnit]] = None
