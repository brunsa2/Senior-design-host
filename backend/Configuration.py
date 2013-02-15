#from cflat.backend import CFlatCom
#from cflat.backend import Note
#from cflat.backend import NoteStream
#from cflat.controller import CFlatApp
#from cflat.controller import CFlatNoteParser
#from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine

'''
Created on Nov 8, 2012

@author: Wesley
'''

class Configuration(object):
    '''
    classdocs
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        print "Created new Configuration"
        self.bpm = 120
        self.timeSig = 4
    def setBPM(self,bpm):
        '''
        sets the Beats Per Minute
        '''
        self.bpm = bpm
    def getBPM(self):
        '''
        returns the Beats per minute
        '''
        return self.bpm
    def getBPMeasure(self):
        '''
        this represents the numerator in the time sig.
        '''
        return self.timeSig