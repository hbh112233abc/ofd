#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path
from typing import Any, Optional, Union
from xml.etree.ElementTree import Element

from lxml import etree
from pydantic import BaseModel
from pydantic.fields import ModelField

from rich import print
from rich.tree import Tree

from .util import boolVal, intVal, FILE_DOC_NS
from .dom import DOM

TAG_PREFIX = f"{{{FILE_DOC_NS['ofd']}}}"

def val(v:Any,tp:object)->Any:
    if v is None:
        return v
    if isinstance(v,(DOM,Element)):
        try:
            return tp(v)
        except Exception as e:
            print("Warning:",e, v, tp)
            v = v.text
    if isinstance(tp,bool):
        return boolVal(v)
    elif isinstance(tp,int):
        return intVal(v)
    else:
        return tp(v)

class Model(BaseModel):
    xml = ""
    dom:object = None
    __children__ = {}
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        if len(args) == 1 and isinstance(args[0],(Element,DOM,Path,str)):
            self.decode(args[0])
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        repr = f'<{self.__class__.__name__}'
        for k,v in self.__dict__.items():
            if k in ('dom', 'xml'):
                continue
            repr += f" {k}={v.__str__()}"
        repr += '>'
        return repr

    def __tree__(self,with_prefix:bool=True,label:str=""):
        label = label if label else self.__class__.__name__
        tree = Tree(f"[b green]{label}[/]")
        for k,v in self.__dict__.items():
            if k in ('dom', 'xml'):
                continue
            color = 'white'
            if k.startswith("Attr"):
                k = k[4:] if not with_prefix else k
                color = 'deep_sky_blue4'
            elif k.startswith("Dom"):
                k = k[3:] if not with_prefix else k
                color = 'yellow'
            elif k.startswith("Nodes"):
                k = k[5:] if not with_prefix else k
                color = 'cyan'
            node = f'[b {color}]{k}[/]'
            if isinstance(v,Model):
                tree.add(v.__tree__(with_prefix,node))
            elif isinstance(v,list):
                sub_tree = tree.add(node)
                for item in v:
                    if isinstance(item,Model):
                        sub_tree.add(item.__tree__(with_prefix))
                    else:
                        sub_tree.add(item)
            else:
                node += f": {v}"
                tree.add(node)
        return tree

    def show(self,with_prefix:bool=True):
        tree = self.__tree__(with_prefix)
        print(tree)

    def __getattr__(self, __name: str) -> Any:
        for k,v in self.__dict__.items():
            if k.endswith(__name):
                return v

    def decode(self, e:Union[Path,DOM,Element]):
        if isinstance(e,(str,Path)):
            dom = DOM(e)
            self.xml = e
        elif isinstance(e,Element):
            dom = DOM(e)
        elif isinstance(e,DOM):
            dom = e
        else:
            raise ValueError("Invalid param for parse,must one of [str,Path,Element,DOM]")
        self.dom = dom
        fields = self.__fields__
        for key, field in fields.items():
            if key.startswith("Attr"):
                self.__Attr(key,field)
                continue

            if key.startswith("Dom"):
                self.__Dom(key,field)
                continue

            if key.startswith("Nodes"):
                self.__Nodes(key,field)
                continue

            if key == "Text":
                setattr(self,key,dom.text)

    def __Attr(self,key:str,field:ModelField):
        k = key[4:]
        setattr(self,key,val(self.dom.get(k,field.default),field.type_))

    def __Dom(self,key:str,field:ModelField):
        k = key[3:]
        el = self.dom.query(k)
        if el is not None:
            setattr(
                self,
                key,
                val(el,field.type_)
            )

    def __items(self,key:str,field:ModelField,dom:DOM)->list:
        return [val(el,field.type_) for el in dom.query_all(key)]

    def __Nodes(self,key:str,field:ModelField):
        k = key[5:]
        items = self.__items(k,field,self.dom)
        if not items:
            return
        setattr(self,key,items)

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
                    children.append(self.__make_xml(doms,k))
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
