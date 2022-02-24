# marana/materials/parser.py
#!/usr/bin/python3
"""
This module that provides a simple parser to parse 'modular expressions'
a modular expression is an invented term that refers to a specific style of
musical idea

    basically, what we want to try here is to load an instruction that causes a
    parse operation and returns a voice with structured pitch data

    The data is queried using lists of selectors

     [(token_type: partial,
      attributes: {args: (root), octave: 4}},
     {token_type: harm,
      attributes: {args: (2), octave: 4}}),

    ({token_type: partial,
      attributes: (root), octave: 4}},
     {token_type: harm,
      attributes: {args: (2), octave: 4}})]

"""

from abc import ABC, abstractmethod
from enum import Enum, auto

from abjad import PitchClassSegment, PitchClassSegment, PitchSegment

from material.pitch import (PitchTuple, PitchSegTuple)

from collections import namedtuple

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
    "Pitch function type  "
    PARTIAL = auto()
    CHORDTONE = auto()


class PitchFunAttrs:
    """ 
    pitch function attributes
    members: 
        funtype
        init_args
        octave
        args -> after resolution, will return a Pitch object
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


class OctaveVoicing:
    """
    simple dataclass for making objects that know how to voice a pitchclass
    members:
        octave: int
        order: str
    order refers to the order of resolution (see
            abjad.PitchClassSegment notes on voice_horizontally etc.)
    """
    def __init__(self, octave: int, order="vert"):
        self.octave = octave
        self.order = order 


def make_octave_voicings(octaves: list[int], orders: list[str]):
    """
    Simple wrapper function to simply zip two lists of equal length, making an
    octave voicing 
    """
    assert len(octaves) == len(orders), "Lists must be of equal length"
    tups = list(zip(octaves, orders))
    ovoicings = [OctaveVoicing(o[0], o[1]) for o in tups] 
    return ovoicings

 
def parse_args(args: tuple, pitchclass_data_segments: list[PitchTuple]):
    """
    extractor function 
    arguments in the tuple are generic selectors for either PARTIAL or
    CHORDTONE type objects. What is returned is a list comprehension whose
    contents is a list of Pitch objects
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


def resolve_pitch(pcseg: PitchClassSegment, ovoicing: OctaveVoicing):
    """
    pitchclass: Partial|ChordTone
    ovoicing is a list of octave voicings

    returns a PitchSegment

    """
    order = ovoicing.order
    octave = ovoicing.octave
    ret = None
    assert order in {"vert", "horiz"}, "direction should be vert or horiz"
    if (order == "vert"):
        ret = pcseg.voice_vertically(octave)
    elif (order == "horiz"):
        ret = pcseg.voice_horizontally(octave)
    assert ret is not None, "res should be bound"
    assert isinstance(ret, PitchSegment), "res should be instance PitchSegment"
    return ret 


def voice_pitchclasses(pitchclasses, ovoicings: list[OctaveVoicing]) -> list[PitchSegTuple]:
    """
    takes a list of pitchclasses and a list of OctaveVoicings, voices the pitchclasses
    according to the members of the OctaveVoicing  

    arguments: pitchclasses: list[Partial] | list[ChordTone]

    returns a list of voiced PitchSegments
    """
    pitch_segments = []
    for (pc, ov) in zip(pitchclasses, ovoicings):
        root_pseg = resolve_pitch(pc.root, ov)
        harmony_pseg = resolve_pitch(pc.harmony, ov)
        psegtuple = PitchSegTuple(root_pseg, harmony_pseg)
        pitch_segments.append(psegtuple)
    return pitch_segments

def parse_pitch_attrs(attrs: dict, pitchclass_data: list[PitchTuple]):
    """
    parse the attributes of pitch selector
    attributes are:
        pitch_selector_args: the args specify what type of Pitch object will be formed
        octave: the octave specifies what octave the pitch will be voices at

    returns an array of PitchSegments
    """
    pitchclass_selector_args = attrs['args']
    pitchclasses = parse_args(pitchclass_selector_args, pitchclass_data) 
    octave = attrs['octave']
    octaves = [octave] * len(pitchclasses)  # we want to zip these later
    order = attrs['order']
    orders = [order] * len(pitchclasses)    # same here
    ovoicings = make_octave_voicings(octaves, orders)
    voiced_pitches = voice_pitchclasses(pitchclasses, ovoicings)
    return voiced_pitches


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
