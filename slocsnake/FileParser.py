import SlocObject
from SlocObject import SlocObject
from enum import Enum

class ParseMode(Enum):
    LOOSE = 1
    PHYSICAL = 2
    LOGICAL = 3

class FileParser:

    tokens = ["[","]","{","}","(",")", "\t", "\n"]

    def parse(self, objectParser, file):
        slocData = SlocObject()
        with open(file) as configReader:
            lines = (line.strip('\n') for line in configReader)
            rawData = list(lines)      
        slocData.loose = FileParser.countLoose(rawData)
        slocData.physical = FileParser.countPhysical(rawData)
        slocData.logical = FileParser.countLogical(rawData, objectParser)

        #test:
        print("***Counting File:\t[", file, "]***")
        print("***LOOSE:\t\t[", slocData.loose, "]")
        print("***Counting File:\t[", file, "]***")
        print("***PHYSICAL:\t\t[", slocData.physical, "]")
        print("***Counting File:\t[", file, "]***")
        print("***LOGICAL:\t\t[", slocData.logical, "]\n\n")

        return slocData

    @staticmethod
    def countLoose(rawData): # includes every raw line of file
        count = 0
        for line in rawData:
            count += 1
        return count

    @staticmethod
    def countPhysical(rawData): # includes everything but whitespace, brackets, braces, parens
        count = 0
        for line in rawData:
            if FileParser.countLine(line):
                count += 1
        return count

    @staticmethod
    def countLogical(rawData, objectParser): # includes everything but comments, brackets, braces, parens, whitespace
        count = 0
        blocked = None
        for line in rawData:
            if (not blocked) and (objectParser.blockFront in line): # check for block comments         
                blocked = True
                continue
            elif (blocked) and (objectParser.blockBack in line):
                blocked = False
                splitLine = line.split(objectParser.blockBack, 1) 
                if FileParser.countLine(splitLine[1]):
                    count += 1
                continue
            if blocked:
                continue
            if line.strip().startswith(objectParser.singleComment):
                continue
            if FileParser.countLine(line):
                count += 1
        return count
                
    @staticmethod
    def countLine(line):
        if len(line) == 1:
            if line in tokens:
                return False
            elif line.isspace():
                return False
        elif len(line) < 1:
            return False
        return True
