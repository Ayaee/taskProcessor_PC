import os
import sys
import six

from PySide2.QtWidgets import QPushButton, QApplication
from Qt import QtCompat, QtWidgets, QtCore

from pipeline.engine import getEngine
from pipeline.tools import datas

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

uiPath = Path(__file__).parent / 'qt' / 'interface.ui'
UserRole = QtCore.Qt.UserRole

class windowTool(QtWidgets.QMainWindow):

    def __init__(self):
        super(windowTool, self).__init__()
        QtCompat.loadUi(str(uiPath), self)




#Test
if __name__ == '__main__':
    app = QApplication([])
    t = windowTool()
    t.show()
    app.exec_()