#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from pathlib import Path
from typing import Any, Union
from xml.etree.ElementTree import Element

from lxml import etree
from lib.dom import DOM


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

def read_xml(xml:Path)->DOM:
    if isinstance(xml,str):
        xml = Path(xml)
    if not xml.exists():
        raise FileNotFoundError(f"XML file does not exist:{xml}")

    if xml.suffix != '.xml':
        raise TypeError("XML file ext error")
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(xml,parser)
    root = tree.getroot()
    check_doc_ns(root)
    return DOM(root)
