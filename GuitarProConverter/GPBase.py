from enum import Enum,unique


#=============================
#枚举类

@unique
class BeatStatus(Enum):
    empty = 0
    normal = 1
    rest = 2

@unique
class BeatStrokeDirection(Enum):
    none = 0
    up = 1
    down = 2


@unique
class BendType(Enum):
    '''推弦技巧'''

    # 无预设
    none = 0
    # 预设推弦类型
    # =====
    # 单推弦
    bend = 1
    # 推弦并归位 
    bendRelease = 2
    # 推归推 >_<
    bendReleaseBend = 3
    # 预推 
    prebend = 4
    # 预推并归位 
    prebendRelease = 5

    # 摇把颤音（TremoloBar）
    # ==========
    dip = 6
    dive = 7
    releaseUp = 8
    invertedDip = 9
    return_ = 10
    releaseDown = 11

@unique
class ChordType(Enum):
    major = 0
    seventh = 1
    majorSeventh = 2
    sixth = 3
    minor = 4
    minorSeventh = 5
    minorMajor = 6
    minorSixth = 7
    suspendedSecond = 8
    suspendedFourth = 9
    seventhSuspendedSecond = 10
    seventhSuspendedFourth = 11
    diminished = 12
    augmented = 13
    power = 14

@unique
class ChordAlteration(Enum):
    perfect = 0
    diminished = 1
    augmented = 2

@unique
class ChordExtension(Enum):
    none = 0
    ninth = 1
    eleventh = 2
    thirteenth = 3

@unique
class Fingering(Enum):
    unknown = -2
    open = -1
    thump = 0
    index = 1
    middle = 2
    annular = 3
    little = 4

@unique
class GraceEffectTransition(Enum):
    none = 0
    slide = 1
    bend = 2
    hammer = 3

@unique
class KeySignature(Enum):
    FMajorFlat = -80
    CMajorFlat = -70
    GMajorFlat = -60
    DMajorFlat = -50
    AMajorFlat = -40
    EMajorFlat = -30
    BMajorFlat = -20
    FMajor = -10
    CMajor = 00
    GMajor = 10
    DMajor = 20
    AMajor = 30
    EMajor = 40
    BMajor = 50
    FMajorSharp = 60
    CMajorSharp = 70
    GMajorSharp = 80
    DMinorFlat = -81
    AMinorFlat = -71
    EMinorFlat = -61
    BMinorFlat = -51
    FMinor = -41
    CMinor = -31
    GMinor = -21
    DMinor = -11
    # 修改记录：python3 不再支持除0以外的整数使用前导0
    AMinor = 1
    EMinor = 11
    BMinor = 21
    FMinorSharp = 31
    CMinorSharp = 41
    GMinorSharp = 51
    DMinorSharp = 61
    AMinorSharp = 71
    EMinorSharp = 81

@unique
class LineBreak(Enum):
    none = 0
    break_ = 1
    protect = 2

@unique
class MeasureClef(Enum):
    treble = 0
    bass = 1
    tenor = 2
    alto = 3
    neutral = 4 #鼓

@unique
class NoteType(Enum):
    rest = 0
    normal = 1
    tie = 2
    dead = 3

@unique
class SlapEffect(Enum):
    none = 0
    tapping = 1
    slapping = 2
    popping = 3

@unique
class SlideType(Enum):
    intoFromAbove = -2
    intoFromBelow = -1
    none = 0
    shiftSlideTo = 1
    legatoSlideTo = 2
    outDownwards = 3
    outUpwards = 4
    pickScrapeOutDownwards = 5
    pickScrapeOutUpwards = 6

@unique
class TripletFeel(Enum):
    none = 0
    eigth = 1
    sixteenth = 2
    dotted8th = 3
    dotted16th = 4
    scottish8th = 5
    scottish16th = 6

@unique
class TupletBracket(Enum):
    none = 0
    start = 1
    end = 2

