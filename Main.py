from GUI import GUI

import wx

def main():

    app = wx.App()
    ex = GUI(None, title="System")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
