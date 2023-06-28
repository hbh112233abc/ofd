#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from typing import List
from .classes import *
from .page import CT_PageBlock

class Page(Model):
    AttrPageID:ST_RefID = 0
    DomFileLoc: ST_Loc = ""

class Annotations(Model):
    NodesPage:Optional[List[Page]] = []

class AnnotType(str,Enum):
    Link = "Link"
    Path = "Path"
    Highlight = "Highlight"
    Stamp = "Stamp"
    Watermark = "Watermark"

class Parameter(Model):
    Text:str = ""

class Parameters(Model):
    NodesParameter:List[Parameter] = Field(default_factory=lambda:[],min_items=1)

class Annot(Model):
    AttrID:ST_ID = 0
    AttrType: AnnotType = ""
    AttrCreator:str = ""
    AttrLastModDate:Date = ""
    AttrSubtype:Optional[str] = None
    AttrVisible:Optional[bool] = None
    AttrPrint:Optional[bool] = None
    AttrNoZoom:Optional[bool] = None
    AttrNoRotate:Optional[bool] = None
    AttrReadOnly:Optional[bool] = None
    DomRemark:Optional[str] = None
    DomParameters: Optional[Parameters] = None
    DomAppearance:CT_PageBlock = None




class PageAnnot(Model):
    NodesAnnot: List[Annot] = []
