import wx

class GUI(wx.Frame):

    def __init__(self, parent, title):

        super(GUI, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Please enter your information below.")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="First Name")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)
        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND,)

        text3 = wx.StaticText(panel, label="Last Name")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT, border=10)
        tc13 = wx.TextCtrl(panel)
        sizer.Add(tc13, pos=(3, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND,)

        text4 = wx.StaticText(panel, label="Date Of Birth")
        sizer.Add(text4, pos=(4, 0), flag=wx.LEFT|wx.TOP, border=10)
        tc4 = wx.TextCtrl(panel)
        sizer.Add(tc4, pos=(4, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND, border=5)

        text5 = wx.StaticText(panel, label="Place Of Birth")
        sizer.Add(text5, pos=(5, 0), flag=wx.TOP|wx.LEFT, border=10)
        tc5 = wx.TextCtrl(panel)
        sizer.Add(tc5, pos=(5, 1), span=(1, 2), flag=wx.TOP|wx.EXPAND, border=5)

        sb = wx.StaticBox(panel, label="Optional Attributes")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        boxsizer.Add(wx.CheckBox(panel, label="Public"), flag=wx.LEFT|wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Generate Default Constructor"), flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Generate Main Method"), flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(6, 0), span=(1, 5), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)


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
            print(' TEST ')
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


def main():

    app = wx.App()
    ex = GUI(None, title="System")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
