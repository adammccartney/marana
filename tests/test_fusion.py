#!/usr/bin/python3

"""
test_fusion.py: suite of tests for marana.fusion 
the fusion module contains helper functions for binding pitch and rhythm
"""
import pytest

from abjadext.rmakers import rmakers
from abjad import Container, CyclicTuple, Duration, LeafMaker

from marana.fusion import make_basic_rhythm
from marana.parser import resolve_pitchselector
from marana.pitch import PitchData, PitchQuery, OctaveVoicing


@pytest.fixture
def bsn_pquery():
    """  
    this is the type of structure that our queries could use
    """
    myvoicing = OctaveVoicing(3, "horiz")
    return PitchQuery("partial", 1, myvoicing)

@pytest.fixture
def my_pitch_data():
    """
    pretty much the same as above, but now using a small class to structure the
    data
    """
    #######################################################################
    # data 
    #######################################################################
    harmonies = ["<e g a>",
                "<ef gf a>",
                "<df f a>",
                "<df gf bf>",
                "<df gf bf>"]
    roots = ["c", "d", "ef", "f", "gf", "a", "bf", "c", "df", "ef"]
    return PitchData(roots, harmonies)


@pytest.fixture
def voiced_pitches(bsn_pquery, my_pitch_data):
    return resolve_pitchselector(bsn_pquery, my_pitch_data)

@pytest.fixture
def cyclic_tuple(voiced_pitches):
    ctup = CyclicTuple(voiced_pitches)
    return ctup

@pytest.fixture
def bsn_talea():
    return rmakers.Talea(counts=[-1, 3, -1, 3, -1, 3], denominator=4)

@pytest.fixture
def time_signature_pairs():
    return [(4, 4), (4, 4), (4, 4)]


def test_make_basic_rhythm(bsn_talea, cyclic_tuple, time_signature_pairs):
    #maker = LeafMaker
    total_duration = sum(Duration(pair) for pair in time_signature_pairs)
    basic_music = make_basic_rhythm(time_signature_pairs, counts=bsn_talea.counts,
            denominator=bsn_talea.denominator) 
    assert isinstance(basic_music, Container) 
