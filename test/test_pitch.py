#!/usr/bin/python3

# test.py

import abjad
import pytest

from material.pitch import ( make_pitch_tuples, 
                    make_pitchclass_segments,
                    make_pitch_segments,
                    PitchTuple, 
                    strip )

@pytest.fixture
def harmonies():
    harmonies = ["<e'' g'' a''>",
                "<ef'' gf'' a''>",
                "<df'' f'' a''>",
                "<df'' gf'' bf''>",
                "<df'' gf'' bf''>"]
    return harmonies

@pytest.fixture
def roots():
    roots = ["c", "d", "ef", "f", "gf", "a", "bf", "c'", "df'", "ef'"]
    return roots


@pytest.fixture
def eroots(roots):
    eroots = [r for r in roots[1::2]]
    return eroots


@pytest.fixture
def oroots(roots):
    oroots = [r for r in roots[::2]]
    return oroots

def test_roots_slices_are_equal(eroots, oroots):
    assert len(oroots) == len(eroots) 


def test_roots_slices_are_well_formed(eroots, oroots):
    assert eroots[0] == "d"
    assert oroots == ["c", "ef", "gf", "bf", "df'"]


@pytest.fixture
def ptups(roots, harmonies):
    return make_pitch_tuples(roots, harmonies)

def test_make_pitch_tuples_returns_list_len_correct(roots, harmonies, ptups):
    assert len(ptups) == len(roots)
    assert len(ptups) == len(harmonies) * 2


@pytest.fixture
def ef_ptup(ptups):
    return ptups[2]

def test_ptups_are_well_formed(ptups, ef_ptup):
    assert ptups[1].root == "d"
    raw = PitchTuple("ef", "<ef'' gf'' a''>")
    assert ef_ptup.root == raw.root
    assert ef_ptup.harmony == raw.harmony


def test_strip_removes_hairpins():
    assert strip("<a b c>") == "a b c"

@pytest.fixture
def df_pseg():
    return abjad.PitchSegment("df'' f'' a''")

@pytest.fixture
def f_pseg():
    return abjad.PitchSegment("f")

def test_make_pitch_segments_creates_well_formed(ptups, f_pseg, df_pseg):
    psegs = make_pitch_segments(ptups)
    df_computed = psegs[4].harmony
    f_computed = psegs[3].root
    assert df_computed == df_pseg
    assert f_computed == f_pseg


@pytest.fixture
def df_pcseg():
    return abjad.PitchClassSegment("df'' f'' a''")

@pytest.fixture
def f_pcseg():
    return abjad.PitchClassSegment("f")

def test_make_pitchclass_segments_created_well(ptups, f_pcseg, df_pcseg):
    pcsegs = make_pitchclass_segments(ptups)
    df_computed = pcsegs[4].harmony
    f_computed = pcsegs[3].root
    assert df_computed == df_pcseg
    assert f_computed == f_pcseg
