#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path
from typing import Any, Optional, Union
from xml.etree.ElementTree import Element

from lxml import etree
from pydantic import BaseModel
from pydantic.fields import ModelField

from .util import read_xml,val,FILE_DOC_NS
from .dom import DOM

TAG_PREFIX = f"{{{FILE_DOC_NS['ofd']}}}"

class Model(BaseModel):
    XMLPath:Optional[str] = ""
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        if len(args) == 1 and isinstance(args[0],(Element,DOM,Path,str)):
            self.decode(args[0])

    def __repr__(self):
        return f"<{self.__class__.__name__} {super().__str__()}>"

    def decode(self, e:Union[Path,DOM,Element]):
        if isinstance(e,(str,Path)):
            dom = read_xml(e)
            self.XMLPath = e
        elif isinstance(e,Element):
            dom = DOM(e)
        elif isinstance(e,DOM):
            dom = e
        else:
            raise ValueError("Invalid param for parse,must one of [str,Path,Element,DOM]")

        fields = self.__fields__
        for key, field in fields.items():
            if key.startswith("Attr"):
                self.__Attr(key,field,dom)
                continue

            if key.startswith("Doms"):
                self.__Doms(key,field,dom)
                continue

            if key.startswith("Dom"):
                self.__Dom(key,field,dom)
                continue

            if key.startswith("Nodes"):
                self.__Nodes(key,field,dom)
                continue

            if key == "Text":
                setattr(self,key,dom.text)

    def __Attr(self,key:str,field:ModelField,dom:DOM):
        k = key[4:]
        setattr(self,key,val(dom.get(k,field.default),field.type_))

    def __Dom(self,key:str,field:ModelField,dom:DOM):
        k = key[3:]
        el = dom.query(k)
        if el is not None:
            setattr(
                self,
                key,
                val(el,field.type_)
            )

    def __items(self,key:str,field:ModelField,dom:DOM)->list:
        return [val(el,field.type_) for el in dom.query_all(key)]

    def __Doms(self,key:str,field:ModelField,dom:DOM):
        k = key[4:]
        dom = dom.query(k)
        if not dom:
            return
        k = field.type_.schema()['title']
        items = self.__items(k,field,dom)
        if items:
            setattr(
                self,
                key,
                items
            )

    def __Nodes(self,key:str,field:ModelField,dom:DOM):
        k = field.type_.schema()['title']
        items = self.__items(k,field,dom)
        if items:
            setattr(
                self,
                key,
                items
            )

    def encode(self,tag:str=""):
        if not tag:
            tag = self.__class__.__name__
        tag = TAG_PREFIX+tag
        text = None
        props = {}
        children = []
        fields = self.__fields__
        for key, field in fields.items():
            if key.startswith("Attr"):
                k = key[4:]
                v = getattr(self,key)
                if v is not None:
                    props[k] = str(v)
                continue

            if key.startswith("Doms"):
                k = key[4:]
                doms = getattr(self,key)
                if doms is not None:
                    children.append(self.__make_xml(doms,k))
                continue

            if key.startswith("Dom"):
                k = key[3:]
                dom = getattr(self,key)
                if dom is not None:
                    children.append(self.__make_xml(dom,k))
                continue

            if key.startswith("Nodes"):
                k = key[5:]
                doms = getattr(self,key)
                if doms is not None:
                    children.append(self.__make_xml(doms))
                continue

            if key == "Text":
                text = getattr(self,key)

        el = etree.Element(tag,props,nsmap=FILE_DOC_NS)
        if children:
            for child in children:
                if isinstance(child,list):
                    [el.append(e) for e in child]
                else:
                    el.append(child)
        if text:
            el.text = text

        return el

    def tostring(self):
        return str(
            etree.tostring(
                self.encode(),
                encoding='utf-8',
                pretty_print=True
            ),
            encoding='utf-8'
        )

    def __make_xml(self,item:Any,tag:str = "")->Element:
        if tag and not tag.startswith(TAG_PREFIX):
            tag = TAG_PREFIX + tag
        if isinstance(item,Model):
            return item.encode(tag)
        elif isinstance(item,DOM):
            el = item.el
            return el
        elif isinstance(item,list):
            el = []
            if tag:
                el = etree.Element(tag,nsmap=FILE_DOC_NS)
            for sub_item in item:
                el.append(self.__make_xml(sub_item))
            return el
        else:
            el = etree.Element(tag,nsmap=FILE_DOC_NS)
            el.text = str(item)
            return el
