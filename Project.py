def readFile(fileName, instructList):
    oneLine = []
    file = open(fileName, "r")
    for line in file:
        x = line.split()
        instructList.append(x)
    file.close()

def createBoard(instructList, scoreBoard):
    for i in range(len(instructList)):
        row = [0,0,0,0, "Issue"]
        scoreBoard.append(row)


def displayBoard(scoreBoard):
    for i in  range(len(scoreBoard)):
        print(scoreBoard[i])


def main():
    fileName = "Instruction Set.txt"
    scoreBoard = []
    instructList = []
    readFile(fileName, instructList)
    createBoard(instructList, scoreBoard)
    displayBoard(scoreBoard)

main()