fileName ="myCreatedFile.txt"
fileContent = input("Enter file data:")

fileInfo = open(fileName,"w")

fileInfo.write(fileContent)

fileInfo.close()
