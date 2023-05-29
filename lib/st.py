#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from xml.etree.ElementTree import Element
from pydantic import BaseModel,Field

from .dom import DOM

class ST_Loc(str):
    """结构包内文件路径
    "." 表示当前路径
    ".." 表示父级路径
    "/" 表示根节点
    未显示指定时表示为当前路径
    路径区分大小写
    """
    def __new__(cls,loc:str):
        if not loc:
            raise ValueError('ST_Loc required')
        self = str(loc)
        return self

class ST_Bool:
    def __new__(cls,b:str,default:bool = False):
        if b is None:
            return default
        if isinstance(b,bool):
            return b
        if isinstance(b,int):
            return bool(b)
        if not isinstance(b,str):
            raise ValueError('Bool value error')
        if b.lower() not in ("true", "false","True", "False","TRUE", "FALSE"):
            raise ValueError("Bool value must one of 'true', 'false','True', 'False','TRUE', 'FALSE'")
        return b.lower() == "true"

    def __str__(self):
        return str(self).lower()

class ST_ID(int):
    """标识ID
    无符号整数,文档内唯一,0表示无效标识
    """
    def __new__(cls,id:str) -> None:
        if not re.match(r'^\d+$',str(id)):
            raise ValueError("Invalid ST_ID")
        return int(id)

class ST_RefID(ST_ID):
    """标识引用
    应为文档内已定义标识
    """
    pass

class ST_Pos(BaseModel):
    """点坐标
    空格分割,前者x,后者y
    """
    x:float = 0.0
    y:float = 0.0
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        if len(args) == 1:
            pos = args[0]
            if isinstance(args[0],(DOM,Element)):
                pos = args[0].text
        self.x,self.y = (float(n) for n in pos.split(' '))

    def __str__(self):
        return f"{self.x} {self.y}"

class ST_Array(list):
    def __new__(cls,arr_str:str = ''):
        if isinstance(arr_str,(DOM,Element)):
            arr_str = arr_str.text
        return arr_str.split(' ')
    def __str__(self):
        return ' '.join(self)

class ST_Box(BaseModel):
    x:float = 0.0
    y:float = 0.0
    width:float = Field(1.0,gt=0)
    height:float = Field(1.0,gt=0)

    def __init__(self,box:str):
        super().__init__()
        if isinstance(box,(DOM,Element)):
            box = box.text
        boxStrSplit = box.split(" ")
        self.x = float(boxStrSplit[0])
        self.y = float(boxStrSplit[1])
        self.width = float(boxStrSplit[2])
        self.height = float(boxStrSplit[3])
        if self.width <= 0:
            raise ValueError("Box width must be greater 0")
        if self.height <= 0:
            raise ValueError("Box height must be greater 0")
