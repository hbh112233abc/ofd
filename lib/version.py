#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *

class Version(Model):
    AttrID:ST_ID = 0
    AttrIndex:int = 0
    AttrBaseLoc:str = ''
    AttrCurrent:Optional[bool] = False

class Versions(Model):
    NodesVersion:List[Version] = Field(default_factory=lambda:[],min_items=1)

class File(Model):
    AttrID:int = 0
    Text:ST_Loc = ''

class DocVersion(Model):
    AttrID:int = 0
    AttrVersion:Optional[str] = ''
    AttrName:Optional[str] = ''
    AttrCreationDate:Date = None
    DomFileList:List[File] = Field(default_factory=lambda:[],min_items=1)
    DomDocRoot:ST_Loc = ''
