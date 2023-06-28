#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from typing import List, Optional

from pydantic import Field

from .classes import *
from .page import CT_PageArea, CT_TemplatePage,Page as PageModel
from .action import Action
from .outline import OutlineElem
from .permission import CT_Permission
from .v_preference import CT_VPreferences
from .bookmark import Bookmark
from .res import Res

class CT_CommonData(Model):
    DomMaxUnitID:ST_ID = Field(0,description="当前文档中所有对象使用标识的最大值,初始为0;用于文档编辑,向文档新增一个对象时,该值+1",ge=0)
    DomPageArea:CT_PageArea = Field(default_factory=lambda:CT_PageArea(),description="指定该文档页面区域的默认大小和位置")
    DomPublicRes:Optional[ST_Loc] = Field("",description="公共资源文档路径")
    DomDocumentRes:Optional[ST_Loc] = Field("",description="文档资源文档路径")
    DomTemplatePage:Optional[CT_TemplatePage] = Field(None,description="模板页")
    DomDefaultCS: Optional[ST_RefID] = Field(None,description="颜色空间标识")


class CommonData(CT_CommonData):pass

class Page(Model):
    AttrID:ST_ID = 0
    AttrBaseLoc:ST_Loc = ""

class Pages(Model):
    NodesPage:List[Page] = Field(None,min_items=1)

class Document(Model):
    DomCommonData:CommonData = Field(default_factory=lambda:CommonData())
    DomPages:Pages = Field(default_factory=lambda:Pages())
    NodesOutline:Optional[List[OutlineElem]] = None
    DomPermission:Optional[CT_Permission] = None
    NodesAction:Optional[List[Action]] = None
    DomVPreference: Optional[CT_VPreferences] = None
    NodesBookmark:Optional[List[Bookmark]] = None
    DomAttachments:Optional[ST_Loc] = None
    DomAnnotations:Optional[ST_Loc] = None
    DomCustomTags:Optional[ST_Loc] = None
    DomExtensions:Optional[ST_Loc] = None

    def pages(self):
        if self.__children__.get('pages'):
            return self.__children__.get('pages')

        self.__children__['pages'] = []
        for page in self.DomPages.NodesPage:
            loc = self.xml.parent / page.AttrBaseLoc
            self.__children__['pages'].append(PageModel(loc))

        return self.__children__['pages']

    def public_res(self):
        if not self.__children__.get('public_res'):
            loc = self.xml.parent / self.DomCommonData.DomPublicRes
            self.__children__['public_res'] = Res(loc)
        return self.__children__['public_res']

    def document_res(self):
        if not self.__children__.get('document_res'):
            loc = self.xml.parent / self.DomCommonData.DomDocumentRes
            self.__children__['document_res'] = Res(loc)
        return self.__children__['document_res']
