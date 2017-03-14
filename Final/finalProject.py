# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:32:20 2017

@author: Ryan Kim
"""

"""
TODO:
    make sure random tiles only appear on valid moves
    Center the grid
    animations? 
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
        #MainWindow.resize(804, 602)
        MainWindow.resize(600, 800)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget { background: #faf8ef}")) 
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        # create a vertical layout
        self.vertLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.vertLayoutWidget.setGeometry(QtCore.QRect(0, 0, 600, 800))
        self.vertLayout = QtGui.QVBoxLayout(self.vertLayoutWidget)  
        
        # create game title
        font = QtGui.QFont(_fromUtf8("Helvetica"), pointSize = 36)
        self.title = QtGui.QLabel(self.vertLayoutWidget)
        self.title.setText('2048')
        self.title.setFont(font)
        self.title.resize(QtCore.QSize(100,100))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.vertLayout.addWidget(self.title)
        
        font.setPointSize(20)
        font.setBold(True)
        
        # create a grid layout for the game board
        self.gridLayoutWidget = QtGui.QWidget(self.vertLayoutWidget)
        self.gridLayoutWidget.setStyleSheet(_fromUtf8("QWidget { background: #776e65}"))
        self.vertLayout.addWidget(self.gridLayoutWidget)
        
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50,50,50,50)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        # create score board
        self.scoreboard = QtGui.QLabel(self.vertLayoutWidget)
        self.scoreboard.setText('Score: 0')
        self.scoreboard.setFont(font)
        self.scoreboard.resize(QtCore.QSize(100,100))
        self.scoreboard.setAlignment(QtCore.Qt.AlignCenter)
        self.vertLayout.addWidget(self.scoreboard)
        
        # add QLabels into the Grid Layout to act as game tiles
        self.lb14 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb14.setFont(font)
        self.lb14.setAlignment(QtCore.Qt.AlignCenter)
        self.lb14.setObjectName(_fromUtf8("lb14"))
        self.gridLayout.addWidget(self.lb14, 3, 2, 1, 1)
        self.lb15 = QtGui.QLabel(self.gridLayoutWidget)

        self.lb15.setFont(font)
        self.lb15.setAlignment(QtCore.Qt.AlignCenter)
        self.lb15.setObjectName(_fromUtf8("lb15"))
        self.gridLayout.addWidget(self.lb15, 3, 3, 1, 1)
        self.lb12 = QtGui.QLabel(self.gridLayoutWidget)

        self.lb12.setFont(font)
        self.lb12.setAlignment(QtCore.Qt.AlignCenter)
        self.lb12.setObjectName(_fromUtf8("lb12"))
        self.gridLayout.addWidget(self.lb12, 3, 0, 1, 1)
        
        self.lb2 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb2.setFont(font)
        self.lb2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.gridLayout.addWidget(self.lb2, 0, 2, 1, 1)
        
        self.lb3 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb3.setFont(font)
        self.lb3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.gridLayout.addWidget(self.lb3, 0, 3, 1, 1)
        
        self.lb11 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb11.setFont(font)
        self.lb11.setAlignment(QtCore.Qt.AlignCenter)
        self.lb11.setObjectName(_fromUtf8("lb11"))
        self.gridLayout.addWidget(self.lb11, 2, 3, 1, 1)
        
        self.lb6 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb6.setFont(font)
        self.lb6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb6.setObjectName(_fromUtf8("lb6"))
        self.gridLayout.addWidget(self.lb6, 1, 2, 1, 1)
        
        self.lb10 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb10.setFont(font)
        self.lb10.setAlignment(QtCore.Qt.AlignCenter)
        self.lb10.setObjectName(_fromUtf8("lb10"))
        self.gridLayout.addWidget(self.lb10, 2, 2, 1, 1)
        
        self.lb9 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb9.setFont(font)
        self.lb9.setAlignment(QtCore.Qt.AlignCenter)
        self.lb9.setObjectName(_fromUtf8("lb9"))
        self.gridLayout.addWidget(self.lb9, 2, 1, 1, 1)
        
        self.lb8 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb8.setFont(font)
        self.lb8.setAlignment(QtCore.Qt.AlignCenter)
        self.lb8.setObjectName(_fromUtf8("lb8"))
        self.gridLayout.addWidget(self.lb8, 2, 0, 1, 1)
        
        self.lb0 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb0.setFont(font)
        self.lb0.setAlignment(QtCore.Qt.AlignCenter)
        self.lb0.setObjectName(_fromUtf8("lb0"))
        self.gridLayout.addWidget(self.lb0, 0, 0, 1, 1)
        
        self.lb7 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb7.setFont(font)
        self.lb7.setAlignment(QtCore.Qt.AlignCenter)
        self.lb7.setObjectName(_fromUtf8("lb7"))
        self.gridLayout.addWidget(self.lb7, 1, 3, 1, 1)
        
        self.lb1 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb1.setFont(font)
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.gridLayout.addWidget(self.lb1, 0, 1, 1, 1)
        
        self.lb4 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb4.setFont(font)
        self.lb4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb4.setObjectName(_fromUtf8("lb4"))
        self.gridLayout.addWidget(self.lb4, 1, 0, 1, 1)
        
        self.lb13 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb13.setFont(font)
        self.lb13.setAlignment(QtCore.Qt.AlignCenter)
        self.lb13.setObjectName(_fromUtf8("lb13"))
        self.gridLayout.addWidget(self.lb13, 3, 1, 1, 1)
        
        self.lb5 = QtGui.QLabel(self.gridLayoutWidget)
        self.lb5.setFont(font)
        self.lb5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb5.setObjectName(_fromUtf8("lb5"))
        self.gridLayout.addWidget(self.lb5, 1, 1, 1, 1)
        
        # Main Window Stuff (Menu bars and other such things)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
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
        self.msg.setStandardButtons(QtGui.QMessageBox.Retry | QtGui.QMessageBox.Close)
        
        # message box to tell user that they won
        self.winMsg = QtGui.QMessageBox()
        self.winMsg.setIcon(QtGui.QMessageBox.Question)
        self.winMsg.setWindowTitle('Congratulations!')
        self.winMsg.setText('You made it to 2048. Would you like to continue?')
        self.winMsg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.Retry)
        
        # adjust all text labels
        for i in xrange(4):
            for j in xrange(4):
                self.gridLayout.itemAtPosition(i,j).widget().setMaximumSize(QtCore.QSize(100,100))
                self.gridLayout.itemAtPosition(i,j).widget().setMinimumSize(QtCore.QSize(100,100))
                self.gridLayout.itemAtPosition(i,j).widget().setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Raised)
                self.gridLayout.itemAtPosition(i,j).widget().setLineWidth(3)
                self.gridLayout.itemAtPosition(i,j).widget().setMidLineWidth(3)
        
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
        
        # create a dictionary that will map directions to their matrix directions
        self.direc = {'up': {'x' : 0, 'y' : -1}, 'right': {'x' : 1, 'y' : 0}, 'down': {'x' : 0, 'y' : 1}, 'left': {'x' : -1, 'y' : 0}}
        
        # another dictionary that will map values to colors
        #self.colorDict = { 2: '#eee4da', 4: '#ede0c8', 8: '#f2b179', 16: '#f59563', 32: '#f67c5f', 64: '#f65e3b', 128: '#edcf72', 256: '#edcc61', 512: '#edc850', 1024: '#edc53f', 2048: '#edc22e'  }
        self.colorDict = { 
                2: {'background': '#eee4da', 'text' : '#776e65'},
                4: {'background': '#ede0c8', 'text': '#776e65'}, 
                8: {'background' : '#f2b179', 'text': '#f9f6f2'}, 
                16: {'background': '#f59563', 'text': '#f9f6f2'}, 
                32: {'background' : '#f67c5f', 'text' : '#f9f6f2'}, 
                64: {'background' : '#f65e3b', 'text' : '#f9f6f2'}, 
                128: {'background' : '#edcf72', 'text' : '#f9f6f2'}, 
                256: {'background' : '#edcc61', 'text' : '#f9f6f2'}, 
                512: {'background' : '#edc850', 'text' : '#f9f6f2'}, 
                1024: {'background' : '#edc53f', 'text' : '#f9f6f2'}, 
                2048: {'background' : '#edc22e', 'text' : '#f9f6f2'}}
        
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
            
        # add either 2 or 4 as starting blocks
        self.tiles[point1] = 2 if random.random() <= 0.60 else 4
        self.tiles[point2] = 2 if random.random() <= 0.60 else 4
        self.gridLayout.itemAtPosition(point1[0], point1[1]).widget().setText(_translate("MainWindow", str(self.tiles[point1[0], point1[1]]), None))
        self.gridLayout.itemAtPosition(point2[0], point2[1]).widget().setText(_translate("MainWindow", str(self.tiles[point2[0], point2[1]]), None))
        
        # set initial score
        self.score = max(self.tiles[point1], self.tiles[point2])
        self.scoreboard.setText('Score: ' + str(self.score))
        
        """Win/Lose scenarios for testing"""
