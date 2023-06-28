#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from .classes import *
from .annotion import Annot

class Provider(Model):
    AttrProviderName:str = ""
    AttrVersion:Optional[str] = None
    AttrCompany:Optional[str] = None

class StampAnnot(Model):
    AttrID:int = 0
    AttrPageRef:ST_RefID = 0
    AttrBoundary:ST_Box = Field(default_factory=lambda:ST_Box())
    AttrClip:Optional[ST_Box] = None


class Seal(Model):
    AttrBaseLoc:ST_Loc = ""


class Reference(Model):
    AttrFileRef:ST_Loc = ""
    DomCheckValue:str = ""

class References(Model):
    AttrCheckMethod: str = "MD5"
    NodesReference: List[Reference] = Field(None,min_items=1)


class SignedInfo(Model):
    DomProvider: Provider = Field(default_factory=lambda: {})
    DomSignatureMethod: Optional[str] = None
    DomSignatureDateTime: Optional[str] = None
    DomReferences: References = Field(default_factory=lambda: [])
    NodesStampAnnot: Optional[List[StampAnnot]] = None
    DomSeal:Optional[Seal] = None

class SignType(str,Enum):
    Seal = "Seal" #签章
    Sign = "Sign" #纯数字签名

class Signature(Model):
    AttrID: int = 0
    AttrType: Optional[SignType] = SignType.Seal
    AttrBaseLoc:ST_Loc = ""
    DomSignedInfo: SignedInfo = None
    DomSignedValue: ST_Loc = ""

class Signatures(Model):
    DomMaxSignId:int = Field(1,gt=0)
    NodesSignature:List[Signature] = None
