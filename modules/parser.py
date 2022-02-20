#!/usr/bin/python3

# marana/modules/bass_segmentA.py
import math
from enum import Enum, auto

from .pitch import (PitchTuple, make_pitch_tuples, strip, make_pitch_segments)

import abjad


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

class Partial:
    """  
    initialized with a partialtype and pitchclass, a partial maintains one internal member -
    offset - this allows to perform a transposition on the pitchclass
    Keyword arg is supplied for the default partial type - default reverts to
    root
    """
    def __init__(self, root, partialtype=PartialType.F1):
        self.pitchclass = abjad.PitchClassSegment(root)
        self.partialtype = partialtype
        self.pcseg = self.transpose()

    def transpose(self):
        if (math.log2(self.partialtype.value) % 2 in {0.0, 1.0}):  # octaves
            return self.pitchclass.transpose(0)
        elif (self.partialtype.value in {3, 6, 12}):  # fifths
            return self.pitchclass.transpose(7)
        elif (self.partialtype.value in {5, 10, 20}): # major third
            return self.pitchclass.transpose(4)
        elif (self.partialtype.value in {7, 14}):
            return self.pitchclass.transpose(9.5)
        elif (self.partialtype.value in {9, 18}):
            return self.pitchclass.transpose(2)
        elif (self.partialtype.value in {11}):
            return self.pitchclass.transpose(5.5)
        elif (self.partialtype.value in {13}):
            return self.pitchclass.transpose(8.5)
        elif (self.partialtype.value in {15}):
            return self.pitchclass.transpose(11)
        elif (self.partialtype.value in {17}):
            return self.pitchclass.transpose(1)
        elif (self.partialtype.value in {19}):
            return self.pitchclass.transpose(3)
        else:
            raise ValueError("PartialType not recognized")

class PitchFunType(Enum):
    PARTIAL = auto()
    HARMONY = auto()

class PitchFunAttrs:
    """
    pitch function attributes
    """
    def __init__(self, funtype: PitchFunType, args: tuple, octave: int):
        self.funtype = funtype
        self.init_args = args
        self.octave = octave
        self.args = self.resolve_args()

    def resolve_args(self):
        if (self.funtype == PitchFunType.PARTIAL):
            return Partial(self.init_args[0], self.init_args[1])
        elif (self.funtype == PitchFunType.HARMONY):
            pass

class PitchFunction:
    def __init__(self, funtype: PitchFunType, attributes: PitchFunAttrs):
        self.funtype = funtype
        self.attributes = attributes

def res_partial_pseg(partial: Partial, octave: int, direction="vert"):
    """
    resolve partial pitch segment
    """
    if direction == "vert":
        res = partial.pcseg.voice_vertically(octave)
    elif direction == "horiz":
        res = partial.pcseg.voice_horizontally(octave)
    else:
        raise ValueError("Direction not recognized, options: vert | horiz")
    return res 


#def interpret_pitch_function(pitchfun: PitchFunction, direction="vert"):
#
#        if (pitchfun.funtype == PitchFunType.PARTIAL):
#            partial_pitch_class = Partial(pitchfun.attributes.args)
#            octave = pitchfun.attributes.octave
#            # resolve the partial pitchclass
#            # resolve the octave
#            # return a pitchsegment
#            pass
#


if __name__ == '__main__':
    ########################################################################
    # DATA 
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

