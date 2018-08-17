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
with open(filePath, "r+") as fp:
    line = fp.readline()
    if line == "":
        print("File is empty. Terminating program.")
        sys.exit(0)
    count = 1
    while line:
        print("Line " + str(count) + ": " + line)
        numOfChars = line.count(chosenChar)
        print("This line has " + str(numOfChars) + "matches!")
        if numOfChars > 1:
            startingChar = 0
            endingChar = len(line)
            if line.find(chosenChar, startingChar, endingChar) != -1: 
                tempString = line[:(line.find(chosenChar) + 1)] 
                print("TempString: " + tempString)
                fp.write(tempString)
        line = fp.readline()
        count += 1
