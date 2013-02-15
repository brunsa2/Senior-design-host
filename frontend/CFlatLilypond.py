#from cflat.backend import NoteStream
#import backend.NoteStream as NoteStream
##from cflat.backend import CFlatCom
from cflat.backend import Note
from cflat.backend import NoteStream
from cflat.backend import Configuration
#from cflat.controller import CFlatApp
from cflat.controller import CFlatNoteParser
##from cflat.controller import CFlatSessionController
##from cflat.controller import CFlatSheetMusicEngine
#from SeniorDesign.cflat.frontend import CFlatLilypond

from cflat.controller import CFlatApp

import time
import thread

'''
Created on Dec 18, 2012

@author: rucinskic
'''

'''
Look here for example code...

http://www.tutorialspoint.com/python/python_multithreading.htm

'''

import threading
import subprocess

exitFlag = 0

'''

This class will allow the seperate creation of PNGs of the sheet music that will
be used within the GUI application.
'''
class threadCreatePNG(threading.Thread):
  
    '''
    Inner-class constructor
    '''
    def __init__(self, parentProcess, lilypondString, counter):
    
        print("threadCreatePNG Constructor")
        #self.note = lilypondNote
        self.lilypondString = lilypondString + "\n" + "}"
        self.parent = parentProcess
        self.imageCounter = counter
    
    '''
    Creates temp files that store music in LilyPond format and creates image files from them
    '''
    def createLilypondImage(self, lilypondString):
        
        try:
    
            # Write the Lilypond String to a file
            f = open("lilypond", "w")
            f.write(lilypondString)
            f.close()
            
        except:
    
            print "Failed to open / write to file"
            
        try: 
            
            # Use the lilypond command to create a PNG of the music
            p = subprocess.Popen("lilypond -fpng -o sheetmusic lilypond", shell=True)   # Sheetmusic is the filename of output...lilypond is input
            p.wait()
            
            # Retrieve the picture file to display or something for now...
            # it will be placed within the frontend package
    
        except:
    
            print "failed to call OS command to Lilypond"
    
    '''
    Run method of the threadCreatePNG class
    '''   
    def run(self):
        
        print "Creating PNG " + str(self.imageCounter) # str(CFlatLilypond.getCounter(self.parent))
        
        # Call method that will look over the priority Queue to get notes from
        self.createLilypondImage(self.lilypondString)
            
class CFlatLilypond(object) :
    
    '''
    Inner-class constructor
    '''
    def __init__(self, noteStream): #noteStream):
    
        print("CFlatLilypond constructor")
        self.lilypondString = "\\version \"2.10.33\"\n\n"
        self.noteStream = noteStream
        self.note = None 
        self.counter = 0   
    
    def retrieveNotes(self):
    
        print("retrieveNotes")
        #print("Note Retrieval Started")
    
        # set up the lilypond string so notes can just be added
        self.lilypondString += "\\relative c'' {" + "\n"
    
        # Get exitFlag update from the GUI...loop forever until value changed
        while not exitFlag:
    
            # Check if a note is available
            if (self.noteStream.hasNextNote()) :
        
                # Get the next note and get the LilyPond format from it
                self.note = self.noteStream.readNextNote();
                self.lilypondString += self.note.toLilyPond();
                
                # Increment counter
                self.counter += 1
                
                threadCreateImage = threadCreatePNG(self, self.lilypondString, self.counter)
                threadCreateImage.run()
                
                time.sleep(0.25)
           
        # Close off the lilypond string so the image file can be created     
        self.lilypondString += "\n" + "}"
      
'''
Main method. Connects all modules together and runs the modules to scan for and
generate the image files of the music played
'''      
if __name__ == '__main__':
    
    
    globals = []
    #con = CFlatSessionController.CFlatSessionController(globals)
    #usb = CFlatCom.CFlatCom([con])
    #config = Configuration.Configuration([con])
    ns = NoteStream.NoteStream(globals)
    np = CFlatNoteParser.CFlatNoteParser(ns)
    #np.setCFlatCom(usb)
    #engine = CFlatSheetMusicEngine.CFlatSheetMusicEngine([con])
    #con = CFlatSessionController.CFlatSessionController([ns,config,engine,np,"GUI"])
    #globals.append(con)
    #globals.append(usb)
    #globals.append(config)
    globals.append(ns)
    globals.append(np)
    #globals.append(engine)
    thread.start_new_thread( CFlatApp.handleNotes, ("Thread-1", np) )
    thread.start_new_thread( CFlatApp.handleNotes, ("Thread-1", np) )
    thread.start_new_thread( CFlatApp.handleNotes, ("Thread-1", np) )
    
    print("Start")
    
    # Create a fake NoteStream object
    #stream = NoteStream();
    
    # Create new threads
    app = CFlatLilypond(ns) #stream)
    
    # Loop through streaming the notes
    app.retrieveNotes()
    