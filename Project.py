def readFile(instructList):
    oneLine = []
    file = open("Instruction Set.txt", "r")
    for line in file:
        inst = line.replace(',','')
        x = inst.split()
        
        instructList.append(x)
       
    file.close()
    
def createBoard(instructList, scoreBoard):
    file = open("Instruction Set.txt", "r")
    firstRow = ["Instruction status"]
    secRow = ["Instruction", "Issue", "Read", "Execution", "Write"]
    scoreBoard.append(firstRow)
    scoreBoard.append(secRow)
    row = ["", "", "", "", "", "", "", ""]
    for x in file:
        row = ["", "", "", "", ""]
        x = x.strip()
        row[0] = x
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
        
def algorithm(scoreBoard, instruction):
    print("")


def getVal(register, memData, floatData, intData):
    
    if (register[0] == 'F'):
        index = int(register[1:])
        num = floatData[index][1]
    elif (register[0] == '$'):
        index = int(register[1:])
        num = intData[index][1]
    else:
        x = register.replace(')', '(')
        number = x.split('(')
        if len(number) > 1:
            num = memData[int(number[0]) + int(number[1])][1]
        else:
            num = int(register)
    return num


def assignVal(value, register, memData, floatData, intData):
    
    if (register[0] == 'F'):
        index = int(register[1:])
        floatData[index][1] = value
    elif (register[0] == '$'):
        index = int(register[1:])
        intData[index][1] = value
    else:
        x = register.replace(')', '(')
        number = x.split('(')
        if len(number) > 1:
            memData[int(number[0]) + int(number[1])][1] = value



def doInstruction(instruction, memData, floatData, intData):

    if(instruction[0] == "L.D"):
        val = getVal(instruction[2], memData, floatData, intData)
        assignVal(val, instruction[1], memData, floatData, intData)
    elif(instruction[0] == "S.D"):
        val = getVal(instruction[1], memData, floatData, intData)
        assignVal(val, instruction[2], memData, floatData, intData)
    elif(instruction[0][0:3] == "ADD"):
        val1 = getVal(instruction[2], memData, floatData, intData)
        val2 = getVal(instruction[3], memData, floatData, intData)
        sum = val1+val2
        assignVal(sum, instruction[1], memData, floatData, intData)
    elif(instruction[0][0:3] == "SUB"):
        val1 = getVal(instruction[2], memData, floatData, intData)
        val2 = getVal(instruction[3], memData, floatData, intData)
        sum = val1-val2
        assignVal(sum, instruction[1], memData, floatData, intData)
    elif(instruction[0] == "MUL.D"):
        val1 = getVal(instruction[2], memData, floatData, intData)
        val2 = getVal(instruction[3], memData, floatData, intData)
        sum = val1*val2
        assignVal(sum, instruction[1], memData, floatData, intData)
    else:
        val1 = getVal(instruction[2], memData, floatData, intData)
        val2 = getVal(instruction[3], memData, floatData, intData)
        sum = val1/val2
        assignVal(sum, instruction[1], memData, floatData, intData)


def main():
    memoryData = [["(0)",45],["(1)",12],["(2)",0],["(3)",0],["(4)",10],["(5)",135],["(6)",254],["(7)",127],["(8)",18],["(9)",4],
                  ["(10)",55],["(11)",8],["(12)",2],["(13)",98],["(14)",13],["(15)",5],["(16)",233],["(17)",158],["(18)",167]]

    floatRegister = []
    intRegister = []
    instruction = []
    readFile(instruction)
    scoreBoard = []
    createBoard(instruction, scoreBoard)
    displayBoard(scoreBoard)
    createRegisters(floatRegister, intRegister)
    doInstruction(["L.D", "F2", "-34"], memoryData, floatRegister, intRegister)
    doInstruction(["L.D", "F3", "60"], memoryData, floatRegister, intRegister)
    doInstruction(["ADD.D", "F10", "F3", "F2"], memoryData, floatRegister, intRegister)
    print(floatRegister)
    
main()