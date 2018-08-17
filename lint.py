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
try:
    chosenChar = input("Input the character you would like to check: ")

    with open(filePath) as fp:
        line = fp.readline()
        if line == "":
            print("File is empty. Terminating program.")
            sys.exit()
    count = 1
    while line:
        print("Line " + str(count) + ": " + line)
        numOfChars = line.count(chosenChar)
        if numOfChars > 0:
            while line.count(chosenChar) > 1:
                startingChar = 0
                endingChar = len(line)
        if line.find(chosenChar, startingChar, endingChar) != -1: 
             line.find(chosenChar, line.find(chosenChar)+line.count(chosenChar))
             tempString = line[:line.find(chosenChar)+line.count(chosenChar)] + line[:line.find(chosenChar)+line.count(chosenChar)+1]
        line = fp.readline()
        count += 1
