#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .color import CT_ColorSpace
from .draw import CT_DrawParam
from .font import CT_Font
from .graph import CT_VectorG

class Fonts(Model):
    NodesFont:List[CT_Font] = None
class ColorSpaces(Model):
    NodesColorSpace:List[CT_ColorSpace] = None

class DrawParams(Model):
    NodesDrawParam:List[CT_DrawParam] = None

class CT_MultiMedia(Model):
    AttrType:str = ""
    DomMediaFile:ST_Loc = ""
    # select ↓
    AttrFormat:Optional[str] = ""


class MultiMedias(Model):
    NodesMultiMedia:List[CT_MultiMedia] = None

class CompositeGraphicUnits(Model):
    NodesCompositeGraphicUnit:List[CT_VectorG] = None

class Res(Model):
    AttrBaseLoc:ST_Loc = ""
    DomColorSpaces: Optional[ColorSpaces] = None
    DomDrawParams: Optional[DrawParams] = None
    DomFonts: Optional[Fonts] = None
    DomMultiMedias: Optional[MultiMedias] = None
    DomCompositeGraphicUnits: Optional[CompositeGraphicUnits] = None

    def fonts(self):
        if not self.__children__.get('fonts'):
            self.__children__['fonts'] = {}
            for font in self.DomFonts.NodesFont:
                self.__children__['fonts'][font.AttrID] = self.xml.parent / self.AttrBaseLoc / font.DomFontFile.text
        return self.__children__['fonts']
