#from cflat.backend import CFlatCom
from cflat.backend import Note
#from cflat.backend import NoteStream
#from cflat.backend import Configuration
#from cflat.controller import CFlatApp
#from cflat.controller import CFlatNoteParser
#from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine
import struct
'''
Created on Nov 1, 2012

@author: Arthur Weborg
The purpose of this class is to handle interrupts from
the CFlatCom class and generate Note objects to be tossed
into the NoteStream (which ultimately produces the sheet music)
'''

class CFlatNoteParser(object):
    '''
    classdocs
    '''

    def __init__(self,notes,params=[]):
        '''
        Constructor
        '''
        self.ns = notes
        self.partialNotes = []
        print "Created new Note Parser"
    def initiate(self):
        '''
        starts polling for data, should be called after the
        CFlatCom has been set.
        '''
        
    def handleNewNote(self,byteArray,timeStamp):
        '''
        processes a MIDI inspired byte array
        byte 0 - command
        byte 1 - frequency
        byte 2 - frequency
        byte 3 - frequency
        byte 4 - frequency
        byte 5 - amplitude
        byte 6 - amplitude
        byte 7 - relative timestamp ms
        byte 8 - relative timestamp ms
        byte 9 - relative timestamp ms
        byte 10 - relative timestamp ms
        byte 11 - relative timestamp ms
        byte 12 - relative timestamp ms
        byte 13 - relative timestamp ms
        byte 14 - relative timestamp ms
        '''
        if byteArray[0] == 0 :
            freq = float(byteArray[1:5])
            amp = int(byteArray[5:7])
            time = struct.unpack('f', str(bytearray(byteArray[7:])))
            n = Note.Note([freq,timeStamp,amp,0])
            self.partialNotes.append(n)
        elif byteArray[0] == 1 :
            for n in self.partialNotes :
                if n.getFrequency() == float(byteArray[1:5]) :
                    ms = timeStamp-n.getStart()
                    #TODO this needs to be implemented for grab the bpm
                    n.setDuration((ms*1000*60)/120.0)
                    self.partialNotes.remove(n)
                    self.ns.append(n)
        else :
            print "something probably went wrong! comand not recognized..."
    def handleNewDump(self):
        '''
        In the event of data dump to the laptop, this will be the algorithm used
        to create notes from the raw data. That or, this will hand the raw data
        off to a filtering class for processing.
        '''
        
    def writeNoteToStream(self,n):
        '''
        concat the note onto the NoteStream
        '''
        self.ns.writeNextNote(n)
#        print n
#        print n.getFrequency()
#        print n.getFrequency
#        print n.freq
#        print self.ns.hasNextNote
        
    def setCFlatCom(self,com):
        '''
        Sets the CFlatCom class
        '''
        