import sys
filePath = ""
if len(sys.argv) == 2:
    filePath = sys.argv[1]
if len(sys.argv) == 1:
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
#chosenChar = input("Input the character you would like to check: ")
print("File name: " + filePath)
fileData = ""
finalMessage = ""
totalCount = 0
originalMessage = ""
with open(filePath, "r") as fp:
    fileData = fp.readlines()
    for i in range(len(fileData)):
        startingChar = 0
        while startingChar < len(fileData[i])-1:
            if (fileData[i][startingChar] == fileData[i][startingChar+1]):
                chosenChar = fileData[i][startingChar]
                originalMessage = fileData[i]
                count = 0
                currentPosition = startingChar
                while (fileData[i][currentPosition] == chosenChar):
                    count += 1 
                    currentPosition += 1 
                    totalCount += 1
                fileData[i] = fileData[i][:startingChar+1] + fileData[i][(startingChar+count):]
                print("Original Message: " + originalMessage)
                print("file data: " + fileData[i])        
                print("Line [" + str(i) + "]: " + originalMessage + "We have found " + str(totalCount) + " match(es) on this line of the character: " + chosenChar)
                print("Your line will be changed to this: " + fileData[i])
                confirmationFlag = input("Would you like to use the following changes (y/n): ")
                confirmationFlag = confirmationFlag.lower()
                if confirmationFlag == "y":
                    print("")
                    print("Your line has been changed to: " + fileData[i]) 
                elif confirmationFlag == "n":
                    fileData[i] = originalMessage
                    print("")
                    print("Your line has remained: " + fileData[i])
                    startingChar = len(fileData[i])-1
                    i += 1
                    break 
                else:
                    pass
            totalCount = 0        
            startingChar += 1 
        
            

with open(filePath, "w") as fp:
    for i in range(len(fileData)):
        fp.write(fileData[i])
    print("We have stripped duplicating characters from " + filePath + ". We hope to see you again! :)")    
