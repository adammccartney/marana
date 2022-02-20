#!/usr/bin/python3

# marana/modules/pitch.py: routines for shaping pitch content

from abjad import PitchClassSegment, PitchSegment

class PitchTuple:
    """Simple dataclass for handling pairs of pitch material"""
    def __init__(self, root, harmony):
        self.root = root
        self.harmony = harmony 

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


def make_pitch_segments(pitch_tuples: list[PitchTuple]):
    """
    iterate over a list of pitch tuples, upgrades the content of each pitch
    tuple from basic lilypond strings to abjad PitchSegments
    """
    root_segs = [PitchSegment(p.root) for p in pitch_tuples]
    harm_segs = [PitchSegment(strip(p.harmony)) for p in pitch_tuples]
    pairs = list(zip(root_segs, harm_segs))
    psegs = [PitchTuple(p[0], p[1]) for p in pairs]
    return psegs

def make_pitchclass_segments(pitch_tuples: list[PitchTuple]):
    """
    iterate over a list of pitch tuples, upgrades the content of each pitch
    tuple from basic lilypond strings to abjad PitchClassSegments
    """
    root_segs = [PitchClassSegment(p.root) for p in pitch_tuples]
    harm_segs = [PitchClassSegment(strip(p.harmony)) for p in pitch_tuples]
    pairs = list(zip(root_segs, harm_segs))
    pcsegs = [PitchTuple(p[0], p[1]) for p in pairs]
    return pcsegs



