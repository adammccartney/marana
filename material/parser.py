# marana/materials/parser.py
#!/usr/bin/python3
"""
This module that provides a simple parser to parse 'modular expressions'
a modular expression is an invented term that refers to a specific style of
musical idea

    basically, what we want to try here is to load an instruction that causes a
    parse operation and returns a voice with structured pitch data
"""

from abc import ABC, abstractmethod
from enum import Enum, auto

from abjad import PitchClassSegment, PitchSegment

from material.pitch import (PitchTuple)

class Pitch(ABC):
    "virtual class for representing pitch objects"
    @property
    @abstractmethod
    def pcseg(self):
        pass

    @abstractmethod
    def resolve(self):
        pass


class PartialType(Enum):
    "partials of the harmonic series (music)"
    F1 = 1; F2 = auto(); F3 = auto() 
    F4 = auto(); F5 = auto(); F6 = auto() 
    F7 = auto(); F8 = auto(); F9 = auto()
    F10 = auto(); F11 = auto(); F12 = auto()
    F13 = auto(); F14 = auto(); F15 = auto()
    F16 = auto(); F17 = auto(); F18 = auto()
    F19 = auto(); F20 = auto()

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
        if (self.partialtype.value in {2, 4, 8, 16}):  # octaves
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
        else: # default simply returns existing root
            return self.rootseg 

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
    "Pitch function type"
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
    pitch = None
    if (attrs.funtype == PitchFunType.PARTIAL):
        pitch = attrs.args   
    if (attrs.funtype == PitchFunType.CHORDTONE):
        pitch = attrs.args
    assert pitch is not None, "pitch should be bound"
    pcseg = pitch.pcseg
    assert isinstance(pcseg, PitchClassSegment), "pcseg should be instance PitchClassSegment"
    res = None
    assert direction in {"vert", "horiz"}, "direction should be vert or horiz"
    if (direction == "vert"):
        res = pcseg.voice_vertically(attrs.octave)
    elif (direction == "horiz"):
        res = pcseg.voice_horizontally(attrs.octave)
    assert res is not None, "res should be bound"
    assert isinstance(res, PitchSegment), "res should be instance PitchSegment"
    return res 


def parse_args(args: tuple, pitchclass_data_segments: list[PitchTuple]):
    """
    resolves the attrs['args'] by looking up their values in the data segment
    """
    tones = None
    harmonies = [pcseg.harmony for pcseg in pitchclass_data_segments]
    roots = [pcseg.root for pcseg in pitchclass_data_segments]
    if (len(args) == 1): # chordtone selector
        i = args[0]
        tones = [ChordTone(h, i) for h in harmonies]
    if (len(args) == 2): # root, partial pair
        p = args[1]
        tones = [Partial(r, p) for r in roots]
    assert tones is not None
    return tones

def parse_pitch_attrs(attrs: dict, pitch_data: list[PitchTuple]):
    """
    parse the attributes of pitch selector
    """
    args = attrs['args']
    octave = attrs['octave']

def parse_pselector(pselector: tuple):
    """
    takes a tuple of pitch selectors and resolves to pitches, returns a
    tuple of lilypond pitch strings
    """
    num_items = len(pselector)
    for ps in pselector:
        if ps["token_type"] == "partial":
            print("resolve the args as partial")
        if ps["token_type"] == "chordtone":
            print("resolve the args as chord tone")
    return num_items


def parse_input(input: tuple):  # returns a flat array of lilypond pitch strings
    num_items = len(input)
    for n in input:
        for k in n:
            pselector_tup = None
            voicing_flag = None
            if k == "selector":
                pselector_tup = n[k]
            if k == "voicing":
                voicing_flag = n[k]
    return num_items



