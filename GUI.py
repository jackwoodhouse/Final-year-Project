
from Person import User
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

        text4 = wx.StaticText(panel, label="Age")
        sizer.Add(text4, pos=(4, 0), flag=wx.LEFT|wx.TOP, border=10)
        self.ageBox = wx.TextCtrl(panel)
        sizer.Add(self.ageBox, pos=(4, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND,)

        text5 = wx.StaticText(panel, label="Place Of Birth")
        sizer.Add(text5, pos=(5, 0), flag=wx.TOP|wx.LEFT, border=10)
        self.location = wx.ComboBox(panel, choices=locationList)

        sizer.Add(self.location, pos=(5, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND, border=5)

        text6 = wx.StaticText(panel, label="Gender")
        sizer.Add(text6, pos=(6, 0), flag=wx.TOP|wx.LEFT, border=10)
        self.gender = wx.ComboBox(panel, choices=genderList)

        sizer.Add(self.gender, pos=(6, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND, border=5)

        sb = wx.StaticBox(panel, label="Optional Attributes")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        sizer.Add(boxsizer, pos=(7, 0), span=(1, 5), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        helpButton = wx.Button(panel, label='Help')
        sizer.Add(helpButton, pos=(8, 0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Help, helpButton)

        submitButton = wx.Button(panel, label="Submit")
        sizer.Add(submitButton, pos=(8, 3))
        self.Bind(wx.EVT_BUTTON, self.OnButton_Submit, submitButton)

        exitButton = wx.Button(panel, label="Cancel")
        sizer.Add(exitButton, pos=(8, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Exit, exitButton)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)




    def OnButton_Help( self, event ) :
        # The button that generated this event:
        helpButton = wx.MessageBox('Download completed', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnButton_Submit( self, event ) :
        # The button that generated this event:
        submitButton = wx.MessageDialog(None, 'Are you sure?', caption='Submit', style=wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION)
        result = submitButton.ShowModal()
        submitButton.Destroy()

        if result == wx.ID_YES:

            firstName = self.nameBox1.GetValue()
            lastName = self.nameBox2.GetValue()
            age = self.ageBox.GetValue()
            location = self.location.GetValue()
            gender = self.gender.GetValue()
            new_user = User(firstName, lastName, age, location, gender)

            new_user.displayUser()

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
