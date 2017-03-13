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
        
        # message box to tell user that they lost
        self.msg = QtGui.QMessageBox()
        self.msg.setIcon(QtGui.QMessageBox.Critical)
        self.msg.setWindowTitle('You Lost!')
        self.msg.setText('You Lost! Press Retry to try again!')
        self.msg.setStandardButtons(QtGui.QMessageBox.Retry)
        
        # message box to tell user that they won
        self.winMsg = QtGui.QMessageBox()
        self.winMsg.setIcon(QtGui.QMessageBox.Question)
        self.winMsg.setWindowTitle('Congratulations!')
        self.winMsg.setText('You made it to 2048. Would you like to continue?')
        self.winMsg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Retry)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "2048", None))
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
        
        # create a dictionary that will map directions
        self.direc = {'up': {'x' : 0, 'y' : -1}, 'right': {'x' : 1, 'y' : 0}, 'down': {'x' : 0, 'y' : 1}, 'left': {'x' : -1, 'y' : 0}}
        
        # another dictionary that will map values to colors
        self.colorDict = { 2: 'yellow', 4: '#4286f4', 8: '#f442b0', 16: '#22cc93', 32: '#cca422', 64: '#cc2b22', 128: '#e56778', 256: '#9967e5', 512: '#67dde5', 1024: '#e3e567', 2048: '#ff0000'  }
        
        # create game
        self.initGame()
        
        # connect signal so that we can undo moves or reset
        self.actionUndo.triggered.connect(self.undo)
        self.actionReset.triggered.connect(self.initGame)
        
    def initGame(self):
        self.userWon = False
        
         # create a matrix that will store the values of the tiles behind the GUI
        self.tiles = np.zeros((4,4), dtype = np.int)

        # select two starting points for initial tiles
        point1 = (random.randint(0,3), random.randint(0,3))
        point2 = (random.randint(0,3), random.randint(0,3))
        
        # make sure the two points are not the same
        while point1 == point2:
            point2 = (random.randint(0,3), random.randint(0,3))
        self.score = 0
