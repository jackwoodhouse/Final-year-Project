from GUI import GUI

def main():

    ex = GUI(None, title="System")
    ex.Show()
    GUI.app.MainLoop()


if __name__ == '__main__':
    main()
