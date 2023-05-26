#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from typing import Any, List
from xml.etree.ElementTree import Element


class DOM:
    def __init__(self,el:Element):
        self.el = el

    def find(self,tag:str)->Element:
        for child in self.el:
            if tag in child.tag:
                return DOM(child)

    def find_text(self,tag:str)->str:
        child = self.find(tag)
        if child is None:
            return None
        return child.text

    def find_all(self,tag:str)->List[Element]:
        items = []
        for child in self.el:
            if tag in child.tag:
                items.append(DOM(child))
        return items

    def __repr__(self) -> str:
        return "<%s %s>" % ("DOM",self.el.__repr__())

    def __str__(self) -> str:
        if self.el.text is not None:
            return self.el.text
        return self.__repr__()

    def __getattr__(self, __name:str) -> Any:
        return getattr(self.el,__name)
