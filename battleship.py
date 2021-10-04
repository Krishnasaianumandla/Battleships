"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["no_of_rows"] = 10
    data["no_of_cols"] = 10
    data["boardSize"] = 500  
    data["cellSize"] = data["boardSize"]/data["no_of_cols"]
    data["no_of_ships"] = 5
    data["comp_board"] = emptyGrid(data["no_of_rows"],data["no_of_cols"])
    data["user_board"] = emptyGrid(data["no_of_rows"],data["no_of_cols"])
    # data["user_board"]= test.testGrid()
    data["comp_board"] = addShips(data["comp_board"],data["no_of_ships"]) 
    data["temporary_ship"]=test.testShip()
    data["user_added_ships"] = 0
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user_board"], True)
    drawShip(data,userCanvas,data["temporary_ship"])
    drawGrid(data,compCanvas,data["comp_board"], True)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
   grid=[[EMPTY_UNCLICKED for i in range(cols)] for j in range(rows)]
   return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row,col=random.randint(1,8),random.randint(1,8)
    """position=1 indicates vertical allignment 
    and position=0 indicated horizontal allignment"""
    position=random.randint(0,1)
    ship=[]
    if position == 1:
        for row in range(row-1,row+2):
            ship.append([row,col])
    else:
        for col in range(col-1,col+2):
            ship.append([row,col])
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in ship:
        if grid[i[0]][i[1]] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    while (numShips!=0):
        ship=createShip()
        if checkShip(grid,ship):
            for i in ship:
                grid[i[0]][i[1]] = SHIP_UNCLICKED
            numShips-=1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["no_of_rows"]):
        for col in range(data["no_of_cols"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(data["cellSize"]*col,data["cellSize"]*row,data["cellSize"]*(col+1),data["cellSize"]*(row+1),fill="yellow")
            else:
                canvas.create_rectangle(data["cellSize"]*col,data["cellSize"]*row,data["cellSize"]*(col+1),data["cellSize"]*(row+1),fill="blue")
            
    return data

### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ship[0][0]+1 == ship[1][0] == ship[2][0]-1 and ship[0][1]== ship[1][1]==ship[1][1]:
        return True
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][1]+1 == ship[1][1] == ship[2][1]-1 and ship[0][0]== ship[1][0]==ship[1][0]:
        return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x,y = int(event.x/data["cellSize"]),int(event.y/data["cellSize"])
    return [y,x]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    cellSize=data["cellSize"]
    for row in range(len(ship)):
        temp = ship[row]
        canvas.create_rectangle(cellSize*temp[1],cellSize*temp[0],cellSize*(temp[1]+1),cellSize*(temp[0]+1),fill="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship):
        if isVertical(ship) or isHorizontal(ship):
            return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if data["user_added_ships"] == 5:
        print("Start playing the game")
        return
    if shipIsValid(data["user_board"],data["temporary_ship"]):
        for ship in data["temporary_ship"]:
            data["user_board"][ship[0]][ship[1]] = SHIP_UNCLICKED
        data["user_added_ships"] += 1
    else:
        print("Ship clicked is not valid")
    data["temporary_ship"]=[]
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if [row,col] not in data["temporary_ship"]:
        data["temporary_ship"].append([row,col])
        if len(data["temporary_ship"]) == 3:
            placeShip(data)
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    # runSimulation(500, 500)
    test.testShipIsValid()
    # test.testIsHorizontal()
    # test.testDrawShip()
