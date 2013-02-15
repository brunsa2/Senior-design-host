#from cflat.backend import CFlatCom
from cflat.backend import Note
#from cflat.backend import Configuration
#from cflat.controller import CFlatApp
#from cflat.controller import CFlatNoteParser
#from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine
'''
Created on Nov 1, 2012

@author: Arthur Weborg

This will be the main datastructer of the software system
It will be a queue of sorts with severeal status booleans
and methods.

It will be thread safe.

Notes will be added as they are parsed and iterated through
by the SheetMusicEngine.

The CFlatNoteParser will inject/append notes to the queue.
'''

class NoteStream(object):
    '''
    classdocs
    '''
#    data = []
#    curIndex = 0

    def __init__(self,params):
        '''
        Constructor
        '''
        self.data = []
        self.curIndex = 0
        print "Created new NoteStream"
        
    def readNextNote(self):
        '''
        returns the next note relative to the index
        '''
        self.curIndex = self.curIndex + 1
        return self.data[(self.curIndex-1)]
        
    def writeNextNote(self,n):
        '''
        Concats the specified note to the Stream
        '''
        self.data.append(n)
        print "Appended new note to NoteStream"
        
    def hasNextNote(self):
        '''
        returns true of index is less than the number of notes.
        if there are no new notes to send out
        '''
        if len(self.data) > self.curIndex :
            return True
        else :
            return False
        
    def initiate(self):
        '''
        
        '''
        
    def clearStream(self):
        '''
        removes all data
        '''
        self.data = []
        self.curIndex = 0;
        
    def reset(self):
        '''
        resets the index to 0 so reading of notes can start over
        '''
        self.curIndex = 0
        
    def toLilyPond(self):
        '''
        returns the notestream in Lilypond notation
        '''
        index = 0;
        lil = ""
        while index < len(self.data) : 
            #if there is potential for a triplet then see if there are two more notes
            if self.data[index].getDurationSymbol() == "12" :
                if len(self.data) - (index + 1) > 2 :
                    if self.data[index+1].getDurationSymbol() == "12" and self.data[index+2].getDurationSymbol() == "12" :
                        a = self.data[index].getNoteSymbol()
                        b = self.data[index+1].getNoteSymbol()
                        c = self.data[index+2].getNoteSymbol()
                        # Check to see if the duration of the total triplet was within acceptable
                        # range, the duration should have been that of a half note!
                        totDur = self.data[index].getDuration() + self.data[index+1].getDuration() + self.data[index+2].getDuration()
                        n = Note.Note([0,0,0,totDur])
                        err = n.getDurationPercentDifference()
                        colr = ""
                        #If positive and above 5%, then it was slower than acceptable
                        if err > 0.05 :
                            colr = "\\override NoteHead #'color = #blue"
                        #If negative and below 5%, then it was faster than acceptable
                        elif err < -0.05 :
                            colr = "\\override NoteHead #'color = #red"
                        #We don't know the current color, but we do know that the note
                        #was in an acceptable range, make the color black again
                        else :
                            colr = "\\revert NoteHead #'color"
                        #Finaly, add the triplet to the lilypond =]
                        lil = lil + " " + colr +  " \times 2/3 {" + a + "4 " + b + "4 " + c + "4 }"
                else :
                    #we called the note a triplet, but unfortunately it needs to be
                    #called an eigth or a dotted eigth note!
                    
                    #if positive, it was slower than the inbetween and should be a dotted eigth
                    if self.data[index].getDurationPercentDifference() > 0 :
                        lil = lil + " \\override NoteHead #'color = #blue " + self.data[index].getNoteSymbol() + "8. "
                    else :
                        lil = lil + " \\override NoteHead #'color = #red " + self.data[index].getNoteSymbol() + "8 "
            #if there is potential for a triplet then see if there are two more notes
            elif self.data[index].getDurationSymbol() == "6" : 
                if len(self.data) - (index + 1) > 2 :
                    if self.data[index+1].getDurationSymbol() == "6" and self.data[index+2].getDurationSymbol() == "6" :
                        a = self.data[index].getNoteSymbol()
                        b = self.data[index].getNoteSymbol()
                        c = self.data[index].getNoteSymbol()
                        # Check to see if the duration of the total triplet was within acceptable
                        # range, the duration should have been that of a quarter note!
                        totDur = self.data[index].getDuration() + self.data[index+1].getDuration() + self.data[index+2].getDuration()
                        n = Note.Note([0,0,0,totDur])
                        err = n.getDurationPercentDifference()
                        colr = ""
                        #If positive and above 5%, then it was slower than acceptable
                        if err > 0.05 :
                            colr = "\\override NoteHead #'color = #blue"
                        #If negative and below 5%, then it was faster than acceptable
                        elif err < -0.05 :
                            colr = "\\override NoteHead #'color = #red"
                        #We don't know the current color, but we do know that the note
                        #was in an acceptable range, make the color black again
                        else :
                            colr = "\\revert NoteHead #'color"
                        #Finaly, add the triplet to the lilypond =]
                        lil + " " + colr +  " \times 2/3 {" + a + "8 " + b + "8 " + c + "8 }"
                else :
                    #we called the note a triplet, but unfortunately it needs to be
                    #called a sixteenth or a dotted sixteenth note!
                    
                    #because the note literally was right inbetween  the two:
                    #if positive, it was slower than the inbetween and should be a dotted sixteenth
                    if self.data[index].getDurationPercentDifference() > 0 :
                        lil = lil + " \\override NoteHead #'color = #blue " + self.data[index].getNoteSymbol() + "16. "
                    #otherwise it was fast and should be a sixteenth
                    else :
                        lil = lil + " \\override NoteHead #'color = #red " + self.data[index].getNoteSymbol() + "16 " 
            #If it is not a triplet, then handle as a normal note =]
            else :
                lil = lil + self.data[index].toLilyPond()
            lil = lil + "\n"
            index = index + 1
        return lil
    def toXML(self):
        '''
        returns the notestream in xml format
        '''
        xml = "<note_list>\n"
        index = 0;
        while index < len(self.data) : 
            xml += "\t<note start=\"" + str(self.data[index].getStart()) + "\">\n"
            xml += "\t\t<duration>" + str(self.data[index].getDuration()) + "</duration>\n"
            xml += "\t\t<frequency>" + str(self.data[index].getFrequency()) + "</frequency>\n"
            xml += "\t\t<volume>" + str(self.data[index].getVolume()) + "</volume>\n"
            xml += "\t</note>\n"
            index += 1
        xml = xml + "</note_list>"
        return xml
    def toScientificPitch(self):
        '''
        returns the notestream in scientific pitch notation
        '''
        return "Scientific pitch"