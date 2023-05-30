#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from typing import List, Optional

from pydantic import Field

from .classes import *
from .version import Version
from .document import Document

class CustomData(Model):
    AttrName: str = ""
    Text: str = ""

class DocInfo(Model):
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


class DocBody(Model):
    DomDocInfo:DocInfo = None
    DomDocRoot:ST_Loc = ""
    DomVersions:Optional[List[Version]] = Field(default_factory=lambda:[])
    DomSignatures:Optional[ST_Loc] = None


class DocTypeEnum(str,Enum):
    OFD = "OFD"
    OFDA = "OFD-A"

class OFD(Model):
    AttrVersion:str = "1.0"
    AttrDocType:str = "OFD"
    NodesDocBodies:List[DocBody] = Field(default_factory=lambda:[],min_items=1)
    __documents:List[Document] =  Field(default_factory=lambda:[],min_items=1)

    def documents(self):
        breakpoint()
        if self.__documents:
            return self.__documents
        for doc_body in self.NodesDocBodies:
            doc_xml = self.XMLPath.parent / doc_body.DocRoot
            doc = Document(doc_xml)
            self.__documents.append(doc)