#        self.tiles[point1] = 2 if random.random() <= 0.60 else 4
#        self.tiles[point2] = 2 if random.random() <= 0.60 else 4
#        self.score = max(self.tiles[point1], self.tiles[point2])
#        
#        self.gridLayout.itemAtPosition(point1[0], point1[1]).widget().setText(_translate("MainWindow", str(self.tiles[point1[0], point1[1]]), None))
#        self.gridLayout.itemAtPosition(point2[0], point2[1]).widget().setText(_translate("MainWindow", str(self.tiles[point2[0], point2[1]]), None))
        
        #self.tiles = np.array([[2,  4,  8,  16], [ 4,  8,  16,  32], [8,  16,  32,  64,], [16,  32,  64,  0]])
        self.tiles[0, 0:2] = 1024
        self.lastMove = self.tiles
        
        
        
        self.nonZeroEntries = np.count_nonzero(self.tiles)
        self.updateTiles()
        
    # function that will update values of the tiles displayed
    def updateTiles(self):
        for i in xrange(4):
            for j in xrange(4):
                if self.tiles[i,j] != 0:
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", str(self.tiles[i,j]), None))
                    color = 'QLabel { background:' + str(self.colorDict[self.tiles[i,j]]) + '}'
                    self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet(_fromUtf8(color))
                else:
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", "", None))
                    self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
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
        
        # place new tile
        self.tiles[possibleLocation[0][choice], possibleLocation[1][choice]] = 2 if random.random() <= 0.50 else 4
        self.gridLayout.itemAtPosition(possibleLocation[0][choice],possibleLocation[1][choice]).widget().setText(_translate("MainWindow", str(self.tiles[possibleLocation[0][choice],possibleLocation[1][choice]]), None))
        color = 'QLabel { background:' + str(self.colorDict[self.tiles[possibleLocation[0][choice], possibleLocation[1][choice]]]) + '}'
        self.gridLayout.itemAtPosition(possibleLocation[0][choice],possibleLocation[1][choice]).widget().setStyleSheet(_fromUtf8(color))
        self.nonZeroEntries += 1
        
        if self.nonZeroEntries == 16:
            if self.isMoveAvailable():
                print 'keep going'
            else:
                self.lose()
        
        return
        
    def moveTiles(self, direction):
        
        # work on making sure things don't mess up or w/e
        print direction, 'before:'
        print self.tiles
        colMov = self.direc[direction]['x']
        rowMov = self.direc[direction]['y']

        # build list of positions to travel in the correct order
        tileOrder = []
        
        # right most
        if colMov != 0:
            for i in xrange(4):
                for j in xrange(3, -1, -1):
                    if self.tiles[i,j] != 0:
                        tileOrder.append((i,j))
        
        # lowest
        elif rowMov != 0:
            for i in xrange(3, -1, -1):
                for j in xrange(4):
                    if self.tiles[i,j] != 0:
                        tileOrder.append((i,j))
            
        # switch to leftmost or highest depending on direction
        if  colMov == -1 or rowMov == -1:
            tileOrder.reverse()
           
        for currTile in tileOrder:
            
            # tile next to one that is being moved
            nextTile = (currTile[0] + rowMov, currTile[1] + colMov)

            # do not move tiles that are already on an edge
            if nextTile[0] > 3 or nextTile[0] < 0 or nextTile[1] > 3 or nextTile[1] < 0:
                continue
            
            # find position to put tile (not super efficient, but this process will take at most 3 steps)
            while self.tiles[nextTile] == 0:
                # stop if the position tile is supposed to move to is an edge
                if nextTile[0] + rowMov > 3 or nextTile[0] + rowMov < 0 or nextTile[1] + colMov > 3 or nextTile[1] + colMov < 0:
                    break
                nextTile = (nextTile[0] + rowMov, nextTile[1] + colMov)

            # if two tiles with same value collide, add the values together
            if self.tiles[currTile] == self.tiles[nextTile]:
                self.tiles[nextTile] *= 2
                self.tiles[currTile] = 0
                self.nonZeroEntries -= 1
                
                self.score = self.tiles[nextTile] if self.tiles[nextTile] > self.score else self.score
                if self.score == 2048 and not self.userWon:
                    self.userWon = True
                    self.updateTiles()
                    self.win()
                    return

            else:
                # if there is already a tile in the position furthest in that direction, place tile in spot before it
                if self.tiles[nextTile] != 0:
                    nextTile = (nextTile[0] - rowMov, nextTile[1] - colMov)
                
                # change value
                self.tiles[nextTile] = self.tiles[currTile]

                # to prevent tiles from being erased if they don't move
                if currTile != nextTile:
                    self.tiles[currTile] = 0
        
        self.updateTiles()
        self.addRandomTile()
        print 'lastmove:\n', self.lastMove
    
    # create a method that checks if there are any moves left that will be called when there are 16 pieces on the board
    def isMoveAvailable(self):
        
        # for each tile
        for i in xrange(0,3):
            for j in xrange(0,3):
                tile = (i,j)
                
                # check all four directions
                for direction in self.direc:
                    nextTile = (tile[0] + self.direc[direction]['y'], tile[1] + self.direc[direction]['x'])
                    
                    # tiles can be merged; move available
                    if self.tiles[tile] == self.tiles[nextTile]:
                        return True
        # otherwise,
        return False
         
    def undo(self):
        print 'undo'
        self.tiles = self.lastMove
        self.updateTiles()
    
    def lose(self):
        self.msg.buttonClicked.connect(self.initGame)
        self.msg.exec_()
        
    def win(self):
        retval = self.winMsg.exec_()
        
        # reset game if user chooses to restart
        if retval == 524288:
            self.initGame()
        # otherwise, continue game as usual
        else:
            self.addRandomTile()
            
    def continueOrReplay(self, click):
        print click
        
    def keyPressEvent(self, key):
        self.lastMove = np.array(self.tiles)  
        if key.key() == QtCore.Qt.Key_Up:
            self.moveTiles('up')
        elif key.key() == QtCore.Qt.Key_Right:
            self.moveTiles('right')
        elif key.key() == QtCore.Qt.Key_Down:
            self.moveTiles('down')
        elif key.key() == QtCore.Qt.Key_Left:
            self.moveTiles('left')
        return

            
if __name__ == '__main__':
    from PyQt4 import QtGui, QtCore
    import numpy as np
    import random
    import sys
 
    app = QtGui.QApplication(sys.argv)
    main = MyGui()
    main.show()
    sys.exit(app.exec_())