# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:32:20 2017

@author: Ryan Kim
"""

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 602)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget { background: #d8d8d2}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lb14 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb14.setFont(font)
        self.lb14.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb14.setFrameShape(QtGui.QFrame.Box)
        self.lb14.setFrameShadow(QtGui.QFrame.Plain)
        self.lb14.setLineWidth(1)
        self.lb14.setAlignment(QtCore.Qt.AlignCenter)
        self.lb14.setObjectName(_fromUtf8("lb14"))
        self.gridLayout.addWidget(self.lb14, 3, 2, 1, 1)
        self.lb15 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb15.setFont(font)
        self.lb15.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb15.setFrameShape(QtGui.QFrame.Box)
        self.lb15.setFrameShadow(QtGui.QFrame.Plain)
        self.lb15.setLineWidth(1)
        self.lb15.setAlignment(QtCore.Qt.AlignCenter)
        self.lb15.setObjectName(_fromUtf8("lb15"))
        self.gridLayout.addWidget(self.lb15, 3, 3, 1, 1)
        self.lb12 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb12.setFont(font)
        self.lb12.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb12.setFrameShape(QtGui.QFrame.Box)
        self.lb12.setFrameShadow(QtGui.QFrame.Plain)
        self.lb12.setLineWidth(1)
        self.lb12.setAlignment(QtCore.Qt.AlignCenter)
        self.lb12.setObjectName(_fromUtf8("lb12"))
        self.gridLayout.addWidget(self.lb12, 3, 0, 1, 1)
        self.lb2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb2.setFont(font)
        self.lb2.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb2.setFrameShape(QtGui.QFrame.Box)
        self.lb2.setFrameShadow(QtGui.QFrame.Plain)
        self.lb2.setLineWidth(1)
        self.lb2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.gridLayout.addWidget(self.lb2, 0, 2, 1, 1)
        self.lb3 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb3.setFont(font)
        self.lb3.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb3.setFrameShape(QtGui.QFrame.Box)
        self.lb3.setFrameShadow(QtGui.QFrame.Plain)
        self.lb3.setLineWidth(1)
        self.lb3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.gridLayout.addWidget(self.lb3, 0, 3, 1, 1)
        self.lb11 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb11.setFont(font)
        self.lb11.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb11.setFrameShape(QtGui.QFrame.Box)
        self.lb11.setFrameShadow(QtGui.QFrame.Plain)
        self.lb11.setLineWidth(1)
        self.lb11.setAlignment(QtCore.Qt.AlignCenter)
        self.lb11.setObjectName(_fromUtf8("lb11"))
        self.gridLayout.addWidget(self.lb11, 2, 3, 1, 1)
        self.lb6 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb6.setFont(font)
        self.lb6.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb6.setFrameShape(QtGui.QFrame.Box)
        self.lb6.setFrameShadow(QtGui.QFrame.Plain)
        self.lb6.setLineWidth(1)
        self.lb6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb6.setObjectName(_fromUtf8("lb6"))
        self.gridLayout.addWidget(self.lb6, 1, 2, 1, 1)
        self.lb10 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb10.setFont(font)
        self.lb10.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb10.setFrameShape(QtGui.QFrame.Box)
        self.lb10.setFrameShadow(QtGui.QFrame.Plain)
        self.lb10.setLineWidth(1)
        self.lb10.setAlignment(QtCore.Qt.AlignCenter)
        self.lb10.setObjectName(_fromUtf8("lb10"))
        self.gridLayout.addWidget(self.lb10, 2, 2, 1, 1)
        self.lb9 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb9.setFont(font)
        self.lb9.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb9.setFrameShape(QtGui.QFrame.Box)
        self.lb9.setFrameShadow(QtGui.QFrame.Plain)
        self.lb9.setLineWidth(1)
        self.lb9.setAlignment(QtCore.Qt.AlignCenter)
        self.lb9.setObjectName(_fromUtf8("lb9"))
        self.gridLayout.addWidget(self.lb9, 2, 1, 1, 1)
        self.lb8 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb8.setFont(font)
        self.lb8.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb8.setFrameShape(QtGui.QFrame.Box)
        self.lb8.setFrameShadow(QtGui.QFrame.Plain)
        self.lb8.setLineWidth(1)
        self.lb8.setAlignment(QtCore.Qt.AlignCenter)
        self.lb8.setObjectName(_fromUtf8("lb8"))
        self.gridLayout.addWidget(self.lb8, 2, 0, 1, 1)
        self.lb0 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb0.setFont(font)
        self.lb0.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb0.setFrameShape(QtGui.QFrame.Box)
        self.lb0.setFrameShadow(QtGui.QFrame.Plain)
        self.lb0.setLineWidth(1)
        self.lb0.setAlignment(QtCore.Qt.AlignCenter)
        self.lb0.setObjectName(_fromUtf8("lb0"))
        self.gridLayout.addWidget(self.lb0, 0, 0, 1, 1)
        self.lb7 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb7.setFont(font)
        self.lb7.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb7.setFrameShape(QtGui.QFrame.Box)
        self.lb7.setFrameShadow(QtGui.QFrame.Plain)
        self.lb7.setLineWidth(1)
        self.lb7.setAlignment(QtCore.Qt.AlignCenter)
        self.lb7.setObjectName(_fromUtf8("lb7"))
        self.gridLayout.addWidget(self.lb7, 1, 3, 1, 1)
        self.lb1 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb1.setFont(font)
        self.lb1.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb1.setFrameShape(QtGui.QFrame.Box)
        self.lb1.setFrameShadow(QtGui.QFrame.Plain)
        self.lb1.setLineWidth(1)
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.gridLayout.addWidget(self.lb1, 0, 1, 1, 1)
        self.lb4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb4.setFont(font)
        self.lb4.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb4.setFrameShape(QtGui.QFrame.Box)
        self.lb4.setFrameShadow(QtGui.QFrame.Plain)
        self.lb4.setLineWidth(1)
        self.lb4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb4.setObjectName(_fromUtf8("lb4"))
        self.gridLayout.addWidget(self.lb4, 1, 0, 1, 1)
        self.lb13 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb13.setFont(font)
        self.lb13.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb13.setFrameShape(QtGui.QFrame.Box)
        self.lb13.setFrameShadow(QtGui.QFrame.Plain)
        self.lb13.setLineWidth(1)
        self.lb13.setAlignment(QtCore.Qt.AlignCenter)
        self.lb13.setObjectName(_fromUtf8("lb13"))
        self.gridLayout.addWidget(self.lb13, 3, 1, 1, 1)
        self.lb5 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb5.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        self.lb5.setFont(font)
        self.lb5.setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
        self.lb5.setFrameShape(QtGui.QFrame.Box)
        self.lb5.setFrameShadow(QtGui.QFrame.Plain)
        self.lb5.setLineWidth(1)
        self.lb5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb5.setObjectName(_fromUtf8("lb5"))
        self.gridLayout.addWidget(self.lb5, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.menuMenu.addAction(self.actionReset)
        self.menuMenu.addAction(self.actionUndo)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lb14.setText(_translate("MainWindow", "", None))
        self.lb15.setText(_translate("MainWindow", "", None))
        self.lb12.setText(_translate("MainWindow", "", None))
        self.lb2.setText(_translate("MainWindow", "", None))
        self.lb3.setText(_translate("MainWindow", "", None))
        self.lb11.setText(_translate("MainWindow", "", None))
        self.lb6.setText(_translate("MainWindow", "", None))
        self.lb10.setText(_translate("MainWindow", "", None))
        self.lb9.setText(_translate("MainWindow", "", None))
        self.lb8.setText(_translate("MainWindow", "", None))
        self.lb0.setText(_translate("MainWindow", "", None))
        self.lb7.setText(_translate("MainWindow", "", None))
        self.lb1.setText(_translate("MainWindow", "", None))
        self.lb4.setText(_translate("MainWindow", "", None))
        self.lb13.setText(_translate("MainWindow", "", None))
        self.lb5.setText(_translate("MainWindow", "", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        
class MyGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, ):
        super(MyGui, self).__init__()
        self.setupUi(self)
        
        # create a matrix that will store the values of the tiles behind the GUI
        self.tiles = np.zeros((4,4), dtype = np.int)
        
        # select two starting points for initial tiles
        point1 = (random.randint(0,3), random.randint(0,3))
        point2 = (random.randint(0,3), random.randint(0,3))
        
        # make sure the two points are not the same
        while point1 == point2:
            point2 = (random.randint(0,3), random.randint(0,3))
            
        # update tiles 
        self.tiles[point1[0], point1[1]] = 2 if random.random() <= 0.60 else 4
        self.tiles[point2[0], point2[1]] = 2 if random.random() <= 0.60 else 4
        self.gridLayout.itemAtPosition(point1[0], point1[1]).widget().setText(_translate("MainWindow", str(self.tiles[point1[0], point1[1]]), None))
        self.gridLayout.itemAtPosition(point2[0], point2[1]).widget().setText(_translate("MainWindow", str(self.tiles[point2[0], point2[1]]), None))
        
    # function that will update values of the tiles displayed
    def updateTiles(self):
        for i in range(4):
            for j in range(4):
                if self.tiles[i,j] != 0:
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", str(self.tiles[i,j]), None))
                else:
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", "", None))
        return
                
    def addRandomTile(self):
        
        # find one of the locations where there are no tiles
        possibleLocation = np.where(self.tiles == 0)
        
        # if there is no where else to place tiles, then the game is over.
        if len(possibleLocation[0]) == 0:
            print 'lost'
            return
        
        # randomly select one of the locations to place the new tile
        choice = random.randint(0,len(possibleLocation[0])-1)
        
        self.tiles[possibleLocation[0][choice], possibleLocation[1][choice]] = 2 if random.random() <= 0.50 else 4
        self.gridLayout.itemAtPosition(possibleLocation[0][choice],possibleLocation[1][choice]).widget().setText(_translate("MainWindow", str(self.tiles[possibleLocation[0][choice],possibleLocation[1][choice]]), None))
        return
        
        
    def moveTiles(self, direction):
        return
        
    def keyPressEvent(self, key):
        if key.key() == QtCore.Qt.Key_Left:
            self.gridLayout.itemAtPosition(0,1).widget().setText(_translate("MainWindow", "18", None))
        if key.key() == QtCore.Qt.Key_Right:
            print 'right'
        if key.key() == QtCore.Qt.Key_Up:
            print 'up'
        if key.key() == QtCore.Qt.Key_Down:
            self.addRandomTile()
            

 
if __name__ == '__main__':
    from PyQt4 import QtGui, QtCore
    import numpy as np
    import random
    import sys
 
    app = QtGui.QApplication(sys.argv)
    main = MyGui()
    main.show()
    sys.exit(app.exec_())