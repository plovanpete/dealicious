# This file will have functions for:
#	Access a file to read
#	Access a file to write
#	Close a file
#	Adding rows representing a restaurant and its relevant data to the file
#	Removing rows representing restaurants
#	----
# 
import csv

inputFile = "mapData.csv"

class MapFile:
	def __init__(self, fileName):
		self.fileName = fileName

	def readFile():
		file = open(fileName, "r")
		

	def writeFile():
		file = open(fileName, "w")

	def closeFile():
		f.close()

	def addData():
		f.writeFile()
		
		closeFile()

	def removeData():
		f.writeFile()
		
		closeFile()

	def getFileName():
		return fileName

def main():
	file = MapFile(inputFile)

	print(file.getFileName())
	print("HELLO WORLD")

	
