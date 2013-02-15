from cflat.backend import CFlatCom
from cflat.backend import Note
from cflat.backend import NoteStream
from cflat.backend import Configuration
#from cflat.controller import CFlatApp
from cflat.controller import CFlatNoteParser
from cflat.controller import CFlatSessionController
from cflat.controller import CFlatSheetMusicEngine
from cflat.frontend import CFlatLilypond
import time
import thread
'''
Created on Nov 1, 2012

@author: Arthur Weborg
This class will have all the execution and initializing of the
entire system. It will be the module called via shortcut or
command line to start-up the system.

The SessionController must be the first class initialized,
followed by the CFlatCom and then CFlatNoteParser.

All other classes may be initialized in any order.
'''
def handleNotes(self,np):
    print "added first"
    n = Note.Note([16.35,0,.75,.5])
    np.writeNoteToStream(n)
    time.sleep(2)
    print "added second"
    n2 = Note.Note([17.32,0,.75,.5])
    np.writeNoteToStream(n2)
    time.sleep(1.75)
    print "added third"
    n3 = Note.Note([18.35,0,.75,.375])
    np.writeNoteToStream(n3)
    time.sleep(1.75)
    print "added fourth"
    n4 = Note.Note([19.45,0,.75,.375])
    np.writeNoteToStream(n4)
    time.sleep(3)
    print "added fifth"
    n5 = Note.Note([20.60,0,.75,.75])
    np.writeNoteToStream(n5)
    time.sleep(3.25)
    print "added sixth"
    n6 = Note.Note([21.83,0,.75,.875])
    np.writeNoteToStream(n6)
    time.sleep(3.5)
    print "added seventh"
    n7 = Note.Note([23.12,0,.75,1])
    np.writeNoteToStream(n7)
    time.sleep(3.75)
    print "added eigth"
    n8 = Note.Note([24.50,0,.75,1.125])
    np.writeNoteToStream(n8)
    time.sleep(4)
    print "added nineth"
    n9 = Note.Note([25.96,0,.75,1.25])
    np.writeNoteToStream(n9)
    con.saveFile(con.LILY_POND, "lily")
    con.saveFile(con.XML,"xm")
    con.saveFile(con.SCIENTIFIC_PITCH,"science")
    
if __name__ == '__main__':
    globals = []
    con = CFlatSessionController.CFlatSessionController(globals)
    usb = CFlatCom.CFlatCom([con])
#    usb.establishConnection()
    config = Configuration.Configuration([con])
    ns = NoteStream.NoteStream(globals)
    np = CFlatNoteParser.CFlatNoteParser(ns)
    np.setCFlatCom(usb)
    engine = CFlatSheetMusicEngine.CFlatSheetMusicEngine([con])
    con = CFlatSessionController.CFlatSessionController([ns,config,engine,np,"GUI"])
    globals.append(con)
    globals.append(usb)
    globals.append(config)
    globals.append(ns)
    globals.append(np)
    globals.append(engine)
#    handleNotes(np)
    try:
        thread.start_new_thread( handleNotes, ("Thread-1", np) )
    except:
        print "Error: unable to start thread"
#        time.sleep(2)
    # Create new threads
    app = CFlatLilypond.CFlatLilypond(ns) #stream)
#    
#    # Loop through streaming the notes
    app.retrieveNotes()
#    print ns.hasNextNote
#    while ns.hasNextNote() :
#        note = ns.readNextNote()
##        print note
#        print note.toLilyPond()
    time.sleep(60);