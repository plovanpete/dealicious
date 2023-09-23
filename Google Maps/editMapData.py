# This file will have functions for:
#	Access a file to read
#	Access a file to write
#	Close a file
#	Adding rows representing a restaurant and its relevant data to the file
#	Removing rows representing restaurants
#	----
# 
import csv

inputFile = 'mapData.csv'

def printFile(file):
    with open(file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            for value in row:
                print(value)
	
def readFile(file):
    f = open(file, 'r')				

def writeFile(file):
    f = open(file, 'w')

def closeFile(file):
    file.close()

def addData(fileName):
    file.writeFile()
		
    closeFile()

def removeData():
    f.writeFile()
		
    closeFile()

def getFileName(fileName):
    return fileName

def main():

    printFile(inputFile)
    print("Main has run")


if __name__ == "__main__":
    main()
