# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import dispenserGui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "数据均分助手", pos = wx.DefaultPosition, size = wx.Size( 510,350 ), style=wx.DEFAULT_FRAME_STYLE^(wx.MAXIMIZE_BOX) )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour('While')

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizerPath = wx.BoxSizer( wx.VERTICAL )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"文件路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.textBoxFilePath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		gbSizer2.Add( self.textBoxFilePath, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.buttonFilePath = wx.Button( self, wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gbSizer2.Add( self.buttonFilePath, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath.Add( gbSizer2, 1, wx.EXPAND, 5 )

		gbSizer21 = wx.GridBagSizer( 0, 0 )
		gbSizer21.SetFlexibleDirection( wx.BOTH )
		gbSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"目标路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gbSizer21.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.textBoxTargetPath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		gbSizer21.Add( self.textBoxTargetPath, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.buttonTargetPath = wx.Button( self, wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gbSizer21.Add( self.buttonTargetPath, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath.Add( gbSizer21, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizerPath, 1, wx.EXPAND, 5 )

		bSizerPath1 = wx.BoxSizer( wx.VERTICAL )

		gbSizer22 = wx.GridBagSizer( 0, 0 )
		gbSizer22.SetFlexibleDirection( wx.BOTH )
		gbSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"请输入数据格式，若为多种格式，请以%号分隔，如jpg%png，并按确认键进行确认", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gbSizer22.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath1.Add( gbSizer22, 1, wx.EXPAND, 5 )

		gbSizer211 = wx.GridBagSizer( 0, 0 )
		gbSizer211.SetFlexibleDirection( wx.BOTH )
		gbSizer211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"数据格式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer211.Add( self.m_staticText9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.textBoxFormat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		gbSizer211.Add( self.textBoxFormat, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.buttonFormat = wx.Button( self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gbSizer211.Add( self.buttonFormat, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath1.Add( gbSizer211, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizerPath1, 1, wx.EXPAND, 5 )

		bSizerPath11 = wx.BoxSizer( wx.VERTICAL )

		gbSizer221 = wx.GridBagSizer( 0, 0 )
		gbSizer221.SetFlexibleDirection( wx.BOTH )
		gbSizer221.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"请输入分组组数，如分10组数据就输入10，请不要输入非数字内容（包括单位）！", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gbSizer221.Add( self.m_staticText12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath11.Add( gbSizer221, 1, wx.EXPAND, 5 )

		gbSizer2111 = wx.GridBagSizer( 0, 0 )
		gbSizer2111.SetFlexibleDirection( wx.BOTH )
		gbSizer2111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"请输入分组组名，如输入group则每一组名为group1，group2等。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gbSizer2111.Add( self.m_staticText15, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath11.Add( gbSizer2111, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizerPath11, 1, wx.EXPAND, 5 )

		bSizerPath12 = wx.BoxSizer( wx.VERTICAL )

		gbSizer222 = wx.GridBagSizer( 0, 0 )
		gbSizer222.SetFlexibleDirection( wx.BOTH )
		gbSizer222.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"分组组数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gbSizer222.Add( self.m_staticText16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.textBoxGroupNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gbSizer222.Add( self.textBoxGroupNum, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"分组组名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gbSizer222.Add( self.m_staticText17, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.textBoxGroupName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gbSizer222.Add( self.textBoxGroupName, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button1111 = wx.Button( self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gbSizer222.Add( self.m_button1111, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath12.Add( gbSizer222, 1, wx.EXPAND, 5 )

		gbSizer2112 = wx.GridBagSizer( 0, 0 )
		gbSizer2112.SetFlexibleDirection( wx.BOTH )
		gbSizer2112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.labelTips = wx.StaticText( self, wx.ID_ANY, u"欢迎使用自动数据分组软件！作者S.Z.Chander，反馈bug请联系szchandler@icloud.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelTips.Wrap( -1 )

		gbSizer2112.Add( self.labelTips, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath12.Add( gbSizer2112, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizerPath12, 1, wx.EXPAND, 5 )

		bSizerPath121 = wx.BoxSizer( wx.VERTICAL )

		gbSizer2221 = wx.GridBagSizer( 0, 0 )
		gbSizer2221.SetFlexibleDirection( wx.BOTH )
		gbSizer2221.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.buttonGo = wx.Button( self, wx.ID_ANY, u"开始分组", wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
		gbSizer2221.Add( self.buttonGo, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.buttonReset = wx.Button( self, wx.ID_ANY, u"重置设定", wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
		gbSizer2221.Add( self.buttonReset, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizerPath121.Add( gbSizer2221, 1, wx.EXPAND, 5 )

		gbSizer21121 = wx.GridBagSizer( 0, 0 )
		gbSizer21121.SetFlexibleDirection( wx.BOTH )
		gbSizer21121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizerPath121.Add( gbSizer21121, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizerPath121, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonFilePath.Bind( wx.EVT_BUTTON, self.buttonFilePathClick )
		self.buttonTargetPath.Bind( wx.EVT_BUTTON, self.buttonTargetPathClick )
		self.buttonFormat.Bind( wx.EVT_BUTTON, self.buttonFormatClick )
		self.m_button1111.Bind( wx.EVT_BUTTON, self.buttonGroupSetClick )
		self.buttonGo.Bind( wx.EVT_BUTTON, self.buttonGoClick )
		self.buttonReset.Bind( wx.EVT_BUTTON, self.buttonResetClick )
		self.buttonGo.Enable(False)

		self.EnableKey = [0,0,0,0,0]



	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def buttonFilePathClick( self, event ):
		dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			pathLabel = dlg.GetPath()  # 文件夹路径
			self.textBoxFilePath.SetLabelText(pathLabel)
			self.EnableKey[0] = 1
		dlg.Destroy()
		self.canThebuttonGoClick()
		event.Skip()

	def buttonTargetPathClick( self, event ):
		dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			pathLabel = dlg.GetPath()  # 文件夹路径
			self.textBoxTargetPath.SetLabelText(pathLabel)
			self.EnableKey[1] = 1
		dlg.Destroy()
		self.canThebuttonGoClick()
		event.Skip()

	def buttonFormatClick( self, event ):
		formatStr = self.textBoxFormat.GetValue()
		if(formatStr.isspace() or len(formatStr)==0):
			self.EnableKey[2] = 0
			formatTips = "您的数据格式为空,请重新输入！"
		else:
			formatGroup = formatStr.split("%")
			formatTips = "您的数据格式为{},若有误请重新输入".format(str(formatGroup))
		self.m_staticText10.SetLabelText(formatTips)
		self.EnableKey[2] = 1
		self.canThebuttonGoClick()
		event.Skip()

	def buttonGroupSetClick( self, event ):
		groupNumStr = self.textBoxGroupNum.GetValue()
		groupName = self.textBoxGroupName.GetValue()
		try:
			groupNum = int(groupNumStr)
			self.m_staticText12.SetLabelText("输入成功，分组组数为{}".format(groupNum))
			self.EnableKey[3] = 1
		except:
			self.m_staticText12.SetLabelText("输入有误！分组组数请输入纯数字，如分10组请输入10，否则无法识别！")
			self.EnableKey[3] = 0
		if(groupName.isspace() or len(groupName)==0):
			self.m_staticText15.SetLabelText("分组名不能为空！")
			self.EnableKey[4] = 0
		else:
			self.m_staticText15.SetLabelText("您的小组分组名为{}".format(groupName))
			self.EnableKey[4] = 1
		self.canThebuttonGoClick()
		event.Skip()

	def buttonGoClick( self, event ):
		respont = "参数错误！请检查所有参数是否正确"
		messDict = {}

		messDict['p'] = self.textBoxFilePath.GetValue()
		messDict['m'] = self.textBoxTargetPath.GetValue()
		messDict['t'] = self.textBoxFormat.GetValue().split("%")
		messDict['c'] = int(self.textBoxGroupNum.GetValue())
		messDict['n'] = self.textBoxGroupName.GetValue()

		success = dispenserGui.getv(messDict).forward()
		if(success):
			respont = "分组成功！请查看分组是否正确！感谢使用！"
		self.labelTips.SetLabelText(respont)
		event.Skip()

	def buttonResetClick( self, event ):
		self.EnableKey = [0,0,0,0,0]
		self.textBoxFilePath.SetLabelText("")
		self.textBoxTargetPath.SetLabelText("")
		self.textBoxFormat.SetLabelText("")
		self.textBoxGroupNum.SetLabelText("")
		self.textBoxGroupName.SetLabelText("")

		self.m_staticText10.SetLabelText("请输入数据格式，若为多种格式，请以%号分隔，如jpg%png，并按确认键进行确认")
		self.m_staticText12.SetLabelText("请输入分组组数，如分10组数据就输入10，请不要输入非数字内容（包括单位）！")
		self.m_staticText15.SetLabelText("请输入分组组名，如输入group则每一组名为group1，group2等。若不输入默认为group")
		self.labelTips.SetLabelText("欢迎使用自动数据分组软件！作者S.Z.Chander，反馈bug请联系szchandler@icloud.com")

		self.canThebuttonGoClick()
		event.Skip()

	def canThebuttonGoClick(self):
		if(0 in self.EnableKey):
			self.buttonGo.Enable(False)
		else:
			self.buttonGo.Enable(True)


