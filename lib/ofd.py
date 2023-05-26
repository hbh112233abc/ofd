#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from typing import List, Optional
from pathlib import Path

from pydantic import BaseModel,Field
from lxml import etree

from .classes import *
from .util import read_xml,val



class DocInfo(DOMModel):
    DomDocId:Optional[str] = Field(default_factory=lambda:uuid4().hex)
    DomTitle:Optional[str] = None
    DomAuthor:Optional[str] = None
    DomSubject:Optional[str] = None
    DomAbstract:Optional[str] = None
    DomCreationDate:Optional[Date] = None
    DomModDate:Optional[Date] = None
    DomDocUsage:Optional[str] = None
    DomCover:Optional[str] = None
    DomKeywords:Optional[List[Keyword]] = Field(default_factory=lambda:[])
    DomCreator:Optional[str] = None
    DomCreatorVersion:Optional[str] = None
    DomsCustomDatas:Optional[List[CustomData]] = Field(default_factory=lambda:[])


class Version(DOMModel):
    AttrID:ST_ID = 0
    AttrIndex:int = 0
    AttrBaseLoc:str = ''
    AttrCurrent:Optional[bool] = False


class DocBody(DOMModel):
    DomDocInfo:DocInfo = None
    DomDocRoot:ST_Loc = ""
    DomVersions:Optional[List[Version]] = Field(default_factory=lambda:[])
    DomSignatures:Optional[ST_Loc] = None


class DocTypeEnum(str,Enum):
    OFD = "OFD"
    OFDA = "OFD-A"

class OFD(DOMModel):
    AttrVersion:str = "1.0"
    AttrDocType:str = "OFD"
    NodesDocBodies:List[DocBody] = Field(default_factory=lambda:[],min_items=1)
