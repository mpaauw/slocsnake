#from FileParser import FileParser
import InitParser
from InitParser import InitParser
import ParsedObject
from ParsedObject import ParsedObject
import FileParser
from FileParser import FileParser
import SlocObject
from SlocObject import SlocObject
import os
from os import listdir
from os.path import isfile, join

class Tracker:
     
    #global tracking variables go here...
    #blockComment = {'front': '', 'back': ''}  

    _slocTotals = SlocObject()

    def run(self): 
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            Tracker.parseDir(f)
        Tracker.logAggregates()

    def parseDir(input):
        if(os.path.isdir(input)):
            return parseDir(input)
        filename, fileExt = os.path.splitext(input)
        init = InitParser()
        parsedObject = init.initialize(fileExt)

        parser = FileParser()
        newSloc = SlocObject()
        newSloc = parser.parse(parsedObject, input)

        Tracker.computeAggregates(newSloc)

    @staticmethod
    def computeAggregates(sloc):
        Tracker._slocTotals.loose += sloc.loose
        Tracker._slocTotals.physical += sloc.physical
        Tracker._slocTotals.logical += sloc.logical

    @staticmethod
    def logAggregates():
        # console / log file functionality regarding sloc aggregates goes here
        print("*******SLOC TOTALS*******")
        print("loose:[", Tracker._slocTotals.loose, "]")
        print("physical:[", Tracker._slocTotals.physical, "]")
        print("logical:[", Tracker._slocTotals.logical, "]")



