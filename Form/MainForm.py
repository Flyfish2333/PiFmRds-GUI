# -*- coding: UTF-8 -*-
from PySide2.QtWidgets import QMainWindow, QFileDialog

from Thread.PiFmRdsThread import PiFmRdsThread
from Ui.MainWindow import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.localFile = ""
        self.freq = ""
        self.rt = ""
        self.ps = ""

    def open(self):
        self.show()

    def chooseFile(self):
        self.localFile, self.fileType = QFileDialog.getOpenFileName(self, "Choose Audio File", "./", "All File (*)")
        if self.localFile == "":
            pass
        else:
            self.filePath.setText(self.localFile)
            self.filePathData.setText(self.localFile)

    def setFreq(self):
        self.freq = self.freqData.text()
        self.fmFreq.setText(self.freq)

    def setPsText(self):
        self.ps = self.psTextData.text()
        self.psText.setText(self.ps)

    def setRtText(self):
        self.rt = self.rtTextData.text()
        self.rtText.setText(self.rt)

    def start(self):
        self.piFmRdsThread = PiFmRdsThread(self.localFile, self.freq, self.ps, self.rt)
        #self.piFmRdsThread.signal.connect(self.piFmRdsThreadBack)
        self.piFmRdsThread.start()
