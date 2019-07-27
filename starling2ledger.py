import wx
import os

class ConverterPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.csv_ctrl = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.ldg_ctrl = wx.TextCtrl(self, 2, style=wx.TE_MULTILINE | wx.TE_READONLY)
        text_sizer.Add(self.csv_ctrl, 1, wx.ALL | wx.EXPAND, 2)
        text_sizer.Add(self.ldg_ctrl, 1, wx.ALL | wx.EXPAND, 2)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        openButton = wx.Button(self, label = "Open")
        convertButton = wx.Button(self, label = "Convert")
        saveButton = wx.Button(self, label = "Save")
        exitButton = wx.Button(self, label = "Exit")

        openButton.Bind(wx.EVT_BUTTON, self.on_open)
        convertButton.Bind(wx.EVT_BUTTON, self.on_convert)
        saveButton.Bind(wx.EVT_BUTTON, self.on_save)
        exitButton.Bind(wx.EVT_BUTTON, self.on_exit)

        buttons_sizer.Add(openButton, 1, wx.EXPAND)
        buttons_sizer.Add(convertButton, 1, wx.EXPAND)
        buttons_sizer.Add(saveButton, 1, wx.EXPAND)
        buttons_sizer.Add(exitButton, 1, wx.EXPAND)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(text_sizer, 1, wx.EXPAND)
        main_sizer.Add(buttons_sizer, 0, wx.EXPAND)

        self.SetSizer(main_sizer)
        self.dirname = ''

    def on_open(self, e):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.csv", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename), 'r')
            self.csv_ctrl.SetValue(filehandle.read())
            filehandle.close()
        dlg.Destroy()

    def on_convert(self, e):
        print("converting")

    def on_save(self, e):
        print("saving")

    def on_exit(self, e):
        print("exiting")

class ConverterFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Starling CSV converter')
        self.panel = ConverterPanel(self)
        self.Centre()
        self.Show()
        self.Fit()


if __name__ == '__main__':
    app = wx.App(False)
    frame = ConverterFrame()
    app.MainLoop()
