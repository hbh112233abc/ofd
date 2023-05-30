#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pydantic import NonNegativeFloat

from .classes import *
from .model import Model

class DestType(str,Enum):
    XYZ = 'XYZ' # 目标区域由左上角位置(Left,Top)以及页面缩放比例(Zoom)确定
    Fit = 'Fit' # 适合整个窗口区域
    FitH = 'FitH' # 适合窗口宽度,目标区域仅由 Top 确定
    FitV = 'FitV' # 适合窗口高度,目标区域仅由 Left 确定
    FitR = 'FitR' # 适合窗口内的目标区域,目标区域为(Left,Top,Right,Bottom) 所确定的矩形区域

class CT_Dest(Model):
    AttrType:DestType = ""
    AttrPageID:ST_RefID = 0
    AttrLeft:Optional[NonNegativeFloat] = 0.0
    AttrTop:Optional[NonNegativeFloat] = 0.0
    AttrRight:Optional[NonNegativeFloat] = None
    AttrBottom:Optional[NonNegativeFloat] = None
    AttrZoom:Optional[float] = Field(0,ge=0,le=64)

class Event(str,Enum):
    DO = 'DO' # 文档打开
    PO = 'PO' # 页面打开
    CLICK = 'CLICK' # 单击区域

class Goto(Model):
    DomDest:CT_Dest = None
    DomBookmark: "Bookmark" = None


class GotoA(Model):
    AttrAttachID:ST_RefID = 0
    AttrNewWindow:bool = True


class URI(Model):
    AttrURI:str = ""
    AttrBase:Optional[str] = None


class Sound(Model):
    AttrResourceID:ST_RefID = 0
    AttrVolume:Optional[int] = 100
    AttrRepeat:Optional[bool] = False
    AttrSynchronous:Optional[bool] = False


class Operator(str,Enum):
    Play = 'Play'
    Stop = 'Stop'
    Pause = 'Pause'
    Resume = 'Resume'


class Movie(Model):
    AttrResourceID:ST_RefID = 0
    AttrOperator:Optional[Operator] = Operator.Play

class CT_Action(Model):
    AttrEvent:Event = ""
    DomRegion:Optional["CT_Region"] = None
    DomGoto:Goto = None #本文档内的跳转
    DomURI:URI = None #打开或访问一个URI链接
    DomGotoA:GotoA = None #打开本文档附件
    DomSound:Sound = None #播放音频
    DomMovie:Movie = None #播放视频

class Action(CT_Action):pass
