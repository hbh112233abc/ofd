#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from dataclasses import dataclass
from enum import Enum, unique
from typing import Optional

from pydantic import BaseModel,Field


@unique
class PageMode(str,Enum):
    _None = 'None'
    FullScreen = 'FullScreen'
    UseOutlines = 'UseOutlines'
    UseThumbs = 'UseThumbs'
    UseCustomTags = 'UseCustomTags'
    UseLayers = 'UseLayers'
    UseAttatchs = 'UseAttatchs'
    UseBookmarks = 'UseBookmarks'

@unique
class PageLayout(str,Enum):
    OnePage = 'OnePage'
    OneColumn = 'OneColumn'
    TwoPageL = 'TwoPageL'
    TwoPageR = 'TwoPageR'
    TwoColumnR = 'TwoColumnR'

@unique
class TabDisplay(str,Enum):
    FileName = 'FileName'
    DocTitle = 'DocTitle'

@unique
class ZoomMode(str,Enum):
    Default = 'Default'
    FitHeight = 'FitHeight'
    FitWidth = 'FitWidth'
    FitRect = 'FitRect'

@dataclass
class CT_VPreferences(BaseModel):
    PageMode:Optional[PageMode] = PageMode._None
    PageLayout:Optional[PageLayout] = PageLayout.OneColumn
    TabDisplay:Optional[TabDisplay] = TabDisplay.FileName
    HideToolbar:Optional[bool] = False
    HideMenubar:Optional[bool] = False
    HideWindowUI:Optional[bool] = False
    ZoomMode:Optional[ZoomMode] = ZoomMode.Default
    Zoom:Optional[float] = 100.0
