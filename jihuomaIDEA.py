"""
@program: jihuomaIDEA
@description: 下载zip包--》解压--》取激活码--》删除中间文件
@author: gaigaibill@gamil.com
@create: 2020-06-19 01:35
"""

import os
from urllib.request import urlretrieve
import zipfile
import shutil

url = 'http://idea.medeming.com/jihuoma/images/jihuoma.zip'
url_bakup = "http://idea.medeming.com/jets/images/jihuoma.zip"


def download_file(url, store_path):
    filename = url.split("/")[-1]
    filepath = os.path.join(store_path, filename)
    urlretrieve(url, filepath)
    return filename


def unzip(filename):
    # filename = 'jihuoma.zip'
    ubzipdir = filename.split('.')[0]
    with zipfile.ZipFile(filename, "r") as read:
        read.extractall(ubzipdir)
        read.close()
    return ubzipdir


def Activation_code(filename):
    base_path = filename
    files = os.listdir(base_path)
    full_path = os.path.join(base_path, files[0])
    with open(full_path) as fp:
        data = fp.read()
        print(data)
        return data


def delfile(dirname, zipname):
    shutil.rmtree(dirname)
    os.remove(zipname)


def main():
    zipname = download_file(url, '')
    dirname = unzip(zipname)
    Activation_code(dirname)
    delfile(dirname, zipname)


if __name__ == '__main__':
    main()
