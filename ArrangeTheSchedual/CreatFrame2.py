# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

    def __init__( self, parent , arg):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.SavingPath = wx.StaticText( self, wx.ID_ANY, u"保存路径", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.SavingPath.Wrap( -1 )

        gbSizer2.Add( self.SavingPath, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.SavingPathCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,20 ), 0 )
        gbSizer2.Add( self.SavingPathCtrl, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.SavingButton = wx.Button( self, wx.ID_ANY, u"打开文件夹", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        gbSizer2.Add( self.SavingButton, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer3.Add( gbSizer2, 0, wx.EXPAND, 5 )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.MemberPath = wx.StaticText( self, wx.ID_ANY, u"人员表格", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.MemberPath.Wrap( -1 )

        gbSizer3.Add( self.MemberPath, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.MemberPathCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,20 ), 0 )
        gbSizer3.Add( self.MemberPathCtrl, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.MemberPathButton = wx.Button( self, wx.ID_ANY, u"打开文件夹", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        gbSizer3.Add( self.MemberPathButton, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer3.Add( gbSizer3, 0, wx.EXPAND, 5 )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.StartTime = wx.StaticText( self, wx.ID_ANY, u"开始时间", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StartTime.Wrap( -1 )

        gbSizer5.Add( self.StartTime, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.StartData = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        gbSizer5.Add( self.StartData, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer3.Add( gbSizer5, 0, wx.EXPAND, 5 )

        gbSizer6 = wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.EndingTime = wx.StaticText( self, wx.ID_ANY, u"结束时间", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.EndingTime.Wrap( -1 )

        gbSizer6.Add( self.EndingTime, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.EndingData = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        gbSizer6.Add( self.EndingData, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer3.Add( gbSizer6, 0, wx.EXPAND, 5 )

        gbSizer7 = wx.GridBagSizer( 0, 0 )
        gbSizer7.SetFlexibleDirection( wx.BOTH )
        gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.ErrorText = wx.StaticText( self, wx.ID_ANY, u"欢迎使用本软件", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ErrorText.Wrap( -1 )

        gbSizer7.Add( self.ErrorText, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer3.Add( gbSizer7, 1, wx.EXPAND, 5 )

        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,300 ), wx.TE_MULTILINE )
        bSizer3.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();

        bSizer3.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events

        self.SavingButton.Bind(wx.EVT_BUTTON, self.SavingButtonClick)
        self.MemberPathButton.Bind(wx.EVT_BUTTON, self.MemberButtonClick)
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.OK_Click)
        self.m_sdbSizer1Cancel.Bind(wx.EVT_BUTTON, self.Cancel_Click)

        self.arg = arg

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def OK_Click(self, event):
        starttime = (self.StartData.GetValue())
        ReturnStartTime = ("{}-{}-{}".format(starttime.year,starttime.month+1,starttime.day))
        self.arg.StartTime = ReturnStartTime
        self.arg.MemberTable = self.MemberPathCtrl.GetValue()
        endtime = (self.EndingData.GetValue())
        ReturnEndTime = ("{}-{}-{}".format(endtime.year, endtime.month + 1, endtime.day))
        self.arg.EndTime = ReturnEndTime
        self.arg.InputMess = self.m_textCtrl6.GetValue()
        self.arg.SavingPath = self.SavingPathCtrl.GetValue()
        self.arg.MemberTable = self.MemberPathCtrl.GetValue()
        self.arg.SavingPath = self.SavingPathCtrl.GetValue()
        self.Destroy()
        event.Skip()

    def SavingButtonClick(self, event):
        # filesFilter = "CSV files (*.csv)|*.csv"
        DirDialog = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
        if DirDialog.ShowModal() == wx.ID_OK:
            DirPath = DirDialog.GetPath()
            self.SavingPathCtrl.SetValue(DirPath)
        event.Skip()

    def MemberButtonClick(self, event):
        filesFilter = "CSV files (*.csv)|*.csv"
        fileDialog = wx.FileDialog(self, message="多文件选择", wildcard=filesFilter, style=wx.FD_OPEN | wx.FD_MULTIPLE)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        paths = fileDialog.GetPaths()
        self.MemberPathCtrl.SetValue(paths[0])
        event.Skip()


    def Cancel_Click(self, event):
        event.Skip()

if __name__ == '__main__':
    app= wx.App()
    a = MyFrame5(None,"")
    a.Show()
    app.MainLoop()