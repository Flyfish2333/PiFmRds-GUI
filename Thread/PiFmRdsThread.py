# -*- coding: utf-8 -*-
import os

from PySide2.QtCore import QThread, Signal


class PiFmRdsThread(QThread):
    signal = Signal(str)

    def __init__(self, filePath:str, freq:str, psText:str, rtText:str):
        super(PiFmRdsThread, self).__init__()
        self.filepath = filePath
        self.freq = freq
        self.psText = psText
        self.rtText = rtText

    def run(self):
        order = "sudo ./pi_fm_rds " + '-freq "' + self.freq + '" -audio "' +self.filepath + '" -ps "' + self.psText + '" -rt "' + self.rtText + '"'
        print("order: ", order)
        result = os.popen(order).read()
        print(result)