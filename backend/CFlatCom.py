from cflat.backend import Note
#from cflat.backend import NoteStream
#from cflat.backend import Configuration
#from cflat.controller import CFlatApp
#from cflat.controller import CFlatNoteParser
#from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine
import usb.core
import usb.util
import array
import time
'''
Created on Nov 1, 2012

@author: Arthur Weborg
This class is responsible for communicating with the USB.
It will take data from communication with the chip and handle
the signals which will be grabbed via the CFlatCom.
'''

class CFlatCom(object):
    '''
    classdocs
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        print "Created CFlatCom"
        
    def establishConnection(self):
        '''
        '''
        # find our device
        #Device class is going to be 'FFh'
        print "searching for our device"
        
        self.dev = usb.core.find(idVendor=0x04D8, idProduct=0x0042)
        
        # was it found?
        if self.dev is None:
            raise ValueError('Device not found')
        else :
            print "Device Found!"
#        for cfg in self.dev:
#            print str(cfg.bConfigurationValue) + '\n'
#            for intf in cfg:
#                print '\t' + \
#                         str(intf.bInterfaceNumber) + \
#                         ',' + \
#                         str(intf.bAlternateSetting) + \
#                         '\n'
#            for ep in intf:
#                print '\t\t' + \
#                             str(ep.bEndpointAddress) + \
#                             '\n'
        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.dev.set_configuration()
        
        # get an endpoint instance
        cfg = self.dev.get_active_configuration()
        interface_number = cfg[(0,0)].bInterfaceNumber
        alternate_setting = usb.control.get_interface(self.dev,interface_number)
        intf = usb.util.find_descriptor(
            cfg, bInterfaceNumber = interface_number,
            bAlternateSetting = alternate_setting
        )
        
        ep = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT
        )
        
        ep2 = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_IN
        )
        print "Commanding LED to toggle"
        ep.write(chr(128))
        
#        time.sleep(1)
        while 1 :
            try :
                print "Polling for LED status..."
                ep.write(chr(130))
                data = ep2.read(64)
                break
            except :
                print "........Timed out........"
                pass
#        sret = ''.join([chr(x) for x in data])
        print ""
        print ""
        if data[0] == 1 :
            print "LED is on"
        else :
            print "LED is off"
#        print data
#        print data.tostring()
#        time.sleep(5)
#        print ep.write(chr(128))
#        print ep.write(chr(130))
#        print ep2.read(64)
#        time.sleep(1)
#        print ep.write(chr(128))
#        print ep.write(chr(130))
#        print ep2.read(64)
#        time.sleep(1)
#        print ep.write(chr(128))
#        print ep.write(chr(130))
#        print ep2.read(64)
#        time.sleep(1)
#        print ep.write(chr(128))
#        print ep.write(chr(130))
#        print ep2.read(64)
#        time.sleep(1)
#        print ep.write(chr(128))
#        print ep.write(chr(130))
#        print ep2.read(64)
#        msg = "\x82"
#        for req in range(255):
##            for type in range(255):
#            try :
##                    aself.dev.ctrl_transfer(bmRequestType=type, bRequest=req, data_or_wLength=msg, 0, 64)
##                    ret = self.dev.ctrl_transfer(bmRequestType=type, bRequest=req, wValue=0,wLength=0, 64)
#                self.dev.ctrl_transfer(0x81, req, 0, 0, msg)
##                ret = self.dev.ctrl_transfer(0x81,req,0,0,64)
##                    print ret
##                    sret2 = ''.join([chr(x) for x in ret])
##                print "\t" + str(req)
##                    time.sleep(1)
##                    print "\t" + ret
#            except :
##                   print "Not found at" + str(x)
#                    pass
#        help(usb.core)
    def getNextByte(self):
        '''
        returns the next byte in the queue
        '''
        
    def hasIncoming(self):
        '''
        if the queue is not emptry, return true
        '''
        
    def readData(self):
        '''
        This method polls and handles communication
        with the audio interface
        '''