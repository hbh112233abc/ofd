#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path
from typing import Union
from xml.etree.ElementTree import Element

from pydantic import BaseModel,Field
from pydantic.fields import ModelField

from .util import read_xml,val
from .dom import DOM


class DOMModel(BaseModel):
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        if len(args) == 1 and isinstance(args[0],(Element,DOM,Path,str)):
            self.decode(args[0])

    def __repr__(self):
        return f"<{self.__class__.__name__} {super().__str__()}>"

    def decode(self, e:Union[Path,DOM,Element]):
        if isinstance(e,(str,Path)):
            dom = read_xml(e)
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
        k = key.lstrip("Attr")
        setattr(self,key,val(dom.get(k,field.default),field.type_))

    def __Dom(self,key:str,field:ModelField,dom:DOM):
        k = key.lstrip("Dom")
        el = dom.find(k)
        if el is not None:
            setattr(
                self,
                key,
                val(el,field.type_)
            )

    def __items(self,key:str,field:ModelField,dom:DOM)->list:
        return [val(el,field.type_) for el in dom.find_all(key)]

    def __Doms(self,key:str,field:ModelField,dom:DOM):
        k = key.lstrip("Doms")
        dom = dom.find(k)
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
        k = key.lstrip("Nodes")
        items = self.__items(k,field,dom)
        if items:
            setattr(
                self,
                key,
                items
            )
