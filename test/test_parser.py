import abjad
import pytest

from material.parser import (Partial,
                             PartialType, 
                             PitchFunAttrs, 
                             PitchFunction, 
                             PitchFunType,
                             res_partial_pseg)


def test_partial_type_values_are_correct():
    assert PartialType.F1.value == 1
    assert PartialType.F2.value == 2
    assert PartialType.F3.value == 3
    assert PartialType.F4.value == 4
    assert PartialType.F5.value == 5
    assert PartialType.F6.value == 6
    assert PartialType.F7.value == 7
    assert PartialType.F8.value == 8
    assert PartialType.F9.value == 9
    assert PartialType.F10.value == 10
    assert PartialType.F11.value == 11
    assert PartialType.F12.value == 12
    assert PartialType.F13.value == 13
    assert PartialType.F14.value == 14
    assert PartialType.F15.value == 15
    assert PartialType.F16.value == 16
    assert PartialType.F17.value == 17
    assert PartialType.F18.value == 18
    assert PartialType.F19.value == 19
    assert PartialType.F20.value == 20

@pytest.fixture
def pc_c():
    return "c"

@pytest.fixture
def c_octaves(pc_c):
    octaves = []
    octaves.append(Partial(pc_c))
    octaves.append(Partial(pc_c, PartialType.F2))
    octaves.append(Partial(pc_c, PartialType.F4))
    octaves.append(Partial(pc_c, PartialType.F8))
    octaves.append(Partial(pc_c, PartialType.F16))
    for o in octaves:
        print(o.pcseg)
    return octaves


def test_parial_understands_octaves(c_octaves):
    for o in c_octaves:
        assert o.pcseg == abjad.PitchClassSegment("c")

@pytest.fixture
def d_fifths():
    fifths = []
    fifths.append(Partial("d", PartialType.F3))
    fifths.append(Partial("d", PartialType.F6))
    fifths.append(Partial("d", PartialType.F12))
    return fifths

def test_partial_understands_fifths(d_fifths):
    for f in d_fifths:
        assert f.pcseg == abjad.PitchClassSegment("a")

@pytest.fixture
def e_thirds():
    thirds = []
    thirds.append(Partial("e", PartialType.F5))
    thirds.append(Partial("e", PartialType.F10))
    thirds.append(Partial("e", PartialType.F20))
    return thirds

def test_partial_understands_thirds(e_thirds):
    for t in e_thirds:
        assert t.pcseg == abjad.PitchClassSegment("gs")

@pytest.fixture
def f_sevenths():
    sevenths = []
    sevenths.append(Partial("f", PartialType.F7))
    sevenths.append(Partial("f", PartialType.F14))
    return sevenths

def test_partial_understands_thirds(f_sevenths):
    for s in f_sevenths:
        assert s.pcseg == abjad.PitchClassSegment("dqs")


@pytest.fixture
def g_ninths():
    ninths = []
    ninths.append(Partial("g", PartialType.F9))
    ninths.append(Partial("g", PartialType.F18))
    return ninths

def test_partial_understands_ninths(g_ninths):
    for n in g_ninths:
        assert n.pcseg == abjad.PitchClassSegment("a")


@pytest.fixture
def c_11():
    return Partial("c", PartialType.F11)

@pytest.fixture
def c_13():
    return Partial("c", PartialType.F13)

@pytest.fixture
def c_15():
    return Partial("c", PartialType.F15)

@pytest.fixture
def c_17():
    return Partial("c", PartialType.F17)

@pytest.fixture
def c_19():
    return Partial("c", PartialType.F19)

def test_partial_understands_singletons(c_11, c_13, c_15, c_17, c_19):
    assert c_11.pcseg == abjad.PitchClassSegment("fqs")
    assert c_13.pcseg == abjad.PitchClassSegment("aqf")
    assert c_15.pcseg == abjad.PitchClassSegment("b")
    assert c_17.pcseg == abjad.PitchClassSegment("df")
    assert c_19.pcseg == abjad.PitchClassSegment("ef")

@pytest.fixture
def cattrs():
    attrs = PitchFunAttrs(PitchFunType.PARTIAL, ("c", PartialType.F3), 5)
    return attrs

def test_resolve_pitch_segment(cattrs):
    res_seg = res_partial_pseg(cattrs.args, cattrs.octave)
    assert res_seg == abjad.PitchSegment("g''")

