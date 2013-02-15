from cflat.backend import CFlatCom
from cflat.backend import Note
from cflat.backend import NoteStream
from cflat.backend import Configuration
#from cflat.controller import CFlatApp
from cflat.controller import CFlatNoteParser
from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine
'''
Created on Nov 1, 2012

@author: Arthur Weborg
This class is to be later merged into the front end.

It will be responsible for grabbing data from the NoteStream and
calling GUI API calls to manipulate the screen and display music.

Like the CFlatSessionController it will also act as a layer between
Front and backend.

A last note, this class will generate the temp file containing
a recording.
'''

class CFlatSheetMusicEngine(object):
    '''
    classdocs
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        print "Created new Engine"
        
    def addNote(self,Note):
        '''
        Pipes a note to the GUI
        '''
        
    def refreshDisplay(self):
        '''
        restarts the stream, pretty much starts over
        '''
        
    def initiate(self):
        '''
        start polling and handling notes from the
        NoteStream
        '''
        