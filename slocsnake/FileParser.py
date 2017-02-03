class FileParser:

    def parse(self, objectParser, file):
        with open(file) as configReader:
            lines = (line.rstrip('\n') for line in configReader)
            rawData = list(lines)
        
        #test:
        iter = 1
        print("*****START OF FILE: [", file, "]*****")
        for item in rawData:
            print(iter, ". ", item)
            iter += 1
        print("*****END OF FILE: [", file, "]*****")