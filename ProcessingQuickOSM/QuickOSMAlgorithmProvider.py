# -*- coding: utf-8 -*-

'''
Created on 10 juin 2014

@author: etienne
'''

from processing.core.AlgorithmProvider import AlgorithmProvider
#from processing.core.ProcessingConfig import Setting, ProcessingConfig
from OverpassQueryGeoAlgorithm import OverpassQueryGeoAlgorithm
from XapiQueryGeoAlgorithm import XapiQueryGeoAlgorithm
from NominatimQueryGeoAlgorithm import NominatimQueryGeoAlgorithm
from OsmParserGeoAlgorithm import OsmParserGeoAlgorithm
from FirstRelationIdParserGeoAlgorithm import FirstRelationIdParserGeoAlgorithm
from ReadIniFileGeoAlgorithm import ReadIniFileGeoAlgorithm
from ReadIniFilePathGeoAlgorithm import ReadIniFilePathGeoAlgorithm
from ListIniFilesGeoAlgorithm import ListIniFilesGeoAlgorithm
from PyQt4.QtGui import QIcon
from os.path import dirname,abspath


class QuickOSMAlgorithmProvider(AlgorithmProvider):
    '''
    QuickOSM provide some GeoAlgorithms
    '''

    def __init__(self):
        AlgorithmProvider.__init__(self)

        self.activate = True

        # Load algorithms
        self.alglist = [OverpassQueryGeoAlgorithm(),
                        NominatimQueryGeoAlgorithm(),
                        OsmParserGeoAlgorithm(),
                        XapiQueryGeoAlgorithm(),
                        FirstRelationIdParserGeoAlgorithm(),
                        ReadIniFileGeoAlgorithm(),
                        ReadIniFilePathGeoAlgorithm(),
                        ListIniFilesGeoAlgorithm()
                        ]
        
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)

    def unload(self):
        AlgorithmProvider.unload(self)

    def getName(self):
        return 'QuickOSM'

    def getDescription(self):
        return 'QuickOSM'

    def getIcon(self):
        return QIcon(dirname(dirname(abspath(__file__)))+"/icon.png")
    
    def _loadAlgorithms(self):
        self.algs = self.alglist
