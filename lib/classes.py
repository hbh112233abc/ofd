#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from dataclasses import dataclass,field
from datetime import date, datetime
from enum import Enum, unique
import re
from typing import List, Union,Optional
from uuid import uuid4

from pydantic import BaseModel,Field,NonNegativeFloat
from xml.etree.ElementTree import Element
import numpy as np


from .util import boolVal
from .dom import DOM
from .model import DOMModel

@dataclass
class ColorRGB:
    r:int = 0
    g:int = 0
    b:int = 0
    def __init__(self,*args,**kwargs):
        if len(args) == 1:
            return self.__init_str__(*args)
        if len(args) == 3:
            return self.__init_rgb__(*args)
        if 'color' in kwargs:
            return self.__init_str__(**kwargs)
        if 'r' in kwargs:
            return self.__init_rgb__(**kwargs)

    def __init_str__(self,color:str):
        color_split = color.split(' ')
        if len(color_split) != 3:
            raise ValueError('Invalid color string format `[0-255] [0-255] [0-255]`')
        self.__init__(*[int(x) for x in color_split])

    def __init_rgb__(self,r,g,b:int):
        if not 0<= r <= 255:
            raise ValueError('Invalid color value,`r` must between 0,255')
        if not 0<= g <= 255:
            raise ValueError('Invalid color value,`g` must between 0,255')
        if not 0<= b <= 255:
            raise ValueError('Invalid color value,`b` must between 0,255')
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.r} {self.g} {self.b}"


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


class Date(date):
    def __new__(cls,date_str:str) -> None:
        if date_str is None:
            return None
        if isinstance(date_str,(DOM,Element)):
            date_str = date_str.text
        y,m,d = (int(n) for n in date_str.split('-'))
        return date(y,m,d)

class Datetime(datetime):
    def __init__(self,date_str:str):
        pass



class ST_Box(BaseModel):
    x:float = 0.0
    y:float = 0.0
    width:float = Field(1.0,gt=0)
    height:float = Field(1.0,gt=0)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if len(args) == 1 and isinstance(args[0],str):
            boxStr = args[0]
            boxStrSplit = boxStr.split(" ")
            self.x = float(boxStrSplit[0])
            self.y = float(boxStrSplit[1])
            self.width = float(boxStrSplit[2])
            self.height = float(boxStrSplit[3])
            if self.width <= 0:
                raise ValueError("Box width must be greater 0")
            if self.height <= 0:
                raise ValueError("Box height must be greater 0")


class CT_Box(ST_Box):pass


class BoxDOM(DOMModel):
    AttrID:str = ''
    AttrBoundary:CT_Box = Field(default_factory=lambda:CT_Box())

@dataclass
class CT_CTM:
    CTM:list = Field(default_factory=lambda:np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]], dtype=float))
    def __init__(self,ctm_str:str):
        ctm_split = ctm_str.split(" ")
        self.CTM[0][0] = float(ctm_split[0])
        self.CTM[0][1] = float(ctm_split[1])
        self.CTM[1][0] = float(ctm_split[2])
        self.CTM[1][1] = float(ctm_split[3])
        self.CTM[2][0] = float(ctm_split[4])
        self.CTM[2][1] = float(ctm_split[5])



@unique
class DestType(str,Enum):
    XYZ = 'XYZ' # 目标区域由左上角位置(Left,Top)以及页面缩放比例(Zoom)确定
    Fit = 'Fit' # 适合整个窗口区域
    FitH = 'FitH' # 适合窗口宽度,目标区域仅由 Top 确定
    FitV = 'FitV' # 适合窗口高度,目标区域仅由 Left 确定
    FitR = 'FitR' # 适合窗口内的目标区域,目标区域为(Left,Top,Right,Bottom) 所确定的矩形区域

@dataclass
class CT_Dest:
    Type:str = ""
    PageID:ST_RefID = 0
    Left:float = 0.0
    Top:float = 0.0
    Right:float = 0.0
    Bottom:float = 0.0
    Zoom:float = 1.0


@dataclass
class Bookmark:
    pass

@dataclass
class Attachment:
    pass
@dataclass
class Annotation:
    pass
@dataclass
class CustomTag:
    pass
@dataclass
class Extension:
    pass


