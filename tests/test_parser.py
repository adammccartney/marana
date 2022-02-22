import abjad
import pytest

from abc import ABC

from material.parser import (ChordTone,
                             parse_args,
                             parse_input,
                             parse_pselector,
                             Partial,
                             PartialType, 
                             Pitch,
                             PitchFunAttrs, 
                             PitchFunType,
                             resolve_pitch)


from material.pitch import (PitchTuple, 
                            make_pitch_tuples, 
                            make_pitch_segments,
                            make_pitchclass_segments,
                            strip,
                            )


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

def test_partial_understands_sevenths(f_sevenths):
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
def par_default():
    return Partial("c")

def test_partial_returns_correct_default(par_default):
    assert par_default.pcseg == abjad.PitchClassSegment("c")

@pytest.fixture
def cattrs():
    attrs = PitchFunAttrs(PitchFunType.PARTIAL, ("c", PartialType.F3), 5)
    return attrs

def test_resolve_pitch_for_partial(cattrs):
    res_seg = resolve_pitch(cattrs)
    assert res_seg == abjad.PitchSegment("g''")


@pytest.fixture
def d_min():
    return ChordTone("d f a", 1)

def test_chord_tone_resolution_is_ok(d_min):
    assert d_min.pcseg == abjad.PitchClassSegment("f")

@pytest.fixture
def fattrs():
    attrs = PitchFunAttrs(PitchFunType.CHORDTONE, ("f a c", 1), 5)
    return attrs

def test_resolve_pitch_for_chord_tone(fattrs):
    res_seg = resolve_pitch(fattrs)
    assert res_seg == abjad.PitchSegment("a''")


@pytest.fixture
def bad_attrs():
    attrs = PitchFunAttrs(PitchFunType.CHORDTONE, ("a b c", 4), 3)
    return attrs

def test_chordtone_raises(bad_attrs):
    """Test ChordTone raises index error when asked for a tone out of range""" 
    with pytest.raises(IndexError) as excinfo:
        resolve_pitch(bad_attrs)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Requested index out of range"


def test_pitchfunattrs_raises():
    """
    Tests that PitchFunAttrs raises value error when it does not know how to
    resolve the PitchFunType
    """
    with pytest.raises(ValueError) as excinfo:
        PitchFunAttrs(PitchFunType, ("a b c", 1), 4)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Unknown pitch function type requested"


@pytest.fixture
def mbad_attrs():
    return PitchFunAttrs(PitchFunType.PARTIAL, ("a", PartialType.F3), 4)

def test_resolve_pitch_raises(mbad_attrs):
    """
    tests that resolve pitch raises a ValueError if no pitch is defined
    """
    with pytest.raises(AssertionError) as excinfo:
        resolve_pitch(mbad_attrs, direction="bad")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "direction should be vert or horiz"

def test_resolve_pitch_horiz(mbad_attrs):
    """tests that horizontal resoultion works"""
    res_seg = resolve_pitch(mbad_attrs, direction="horiz")
    assert res_seg == abjad.PitchSegment("e'")


@pytest.fixture
def input():
    return (({ 'selector': ({'token_type': "partial",
                        'attributes': {'args': ("root"), 'octave': 4}},
                       {'token_type': "chordtone",
                        'attributes': {'args': (2), 'octave': 4}}),
               'voicing': 'vert'}),
            ({ 'selector': ({'token_type': "partial",
                       'attributes': ("root"), 'octave': 4},
                      {'token_type': "chordtone",
                       'attributes': {'args': (2), 'octave': 4}}),
               'voicing': 'horiz' }))

def test_parse_input_reads_tree(input):
    assert parse_input(input) == 2


@pytest.fixture
def pselector():
    return ({'token_type': "partial",
                        'attributes': {'args': ("root"), 'octave': 4}},
                       {'token_type': "chordtone",
                        'attributes': {'args': (2), 'octave': 4}})


def test_parse_pselector(pselector):
    """pselector is correct type"""
    assert parse_pselector(pselector) == 2


def test_parse_pselector_reads_dict(pselector):
    """dictionary keys are correct"""
    for ps in pselector:
        for k in ps.keys():
            assert k in {"token_type", "attributes"}


@pytest.fixture
def pdata():
    """test data segment with harmonies and root pitches as lilypond strings"""
    #######################################################################
    # data 
    #######################################################################
    harmonies = ["<e g a>",
                "<ef gf a>",
                "<df f a>",
                "<df gf bf>",
                "<df gf bf>"]

    roots = ["c", "d", "ef", "f", "gf", "a", "bf", "c", "df", "ef"]
    return (roots, harmonies)



@pytest.fixture
def ptups(pdata):
    """returns a list of pitchtuples"""
    return make_pitch_tuples(pdata[0], pdata[1])

@pytest.fixture
def pcsegs(ptups):
    """returns a list of pitchclass segments"""
    return make_pitchclass_segments(ptups)

def test_parse_args_forms_list(pcsegs):
    """Test that parse args returns a well formed list"""
    tones = parse_args((1,), pcsegs)
    assert len(tones) == 10



