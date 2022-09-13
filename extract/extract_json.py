import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])

from common.util import test_function
import json



def readjson():
    # 设置以utf-8R解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    f = open("../data/demo1.json", encoding="utf-8")
    file = json.load(f)
    family = file["fontFamily"]
    size = file["fontSize"]
    basesetting = file["BaseSettings"]["font"]  #注意多重结构的读取语法R

    return (family, size, basesetting)

if __name__ == '__main__':
    test_function()
    print(readjson())