@dataclass
class CT_Path(BoxDOM):
    __AbbreviatedData:List[str] = Field(default_factory=lambda:[])
    __Stroke:bool = True
    __Fill:bool = False
    __Rule:str = "" # NonZero or EvenOdd
    __FillColor:ColorRGB = Field(default_factory=lambda:ColorRGB(255, 255, 255))
    __StrokeColor:ColorRGB = Field(default_factory=lambda:ColorRGB(0, 0, 0))

    @property
    def Boundary(self):
        return self.__Boundary

    @Boundary.setter
    def Boundary(self,box:str):
        self.__Boundary = CT_Box(box)

    @property
    def AbbreviatedData(self):
        return self.__AbbreviatedData

    @AbbreviatedData.setter
    def AbbreviatedData(self, data:str):
        self.__AbbreviatedData = data.split(" ")

    @property
    def Stroke(self):
        return self.__Stroke
    @Stroke.setter
    def Stroke(self,b:str):
        self.__Stroke = boolVal(b)
    @property
    def Fill(self):
        return self.__Fill
    @Fill.setter
    def Fill(self,b:str):
        self.__Fill = boolVal(b)

    @property
    def Rule(self):
        return self.__Rule
    @Rule.setter
    def Rule(self,rule:str):
        if rule not in ("NonZero", "Even-Odd"):
            raise ValueError(".Rule must one of 'NonZero', 'Even-Odd'.")
        self.__Rule = rule

    @property
    def FillColor(self):
        return self.__FillColor
    @FillColor.setter
    def FillColor(self,c:str):
        self.__FillColor = ColorRGB(c)

    @property
    def StrokeColor(self):
        return self.__StrokeColor
    @StrokeColor.setter
    def StrokeColor(self,c:str):
        self.__StrokeColor = ColorRGB(c)


class CGTransform(DOMModel):
    AttrCodePosition:int = 0
    # select ↓
    AttrCodeCount:Optional[int] = 0
    AttrGlyphCount:Optional[int] = 0
    DomGlyphs:ST_Array = Field(default_factory=lambda:[])


class CT_Image(BoxDOM):
    __CTMArray:CT_CTM = Field(default_factory=lambda:np.empty([3, 3], dtype=float))
    ResourseID:str = ''

    @property
    def CTM(self):
        return self.__CTMArray
    @CTM.setter
    def CTM(self,ctm_string:str):
        self.__CTMArray = CT_CTM(ctm_string)

@dataclass
class CT_Composite:
    ResourseID:str = ''


@dataclass
class CT_VectorG:
    Width:float = 0.0
    Height:float = 0.0

@dataclass
class CT_Font:
    ID:str = ''
    FontName:str = ''
    FamilyName:str = ''
    FontFile:str = ''

@dataclass
class SignedInfo:
    Provider: dict = Field(default_factory=lambda: {})
    SignatureMethod: str = ""
    SignatureDateTime: str = ""
    References: List[str] = Field(default_factory=lambda: [])
    StampAnnot: dict = Field(default_factory=lambda: {})

@dataclass
class Signature:
    ID: int = 0
    Type: str = ""
    BaseLoc:ST_Loc = ""
    SignedInfo: SignedInfo = None
    SignedValue: str = ""

@dataclass
class CT_MultiMedia:
    ID:str = ""
    Type:str = ""
    MediaFile:str = ""
    # select ↓
    Format:str = ""

class CustomData(DOMModel):
    AttrName: str = ""
    Text: str = ""


class Keyword(DOMModel):
    Text: str = ""
    def parse(self,el:DOM):
        self.Text = el.get('Text')

class PublicRes(BaseModel):
    BaseLoc:ST_Loc = ""
    __Fonts:List[CT_Font] = Field(default_factory=lambda:[])

    @property
    def Fonts(self):
        return self.__Fonts
    @Fonts.setter
    def Fonts(self, font:CT_Font):
        self.__Fonts.append(font)


class DocumentRes(BaseModel):
    BaseLoc:ST_Loc = ""
    __MultiMedias:List[CT_MultiMedia] = []
    @property
    def MultiMedias(self):
        return self.__MultiMedias
    @MultiMedias.setter
    def MultiMedias(self, media:CT_MultiMedia):
        self.__MultiMedias.append(media)
