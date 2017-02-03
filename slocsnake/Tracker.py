from InitParser import InitParser
from ParsedObject import ParsedObject
from FileParser import FileParser
from SlocObject import SlocObject
import os
from os import listdir
from os.path import isfile, join

class Tracker:
     
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
        print("*******SLOC TOTALS*******")
        print("loose:\t\t[", Tracker._slocTotals.loose, "]")
        print("physical:\t[", Tracker._slocTotals.physical, "]")
        print("logical:\t[", Tracker._slocTotals.logical, "]")
