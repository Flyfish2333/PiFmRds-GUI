# -*- coding: UTF-8 -*-
import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication
from Form.MainForm import *

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    _translate = QtCore.QCoreApplication.translate

    mainForm = MainForm()
    mainForm.open()

    mainForm.chooseFile_btn.clicked.connect(mainForm.chooseFile)
    mainForm.setFreq_btn.clicked.connect(mainForm.setFreq)
    mainForm.setPsText_btn.clicked.connect(mainForm.setPsText)
    mainForm.setRtText_btn.clicked.connect(mainForm.setRtText)
    mainForm.start_btn.clicked.connect(mainForm.start)

    sys.exit(app.exec_())
