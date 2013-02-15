#from cflat.backend import CFlatCom
#from cflat.backend import NoteStream
#from cflat.backend import Configuration
#from cflat.controller import CFlatApp
#from cflat.controller import CFlatNoteParser
#from cflat.controller import CFlatSessionController
#from cflat.controller import CFlatSheetMusicEngine
'''
Created on Nov 1, 2012

@author: Wesley
'''

class Note(object):
    '''
    classdocs
    '''
    hello = "world"
    #Symbols        C        C#        D    D#        E        F    F#        G        G#   A        A#        B
    #Symbols        C        Des       D    Ees       E        F    Ges       G        Aes  A        Bes       B
    #Symbols        C        Cis       D    Dis       E        F    Fis       G        Gis  A        Ais       B
    frequencies = [16.35,   17.32,  18.35,  19.45,  20.60,  21.83,  23.12,  24.50,  25.96,  27.50,  29.14,  30.87,  #concert 0
                   32.70,   34.65,	36.71,  38.89,	41.20,	43.65,	46.25,	49.00,	51.91,	55.00,	58.27,	61.74,	#concert 1
                   65.41,	69.30,	73.42,	77.78,	82.41,	87.31,	92.50,	98.00,	103.81,	110.00,	116.54,	123.47,	#concert 2
                   130.81,	138.59,	146.83,	155.56,	164.81,	174.61,	185.00,	196.00,	207.65,	220.00,	233.08,	246.94,	#concert 3
                   261.63,	277.18,	293.66,	311.13,	329.63,	349.23,	369.99,	392.00,	415.30,	440.00,	466.16,	493.88,	#concert 4
                   523.25,	554.37,	587.33,	622.25,	659.26,	698.46,	739.99,	783.99,	830.61,	880.00,	932.33,	987.77,	#concert 5
                   1046.50,	1108.73,	1174.66,	1244.51,	1318.51,	1396.91,	1479.98,	1567.98,	1661.22,	1760.00,	1864.66,	1975.53,	#concert 6
                   2093.00,	2217.46,	2349.32,	2489.02,	2637.02,	2793.83,	2959.96,	3135.96,	3322.44,	3520.00,	3729.31,	3951.07,	#concert 7
                   4186.01,	4434.92,	4698.64,	4978.03]  #concert 8

    def __init__(self,params):
        '''
        Constructor
        '''
        self.freq = params[0]
        self.start = params[1]
        self.volume = params[2]
        self.duration = params[3]
        print "Created new Note"
       
    def getOctive(self):
        '''
        returns the concert octave for the note
        
        returns -1 if a rest
        '''
        if self.freq <= 1.0 :
            return -1 
        elif self.freq <= (30.87+32.70)/2 :
            return 0
        elif self.freq <= (61.74+65.41)/2 :
            return 1
        elif self.freq <= (123.47+130.81)/2 :
            return 2
        elif self.freq <= (246.94+261.63)/2 :
            return 3
        elif self.freq <= (493.88+523.25)/2 :
            return 4
        elif self.freq <= (987.77+1046.50)/2 :
            return 5
        elif self.freq <= (1975.53+2093.00)/2 :
            return 6
        elif self.freq <= (2951.07+4186.01)/2 :
            return 7
        else :
            return 8
    def getSymbol(self):
        '''
        this calculates based on the frequency, the note symbol
        such as C,F,A,G, ect...
        
        returns C,C#,D,D#,E,F,G,G#,A,A#,B if an actual note
        returns R or "Very Odd notes!!!" if a rest or very high pitch sound
        '''
        #Calculate
            #    symbol    freq
        if self.freq <= 1.0 :
            return "r"
        elif self.freq <= (16.35+17.32)/2 :
            return "c" #    C0        16.35
        elif self.freq <= (17.32+18.35)/2 :
            return "cis"    #C#0/Db0   17.32  
        elif self.freq <= (18.35+19.45)/2 :
            return "d" #D0        18.35
        elif self.freq <= (19.45+20.60)/2 :
            return "dis"   #D#0/Eb0   19.45 
        elif self.freq <= (20.60+21.83)/2 :
            return "e"   #E0        20.60 
        elif self.freq <= (21.83+23.12)/2 :
            return "f"   #F0        #21.83
        elif self.freq <= (23.12+24.50)/2 :
            return "fis"   #F#0/Gb0   #23.12
        elif self.freq <= (24.50+25.96)/2 :
            return "g"   #G0     24.50
        elif self.freq <= (25.96+27.50)/2 :
            return "gis"   #G#0/Ab0     25.96
        elif self.freq <= (27.50+29.14)/2 :
            return "a"   #A0     27.50
        elif self.freq <= (29.14+30.87)/2 :
            return "ais"   #A#0/Bb0     29.14
        elif self.freq <= (30.87+32.70)/2 :
            return "b"   #B0     30.87
        elif self.freq <= (32.70+34.65)/2 :
            return "c"   #C1     32.70
        elif self.freq <= (34.65+36.71)/2 :
            return "cis"	#C#1/Db1     34.65
        elif self.freq <= (36.71+38.89)/2 :
            return "d"	#D1     36.71
        elif self.freq <= (38.89+41.20)/2 :
            return "dis"	#D#1/Eb1     38.89
    	elif self.freq <= (41.20+43.65)/2 :
            return "e"	#E1     41.20
    	elif self.freq <= (43.65+46.25)/2 :
            return "f"	#F1     43.65
    	elif self.freq <= (46.25+49.00)/2 :
            return "fis"	#F#1/Gb1     46.25
    	elif self.freq <= (49.00+51.91)/2 :
            return "g"	#G1     49.00
    	elif self.freq <= (51.91+55.00)/2 :
            return "gis"	#G#1/Ab1     51.91
    	elif self.freq <= (55.00+58.27)/2 :
            return "a"	#A1     55.00
    	elif self.freq <= (58.27+61.74)/2 :
            return "ais"	#A#1/Bb1     58.27
    	elif self.freq <= (61.74+65.41)/2 :
            return "b"	#B1     61.74
    	elif self.freq <= (65.41+69.30)/2 :
            return "c"	#C2     65.41
    	elif self.freq <= (69.30+73.42)/2 :
            return "cis"	#C#2/Db2     69.30
    	elif self.freq <= (73.42+77.78)/2 :
            return "d"	#D2     73.42
    	elif self.freq <= (77.78+82.41)/2 :
            return "dis"	#D#2/Eb2     77.78
    	elif self.freq <= (82.41+87.31)/2 :
            return "e"	#E2     82.41
    	elif self.freq <= (87.31+92.50)/2 :
            return "f"	#F2     87.31
    	elif self.freq <= (92.50+98.00)/2 :
            return "fis"	#F#2/Gb2     92.50
    	elif self.freq <= (98.00+103.81)/2 :
            return "g"	#G2     98.00
    	elif self.freq <= (103.83+110.00)/2 :
            return "gis"	#G#2/Ab2     103.83
    	elif self.freq <= (110.00+116.54)/2 :
            return "a"	#A2     110.00
    	elif self.freq <= (116.54+123.47)/2 :
            return "ais"	#A#2/Bb2     116.54
    	elif self.freq <= (123.47+130.81)/2 :
            return "b"	#B2     123.47
    	elif self.freq <= (130.81+138.59)/2 :
            return "c"	#C3     130.81
    	elif self.freq <= (138.59+146.83)/2 :
            return "cis"	#C#3/Db3     138.59
    	elif self.freq <= (146.83+155.56)/2 :
            return "d"	#D3     146.83
    	elif self.freq <= (155.56+164.81)/2 :
            return "dis"	#D#3/Eb3     155.56
    	elif self.freq <= (164.81+174.61)/2 :
            return "e"	#E3     164.81
    	elif self.freq <= (174.61+185.00)/2 :
            return "f"	#F3     174.61
    	elif self.freq <= (185.00+196.00)/2 :
            return "fis"	#F#3/Gb3     185.00
    	elif self.freq <= (196.00+207.65)/2 :
            return "g3"	#G3     196.00
    	elif self.freq <= (207.65+220.00)/2 :
            return "gis"	#G#3/Ab3     207.65
    	elif self.freq <= (220.00+233.08)/2 :
            return "a"	#A3     220.00
    	elif self.freq <= (233.08+246.94)/2 :
            return "is"	#A#3/Bb3     233.08
    	elif self.freq <= (246.94+261.63)/2 :
            return "b"	#B3     246.94
    	elif self.freq <= (261.63+277.18)/2 :
            return "c"	#C4     261.63
    	elif self.freq <= (277.18+293.66)/2 :
            return "cis"	#C#4/Db4     277.18
    	elif self.freq <= (293.66+311.13)/2 :
            return "d"	#D4     293.66
    	elif self.freq <= (311.13+329.63)/2 :
            return "dis"	#D#4/Eb4     311.13
    	elif self.freq <= (329.63+349.23)/2 :
            return "e"	#E4     329.63
    	elif self.freq <= (349.23+369.99)/2 :
            return "f"	#F4     349.23
    	elif self.freq <= (369.99+392.00)/2 :
            return "fis"	#F#4/Gb4     369.99
    	elif self.freq <= (392.00+415.30)/2 :
            return "g"	#G4     392.00
    	elif self.freq <= (415.30+440.00)/2 :
            return "gis"	#G#4/Ab4     415.30
    	elif self.freq <= (440.00+466.16)/2 :
            return "a"	#A4     440.00
    	elif self.freq <= (466.16+493.88)/2 :
            return "ais"	#A#4/Bb4     466.16
    	elif self.freq <= (493.88+523.25)/2 :
            return "b"	#B4     493.88
    	elif self.freq <= (523.25+554.37)/2 :
            return "c"	#C5     523.25
    	elif self.freq <= (554.37+587.33)/2 :
            return "cis"	#C#5/Db5     554.37
    	elif self.freq <= (587.33+622.25)/2 :
            return "d"	#D5     587.33
    	elif self.freq <= (622.25+659.26)/2 :
            return "dis"	#D#5/Eb5    622.25
    	elif self.freq <= (659.26+698.46)/2 :
            return "e"	#E5     659.26
    	elif self.freq <= (698.46+739.99)/2 :
            return "f"	#F5     698.46
    	elif self.freq <= (739.99+783.99)/2 :
            return "fis"	#F#5/Gb5     739.99
    	elif self.freq <= (783.99+830.61)/2 :
            return "g5"	#G5     783.99
    	elif self.freq <= (830.61+880.00)/2 :
            return "gis"	#G#5/Ab5     830.61
    	elif self.freq <= (880.00+932.33)/2 :
            return "a"	#A5     880.00
    	elif self.freq <= (932.33+987.77)/2 :
            return "ais"	#A#5/Bb5     932.33
    	elif self.freq <= (987.77+1046.50)/2 :
            return "b"	#B5     987.77
    	elif self.freq <= (1046.50+1108.73)/2 :
            return "c"	#C6     1046.50
    	elif self.freq <= (1108.73+1174.66)/2 :
            return "cis"	#C#6/Db6     1108.73
    	elif self.freq <= (1174.66+1244.51)/2 :
            return "d"	#D6     1174.66
    	elif self.freq <= (1244.51+1318.51)/2 :
            return "dis"	#D#6/Eb6     1244.51
    	elif self.freq <= (1318.51+1396.91)/2 :
            return "e"	#E6     1318.51
    	elif self.freq <= (1396.91+1479.98)/2 :
            return "f"	#F6     1396.91
    	elif self.freq <= (1479.98+1567.98)/2 :
            return "fis"	#F#6/Gb6     1479.98
    	elif self.freq <= (1567.98+1661.22)/2 :
            return "g"	#G6     1567.98
    	elif self.freq <= (1661.22+1760.00)/2 :
            return "gis"	#G#6/Ab6     1661.22
    	elif self.freq <= (1760.00+1864.66)/2 :
            return "a"	#A6     1760.00
    	elif self.freq <= (1864.66+1975.53)/2 :
            return "ais"	#A#6/Bb6     1864.66
    	elif self.freq <= (1975.53+2093.00)/2 :
            return "b"	#B6     1975.53
    	elif self.freq <= (2093.00+2217.46)/2 :
            return "c"	#C7     2093.00
    	elif self.freq <= (2217.46+2349.32)/2 :
            return "cis"	#C#7/Db7     2217.46
    	elif self.freq <= (2349.32+2489.02)/2 :
            return "d"	#D7     2349.32
    	elif self.freq <= (2489.02+2637.02)/2 :
            return "dis"	#D#7/Eb7     2489.02 
    	elif self.freq <= (2637.02+2793.83)/2 :
            return "e"	#E7     2637.02 
    	elif self.freq <= (2793.83+2959.96)/2 :
            return "f"	#F7     2793.83
    	elif self.freq <= (2959.96+3135.96)/2 :
            return "fis"	#F#7/Gb7     2959.96
    	elif self.freq <= (3135.96+3322.44)/2 :
            return "g"	#G7     3135.96
    	elif self.freq <= (3322.44+3520.00)/2 :
            return "gis"	#G#7/Ab7     3322.44
    	elif self.freq <= (3520.00+3729.31)/2 :
            return "a"	#A7     3520.00
    	elif self.freq <= (3729.31+3951.07)/2 :
            return "ais"	#A#7/Bb7     3729.31
    	elif self.freq <= (3951.07+4186.01)/2 :
            return "b"	#B7     3951.07
    	elif self.freq <= (4186.01+4434.92)/2 :
            return "c"	#C8     4186.01
    	elif self.freq <= (4434.92+4698.64)/2 :
            return "cis"	#C#8/Db8     4434.92
    	elif self.freq <= (4698.64+4978.03)/2 :
            return "d"	#D8     4698.64
    	elif self.freq <= (4978.03+5300.00)/2 :
            return "dis"	#D#8/Eb8     4978.03
        else :
            return "Very Odd notes!!!"
        
    def getNoteSymbolPercentDiff(self):
        '''
        this calculates based on note symbol frequency and actual frequency
        '''
        #Calculate
        
    def getDurationSymbol(self,bpm=120.0):
        '''
        this calculates the duration based on bpm
        bpm must be an integer between 0 and 300
        '''
        #4 second beat, 120 beats a minute, 8 beats total
        beatsPerSecond = bpm/60.0
        frac = (self.getDuration()*beatsPerSecond)/4.0;
        symbol = ""
        #calculate
        #whole-note                  1
        if frac < ( .015625 + .0078125)/2:
            symbol = "128"#one-twenty-eigth            .0078125
        elif frac < ( .0234275 + .015625 )/2:
            symbol = "64"#sixty-fourth-note           .015625
        elif frac < ( .03125 + .0234275 )/2:
            symbol = "64."#dotted sixty-fourth note    .0234275
        elif frac < ( .046875 + .03125 )/2:
            symbol = "32"#thirty-second-note          .03125
        elif frac < ( .0625 + .046875 )/2:
            symbol = "32."#dotted thirtysecond note    .046875
        elif frac < ( .0833333 + .0625 )/2:
            symbol = "16"#sixteenth-note              .0625      
        elif frac < ( .09375 + .0833333 )/2:
            symbol = "12"#triplet(1/12)               .0833333
        elif frac < ( .125 + .09375 )/2:
            symbol = "16."#dotted sixteenth note       .09375
        elif frac < ( .1666667 + .125 )/2:
            symbol = "8"#eigth-note                  .125
        elif frac < ( .1875 + .1666667 )/2:
            symbol = "6"#triplet(1/6)                .1666667
        elif frac < ( .25 + .1875 )/2:
            symbol = "8."#dotted eigth note           .1875
        elif frac < ( .375 + .25 )/2:
            symbol = "4"#quarter-note                .25
        elif frac < ( .5 + .375 )/2:
            symbol = "4."#dotted quarter note         .375
        elif frac < ( .75 + .5 )/2:
            symbol = "2"#half-note                   .5                                   
        elif frac < (1.0 + .75)/2:
            symbol = "2."#dotted half-note            .75
        else :
            symbol = "1"
            
        return symbol
            
            
    def getDurationPercentDifference(self,bpm=120.0):
        '''
        this calculates the duration percent difference
        '''
        #calculate
        frac = (self.getDuration()*(bpm/60.0))/4.0
        target = .0078125
        #calculate
        #whole-note                  1
