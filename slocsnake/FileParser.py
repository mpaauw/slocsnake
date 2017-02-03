import SlocObject
from SlocObject import SlocObject

class FileParser:

    def parse(self, objectParser, file):

        slocData = SlocObject()

        with open(file) as configReader:
            lines = (line.rstrip('\n') for line in configReader)
            rawData = list(lines)
        
        slocData.loose = FileParser.countLoose(rawData)

        # #test:
        # iter = 1
        # print("*****START OF FILE: [", file, "]*****")
        # for item in rawData:
        #     print(iter, ". ", item)
        #     iter += 1
        # print("*****END OF FILE: [", file, "]*****")

        return slocData

    @staticmethod
    def countLoose(rawData):
        count = 0
        for line in rawData:
            count += 1
        return count

        