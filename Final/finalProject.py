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
        MainWindow.setFixedSize(600, 700)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget { background: #faf8ef }")) 
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        font = QtGui.QFont(_fromUtf8("Helvetica"), pointSize = 20)
        font.setBold(True)
        
        # create a lose/win screen
        self.blankScreen = QtGui.QWidget(MainWindow)
        self.blankScreen.setStyleSheet('QWidget { background: #faf8ef }')
        self.blankScreen.setVisible(False)
        self.blankScreen.setFixedSize(600, 700)
        self.blankVertLayout = QtGui.QVBoxLayout(self.blankScreen)  
        self.winLose = QtGui.QLabel(self.blankScreen)
        self.winLose.setStyleSheet('QLabel { color: #776e65 }')
        self.winLose.setFont(font)
        self.winLose.setAlignment(QtCore.Qt.AlignCenter)
        self.blankVertLayout.addWidget(self.winLose)
        self.winLose.setVisible(True)
        
        # create a vertical layout
        self.vertLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.vertLayoutWidget.setGeometry(QtCore.QRect(0, 0, 600, 800))
        self.vertLayoutWidget.setMaximumHeight(700)
        self.vertLayoutWidget.setContentsMargins(25, 25, 25, 25)
        self.vertLayout = QtGui.QVBoxLayout(self.vertLayoutWidget)  
        
        # create game title
        font.setPointSize(36)
        font.setBold(False)
        self.title = QtGui.QLabel(self.vertLayoutWidget)
        self.title.setText('2048')
        self.title.setFont(font)
        self.title.setMaximumHeight(50)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setStyleSheet(_fromUtf8("QLabel { color : #776e65 }"))
        self.vertLayout.addWidget(self.title)
        
        # create score board and reset/undo buttons. Put in horizontal layout
        self.controlsWidget = QtGui.QWidget(self.vertLayoutWidget)
        self.controlsLayout = QtGui.QHBoxLayout(self.controlsWidget)
        self.controlsWidget.setMaximumHeight(50)
        
        # undo/reset buttons
        self.undoButton = QtGui.QPushButton(self.controlsWidget)
        self.undoButton.setText('undo')
        self.resetButton = QtGui.QPushButton(self.controlsWidget)
        self.resetButton.setText('reset')
        self.undoButton.setMaximumSize(50, 50)
        self.resetButton.setMaximumSize(50, 50)
        self.undoButton.setStyleSheet(_fromUtf8("QPushButton { background: #b2a392; color : #faf8ef; border-radius: 4px; border-color: #faf8ef }"))
        self.resetButton.setStyleSheet(_fromUtf8("QPushButton { background: #b2a392; color : #faf8ef; border-radius: 4px; border-color: #faf8ef }"))
        self.undoButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resetButton.setFocusPolicy(QtCore.Qt.NoFocus)
        font.setPointSize(12)
        font.setBold(True)
        self.undoButton.setFont(font)
        self.resetButton.setFont(font)
        self.controlsLayout.addWidget(self.undoButton)
        
        # display score
        self.scoreboard = QtGui.QLabel(self.vertLayoutWidget)
        self.scoreboard.setText('Score: 0')
        font.setPointSize(20)
        self.scoreboard.setFont(font)
        self.scoreboard.setMaximumHeight(50)
        self.scoreboard.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreboard.setStyleSheet(_fromUtf8("QLabel { color : #776e65 }"))
        self.controlsLayout.addWidget(self.scoreboard)
        self.controlsLayout.addWidget(self.resetButton)
        
        self.vertLayout.addWidget(self.controlsWidget)
        
        # create a grid layout for the game board
        self.gridLayoutWidget = QtGui.QWidget(self.vertLayoutWidget)
        self.vertLayout.addWidget(self.gridLayoutWidget)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        # add QLabels into the Grid Layout to act as game tiles (16)
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
        
        # adjust all text labels
        for i in xrange(4):
            for j in xrange(4):
                self.gridLayout.itemAtPosition(i,j).widget().setMaximumSize(QtCore.QSize(100,100))
                self.gridLayout.itemAtPosition(i,j).widget().setMinimumSize(QtCore.QSize(100,100))
                self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet('QLabel { background: #eee4da; border: 1px solid #faf8ef; border-radius: 4px }')
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "2048", None))
        
