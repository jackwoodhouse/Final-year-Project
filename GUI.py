
from Person import User
from Input import Language
import wx

class GUI(wx.Frame):

    app = wx.App()
    app.MainLoop()

    def __init__(self, parent, title):

        super(GUI, self).__init__(parent, title=title)

        self.InitUI()
        self.Center()

    def InitUI(self):

        locationList = ["South Yorkshire", "London", "Cambridge"]
        genderList = ["Male", "Female"]
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 10)

        text1 = wx.StaticText(panel, label="Please enter your information below.")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="First Name")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)
        self.nameBox1 = wx.TextCtrl(panel)
        sizer.Add(self.nameBox1, pos=(2, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND,)

        text3 = wx.StaticText(panel, label="Last Name")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT, border=10)
        self.nameBox2 = wx.TextCtrl(panel)
        sizer.Add(self.nameBox2, pos=(3, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND,)

        sb = wx.StaticBox(panel, label="Give a short description of yourself including Age, Gender, Height, Weight and City")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.descBox = wx.TextCtrl(panel, -1, size=(500, 100))
        boxsizer.Add(self.descBox, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)
        sizer.Add(boxsizer, pos=(5, 0), span=(5, 5), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        sb = wx.StaticBox(panel, label="Results")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.answerBox = wx.TextCtrl(panel, -1, size=(500, 100))
        boxsizer.Add(self.answerBox,
            flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)
        sizer.Add(boxsizer, pos=(10, 0), span=(5, 5),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        helpButton = wx.Button(panel, label='Help')
        sizer.Add(helpButton, pos=(15, 0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Help, helpButton)

        submitButton = wx.Button(panel, label="Submit")
        sizer.Add(submitButton, pos=(15, 3))
        self.Bind(wx.EVT_BUTTON, self.OnButton_Submit, submitButton)

        exitButton = wx.Button(panel, label="Cancel")
        sizer.Add(exitButton, pos=(15, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Exit, exitButton)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)




    def OnButton_Help( self, event ) :

        helpButton = wx.MessageBox('Download completed', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnButton_Submit( self, event ) :

        submitButton = wx.MessageDialog(None, 'Are you sure?', caption='Submit', style=wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION)
        result = submitButton.ShowModal()
        submitButton.Destroy()

        if result == wx.ID_YES:

            firstName = self.nameBox1.GetValue()
            lastName = self.nameBox2.GetValue()
            text = self.descBox.GetValue()

            text = Language(text)

            print(Language.f1(text))




        else:
            print(' CLOSED ')

    def OnButton_Exit( self, event ) :
        exitButton = wx.MessageDialog(None, 'Are you sure?', caption='Submit', style=wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION)
        result = exitButton.ShowModal()
        exitButton.Destroy()

        if result == wx.ID_YES:
            exitButton = self.Close()
        else:
            print(' CLOSED ')
