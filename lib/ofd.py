#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from typing import List, Optional

from pydantic import Field


from .classes import *
from .document import Document
from .version import DocVersion, Version
from .signature import Signature, Signatures

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
    NodesCutomDatas:Optional[List[CustomData]] = Field(default_factory=lambda:[])


class DocBody(Model):
    DomDocInfo:DocInfo = None
    DomDocRoot:ST_Loc = ""
    NodesVerions:Optional[List[Version]] = Field(default_factory=lambda:[])
    DomSignatures:Optional[ST_Loc] = None

    def versions(self)->List[DocVersion]:
        if self.__children__.get('versions'):
            return self.__children__.get('versions')
        self.__children__['versions'] = []
        for version in self.NodesVerions:
            doc_xml = self.__xml__.parent / version.AttrBaseLoc
            doc = DocVersion(doc_xml)
            self.__children__['versions'].append(doc)

        return self.__children__['versions']

    def signatures(self)->List[Signatures]:
        if self.__children__.get('signatures'):
            return self.__children__.get('signatures')
        self.__children__['signatures'] = []
        if not self.DomSignatures:
            return []
        sign_xml = self.__xml__.parent / self.DomSignatures
        signs = Signatures(sign_xml)
        for loc in signs.NodesSignature:
            loc = signs.__xml__.parent / loc
            sign = Signature(loc)
            self.__children__['signatures'].append(sign)

        return self.__children__['signatures']


class DocTypeEnum(str,Enum):
    OFD = "OFD"
    OFDA = "OFD-A"

class OFD(Model):
    AttrVersion:str = "1.0"
    AttrDocType:str = "OFD"
    NodesDocBody:List[DocBody] = Field(default_factory=lambda:[],min_items=1)

    def documents(self)->List[Document]:
        if self.__children__.get('documents'):
            return self.__children__.get('documents')
        self.__children__['documents'] = []
        for doc_body in self.NodesDocBody:
            doc_xml = self.xml.parent / doc_body.DomDocRoot
            doc = Document(doc_xml)
            self.__children__['documents'].append(doc)

        return self.__children__['documents']
