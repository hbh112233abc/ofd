#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from lib.action import Action
from lib.text import CT_Text
from .classes import *
from .image import CT_Image

class CT_PageBlock(Model):
    NodesTextObject:List[CT_Text] = Field(default_factory=lambda:[])
    NodesPathObject:List["CT_Path"] = Field(default_factory=lambda:[])
    NodesImageObject:List[CT_Image] = Field(default_factory=lambda:[])
    NodesCompositeObject:List[CT_Composite] = Field(default_factory=lambda:[])


class LayerType(str,Enum):
    Body = "Body"
    Foreground = "Foreground"
    Background = "Background"

class CT_Layer(BaseModel):
    AttrType:Optional[LayerType] = "Body"
    AttrDrawParam:Optional[ST_RefID] = None
    NodesPageBlock:Optional[List[CT_PageBlock]] = None


class Layer(Model):
    AttrLayerId:str = ""
    AttrPageBlock:CT_PageBlock = Field(default_factory=lambda:CT_PageBlock())


class Content(Model):
    DomLayer:Layer = Field(default_factory=lambda:Layer())


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


class PageArea(CT_PageArea):pass

class Page(BaseModel):
    ID:ST_ID = 0
    NodesTemplate:List[Template] = None
    DomArea:Optional[CT_PageArea] = None
    NodesPageRes:Optional[ST_Loc] = None
    DomContent:Optional[List[CT_Layer]] = None
    DomsActions:Optional[List[Action]] = None
