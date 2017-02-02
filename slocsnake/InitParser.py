from ParsedObject import ParsedObject

class InitParser:

        _configDir = './configs/'

        def initialize(extension):
        configFile = open(_configDir + extension, r)
        
        #test driver:
        print configFile