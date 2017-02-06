import SlocObject
from SlocObject import SlocObject

class FileParser:

    tokens = ["[","]","{","}","(",")", "\t", "\n"]

    def parse(self, objectParser, file):
        slocData = SlocObject()
        with open(file) as configReader:
            lines = (line.rstrip('\n') for line in configReader)
            rawData = list(lines)      
        slocData.loose = FileParser.countLoose(rawData)
        slocData.physical = FileParser.countPhysical(rawData)

        #test:
        print("***Counting File:\t[", file, "]***")
        print("***LOOSE:\t\t[", slocData.loose, "]")
        print("***Counting File:\t[", file, "]***")
        print("***PHYSICAL:\t\t[", slocData.physical, "]\n\n")

        return slocData

    @staticmethod
    def countLoose(rawData): #includes every raw line of file
        count = 0
        for line in rawData:
            count += 1
        return count

    @staticmethod
    def countPhysical(rawData): #includes everything but whitespace, brackets, braces, parens
        count = 0
        for line in rawData:
            if len(line) == 1:
                if line in tokens:
                    continue
                elif line.isspace():
                    continue
            elif len(line) < 1:
                continue
            count += 1
        return count

    @staticmethod
    def countLogical(rawData): #includes everything but comments, brackets, braces, parens, whitespace