class game2048(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, ):
        super(game2048, self).__init__()
        self.setupUi(self)
        
        # create a dictionary that will map directions to their matrix directions
        self.direc = {
                'up': {'x' : 0, 'y' : -1}, 
                'right': {'x' : 1, 'y' : 0}, 
                'down': {'x' : 0, 'y' : 1}, 
                'left': {'x' : -1, 'y' : 0} }
        
        # another dictionary that will map tile values to colors
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
        
        # connect signals so that we can undo moves or reset
        self.undoButton.clicked.connect(self.undo)
        self.resetButton.clicked.connect(self.initGame)
    
    """
    Initialize game board. Called whenever a new game is started.
    Randomly selects two positions to place the initial tiles. 
    Then initializes those tiles as either 2 or 4. 
    """
    def initGame(self):
        self.userWon = False
        self.userLost = False

         # create a matrix that will store the values of the tiles behind the GUI
        self.tiles = np.zeros((4,4), dtype = np.int)

        # select two starting points for initial tiles. Saves positions as a tuple
        point1 = (random.randint(0,3), random.randint(0,3))
        point2 = (random.randint(0,3), random.randint(0,3))
        
        # make sure the two points are not the same
        while point1 == point2:
            point2 = (random.randint(0,3), random.randint(0,3))
            
        # add either 2 or 4 as starting blocks
        self.tiles[point1] = 2 if random.random() <= 0.90 else 4
        self.tiles[point2] = 2 if random.random() <= 0.90 else 4
        self.gridLayout.itemAtPosition(point1[0], point1[1]).widget().setText(_translate("MainWindow", str(self.tiles[point1[0], point1[1]]), None))
        self.gridLayout.itemAtPosition(point2[0], point2[1]).widget().setText(_translate("MainWindow", str(self.tiles[point2[0], point2[1]]), None))

        self.score = 0
        self.lastScore = self.score
        self.scoreboard.setText('Score: ' + str(self.score))
        
        self.updateTiles()
        
        return
        
    """
    This function will take the values from the tile numpy array and have the GUI reflect those values.
    It will also update the score displayed for the user
    """
    def updateTiles(self):
        
        # iterate through all tiles
        for i in xrange(4):
            for j in xrange(4):
                
                # tile that is greater than 0
                if self.tiles[i,j] != 0:
                    
                    # set the text to match the value
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", str(self.tiles[i,j]), None))
                    
                    # if user has already won, make tiles a pleasant pink color
                    if self.tiles[i,j] > 2048:
                        color = 'QLabel { background: #ffc1f7; color: #f9f6f2; border: 1px solid #faf8ef; border-radius: 4px }'
                    
                    # otherwise, grab the color from self.colorDict initialize in the constructor
                    else:
                        color = 'QLabel { background:' + str(self.colorDict[self.tiles[i,j]]['background']) + '; color:' + str(self.colorDict[self.tiles[i,j]]['text']) + '; border: 1px solid #faf8ef; border-radius: 4px' + '}'
                    
                    self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet(_fromUtf8(color))
                
                # if tile is zero, clear it out
                else:
                    
                    # clear out the text
                    self.gridLayout.itemAtPosition(i,j).widget().setText(_translate("MainWindow", "", None))
                    # clear the background color
                    self.gridLayout.itemAtPosition(i,j).widget().setStyleSheet(_fromUtf8("QLabel { background: #b2a392; border: 1px solid #faf8ef; border-radius: 4px }"))
                    
        # update score
        self.scoreboard.setText('Score: ' + str(self.score))
        return
    
    """
    This function will add a 2 or 4 tile to a random location that does not have a tile already.
    This will be called after the user makes a valid move
    """
    def addRandomTile(self):
        
        # find one of the locations where there are no tiles
        possibleLocation = np.where(self.tiles == 0)
        
        # if there is no where else to place tiles, then the game is over.
        if len(possibleLocation[0]) == 0:
            return
        
        # randomly select one of the locations to place the new tile
        choice = random.randint(0,len(possibleLocation[0])-1)
        
        # place new tile
        self.tiles[possibleLocation[0][choice], possibleLocation[1][choice]] = 2 if random.random() <= 0.90 else 4
        
        # check if user lost
        if np.count_nonzero(self.tiles) == 16:
            if not self.isMoveAvailable():
                self.lose()
        
        return
    
    """
    This function will move the tiles based on the user input.
    This is where most of the game logic is performed.
    """
    def moveTiles(self, direction):

        colMov = self.direc[direction]['x']
        rowMov = self.direc[direction]['y']
        validMove = False

        # build stack of positions to travel in the correct order
        tileOrder = []
        
        # store all nonzero tiles in right most order
        if colMov != 0:
            for i in xrange(4):
                for j in xrange(3, -1, -1):
                    if self.tiles[i,j] != 0:
                        tileOrder.append((i,j))
        
        # store all nonzero tiles in bottom to top order
        elif rowMov != 0:
            for i in xrange(3, -1, -1):
                for j in xrange(4):
                    if self.tiles[i,j] != 0:
                        tileOrder.append((i,j))
            
        # switch to leftmost or highest order depending on direction
        if  colMov == -1 or rowMov == -1:
            tileOrder.reverse()
            
        # tiles merged on this move
        mergedTiles = []
        
        # iterate through the tiles to move
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
            if self.tiles[currTile] == self.tiles[nextTile] and nextTile not in mergedTiles:
                validMove = True
                self.tiles[nextTile] *= 2
                self.tiles[currTile] = 0
                
                # mark that tile has been merged once
                mergedTiles.append(nextTile)
                
                # update score
                self.score += self.tiles[nextTile]
                
                # user won
                if self.score == 2048 and not self.userWon:
                    self.userWon = True
                    self.updateTiles()
                    self.win()
                    return
            
            # otherwise, just push a tile all the way in that direction
            else:
                # if there is already a tile in the position furthest in that direction, place tile in spot before it
                if self.tiles[nextTile] != 0:
                    nextTile = (nextTile[0] - rowMov, nextTile[1] - colMov)
                
                # change value
                self.tiles[nextTile] = self.tiles[currTile]

                # only erase if currTile moved
                if currTile != nextTile:
                    validMove = True
                    self.tiles[currTile] = 0
        
        if validMove:    
            self.addRandomTile()
            
        self.updateTiles()

        return
    
    """
    This will be called when there is a potential for the user to lose (i.e. 16 tiles are on the board)
    It does this by checking if there are any tiles next to each other that are the same
    """
    def isMoveAvailable(self):

        # for each tile
        for i in xrange(0,4,1):
            for j in xrange(0,4,1):
                tile = (i,j)
                
                for direction in self.direc:
                    
                    nextTile = (tile[0] + self.direc[direction]['y'], tile[1] + self.direc[direction]['x'])
                    
                    # ignore tiles past the edge
                    if nextTile[0] > 3 or nextTile[0] < 0 or nextTile[1] > 3 or nextTile[1] < 0:
                        continue
                    
                    # tiles can be merged; move available
                    if self.tiles[tile] == self.tiles[nextTile]:
                        return True

        # otherwise,
        return False
    
    """
    To be called when user presses the reset button. 
    Will bring user back to board before move made. Also works to undo resets.
    """
    def undo(self):
        self.tiles = self.lastMove
        self.score = self.lastScore
        self.updateTiles()
        return
    
    """
    displays the lose message. Gives user option to either quit or retry
    """
    def lose(self):
        self.winLose.setText('you lost. press r to retry or x to exit')
        self.blankScreen.setVisible(True)
        self.userLost = True
        return
    
    """ 
    win message. Gives user option to either restart the game or continue
    """
    def win(self):
        self.winLose.setText('you won! press c to continue or r to retry')
        self.blankScreen.setVisible(True)
        return
    
    """
    catches key presses and interprets them as moves
    """
    def keyPressEvent(self, key):

        # store last move
        if not self.blankScreen.isVisible():
            self.lastMove = np.array(self.tiles)
            self.lastScore = self.score
        
        # interpret key for board moves
        if key.key() == QtCore.Qt.Key_Up:
            self.moveTiles('up')
        elif key.key() == QtCore.Qt.Key_Right:
            self.moveTiles('right')
        elif key.key() == QtCore.Qt.Key_Down:
            self.moveTiles('down')
        elif key.key() == QtCore.Qt.Key_Left:
            self.moveTiles('left')
        
        # win/lose scenarios
        elif key.key() == QtCore.Qt.Key_C:
            if self.userWon and self.blankScreen.isVisible():
                self.blankScreen.setVisible(False)
                self.addRandomTile()
                self.updateTiles()
        elif key.key() == QtCore.Qt.Key_X:
            if self.userLost and self.blankScreen.isVisible():
                QtGui.QApplication.quit()
        elif key.key() == QtCore.Qt.Key_R and self.blankScreen.isVisible():
            self.initGame()
            self.blankScreen.setVisible(False)
            
        return

if __name__ == '__main__':
    from PyQt4 import QtGui, QtCore
    import numpy as np
    import random
    import sys
 
    app = QtGui.QApplication(sys.argv)
    main = game2048()
    main.show()
    sys.exit(app.exec_())