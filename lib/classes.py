#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from datetime import date, datetime
from enum import Enum

from typing import List, Union,Optional
from uuid import uuid4

from pydantic import BaseModel,Field,NonNegativeFloat
from xml.etree.ElementTree import Element
import numpy as np

from .st import *
from .util import boolVal
from .dom import DOM
from .model import Model

class ColorRGB:
    r:int = 0
    g:int = 0
    b:int = 0
    def __init__(self,*args,**kwargs):
        if len(args) == 1:
            return self.__init_str__(*args)
        if len(args) == 3:
            return self.__init_rgb__(*args)
        if 'color' in kwargs:
            return self.__init_str__(**kwargs)
        if 'r' in kwargs:
            return self.__init_rgb__(**kwargs)

    def __init_str__(self,color:str):
        color_split = color.split(' ')
        if len(color_split) != 3:
            raise ValueError('Invalid color string format `[0-255] [0-255] [0-255]`')
        self.__init__(*[int(x) for x in color_split])

    def __init_rgb__(self,r,g,b:int):
        if not 0<= r <= 255:
            raise ValueError('Invalid color value,`r` must between 0,255')
        if not 0<= g <= 255:
            raise ValueError('Invalid color value,`g` must between 0,255')
        if not 0<= b <= 255:
            raise ValueError('Invalid color value,`b` must between 0,255')
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.r} {self.g} {self.b}"


class Date(date):
    def __new__(cls,date_str:str) -> None:
        if date_str is None:
            return None
        if isinstance(date_str,(DOM,Element)):
            date_str = date_str.text
        y,m,d = (int(n) for n in date_str.split('-'))
        return date(y,m,d)

class Datetime(datetime):
    def __init__(self,date_str:str):
        pass


class CT_Box(ST_Box):pass


class BoxDOM(Model):
    AttrID:str = ''
    AttrBoundary:CT_Box = Field(default_factory=lambda:CT_Box())

class CT_CTM(BaseModel):
    CTM:list = Field(default_factory=lambda:np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]], dtype=float))
    def __init__(self,ctm_str:str):
        super().__init__()
        if isinstance(ctm_str,(DOM,Element)):
            ctm_str = ctm_str.text
        ctm_split = ctm_str.split(" ")
        self.CTM[0][0] = float(ctm_split[0])
        self.CTM[0][1] = float(ctm_split[1])
        self.CTM[1][0] = float(ctm_split[2])
        self.CTM[1][1] = float(ctm_split[3])
        self.CTM[2][0] = float(ctm_split[4])
        self.CTM[2][1] = float(ctm_split[5])


class CustomTag(Model):
    AttrTypeID:str = ""
    DomSchemaLoc: Optional[ST_Loc] = None
    DomFileLoc:ST_Loc = ""
class Extension:
    pass


class Keyword(Model):
    Text: str = ""
    def parse(self,el:DOM):
        self.Text = el.get('Text')
