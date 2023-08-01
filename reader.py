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

    def verify(self):
        """校验ofd格式
        """
        # OFD
        print(
            "Versions: {}\nDocType: {}".format(
                self.OFD.Version, self.OFD.DocType
            )
        )
        print("\n")

        # Document
        Document = self.documents[0]
        print("-" * 46)
        print(" " * 10 + "---Parsing Document.xml---")
        print("MaxUnitID: {}".format(Document.CommonData.MaxUnitID))
        print("Length of Pages: {}".format(Document.pages().__len__()))
        print("\n")

        # Pages
        print("-" * 46)
        print(" " * 10 + "---Parsing Pages---")
        for i,page in enumerate(Document.pages()):
            print(
                ("Pages{}" + " " * 4 + "PageID: {}" + " " * 4 + "PageRes: {}").format(
                    i + 1,
                    Document.Pages.Page[i].ID,
                    page.PageRes,
                )
            )

        # Res
        print("\n")
        print("-" * 46)
        print(" " * 10 + "---Parsing Res---")
        public_res = Document.public_res()
        if public_res:
            for font in public_res.Fonts.Font:
                print(
                    (
                        "ID: {}"
                        + " " * 4
                        + "FontName: {}"
                        + " " * 4
                        + "FamilyName: {}"
                        + " " * 4
                        + "FontFile: {}"
                    ).format(
                        font.ID,
                        font.FontName,
                        font.FamilyName,
                        font.FontFile,
                    )
                )
        else:
            print("No PublicRes")

        print("\n")
        document_res = Document.document_res()
        if document_res:
            if document_res.MultiMedias:
                for mm in document_res.MultiMedias.MultiMedia:
                    print(
                        (
                            "ID: {}"
                            + " " * 4
                            + "Type: {}"
                            + " " * 4
                            + "MediaFile: {}"
                            + " " * 4
                            + "Format: {}"
                        ).format(
                            mm.ID(),
                            mm.Type(),
                            mm.MediaFile(),
                            mm.select_Format(),
                        )
                    )
        else:
            print("No DocumentRes")



if __name__ == '__main__':
    ofd_file = Path(__file__).parent / 'tests' / 'files' / 'test3.ofd'
    ofd = Reader(ofd_file)
    print(ofd.OFD)
    ofd.verify()
