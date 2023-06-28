#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'


from pathlib import Path
from typing import Any, List, Union
from xml.etree.ElementTree import Element
from lxml import etree


from lib.util import check_doc_ns


class DOM:
    def __init__(self,el:Union[Element,Path]):
        if isinstance(self.el,Path):
            self.read_xml(self.el)
        else:
            self.el = el

    def read_xml(self,xml:Path):
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
        self.el = root

    def query(self,tag:str)->Element:
        tags = tag.split('.')
        for child in self.el:
            if tags[0] in child.tag:
                if len(tags) == 1:
                    return DOM(child)
                parent = DOM(child)
                return parent.query('.'.join(tags[1:]))

    def query_text(self,tag:str)->str:
        child = self.query(tag)
        if child is None:
            return None
        return child.text

    def query_all(self,tag:str)->List[Element]:
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
