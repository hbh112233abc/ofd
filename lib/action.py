#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from dataclasses import dataclass

from lib.draw import CT_Region

from .classes import *

@unique
class Event(str,Enum):
    DO = 'DO' # 文档打开
    PO = 'PO' # 页面打开
    CLICK = 'CLICK' # 单击区域

class Goto:
    Dest:CT_Dest
    Bookmark: Bookmark


class GotoA:
    AttachID:ST_RefID = 0
    NewWindow:bool = True


class URI:
    URI:str
    Base:str


class Sound:
    ResourceID:ST_RefID = 0
    Volume:int = 100
    Repeat:bool = False
    Synchronous:bool = False

@unique
class Operator(Enum):
    Play = 'Play'
    Stop = 'Stop'
    Pause = 'Pause'
    Resume = 'Resume'


class Movie:
    ResourceID:ST_RefID = 0
    Operator:str = "Play"


class CT_Action(DOMModel):
    Event:Event
    Region:Optional[CT_Region] = None
    Goto:Goto = None #本文档内的跳转
    URI:URI = None #打开或访问一个URI链接
    GotoA:GotoA = None #打开本文档附件
    Sound:Sound = None #播放音频
    Movie:Movie = None #播放视频

    def parse(self,e:DOM):
        self.Event = e.get("Event")
        region = e.find("Region")
        if region:
            self.Region = CT_Region(region)

class Action(CT_Action):pass
