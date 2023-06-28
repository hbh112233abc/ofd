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
        self.documents = self.OFD.documents()



if __name__ == '__main__':
    ofd_file = Path(__file__).parent / 'tests' / 'files' / 'test3.ofd'
    ofd = Reader(ofd_file)
    breakpoint()
    print(ofd.OFD)
