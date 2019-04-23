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

        sb = wx.StaticBox(panel, label="Please enter your "
                                       "Current Location, Age, and Gender. For example: Location: Leeds, Age: 55, Gender: Male")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.descBox = wx.TextCtrl(panel, -1, value="Location: , Age: , Gender: ", size=(600, 100))
        boxsizer.Add(self.descBox, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)
        sizer.Add(boxsizer, pos=(5, 0), span=(5, 5), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        sb = wx.StaticBox(panel, label="Results")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.answerBox = wx.TextCtrl(panel, -1, size=(600, 100), style= wx.TE_MULTILINE|wx.TE_READONLY)
        boxsizer.Add(self.answerBox, flag=wx.LEFT|wx.TOP|wx.RIGHT, border=5)
        sizer.Add(boxsizer, pos=(10, 0), span=(5, 5), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        help_button = wx.Button(panel, label='Help')
        sizer.Add(help_button, pos=(15, 0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Help, help_button)

        submit_button = wx.Button(panel, label="Submit")
        sizer.Add(submit_button, pos=(15, 3))
        self.Bind(wx.EVT_BUTTON, self.OnButton_Submit, submit_button)

        exit_button = wx.Button(panel, label="Cancel")
        sizer.Add(exit_button, pos=(15, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, self.OnButton_Exit, exit_button)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)


    def OnButton_Help(self, event):
        help_button = wx.MessageBox('Please enter your information in this format: location: , age: , gender: ,'
                                    ' The order is not important however please include these 3 attributes.'
                                    ' You are required to enter this information so that the data set can provide'
                                    ' you with some health information. Not entering this information will result in an error.',
                                    'Info', wx.OK | wx.ICON_INFORMATION)

    def OnButton_Submit(self, event):

        submit_button = wx.MessageDialog(None, 'Are you sure?', caption='Submit',
                                        style=wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION)
        result = submit_button.ShowModal()
        submit_button.Destroy()

        if result == wx.ID_YES:

            first_name = self.nameBox1.GetValue()
            last_name = self.nameBox2.GetValue()
            description = self.descBox.GetValue()
            new_user = User(first_name, last_name, description);
            language = Language(description)

            print(Language.processContent(language))

            results = open("results.txt", "r")

            self.answerBox.AppendText(results.read())
            print(results.read())

            results.close()
            print(User.display_user(new_user))

    def OnButton_Exit( self, event):

        exit_button = wx.MessageDialog(None, 'Are you sure?', caption='Close',
                                      style=wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION)
        result = exit_button.ShowModal()
        exit_button.Destroy()

        if result == wx.ID_YES:
            open('results.txt', 'w').close()
            exit_button = self.Close()


