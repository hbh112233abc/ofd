#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from enum import Enum
from typing import Optional

from pydantic import NonNegativeFloat

from .model import Model

class PageMode(str,Enum):
    _None = 'None'
    FullScreen = 'FullScreen'
    UseOutlines = 'UseOutlines'
    UseThumbs = 'UseThumbs'
    UseCustomTags = 'UseCustomTags'
    UseLayers = 'UseLayers'
    UseAttatchs = 'UseAttatchs'
    UseBookmarks = 'UseBookmarks'
class PageLayout(str,Enum):
    OnePage = 'OnePage'
    OneColumn = 'OneColumn'
    TwoPageL = 'TwoPageL'
    TwoPageR = 'TwoPageR'
    TwoColumnR = 'TwoColumnR'
class TabDisplay(str,Enum):
    FileName = 'FileName'
    DocTitle = 'DocTitle'
class ZoomMode(str,Enum):
    Default = 'Default'
    FitHeight = 'FitHeight'
    FitWidth = 'FitWidth'
    FitRect = 'FitRect'

class CT_VPreferences(Model):
    DomPageMode:Optional[PageMode] = PageMode._None
    DomPageLayout:Optional[PageLayout] = PageLayout.OneColumn
    DomTabDisplay:Optional[TabDisplay] = TabDisplay.FileName
    DomHideToolbar:Optional[bool] = False
    DomHideMenubar:Optional[bool] = False
    DomHideWindowUI:Optional[bool] = False
    DomZoomMode:Optional[ZoomMode] = ZoomMode.Default
    DomZoom:Optional[NonNegativeFloat] = 100.0

class VPreferences(CT_VPreferences):pass
