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
    '''
    Attributes:
        start
        end 
        fret
    '''
    def __init__(self, fret = 0, start = 0, end = 0):
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
    
        self.tempoName = tempoName
        self.hideTempo = hideTempo
        self.useRSE = useRSE

    def isJustWah(self):
    
        return (instrument.isNull == True and volume.isNull == True and balance.isNull == True and
               chorus.isNull == True and reverb.isNull == True and phaser.isNull == True and 
               tremolo.isNull == True and wah.isNull == False)
    

class myColor:
    '''
    Attributes:
        float r, g, b, a
    '''
    
    def __init__(self, r=1.0, g=1.0, b=1.0, a = 255.0):
        self.r = r / 255.0
        self.g = g /255.0
        self.b = b / 255.0
        self.a = a / 255.0

#=========================================
class Padding:
    '''
    Attributes:
        int right, top, left, bottom
    '''
    def __init__(self, right = 0, top=0, left=0, bottom = 0):
        self.right = right; self.top = top; self.left = left; self.bottom = bottom

class Point:
    '''
    Attributes:
        int x, y
    '''
    def __init__(self, x=0, y=0):
        self.x = x; self.y = y

#枚举类
@unique
class HeaderFooterElements(Enum):
    none = 0x000
    title = 0x001
    subtitle = 0x002
    artist = 0x004
    album = 0x008
    words = 0x010
    music = 0x020
    wordsAndMusic = 0x040
    copyright = 0x080
    pageNumber = 0x100
    all = title | subtitle | artist | album | words | music | wordsAndMusic | copyright | pageNumber

#及其应用
class PageSetup:
    '''
    描述文件的渲染方式（预设）：

        %title%, %subtitle%, %artist%, %album%, %words%, %music%, %copyright%在具体曲目中会被对应的Song.*代替。
        %N%, %P%则会根据具体页数变化
    '''
    
    pageSize = Point(210,297)
    pageMargin = Padding(10, 15, 10, 10)
    scoreSizeProportion = 1.0
    headerAndFooter = HeaderFooterElements.all
    title = "%title%"
    subtitle = "%subtitle%"
    artist = "%artist%"
    album = "%album%"
    words = "Words by %words%"
    music = "Music by %music%"
    wordsAndMusic = "Words & Music by %WORDSMUSIC%"
    copyright = "Copyright %copyright%\nAll Rights Reserved - International Copyright Secured"
    pageNumber = "Page %N%/%P%"


class PitchClass:
    '''

    '''
    just = 0
    accidental = 0
    value = 0
    intonation = ""
    actualOvertone = 0.0

    def __init__(self, arg0i = 0, arg1i = -1, arg0s = "", intonation = "", actualOvertone = 0.0):
        _notes_sharp = ( "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" )
        _notes_flat = ( "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B" )
        value = 0
        str = ""
        accidental = 0
        pitch = 0
        self.actualOvertone = actualOvertone
        # ^ 使得在内部格式里更易于使用
        if arg1i == -1:
            if arg0s != "":
                str = arg0s
                x = 0
                while x < len(_notes_sharp):
                    if str == _notes_sharp[x]: value = x; break
                    if str == _notes_flat[x]: value = x; break
                    x += 1
            else:
                value = arg0i % 12
               
                str = _notes_sharp[max(value,0)]
                if intonation == "flat": str = _notes_flat[value]

            if str.endswith("b"): accidental = -1
            elif str.endswith("#"): accidental = 1
        else:
            pitch = arg0i; accidental = arg1i
            self.just = pitch % 12
            self.accidental = accidental
            self.value = self.just + accidental
            if intonation != null: 
                self.intonation = intonation
            else:
                if accidental == -1: self.intonation = "flat"
                else: self.intonation = "sharp"   

