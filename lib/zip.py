#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hbh112233abc@163.com'

from pathlib import Path
import zipfile
import os
from tempfile import NamedTemporaryFile

def extract(ofd_file:Path)->Path:
    """提取ofd文件
    1. 创建临时zip文件,复制ofd文件为zip文件
    2. 解压zip到_unzip_files目录
    3. 删除临时zip文件
    4. 返回_unzip_files目录

    Args:
        ofd_file (Path): ofd文件

    Returns:
        Path: 解压后的_unzip_files目录
    """
    if isinstance(ofd_file,str):
        ofd_file = Path(ofd_file)
    # 读取OFD文件
    ofd_dir = ofd_file.parent
    ofd_name = ofd_file.stem
    # 创建临时zip文件
    temp = NamedTemporaryFile(suffix=".zip", dir=ofd_dir, delete=False)
    # 获取临时文件完整路径
    temp_path = temp.name
    # 将OFD文件数据复制到临时zip文件中
    temp.write(ofd_file.read_bytes())
    # 解压缩
    dst_path = ofd_dir / ofd_name+'_unzip_files'
    dst_path.mkdir()
    zip_file = zipfile.ZipFile(temp_path)
    for names in zip_file.namelist():
        zip_file.extract(names,dst_path)
    zip_file.close()
    # 删除临时文件
    temp.close()
    os.remove(temp_path)
    # 返回解压缩文件夹路径
    return dst_path

def compress(files_dir:Path,filename:str)->Path:
    """生成ofd文件
    1. 创建临时文件
    2. 将目标目录压缩到临时文件
    3. 临时文件复制为ofd文件
    4. 删除临时文件
    5. 返回ofd文件

    Args:
        files_dir (Path): 文件目录
        filename (str): ofd文件名

    Returns:
        Path: ofd文件
    """
    if isinstance(files_dir,str):
        files_dir = Path(files_dir)
    ofd_dir = files_dir.parent
    # 创建临时zip文件
    temp = NamedTemporaryFile(suffix=".zip", dir=ofd_dir, delete=False)
    # 获取临时文件完整路径
    temp_path = temp.name
    # 生成压缩包
    zip_file = zipfile.ZipFile(temp_path)
    for file in files_dir.iterdir():
        zip_file.write(file)
    zip_file.close()
    # 临时文件复制到ofd文件
    ofd_file = ofd_dir / filename
    with ofd_file.open('wb',encoding='utf-8') as ofd:
        ofd.write(temp.read())
    # 删除临时文件
    temp.close()
    os.remove(temp_path)
    return ofd_file
