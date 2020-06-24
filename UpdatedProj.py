
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
    print(instruction)
    print(instruction[0][0])
    
    
main()
