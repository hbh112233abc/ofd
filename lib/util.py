#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from typing import Any, Union
from xml.etree.ElementTree import Element


# docNS that have to be part of every ofd file
FILE_DOC_NS = {"ofd": "http://www.ofdspec.org/2016"}

def boolVal(b:Union[str,bool,int])->bool:
    if b is None:
        return False
    if isinstance(b,bool):
        return b
    if isinstance(b,int):
        return bool(b)
    if not isinstance(b,str):
        raise ValueError('Bool value error')
    if b.lower() not in ("true", "false","True", "False","TRUE", "FALSE"):
        raise ValueError("Bool value must one of 'true', 'false','True', 'False','TRUE', 'FALSE'")
    return b.lower() == "true"

def intVal(i:Union[None,int,str])->int:
    if i is None:
        return None
    return int(i)



def check_doc_ns(node:Element)->None:
    if node.nsmap != FILE_DOC_NS:
        raise ValueError("XML DOC Root node nsmap error")