#        if frac > ( .015625 + .0078125)/2:
#            symbol = "128"#one-twenty-eigth            .0078125
        if frac < ( .0234275 + .015625 )/2:
            target = .015625    #sixty-fourth-note           .015625
        elif frac < ( .03125 + .0234275 )/2:
            target = .0234275   #dotted sixty-fourth note    .0234275
        elif frac < ( .046875 + .03125 )/2:
            target = .03125     #thirty-second-note          .03125
        elif frac < ( .0625 + .046875 )/2:
            target = .046875    #dotted thirtysecond note    .046875
        elif frac < ( .0833333 + .0625 )/2:
            target = .0625      #sixteenth-note              .0625        
        elif frac < ( .09375 + .0833333 )/2:
            target = .0833333   #triplet(1/12)               .0833333
        elif frac < ( .125 + .09375 )/2:
            target = .09375     #dotted sixteenth note       .09375
        elif frac < ( .1666667 + .125 )/2:
            target = .125       #eigth-note                  .125
        elif frac < ( .1875 + .1666667 )/2:
            target = .1666667   #triplet(1/6)                .1666667
        elif frac < ( .25 + .1875 )/2:
            target = .1875      #dotted eigth note           .1875
        elif frac < ( .375 + .25 )/2:
            target = .25        #quarter-note                .25
        elif frac < ( .5 + .375 )/2:
            target =  .375      #dotted quarter note         .375
        elif frac < ( .75 + .5 )/2:
            target = .5        #half-note                   .5                                    
        elif frac < (1.0 + .75)/2:
            target = .75        #dotted half-note            .75
        else :
            target = 1
            
        actual = (self.getDuration()*(bpm/60.0))/4.0
