import re

def readFile(fileName, instructList):
    oneLine = []
    file = open(fileName, "r")
    for line in file:
        inst = line.replace(',','')
        x = inst.split()
        instructList.append(x)
    file.close()

def createBoard(instructList, scoreBoard):
    for i in range(len(instructList)):
        row = [0,0,0,0, "Issue", 0]
        if(instructList[i][0] == "L.D" or instructList[i][0] == "S.D"):
            row[5] = 1
        elif(instructList[i][0][0:3] == "ADD" or instructList[i][0][0:3] == "SUB"):
            row[5] = 2
        elif(instructList[i][0] == "MUL.D"):
            row[5] = 10
        else:
            row[5] = 40
        scoreBoard.append(row)


def displayBoard(scoreBoard):
    for i in  range(len(scoreBoard)):
        print(scoreBoard[i])

def createRegisters(floatRegister, intRegister):
    firstLetter = "F"
    index = 0
    fullword = ""
    for i in range(32):
        element = ["" , 0.0]
        fullword = firstLetter + str(i)
        element[0] = fullword
        floatRegister.append(element)
        fullword = ""
    firstLetter = "$"
    index = 0
    fullword = ""
    for i in range(32):
        element = ["" , 0]
        fullword = firstLetter + str(i)
        element[0] = fullword
        intRegister.append(element)
        fullword = ""

def insertUnit(instruction, index, funcUnit):
    theUnit = ""
    if(instruction[0] == "L.D" or instruction[0] == "S.D"):
        theUnit = "Integer"
    elif(instruction[0][0:3] == "ADD" or instruction[0][0:3] == "SUB"):
        theUnit = "Add"
    elif(instruction[0] == "MUL.D"):
        theUnit = "Mul"
    else:
        theUnit = "Div"

    for i in range(len(funcUnit)):
        if (funcUnit[i][0] == theUnit):
            if(funcUnit[i][1] == -1 or funcUnit[i][1] == index):
                if (instruction[0] == "S.D"):
                    funcUnit[i][1] = index
                    funcUnit[i][2] = instruction[2]
                    funcUnit[i][3] = instruction[1]
                elif (instruction[0] == "L.D"):
                    funcUnit[i][1] = index
                    funcUnit[i][2] = instruction[1]
                    funcUnit[i][3] = instruction[2]
                else:
                    funcUnit[i][1] = index
                    funcUnit[i][2] = instruction[1]
                    funcUnit[i][3] = instruction[2]
                    funcUnit[i][4] = instruction[3]
                return True
    return False

def removeUnit(instruction, index, funcUnit):
    theUnit = ""
    if(instruction[0] == "L.D" or instruction[0] == "S.D"):
        theUnit = "Integer"
    elif(instruction[0][0:3] == "ADD" or instruction[0][0:3] == "SUB"):
        theUnit = "Add"
    elif(instruction[0] == "MUL.D"):
        theUnit = "Mul"
    else:
        theUnit = "Div"

    for i in range(len(funcUnit)):
        if (funcUnit[i][0] == theUnit):
            if(funcUnit[i][1] == index):
                funcUnit[i][1] = -1
                funcUnit[i][2] = ""
                funcUnit[i][3] = ""
                funcUnit[i][4] = ""
            return True
    return False



def main():
    memoryData = [["(0)",45],["(1)",12],["(2)",0],["(3)",0],["(4)",10],["(5)",135],["(6)",254],["(7)",127],["(8)",18],["(9)",4],
                  ["(10)",55],["(11)",8],["(12)",2],["(13)",98],["(14)",13],["(15)",5],["(16)",233],["(17)",158],["(18)",167]]

    funcUnit = [["Integer", -1, "", "", ""],
                ["Add", -1, "", "", ""],
                ["Mul", -1, "", "", ""],
                ["Div", -1, "", "", ""]]

    floatRegister = []
    intRegister = []
    createRegisters(floatRegister, intRegister)
    fileName = "Instruction Set.txt"
    scoreBoard = []
    instructList = []
    readFile(fileName, instructList)
    createBoard(instructList, scoreBoard)

main()