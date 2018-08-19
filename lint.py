import sys
if sys.version_info[0] == 2:
    try:
        user_input = raw_input("Please enter the file you would like to use: ")
        if not user_input:
            raise ValueError("Empty String")
    except ValueError as e:
        print(e)
if sys.version_info[0] == 3:
    try:
        user_input = input("Please enter the file you would like to use: ")
        if not user_input:
            raise ValueError("Empty String")
    except ValueError as e:
        print(e)
filePath = user_input 
chosenChar = input("Input the character you would like to check: ")
print("File name: " + filePath)
count = 0
fileData = ""
finalMessage = ""
with open(filePath, "r") as fp:
    fileData = fp.readlines()
    for i in range(len(fileData)):
        print(fileData[i])
    for i in range(len(fileData)):
        startingChar = 0
        fileData[i] = fileData[i].strip()
            while startingChar < len(fileData[i]):
                if fileData[i][startingChar] == chosenChar:
                    if fileData[i][startingChar+1] == chosenChar:
                        finalMessage += fileData[i][startingChar] 
                        startingChar += 1
                        if fileData[i][startingChar] == chosenChar:
                            continue
                    else:
                        finalMessage += fileData[i][startingChar]                        
                else:
 
                    finalMessage += fileData[i][startingChar]
                startingChar += 1 
    fileData[i] = finalMessage
with open(filePath, "w") as fp:
    for i in range(len(fileData)):
        fp.write(fileData[i])
        