#        self.tiles = np.array([[2,  4,  8,  16], [ 4,  8,  16,  32], [8,  16,  32,  64,], [16,  32,  64,  0]])
#        self.tiles[0, 0:2] = 2048
#        self.lastMove = self.tiles
        
        self.updateTiles()
        
    # function that will update values of the tiles displayed
    def updateTiles(self):
        for i in xrange(4):
            for j in xrange(4):
                if self.tiles[i,j] != 0:
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", str(self.tiles[i,j]), None))
                    if self.tiles[i,j] > 2048:
                        color = 'QLabel { background:' + '#ffc1f7' + '}'
                    else:
                        color = 'QLabel { background:' + str(self.colorDict[self.tiles[i,j]]['background']) + '; color:' + str(self.colorDict[self.tiles[i,j]]['text']) + '}'
                    self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet(_fromUtf8(color))
                else:
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", "", None))
                    self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet(_fromUtf8("QLabel { background: transparent}"))
                    
        # update score
        self.scoreboard.setText('Score: ' + str(self.score))
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
        color = 'QLabel { background:' + str(self.colorDict[self.tiles[possibleLocation[0][choice], possibleLocation[1][choice]]]['background']) + '; color: ' + str(self.colorDict[self.tiles[possibleLocation[0][choice], possibleLocation[1][choice]]]['text']) + '}'
        self.gridLayout.itemAtPosition(possibleLocation[0][choice],possibleLocation[1][choice]).widget().setStyleSheet(_fromUtf8(color))
        
        if np.count_nonzero(self.tiles) == 16:
            if self.isMoveAvailable():
                print 'keep going'
            else:
                self.lose()
        
        return
        
    def moveTiles(self, direction):
    
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
                
                # update score
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
        
        # generate tile if valid move was made
        # probably a better way to do this, but since there are only 16 comparisons to make, shouldn't be horrendous
        validMove = False
        for i in xrange(0, 4, 1):
            for j in xrange(0, 4, 1):
                if self.tiles[i, j] != self.lastMove[i, j]:
                    validMove = True
                    break
        if validMove:    
            self.addRandomTile()
        #print 'lastmove:\n', self.lastMove
    
    # create a method that checks if there are any moves left that will be called when there are 16 pieces on the board
    def isMoveAvailable(self):
        print 'checking if user lost'
        # for each tile
        for i in xrange(0,4,1):
            for j in xrange(0,4,1):
                tile = (i,j)
                for direction in self.direc:
                    nextTile = (tile[0] + self.direc[direction]['y'], tile[1] + self.direc[direction]['x'])
                    if nextTile[0] > 3 or nextTile[0] < 0 or nextTile[1] > 3 or nextTile[1] < 0:
                        continue
                    # tiles can be merged; move available
                    if self.tiles[tile] == self.tiles[nextTile]:
                        return True

        # otherwise,
        return False
    
    # To be called when user presses the reset button. Will bring user back to board before move made. Also works to undo resets.
    def undo(self):
        self.tiles = self.lastMove
        self.score = np.amax(self.lastMove)
        self.updateTiles()
    
    # displays the lose message box. Gives user option to either quit or retry
    def lose(self):
        retval = self.msg.exec_()
        if retval == 2097152:
            sys.exit(app.exec_())
        elif retval == 524288:
            self.initGame()
    
    # win message box. Gives user option to either restart the game or continue
    def win(self):
        retval = self.winMsg.exec_()
        
        # reset game if user chooses to restart
        if retval == 524288:
            self.initGame()
        # otherwise, continue game as usual
        else:
            self.addRandomTile()
    
    # catches key presses and interprets them as moves
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