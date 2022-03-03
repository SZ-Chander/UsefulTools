import os
import argparse
import pandas as pd
import CreatFrame2
import TableFrame1
import wx
import wx.xrc
import wx.adv

class MessTranser():
    def __init__(self,mess,Times):
        self.mess = mess
        self.WokrTimeBase = ['夕','晨','早','晚','通']
        self.DateTimeKey = '全通'
        self.UsefulSysmbol = ['-','.']
        self.UselessSysmbol = ['，','、',",",';','；','$$']
        self.StandardTimes = Times

    def RemoveSysmbol(self,input_str):
        for i in self.UselessSysmbol:
            input_str = input_str.replace(i,'$')
        return input_str

    def forward(self):
        Totaltable = {}
        CheckedMess = self.WorkTimeTranslate()
        return CheckedMess

    def IsAllPass(self,Data):
        if(self.DateTimeKey in Data):
            return True
        else:
            return False

    def CheckDict(self,input_str):
        UsingDict = self.WokrTimeBase
        if(input_str.find(UsingDict[0]) != -1):
            return 0
        elif(input_str.find(UsingDict[1]) != -1):
            return 1
        elif(input_str.find(UsingDict[2]) != -1):
            return 2
        else:
            return -1

    def GetTime(self,Data):
        print('')

    def remove_char(self,str, n):
        front = str[:n]  # up to but not including n
        back = str[n + 1:]  # n+1 till the end of string
        return front + back

    def Point2Comma(self,input_str):
        try:
            float(input_str)
            if(input_str not in self.StandardTimes):
                return input_str.replace('.',',')
            else:
                return input_str
        except:
            return input_str

    def FindWorkTimeKeyLocation(self,ListDatas):
        KeyBox = []
        for num,data in enumerate(ListDatas):
            loacations = []
            if(data in self.WokrTimeBase):
                KeyBox.append(num)
            else:
                for worktimekey in self.WokrTimeBase:
                    loacation = data.find(worktimekey)
                    if(loacation != -1):
                        loacations.append(loacation)
                        break
                loacations.sort()
                for l in loacations:
                    KeyBox.append([num,l])
        return KeyBox

    def Period2Date(self,input_group):
        NewGroup = []
        month = self.StandardTimes[0].month
        for date in input_group:
            if(date.find('-') != -1):
                TimeGroup = date.split('-')
                # print(TimeGroup)
                for n, time in enumerate(TimeGroup):
                    try:
                        int(time)
                        TimeGroup[n] = "{}.{}".format(month,time)
                    except:
                        TimeGroup[n] = time
                    # print(n_time)
                StartTime = "2022-{}".format(TimeGroup[0]).replace('.','-')
                EndTime = "2022-{}".format(TimeGroup[1]).replace('.','-')
                # print(StartTime,EndTime)
                DateIndex = pd.date_range(StartTime,EndTime, freq='D')
                for DateTime in DateIndex:
                    TidyedTime = "{}.{}".format(DateTime.month, DateTime.day)
                    NewGroup.append(TidyedTime)
            else:
                try:
                    int(date)
                    NewDate = "{}.{}".format(month,date)
                    NewGroup.append(NewDate)
                except:
                    NewDate = date
                    NewGroup.append(NewDate)
        return NewGroup

    def TimeTranser(self,input_time):
        TimeSplitComma = input_time.split(',')
        NewGroup = self.Period2Date(TimeSplitComma)
        return NewGroup

    def TidyTimeStr(self,Datas):
        TimeDict = {'通':[],'早':[],'晚':[],'夕':[],'晨':[]}
        TimeString = ""
        for data in Datas:
            if(self.CheckDict(data) == -1):
                if(TimeString == ""):
                    TimeString = data
                else:
                    TimeString = "{}${}".format(TimeString,data)

            else:
                if (TimeString == ""):
                    TimeString = "{}*".format(data)
                else:
                    TimeString = "{}${}*".format(TimeString, data)

        OldData = (TimeString.split('*'))
        NewGroup = []
        for n_data in OldData:
            if(n_data != ''):
                n_data = self.RemoveSysmbol(n_data)
                n_data = n_data.replace('晚插','夕').replace('早插','晨').replace('$通','通').replace('$夕','夕').replace('$晨','晨').replace('$早','早').replace('$晚','晚')
                if(n_data[0] == '$'):
                    n_data = self.remove_char(n_data,0)
                NewGroup.append(n_data)
        KeyBox = self.FindWorkTimeKeyLocation(NewGroup)

        for num, key in enumerate(KeyBox):
            try:
                WorkTimeKey = NewGroup[num][key[1]]
                TimeContent = NewGroup[num].replace('夕','').replace('晨','').replace('早','').replace('晚','').replace('通','')
                TimeContent = self.Point2Comma(TimeContent).replace('$',',')
                TimeTotal = self.TimeTranser(TimeContent)
                TimeDict[WorkTimeKey] += TimeTotal
            except:
                continue
        return TimeDict

    def WorkTimeTranslate(self):
        UsefulData = []
        for n in range(len(self.mess)):
            if(n == 0):
                name = self.mess[n]
            else:
                UsefulData.append(self.mess[n])
        AllPass = self.IsAllPass(UsefulData)
        if(AllPass):
            ReturnMess = (name,True)
        else:
            Times = self.TidyTimeStr(UsefulData)
            ReturnMess = (name, False, Times)
        return ReturnMess

