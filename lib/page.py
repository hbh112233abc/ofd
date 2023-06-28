#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .action import Action
from .text import CT_Text
from .classes import *
from .image import CT_Image
from .draw import CT_Composite

class CT_PageBlock(Model):
    NodesTextObject:Optional[List[CT_Text]] = Field(default_factory=lambda:[])
    NodesPathObject:Optional[List["CT_Path"]] = Field(default_factory=lambda:[])
    NodesImageObject:Optional[List[CT_Image]] = Field(default_factory=lambda:[])
    NodesCompoiteObject:Optional[List[CT_Composite]] = Field(default_factory=lambda:[])


class LayerType(str,Enum):
    Body = "Body"
    Foreground = "Foreground"
    Background = "Background"

class CT_Layer(Model):
    AttrType:Optional[LayerType] = "Body"
    AttrDrawParam:Optional[ST_RefID] = None
    NodesPageBlock:Optional[List[CT_PageBlock]] = None


class Layer(CT_PageBlock):
    AttrID:str = ""


class Content(Model):
    NodesLayer:List[Layer] = Field(None,min_items=1)


class Template(Model):
    AttrTemplateID:ST_RefID = 0
    AttrZOrder:Optional[LayerType] = "Background"

class CT_TemplatePage(Model):
    AttrID:ST_ID = 0
    AttrBaseLoc:ST_Loc = ""
    AttrName:Optional[str] = ""
    AttrZOrder:Optional[LayerType] = "Background"

class TemplatePage(CT_TemplatePage):pass

class CT_PageArea(Model):
    DomPhysicalBox:ST_Box = None
    # select ↓
    DomApplicationBox:Optional[ST_Box] = None
    DomContentBox:Optional[ST_Box] = None
    DomBleedBox:Optional[ST_Box] = None
    DomCropBox:Optional[ST_Box] = None


class PageArea(CT_PageArea):pass

class PageRes(Model):
    Text:ST_Loc = None

class Page(Model):
    NodesTemplate:Optional[List[Template]] = None
    DomArea:Optional[CT_PageArea] = None
    NodesPageRe:Optional[PageRes] = None
    DomContent:Optional[Content] = None
    NodesAction:Optional[List[Action]] = None
