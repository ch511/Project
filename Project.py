def readFile(fileName, instructList):
    oneLine = []
    file = open(fileName, "r")
    for line in file:
        x = line.split()
        instructList.append(x)
    file.close()


def main():
    fileName = "Instruction Set.txt"
    instructList = []
    readFile(fileName, instructList)
    print(instructList)

main()