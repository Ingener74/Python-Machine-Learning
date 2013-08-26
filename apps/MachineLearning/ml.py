#!/usr/bin/env python

import sys
try:
    from PySide import QtCore, QtGui
    from ui_mainform import Ui_MainWindow
except():
    print sys.exc_info()[0]
    print 'install PySide4'
    print 'sudo apt-get install python-pyside'
    sys.exit(1)

#from PySide import QtCore, QtGui
#from ui_mainform import Ui_MainWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

def main():
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
