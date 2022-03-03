# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import time

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

    def __init__( self, parent, TimeData, MemberTable, InputTableData, SavePath ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 834,427 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.DataTable = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 834,427 ), 0 )
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.SavePath = SavePath
        self.TimeData = TimeData
        self.MemberTable = MemberTable
        self.InputTableData = InputTableData
        self.PeopleDict = {}
        self.worktimetable = {'通班':8,'早班':8,'晚班':8,'晨班':4,'夕班':4,'中插班':5,'/':0,'':0}

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.ConfirmButton = wx.Button(self, wx.ID_ANY, u"导出表格", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.ConfirmButton, 0, wx.ALL, 5)

        self.UpDateButton = wx.Button(self, wx.ID_ANY, u"更新表格", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.UpDateButton, 0, wx.ALL, 5)

        self.DataTable = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.DataTable.CreateGrid(len(MemberTable), len(TimeData)+1 )
        self.DataTable.EnableEditing(True)
        self.DataTable.EnableGridLines(True)
        self.DataTable.EnableDragGridSize(False)
        self.DataTable.SetMargins(0, 0)

        # Columns
        self.DataTable.EnableDragColMove(False)
        self.DataTable.EnableDragColSize(True)
        self.DataTable.SetColLabelSize(30)
        self.DataTable.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.DataTable.EnableDragRowSize(True)
        self.DataTable.SetRowLabelSize(80)
        self.DataTable.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.DataTable.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1.Add(self.DataTable, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ConfirmButton.Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.UpDateButton.Bind(wx.EVT_BUTTON, self.UpDateGird)
        self.DataTable.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.CellChange)
        self.DataTable.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.SelectCell)


        for num,row in enumerate(TimeData):
            self.DataTable.SetColLabelValue(num,row)
            if(num == len(TimeData) - 1):
                self.DataTable.SetColLabelValue(num+1,'工时')
        for num,row in enumerate(MemberTable):
            self.DataTable.SetRowLabelValue(num,row[0])

        self.MakeTable()

    def __del__( self ):
        pass

    def CellChange(self, event):
        event.Skip()

    def MakeTable(self):
        TimeDict = {}
        for person in self.MemberTable:
            name = person[0]
            self.PeopleDict[name] = []

        for num, time in enumerate(self.TimeData):
            TimeDict[time] = num

        for name in self.InputTableData:
            WorkTimeGroup = []
            for i in range(len(self.TimeData)):
                WorkTimeGroup.append('')
            for worktime in self.InputTableData[name]:
                Times = self.InputTableData[name][worktime]
                for time in Times:
                    WorkTimeGroup[TimeDict[time]] = worktime
            for num,worktime in enumerate(WorkTimeGroup):
                if(worktime == ''):
                    WorkTimeGroup[num] = '/'
                else:
                    WorkTimeGroup[num] = "{}班".format(WorkTimeGroup[num])

            self.PeopleDict[name] = WorkTimeGroup

        for num, name in enumerate(self.PeopleDict):
            RowNum = num
            for ListNum, TimeWorktime in enumerate(self.PeopleDict[name]):
                # print(RowNum,ListNum)
                try:
                    self.DataTable.SetCellValue(RowNum,ListNum,TimeWorktime.replace('夕','晚插').replace('晨','早插'))
                except:
                    continue
        self.UpDateTable()

    def UpDateTable(self):
        for num,name in enumerate(self.PeopleDict):
            TotalGroup = []
            try:
                for cell in range(len(self.TimeData)):
                    CellData = self.DataTable.GetCellValue(num,cell).replace('晚插','夕').replace('早插','晨')
                    TotalGroup.append(CellData)
                TotalWorkTime = 0
            except:
                continue
            for Work in TotalGroup:
                try:
                    TotalWorkTime += self.worktimetable[Work]
                except:
                    continue
            self.DataTable.SetCellValue(num,len(self.TimeData),str(TotalWorkTime).replace('夕','晚插').replace('晨','早插'))
            # print(name,TotalWorkTime)

    def GetTableMess(self):
        total = []
        num = len(self.MemberTable)
        cell = len(self.TimeData) + 1
        for n in range(num):
            line = []
            for c in range(cell):
                line.append(self.DataTable.GetCellValue(n,c))
            total.append(line)
        return total


    def CreatExcelList(self):
        Total = []
        TotalLineMess = self.GetTableMess()
        TotalList = []
        MemberList = self.MemberTable
        TotalList.append(self.TimeData)
        for num,MessLine in enumerate(MemberList):
            MessLineGroup = []
            MessLineGroup.append("{}".format(MessLine[1].replace('\n','')))
            MessLineGroup.append("{}".format(MessLine[2].replace('\n','')))
            MessLineGroup.append("{}".format(MessLine[0].replace('\n','')))

            for sigleMess in TotalLineMess[num]:
                MessLineGroup.append(sigleMess)
            for num,mess in enumerate(MessLineGroup):
                if(MessLineGroup[num] == ''):
                    MessLineGroup[num] = '/'
            Total.append(MessLineGroup)
        return Total

    def WriteCsvTable(self,DataTable):
        SavePath = self.SavePath
        NowTime = time.localtime()
        filename = "{}-{}-{}-{}-{}导出表".format(NowTime.tm_year, NowTime.tm_mon, NowTime.tm_mday,NowTime.tm_hour, NowTime.tm_min)
        CSVPath = "{}/{}.csv".format(SavePath,filename)

        csv_str = []

        for line in DataTable:
            line_str = ""
            for cell in line:
                line_str += "{},".format(cell)
            csv_str.append(line_str)

        with open(CSVPath,'w',encoding='gbk') as csv:
            for line in csv_str:
                csv.writelines(line)
                csv.write('\n')

    # Virtual event handlers, overide them in your derived class
    def SelectCell( self, event ):
        event.Skip()

    def ButtonClick( self, event ):
        TotalTable = self.CreatExcelList()
        self.WriteCsvTable(TotalTable)
        event.Skip()

    def UpDateGird(self, event):
        self.UpDateTable()
        event.Skip()


if __name__ == '__main__':
    app= wx.App()
    a = MyFrame4(None,['5','6','7','8','9'])
    a.Show()
    app.MainLoop()