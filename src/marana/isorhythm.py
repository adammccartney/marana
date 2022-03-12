#!/usr/bin/python3
"""
marana.isorhythm module geared primarily toward the isorhythm of pitch and rhythm
"""
import abjad
from abjad import Container, CyclicTuple, Duration, LeafMaker, NamedPitch
from abjadext.rmakers import rmakers

from marana.pitch import PitchSegTuple

def make_basic_rhythm(time_signature_pairs, counts, denominator):
    """
    total duration of the rhytmic bloc is calculated from time_signature_pairs
    this value is then used to create a rhytmical structure after an instance
    of the Talea has been created using the counts and denominator
    Talea is a fancy term from the middle ages that basically means rhythmic
    pattern. It's a bit like paint by numbers. 
    This function determines where on the grid the pitches will eventually
    fall
    This code owes much of its existence to the abjad mailing list
    and probably comes from Trevor Bača and Josiah Wolf Oberholzer

    Note: The resolution of some of the methods that use NonreducedFraction is
    complex enough to confuse some language servers (at least the pyright
    language server). Altough the static analysis seems to show up some
    inconsistencies, a test of this function shows that the logic is sound and
    it does what it's supposed to do.
    """
    total_duration = sum(Duration(pair) for pair in time_signature_pairs)
    talea = rmakers.Talea(counts=counts, denominator=denominator)
    talea_index = 0
    all_leaves = []
    current_duration = Duration(0)
    while current_duration < total_duration:
        leaf_duration = talea[talea_index]
        if leaf_duration.numerator > 0:
            pitch = NamedPitch("c'")
        else:
            pitch = None
        leaf_duration = abs(leaf_duration)
        if (leaf_duration + current_duration) > total_duration:
            leaf_duration = total_duration - current_duration
        current_leaves = LeafMaker()([pitch], [leaf_duration])
        all_leaves.extend(current_leaves)
        current_duration += leaf_duration
        talea_index += 1
    music = Container(all_leaves)
    return music


def add_pitches(music: Container, pitches: PitchSegTuple) -> Container:
    """
    attaches pitches to points in the music where a pitch should sound
    does not attach to rests

    arguments: as hinted above,

    returns an abjad Container
    """
    npitches = CyclicTuple(pitches)
    pitch_index = 0
    for logical_tie in abjad.iterate.logical_ties(music, pitched=True):
        pitch = npitches[pitch_index]
        for note in logical_tie:
            note.written_pitch = pitch[0]
        pitch_index = pitch_index + 1
    return music


