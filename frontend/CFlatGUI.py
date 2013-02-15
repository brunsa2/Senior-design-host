# Web Tutorial of GTK.Builder() ... http://www.overclock.net/t/342279/tutorial-using-python-glade-to-create-a-simple-gui-application/10

import sys
import threading
import subprocess
import time

try:  
    import gtk  
except:  
    print("GTK Not Availible")
    sys.exit(1)

class SheetMusicUpdater(threading.Thread) :

    # Make this class a thread object and search for new images in the folder
    # and update the image on the screen (must use gtk.Builder to grab the
    # image from the GUI)
    def __init__(self):

        self.builder = gtk.Builder()
        self.builder.add_from_file("CFlatGUI.glade")

        self.imgSheetMusic = self.builder.get_object("imgSheetMusic")
        
    def run(self):  
        
        while (1) :
            
            #print time.clock()
            self.imgSheetMusic.set_from_file("sheetmusic.png")
            #self.image.show()
            
            #self.builder.get_object("application").set_title("Hello World")
            #self.lblStatus.set_label(str(time.clock()))
            
            time.sleep(0.5)

class CFlatGUI(object) :

    def __init__(self):

        self.builder = gtk.Builder()
        self.builder.add_from_file("CFlatGUI.glade")
        self.window = self.builder.get_object("application")
        self.window.set_title("C Flat")

        # Connect the exit button to GTK's application quit handler
        if self.window:

           self.window.connect("destroy", gtk.main_quit)

        # Connect all event signals from the dictionary to the application
        self.builder.connect_signals( Handler(self.builder) )
        
        ##image_updater = SheetMusicUpdater()
        #image_updater.run()

##############################
# Start of callback handlers #
##############################
class Handler:

    def __init__(self, builder):

        self.builder = builder

        #################################
        # Create menu object References #
        #################################
        
        # Create menu File object references
        self.mnuFileNew = self.builder.get_object("mnuFileNew")
        self.mnuFileOpen = self.builder.get_object("mnuFileOpen")
        self.mnuFileSaveAs = self.builder.get_object("mnuFileSaveAs")
        self.mnuFileSave = self.builder.get_object("mnuFileSave")
        self.mnuFileQuit = self.builder.get_object("mnuFileQuit")

        # Create menu Edit object references
        self.mnuEditProperties = self.builder.get_object("mnuEditProperties")
        self.mnuEditPreferences = self.builder.get_object("mnuEditPreferences")

        # Create menu Record object references
        self.mnuRecordStart = self.builder.get_object("mnuRecordStart")
        self.mnuRecordCalibrate = self.builder.get_object("mnuRecordCalibrate")

        # Create menu Help object references
        self.mnuHelpAbout = self.builder.get_object("mnuHelpAbout")

        ###################################
        # Create dialog object References #
        ###################################

        # Create dialog Calibrate object references
        self.dlgCalibrate = self.builder.get_object("dlgCalibrate")
        self.btnCancel_Calibrate = self.builder.get_object("btnCancel_Calibrate")
        self.btnOK_Calibrate = self.builder.get_object("btnOK_Calibrate")

        # Create dialog Music Properties object references
        self.dlgMusicProperties = self.builder.get_object("dlgMusicProperties")
        self.btnCancel_Properties = self.builder.get_object("btnCancel_Properties")
        self.btnOK_Properties = self.builder.get_object("btnOK_Properties")

        # Create dialog New object references
        self.dlgNew = self.builder.get_object("dlgNew")
        self.btnCancel_New = self.builder.get_object("btnCancel_New")
        self.btnCreate_New = self.builder.get_object("btnCreate_New")

        # Create dialog Open object references
        self.dlgOpen = self.builder.get_object("dlgCOpen")
        self.btnCancel_Open = self.builder.get_object("btnCancel_Open")
        self.btnOpen_Open = self.builder.get_object("btnOpen_Open")

        # Create dialog Save / Save As object references
        self.dlgSave = self.builder.get_object("dlgSave")
        self.btnCancel_Save = self.builder.get_object("btnCancel_Save")
        self.btnSave_Save = self.builder.get_object("btnSave_Save")

        # Create dialog About object references
        self.dlgAbout = self.builder.get_object("dlgAbout")

    def on_dlgCalibrate_response(self):
        print "on_btnOK_Calibrate"
    def on_dlgCalibrate_close(self):
        print "on_btnCancel_Calibrate"
    
    
    def on_dlgMusicProperties_close(self, widget):
        print "on_btnCancel_Properties"
    def on_dlgMusicProperties_response(self, widget):
        print "on_btnOK_Properties"
    
    def on_dlgNew_close(self, widget):
        print "on_btnCancel_New"
    def on_dlgNew_response(self, widget):
        print "on_btnCreate_New"
    
    def on_dlgOpen_close(self, widget):
        print "on_btnCancel_Open"
    def on_dlgOpen_response(self, widget):
        print "on_btnOpen_Open"
    
    def on_dlgSave_close(self, widget):
        print "on_btnCancel_Save"
    def on_dlgSave_response(self, widget):
        print "on_btnSave_Save"

    def on_dlgAbout_close(self, widget):
        print "on_dlgAbout_close"
        self.dlgAbout.hide() # BUT THIS DOES NOT SHOW ABOUT BOX!!!!!

        
        
    def on_mnuFile_activate(self, widget):

        menuItem = widget.get_label()

        if (menuItem == "_New"):
            response = self.dlgNew.run()
            self.dlgNew.hide()
        if (menuItem == "_Open"):
            response = self.dlgOpen.run()
            self.dlgOpen.hide()
        if (menuItem == "_Save"):
            response = self.dlgSave.run()
            self.dlgSave.hide()
        if (menuItem == "Save _As"):
            response = self.dlgSave.run()
            self.dlgSave.hide()
        if (menuItem == "_Exit"):
            gtk.main_quit()

        if (menuItem != "_Exit"): print response
        
    def on_mnuEdit_activate(self, widget):

        menuItem = widget.get_label()

        if (menuItem == "Music Properties"):
            response = self.dlgMusicProperties.run()
            self.dlgMusicProperties.hide()
        if (menuItem == "Preferences"): print "preferences"
        print response
        
    def on_mnuRecord_activate(self, widget):

        menuItem = widget.get_label()

        if (menuItem == "_Start Recording"): print "Start Recording"
        if (menuItem == "_End Recording"): print "End Recording"
        if (menuItem == "Calibrate _Instrument"):
            response = self.dlgCalibrate.run()
            self.dlgCalibrate.hide()
            print response
            

    def on_mnuHelp_activate(self, widget):

        response = self.dlgAbout.run()
        self.dlgAbout.hide()
        print response
        
app = CFlatGUI()
app.window.show()


# app.dlgAbout.show() ## THIS UNCOMMENTED WILL SHOW ABOUT BOX!!!!
gtk.main()  # Loop that handles all GTK items such as signals


if __name__ == '__main__':

    CFlatGUI()
