#!/usr/bin/python3

# marana/modules/bass_segmentA.py
from abc import ABC, abstractmethod
import math
from enum import Enum, auto

from .pitch import (PitchTuple, make_pitch_tuples, strip, make_pitch_segments)

from abjad import PitchClassSegment, PitchSegment

class Pitch(ABC):

    @property
    @abstractmethod
    def pcseg(self):
        pass

    @abstractmethod
    def resolve(self):
        pass


class PartialType(Enum):
    # given an overt  one partial
    F1 = 1
    F2 = auto() 
    F3 = auto() 
    F4 = auto() 
    F5 = auto() 
    F6 = auto() 
    F7 = auto() 
    F8 = auto() 
    F9 = auto()
    F10 = auto()
    F11 = auto()
    F12 = auto()
    F13 = auto()
    F14 = auto()
    F15 = auto()
    F16 = auto()
    F17 = auto()
    F18 = auto()
    F19 = auto()
    F20 = auto()

class Partial(Pitch):
    """  
    Concrete instance of a pitch
    partial refers to the fact that the object is intended to represent a
    partial of the harmonic series (music)
    """
    def __init__(self, root, partialtype=PartialType.F1):
        self.rootseg = PitchClassSegment(root)
        self.partialtype = partialtype

    @property
    def pcseg(self) -> PitchClassSegment: 
        return self.resolve()

    def resolve(self):
        if (math.log2(self.partialtype.value) % 2 in {0.0, 1.0}):  # octaves
            return self.rootseg.transpose(0)
        elif (self.partialtype.value in {3, 6, 12}):  # fifths
            return self.rootseg.transpose(7)
        elif (self.partialtype.value in {5, 10, 20}): # major third
            return self.rootseg.transpose(4)
        elif (self.partialtype.value in {7, 14}):
            return self.rootseg.transpose(9.5)
        elif (self.partialtype.value in {9, 18}):
            return self.rootseg.transpose(2)
        elif (self.partialtype.value in {11}):
            return self.rootseg.transpose(5.5)
        elif (self.partialtype.value in {13}):
            return self.rootseg.transpose(8.5)
        elif (self.partialtype.value in {15}):
            return self.rootseg.transpose(11)
        elif (self.partialtype.value in {17}):
            return self.rootseg.transpose(1)
        elif (self.partialtype.value in {19}):
            return self.rootseg.transpose(3)
        else:
            raise ValueError("PartialType not recognized")

class Harmony:
    """
    harmony refers to the fact taht the object is intended to represent a
    (triadic / tetradic) harmony
    """
    def __init__(self, pseg: PitchClassSegment):
        self.pseg = PitchSegment

    @property
    def pseg(self):
        return self.pseg

    @pseg.setter
    def pseg(self, pseg: PitchSegment):
        self.pseg = pseg

    def resolve(self):
        pass


class ChordTone(Pitch):
    """
    concrete instance of a pitch
    so called because chord tone is one of the tones that makes up a chord 
    """
    def __init__(self, harmony: str, selector: int):
        self.rootseg = PitchClassSegment(harmony)
        self.selector = selector

    @property
    def pcseg(self) -> PitchClassSegment:
        return self.resolve()

    def resolve(self):
        if (0 < self.selector) and (self.selector < len(self.rootseg)):
            named_pitch_class = self.rootseg[self.selector]
            return PitchClassSegment(str(named_pitch_class))
        else:
            raise IndexError("Requested index out of range")


class PitchFunType(Enum):
    PARTIAL = auto()
    CHORDTONE = auto()


class PitchFunAttrs:
    """
    pitch function attributes
    """
    def __init__(self, funtype: PitchFunType, args: tuple, octave: int):
        self.funtype = funtype
        self.init_args = args
        self.octave = octave
        self.args = self.resolve_args()

    def resolve_args(self) -> Pitch:
        if (self.funtype == PitchFunType.PARTIAL):
            return Partial(self.init_args[0], self.init_args[1])
        elif (self.funtype == PitchFunType.CHORDTONE):
            return ChordTone(self.init_args[0], self.init_args[1])
        else:
            raise ValueError("Unknown pitch function type requested")


def resolve_pitch(attrs: PitchFunAttrs, direction="vert"):
    """
    resolves a pitchclass segment by voicing in a particular octave,
    direction specifies the resolution order for the voicing
    from abjad docs:
    voice_horizontally
        Voices segment with each pitch as close to the previous pitch as
        possible.
    voice_vertically
        Voices segment with each pitch higher than the previous.
    """
    if (attrs.funtype == PitchFunType.PARTIAL):
        pitch = attrs.args   
    elif (attrs.funtype == PitchFunType.CHORDTONE):
        pitch = attrs.args
    else:
        raise ValueError("No pitch defined")
    pcseg = pitch.pcseg
    if (direction == "vert"):
        res = pcseg.voice_vertically(attrs.octave)
    elif (direction == "horiz"):
        res = pcseg.voice_horizontally(attrs.octave)
    else:
        raise ValueError("Direction not recognized, options: vert | horiz")
    return res 


if __name__ == '__main__':
    ########################################################################
    # data 
    ########################################################################
    HARMONIES = ["<e g a>",
                "<ef gf a>",
                "<df f a>",
                "<df gf bf>",
                "<df gf bf>"]

    ROOTS = ["c", "d", "ef", "f", "gf", "a", "bf", "c", "df", "ef"]
    PTUPS = make_pitch_tuples(ROOTS, HARMONIES)
    PSEGS = make_pitch_segments(PTUPS)
    ########################################################################
    """
    basically, what we want to try here is to load an instruction that causes a
    parse operation and returns a voice with structured pitch data

    i.e. 
    voice = (pitch_function(pitch_segment_data))

    ({token_type: partial,
      attributes: {args: (root), octave: 4}},
     {token_type: harm,
      attributes: {args: (2), octave: 4}}),
    ({token_type: partial,
      attributes: (root), octave: 4}},
     {token_type: harm,
      attributes: {args: (2), octave: 4}})

    my_pitches = parse_pitch_set([["<(getpart [pitch: root, 4] (getharm(2), 4)>"],
                                  ["<(getpart(root), 4) (getharm(2), 4)>"],
                                  ["<(getpart(root), 4) (getharm(1), 4)>"]]) 

    returns 
    [[["<c' a'>"], ["<g' a'>"], ["<c'' g'>"]],
     [["<d' a'>"], ["<g' a'>"], ["<d'' g'>"]]
     ...
    ]
    """

    import abjad
    myseg = abjad.PitchClassSegment("c")
    g = myseg.transpose(7)
