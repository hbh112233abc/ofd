# OFD

OFD 文档解析库,开发中...

- [x] Reader
- [ ] Writer
- [ ] Convertor

## OFD 解析

```python
from ofdlib import Reader

file = "your_path_of_ofd_document.ofd"
ofd = Reader(file)

print(ofd.OFD)
print(ofd.documents)

for page in ofd.documents[0].pages():
    print(page)
    page.show()

```

## 参考资料

[jyh2012/ofd-parser](https://github.com/jyh2012/ofd-parser)
[DLTech21/ofd.js](https://github.com/DLTech21/ofd.js)
[ofdrw/ofdrw](https://github.com/ofdrw/ofdrw)