def TimeTranser(StartTimeStr,EndTimeStr):
    DatetimeIndex = pd.date_range(StartTimeStr,EndTimeStr,freq='D')
    TidyedTimeBox = [DatetimeIndex[0],DatetimeIndex[-1]]
    for DateTime in DatetimeIndex:
        TidyedTime = "{}.{}".format(DateTime.month,DateTime.day)
        TidyedTimeBox.append(TidyedTime)
    return TidyedTimeBox

def FirstInt(line):
    LineMess = line.replace('\n','').split('. ')
    if((len(LineMess)) == 1):
        return False,114514
    else:
        number = int(LineMess[0])
        PersonalMesses = LineMess[1].split(' ')
        pre_dels = []
        for n,mess in enumerate(PersonalMesses):
            if(mess == ''):
                pre_dels.append(n)
        for i in pre_dels:
            del PersonalMesses[i]
        return True,number,PersonalMesses

def GetTotalTable(mess,times):
    UsefulTimes = times
    del UsefulTimes[0]
    del UsefulTimes[0]
    TotalTable = {}

    for line in mess:
        Name = line[0]
        if(line[1]):
            TimeTable = {'通':UsefulTimes,'早':[],'晚':[],'夕':[],'晨':[]}
        else:
            TimeTable = line[2]
        TotalTable[Name] = TimeTable
    return TotalTable

def ReadMess(mess,timebox):
    numbers = []
    ReturnMesses = []
    for line in mess:
        line = line.replace('班','').replace('到','-').replace('晚插','夕').replace('早插','晨')
        ReturnMess = FirstInt(line)
        # print(ReturnMess)
        if(ReturnMess[0]):
            numbers.append(ReturnMess[1])
            UsefulMesses = ReturnMess[2]
            ReturnMesses.append(MessTranser(UsefulMesses,timebox).forward())
    TotalTable = GetTotalTable(ReturnMesses,timebox)
    return len(numbers), TotalTable

def UseCreatFrame(arg):
    app = wx.App()
    CreatFrame = CreatFrame2.MyFrame5(None,arg)
    CreatFrame.Show()
    app.MainLoop()
    return arg

def ReadInputCSV(inputpath):
    try:
        with open(inputpath,encoding='gbk') as csv_r:
            csv = csv_r.readlines()
    except:
        with open(inputpath,encoding='utf-8') as csv_r:
            csv = csv_r.readlines()
    new_csv = []
    for line in csv:
        line = line.replace(' ','')
        line = line.split(',')
        new_csv.append(line)
    return new_csv

def CreatTable(ColLabel, MemberTable, DataTable,SavePath):
    app = wx.App()
    TableApp = TableFrame1.MyFrame4(None, ColLabel, MemberTable,DataTable,SavePath)
    TableApp.Show()
    app.MainLoop()

def SetTable(TimesGroup,DataTable,MemberTable,SavePath):
    del MemberTable[0]
    CreatTable(TimesGroup, MemberTable, DataTable, SavePath)
    # print(DataTable,MemberTable,SavePath)

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-StartTime',type=str,default="2021-2-1")
    parse.add_argument('-EndTime',type=str,default="2021-2-15")
    parse.add_argument('-InputMess',type=str,default="Error!输入错误!")
    parse.add_argument('-MemberTable',type=str,default="Error!输入错误!")
    parse.add_argument('-SavingPath',type=str,default="Error!输入错误!")
    arg = parse.parse_args()

    arg = UseCreatFrame(arg)

    messes = arg.InputMess.split('\n')

    Times = TimeTranser(arg.StartTime,arg.EndTime)
    BaseDir = os.getcwd()
    MessPath = "{}/{}".format(BaseDir,"Mess.txt")

    MemberTable = ReadInputCSV(arg.MemberTable)

    PeopleNum,TableData = ReadMess(messes,Times)

    SetTable(Times,TableData,MemberTable,arg.SavingPath)
