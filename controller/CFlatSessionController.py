from cflat.backend import CFlatCom
from cflat.backend import Note
from cflat.backend import NoteStream
from cflat.backend import Configuration
#from cflat.controller import CFlatApp
from cflat.controller import CFlatNoteParser
#from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine
'''
Created on Nov 1, 2012

@author: Arthur Weborg
This class will maintain all data relevant to a recording.
Specifically it will act as a layer between the GUI and the backend.
It will save recordings and load previous recordings and modify
and manipulate both the front and and back end services/data
'''
class CFlatSessionController(object):
    '''
    classdocs
    '''
#    stream = NoteStream.NoteStream([])
#    config = ""
#    engine = ""
#    parser = ""
#    test = "TESTING"
    LILY_POND = 0
    XML = 1
    SCIENTIFIC_PITCH = 2

    def __init__(self,params):
        '''
        Constructor
        '''
        if len(params) == 5 :
            self.stream = params[0]
            self.config = params[1]
            self.engine = params[2]
            self.parser = params[3]
#        self.gui = CFlatGUI
#        self.app = params[5]
            print "created CFlatSessionController"
        else :
            print "Temporary Controller Created"
        
        
    def saveFile(self,format,filename):
        '''
        save the file as a given format(scientific pitch notation, xml,
        JSON,...,TBD)with the filename passed through
        '''        
        if format == self.LILY_POND :
            #do stuff
            f = open(filename + ".ly", "w")
            f.write(self.stream.toLilyPond())
            f.close()
        elif format == self.XML :
            #do stuff
            f = open(filename + ".xml", "w")
            f.write(self.stream.toXML())
            f.close()
        elif format == self.SCIENTIFIC_PITCH :
            #do stuff 
            f = open(filename + ".spn", "w")
            f.write(self.stream.toScientificPitch())
            f.close()
        else :
            #do stuff
            print "Did not save file"
        
    def loadGUI(self):
        '''
        Starts/initializes the GUI, loads it with data
        '''
        
    def modifyNote(self,n,n2):
        '''
        replace the original note with the modified
        '''
        
    def playback(self,measure):
        '''
        start audio playback at a given measure
        '''
        
    def updateMusicDisplay(self,json):
        '''
        IF a file was just loaded, send the JSON string
        of notes
        '''
        
    def updateTracker(self):
        '''
        move the tracker bar, increment the counter
        '''
        
    def startAudioPlayback(self,int):
        '''
        Start audio playback at a given measure
        '''
        
    def loadFile(self,String):
        '''
        Load the notes found from a previous recording
        '''
        
    def changeConfiguration(self,name,value):
        '''
        Change a given configuration(name) to
        the new value
        '''
        
    def clearDisplay(self):
        '''
        remove all the notes from the GUI
        '''
        
    