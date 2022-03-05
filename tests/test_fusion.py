#!/usr/bin/python3

"""
test_fusion.py: suite of tests for marana.fusion 
the fusion module contains helper functions for binding pitch and rhythm
"""
import pytest

import abjad
from abjadext.rmakers import rmakers
from abjad import Container, CyclicTuple, Duration, LeafMaker

from marana.fusion import add_pitches, make_basic_rhythm
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
    """
    returns a list of namedtuple("PitchSegTuple", "root", "harmony")
    """
    return resolve_pitchselector(bsn_pquery, my_pitch_data)

@pytest.fixture
def cyclic_tuple(voiced_pitches):
    """
    cyclic tuple is an abjad class that has many of the same features of a
    normal touple, but allows for repeated cycling (as is commonly required in
            music)
    """
    ctup = CyclicTuple(voiced_pitches)
    return ctup

@pytest.fixture
def bsn_talea():
    """
    talea is the brains of the operation in terms of rhythm - it contains the
    pattern of rests and sounding notes that are used to articulate the music
    """
    return rmakers.Talea(counts=[-1, 3] * 3, denominator=4)

@pytest.fixture
def time_signature_pairs():
    """
    this is used to determine the duration in time of the musical segment we
    are creating 
    """
    return [(4, 4)] * 3


def test_make_basic_rhythm(bsn_talea, time_signature_pairs):
    """
    simple test that shows make basic rhythm returns a usable container
    """
    basic_music = make_basic_rhythm(time_signature_pairs, counts=bsn_talea.counts,
            denominator=bsn_talea.denominator) 
    assert isinstance(basic_music, Container) 
    assert str(basic_music[1]) == "c'2."
    assert str(basic_music[2]) == "r4"
    assert str(basic_music[3]) == "c'2."
    assert str(basic_music[3]) == "c'2." 
    assert str(basic_music[4]) == "r4"
    assert str(basic_music[5]) == "c'2." 

@pytest.fixture
def music(bsn_talea, time_signature_pairs):
    """
    more or less wraps the previous test into a fixture
    """
    return make_basic_rhythm(time_signature_pairs, counts=bsn_talea.counts,
            denominator=bsn_talea.denominator)

def test_make_pitches_returns_container(music, voiced_pitches):
    """
    tests that our function constructs a meaningful abjad Container
    """
    pitch_selection = voiced_pitches[:3]
    new_music = add_pitches(music, pitch_selection)
    assert isinstance(new_music, Container)
    assert str(new_music[1]) == "c2." 
    assert str(new_music[2]) == "r4"
    assert str(new_music[3]) == "d2." 
    assert str(new_music[4]) == "r4"
    assert str(new_music[5]) == "ef2." 
