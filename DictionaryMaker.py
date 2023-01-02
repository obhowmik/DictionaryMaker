#SumanWorkTrack by Suman
import sys, os
from PyQt6 import uic, QtSql #QtGui,, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from natdictionary import *
sys.dont_write_bytecode = True

# get the directory of this script
path = os.path.dirname(os.path.abspath(__file__))

MainWindowUI, MainWindowBase = uic.loadUiType(
    os.path.join(path, 'Core.ui'))

class MyWindowClass(MainWindowBase, MainWindowUI):

    def __init__(self, parent=None):
        MainWindowBase.__init__(self, parent)
        self.setupUi(self)

        self.applist.insertItem (0, 'NatDictionary'  )
        self.stack.addWidget (NatDictionary(self))

        # CONNECTIONs
        #connect list to stack
        self.applist.currentRowChanged.connect(self.display)

    def display(self,i):
        self.stack.setCurrentIndex(i)

#Starts the main GUI window
app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.setWindowTitle('DictionaryMaker')
myWindow.show()
app.exec()