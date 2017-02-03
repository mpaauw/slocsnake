#from FileParser import FileParser
import InitParser
from InitParser import InitParser
import ParsedObject
from ParsedObject import ParsedObject
import FileParser
from FileParser import FileParser
import os
from os import listdir
from os.path import isfile, join

class Tracker:
     
    #global tracking variables go here...


    def run(self): 
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            Tracker.parseDir(f)

    def parseDir(input):
        if(os.path.isdir(input)):
            return parseDir(input)
        filename, fileExt = os.path.splitext(input)
        init = InitParser()
        parsedObject = init.initialize(fileExt)

        parser = FileParser()
        parser.parse(parsedObject, input)



