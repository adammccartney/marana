#!/usr/bin/python3

# marana/pitch.py: routines for shaping pitch content

from abjad import PitchClassSegment, PitchClassSegment, PitchSegment
from collections import namedtuple

from abc import ABC, abstractmethod
from enum import Enum, auto

class PitchToken(Enum):
    PARTIAL = auto()
    CHORDTONE = auto()

class PitchTuple:
    """Simple dataclass for handling pairs of pitch material"""
    def __init__(self, root, harmony):
        self.root = root
        self.harmony = harmony 

PcSegTuple = namedtuple("PcSegTuple", ["root", "harmony"])
PitchSegTuple = namedtuple("PitchSegTuple", ["root", "harmony"])

def make_pitch_tuples(roots: list, harmonies: list) -> list[PitchTuple]:
    """
    Take two arrays of lilypond strings representing roots and harmonies,
    structure them into a list of PitchTuple objects where each harmony is
    paired with two roots. The pairings a sequential so that harmony one occurs
    over root one and root two
    """
    oroots = [r for r in roots[::2]]
    eroots = [r for r in roots[1::2]]
    opairs = list(zip(oroots, harmonies))
    epairs = list(zip(eroots, harmonies))
    pairs = opairs + epairs
    pairs[::2] = opairs
    pairs[1::2] = epairs
    res = [PitchTuple(p[0], p[1]) for p in pairs]
    return res

def strip(chord: str) -> str:
    "strip the hairpins from a string"
    chord = chord.lstrip("<")
    chord = chord.rstrip(">")
    return chord


def make_pitch_segments(pitch_tuples: list[PitchTuple]) -> list[PitchTuple]:
    """
    iterate over a list of pitch tuples, upgrades the content of each pitch
    tuple from basic lilypond strings to abjad PitchSegments
    """
    root_segs = [PitchSegment(p.root) for p in pitch_tuples]
    harm_segs = [PitchSegment(strip(p.harmony)) for p in pitch_tuples]
    pairs = list(zip(root_segs, harm_segs))
    psegs = [PitchTuple(p[0], p[1]) for p in pairs]
    return psegs

def make_pitchclass_segments(pitch_tuples: list[PitchTuple]) -> list[PcSegTuple]:
    """
    iterate over a list of pitch tuples, upgrades the content of each pitch
    tuple from basic lilypond strings to abjad PitchClassSegments
    """
    root_segs = [PitchClassSegment(p.root) for p in pitch_tuples]
    harm_segs = [PitchClassSegment(strip(p.harmony)) for p in pitch_tuples]
    pairs = list(zip(root_segs, harm_segs))
    pcsegs = [PcSegTuple(p[0], p[1]) for p in pairs]
    return pcsegs



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
    "partials of   the harmonic series (music)"
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

class PitchFunAttrs:
    """ 
    pitch function attributes
    members: 
        funtype
        init_args
        octave
        args -> after resolution, will return a Pitch object
    """
    def __init__(self, funtype: PitchToken, args: tuple, octave: int):
        self.funtype = funtype
        self.init_args = args
        self.octave = octave
        self.args = self.resolve_args()

    def resolve_args(self) -> Pitch:
        if (self.funtype == PitchToken.PARTIAL):
            return Partial(self.init_args[0], self.init_args[1])
        elif (self.funtype == PitchToken.CHORDTONE):
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


class PitchQuery:
    """
    A pitch query is a simple struct for holding information used to interpret
    pitch data in a structured way.

    attributes:
        pitchtype
        resolution (this is partial num or selector index)
        voicing
    """
    def __init__(self, ptype: str, resolution: int, voicing: OctaveVoicing):
        self.checkptype(ptype)
        self.resolution = resolution
        self.voicing = voicing

    def checkptype(self, ptype: str):
        if ptype not in {"partial", "chordtone"}:
            raise ValueError("Unknown pitch type")
        if ptype == "partial":
            self.ptype = PitchToken.PARTIAL
        if ptype == "chordtone":
            self.ptype = PitchToken.CHORDTONE


class PitchData:
    """
    Another simple structure used for storing pitch data

    attributes:
        roots
        harmonies
    """
    def __init__(self, roots, harmonies):
        self.roots = roots
        self.harmonies = harmonies


