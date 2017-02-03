from ParsedObject import ParsedObject

class InitParser:

    _configPath = "../configs/config"

    def initialize(self, extension):       
        with open(self._configPath + extension) as configReader:
            lines = (line.rstrip('\n') for line in configReader)
            parsed = list(lines)

        newParsedObject = ParsedObject(parsed[0], parsed[1], parsed[2], parsed[3], parsed[4])
        return newParsedObject