#        print target
#        print actual
#            
        return (target-actual)/actual
        
    def getFrequency(self):
        '''
        return the frequency(hertz)
        '''
        return self.freq
        
    def getStart(self):
        '''
        return the relative start
        '''
        return self.start
        
    def getVolume(self):
        '''
        return the volume/amplitude
        '''
        return self.volume
        
    def getDuration(self):
        '''
        return the duration
        '''
        return self.duration
        
    def setFrequency(self,num):
        '''
        sets the hertz
        '''
        self.freq = num
         
    def setStart(self,num):
        '''
        set the relative start (in milliseconds)
        '''
        self.start = num
        
    def setDuration(self,num):
        '''
        set the Duration of the note (milliseconds)
        '''
        self.duration = num
        
    def setVolume(self,num):
        '''
        Set the volume/amplitude
        '''
        self.volume = num
        
    def toLilyPond(self):
        '''
        generates a LilyPond representation of the note
        '''
        err = self.getDurationPercentDifference()
#        print err
        colr = ""
        if err > 0.05 :
            colr = "\\override NoteHead #'color = #blue"# + str(int(err*100)/5)
        elif err < -0.05 :
            colr = "\\override NoteHead #'color = #red"# + str(int(-1*err*100)/5)
        else :
            colr = "\\revert NoteHead #'color"
        return colr + " \n" + self.getSymbol() + self.getDurationSymbol() + " "