@unique
class Octave(Enum):
    none = 0
    ottava = 1
    quindicesima = 2
    ottavaBassa = 3
    quindicesimaBassa = 4

@unique
class VoiceDirection(Enum):

    none = 0
    up = 1
    down = 2

@unique
class SimileMark(Enum):

    none = 0
    simple = 1
    firstOfDouble = 2
    secondOfDouble = 3

@unique
class WahState(Enum):
    off =-2
    none=-1
    opened = 0
    closed = 100
#===========================

class WahEffect:

    state = WahState.none
    display = False


#===============================================

#抽象类
class HarmonicEffect:
    fret = 0
    type = 0

#及其派生
class NaturalHarmonic(HarmonicEffect):
    def __init__(self): type = 1

class ArtificialHarmonic(HarmonicEffect):
    pitch = 0
    octave = Octave.none
    def __init__(self, pitch = 0, octave = Octave.none):
        self.pitch = pitch; self.octave = octave; self.type = 2

class TappedHarmonic(HarmonicEffect):
    def TappedHarmonic(self, fret = 0):
        self.fret = fret; self.type = 3

class PinchHarmonic(HarmonicEffect):
    def __init__(self): type = 4

class SemiHarmonic(HarmonicEffect):
    def __init__(self): type = 5

class FeedbackHarmonic(HarmonicEffect):
   def __init__(self): type = 6

#=======================================================

class LyricLine:
    startingMeasure = 1
    lyrics = ""

class Lyrics:

    __maxLineCount = 5
    trackChoice = -1

    def __init__(self):
        trackChoice = -1
        lines = LyricLine[__maxLineCount]
        x = 0
        while x < __maxLineCount:
            lines[x] = LyricLine()
            x += 1

#==================================================
class Barre:
    start = 0
    end = 0
    fret = 0
    def __init__(self, fret, start, end):
        self.start = start; self.fret = fret; self.end = end
    
    def range(self):   
        return [self.start, self.end]

class MidiChannel:

    channel=effectChannel=instrument=volume=balance=chorus=reverb=phaser=tremolo=bank = 0

    DEFAULT_PERCUSSION_CHANNEL = 9

    def __init__(self):
        self.channel = 0; self.effectChannel = 1; self.instrument = 25; self.volume = 104
        self.balance = 64; self.chorus = 0; self.reverb = 0; self.phaser = 0
        self.tremolo = 0; self.bank = 0

    def isPercussionChannel(self):
        return channel % 16 == DEFAULT_PERCUSSION_CHANNEL


class MixTableItem:
    '''
    Attributes:
        int value
        int duration
        bool allTracks
        bool isNull
    '''
    
    def __init__(self, value = 0, duration = 0, allTracks = False, isNull = True):
        self.value = value; self.duration = duration; self.allTracks = allTracks; self.isNull = isNull

class MixTableChange:
    '''
    Attributes:
        string tempoName
        bool hideTempo
        bool useRSE
        MixTableItem instrument,volume,balance,chorus,reverb,phaser,tremolo,tempo,wah,rse
    '''
    instrument = MixTableItem()
    volume = MixTableItem()
    balance = MixTableItem()
    chorus = MixTableItem()
    reverb = MixTableItem()
    phaser = MixTableItem()
    tremolo = MixTableItem()
    tempo = MixTableItem()
    wah = MixTableItem()
    #rse = RSEInstrument()

    def __init__(self, tempoName = "", hideTempo = True, useRSE = True):
    
        self.tempoName = tempoName;
        self.hideTempo = hideTempo;
        self.useRSE = useRSE;

    def isJustWah(self):
    
        return (instrument.isNull == True and volume.isNull == True and balance.isNull == True and
               chorus.isNull == True and reverb.isNull == True and phaser.isNull == True and 
               tremolo.isNull == True and wah.isNull == False)
    

class myColor:
    def __init__(self, r=1.0, g=1.0, b=1.0, a = 255.0):
        this.r = r / 255.0;
        this.g = g /255.0;
        this.b = b / 255.0;
        this.a = a / 255.0;
