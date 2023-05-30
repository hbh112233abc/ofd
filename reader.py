#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path

from lib.zip import extract
from lib.ofd import OFD


class Reader:
    def __init__(self,ofd_file:str,unzip_overwrite = False) -> None:
        self.ofd_file = Path(ofd_file)
        if not self.ofd_file.exists():
            raise FileNotFoundError("ofd file %s not found" % ofd_file)
        self.ofd_path = extract(self.ofd_file,unzip_overwrite)

        self.OFD = OFD(self.ofd_path / 'OFD.xml')
