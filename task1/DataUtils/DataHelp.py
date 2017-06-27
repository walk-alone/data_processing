#coding:utf-8

import os
from os.path import join
import datetime
today = datetime.datetime.now().strftime('%Y%m%d')

class DataProcess(object):
    def __init__(self,name='data_obj'):
        self.name = name
        self.S1_old = set()
        self.dic_Id1_old = {}
        self.S1_new = set()
        self.dic_Id1_new = {}
        self.detele_dataLine_num = set()
        self.add_dataLine_num = set()

    def reset(self):
        self.S1_old.clear()
        self.dic_Id1_old.clear()
        self.S1_new.clear()
        self.dic_Id1_new.clear()
        self.detele_dataLine_num.clear()
        self.add_dataLine_num.clear()

    # 在路径下建立一个文件夹
    def mkDir(self, path):
        dir_path =  path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path
    def getDirFiles(self,mypath='/mnt/data_documentRoot/data/'+today):
        return [f for f in os.listdir(mypath) if os.path.isfile(join(mypath, f))]