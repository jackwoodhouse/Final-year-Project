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
        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(8, 0), flag=wx.LEFT, border=10)
        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(8, 3))
        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(8, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)


def main():

    app = wx.App()
    ex = GUI(None, title="System")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
