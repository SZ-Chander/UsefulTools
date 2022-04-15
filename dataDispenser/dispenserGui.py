import argparse
import wx
import os
import shutil

import GUIDesign1

class Dispenser:
    def __init__(self,arg):
        self.arg = arg
        self.dataPath = self.arg.p
        self.dataType = self.arg.t
        self.dataClass = self.arg.c
        self.targetPath = self.arg.m
        self.groupName = self.arg.n

        self.dataGroup = []
        self.groupDict = {}

    def forward(self):
        self.dfsDataGetter(self.dataPath)
        self.dataDispen(self.dataClass, self.groupName)
        self.creatGroupDir(self.targetPath)

    def dfsDataGetter(self,path):
        dirFiles = os.listdir(path)
        for name in dirFiles:
            fullPath = "{}/{}".format(path,name)
            if(os.path.isdir(fullPath)):
                self.dfsDataGetter(fullPath)
            else:
                if(name.split('.')[-1] in self.dataType):
                    self.dataGroup.append(fullPath)

    def dataDispen(self, groupNum, groupNameSet):
        for num in range(groupNum):
            groupName = "{}{}".format(groupNameSet,num+1)
            self.groupDict[groupName] = self.dataGroup[num::groupNum]

    def creatGroupDir(self,path):
        for groupName in self.groupDict:
            for filePath in self.groupDict[groupName]:
                fileName = filePath.split('/')[-1]
                fullPath = "{}/{}/{}".format(path,groupName,fileName)
                if(os.path.isdir("{}/{}".format(path,groupName))!= True):
                    os.mkdir("{}/{}".format(path,groupName))
                shutil.copy(filePath,fullPath)

class getv:
    def __init__(self,value):
        self.value = value

    def forward(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--p", type=str,default=self.value['p'],help="数据一级路径")
        parser.add_argument('--t', default=self.value['t'], help="你想要分配的数据格式")
        parser.add_argument('--c', type=int, default=self.value['c'], help="你想要分配的组数")
        parser.add_argument('--n', type=str, default=self.value['n'], help="小组组名")
        parser.add_argument('--m', type=str, default=self.value['m'],help="数据目标路径")
        arg = parser.parse_args()
        try:
            Dispenser(arg).forward()
            return True
        except:
            return False



if __name__ == '__main__':
    app = wx.App()
    GUI = GUIDesign1.MyFrame1(None)
    GUI.Show()
    app.MainLoop()