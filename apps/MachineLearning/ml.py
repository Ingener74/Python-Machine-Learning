#!/usr/bin/env python

import sys
from PySide.QtCore import QObject
try:
    from PySide import QtCore, QtGui
    from ui_mainform import Ui_MainWindow
except():
    print sys.exc_info()[0]
    print 'install PySide4'
    print 'sudo apt-get install python-pyside'
    sys.exit(1)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('button1()'))
        
    def button1(self):
        print "button 1"

def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
