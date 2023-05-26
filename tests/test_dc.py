#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

# from dataclasses import dataclass
from typing import Optional
from pydantic.dataclasses import dataclass
from pydantic import BaseModel,Field
from enum import Enum

class Color(str,Enum):
    Yellow = "Yellow"
    White = "White"
    Black = "Black"
    Brown = "Brown"


class ST_Array(list):
    def __init__(self,arr_str:str = ''):
        arr = arr_str.split(' ')
        super().__init__(*arr)


class Human(BaseModel):
    Name:str
    Age:int
    # Color:Color = Color.Yellow

class Skill(BaseModel):
    Name:str
    Score:float = Field(0,ge=0,le=100)


class Person(Human):
    Country:Optional[str] = ""
    Skill:Optional["Skill"] = None
    Hobby:ST_Array = Field(default_factory=lambda: ST_Array())

def test_dc():
    hbh = Person(Name="huangbh",Age='10')
    print(hbh)
    print(hbh.__fields__)
    breakpoint()
    hbh.Name = "Hangbh"
    print(hbh)
    assert isinstance(hbh,Person)
