import abjad
import pytest

from marana.parser import (make_octave_voicings,
                           parse_args,
                           resolve_pitch, 
                           resolve_pitchselector,
                           voice_pitchclasses)


from marana.pitch import (ChordTone, 
                          PcSegTuple,
                          OctaveVoicing,
                          Partial,
                          PartialType, 
                          PitchData,
                          PitchFunAttrs, 
                          PitchQuery,
                          PitchToken,
                          make_pitch_tuples, 
                          make_pitchclass_segments)


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



def test_pitchfunattrs_raises():
    """
    Tests that PitchFunAttrs raises value error when it does not know how to
    resolve the PitchToken
    """
    with pytest.raises(ValueError) as excinfo:
        PitchFunAttrs(PitchToken, ("a b c", 1), 4)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Unknown pitch function type requested"

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


def test_make_pitchclass_segments(ptups):
    """
    returns a list of pitchclass segments given a list of pitch tuples
    """
    pcdatasegs = make_pitchclass_segments(ptups)
    assert isinstance(pcdatasegs[0], PcSegTuple)


@pytest.fixture
def pcdatasegs(ptups):
    """returns a list of pitchclass segments"""
    return make_pitchclass_segments(ptups)

def test_parse_args_forms_list(pcdatasegs):
    """Test that parse args returns a well formed list"""
    tones = parse_args(PitchToken.PARTIAL, 3, pcdatasegs)
    assert len(tones) == 10


@pytest.fixture
def eminsus4():
    """eminor chordtone object with selector at index 1"""
    return ChordTone("e g a", 1) 

def test_parse_args_selects_chordtone(pcdatasegs, eminsus4):
    """
    the parse args function returns a list of ChordTones, 
    singular chord tones selected from an
    array of harmonies
    """
    tones = parse_args(PitchToken.CHORDTONE, 1, pcdatasegs)
    assert isinstance(tones[0], ChordTone)
    assert tones[0].selector == eminsus4.selector
    assert tones[0].pcseg == eminsus4.pcseg

@pytest.fixture
def c_third_partial():
    """fixture for creating the third partial above an ef"""
    return Partial("c", PartialType.F3) 

def test_parse_args(pcdatasegs, c_third_partial):
    """
    checks that the partials being returned from our list are well formed and
    of the correct type
    """
    tones = parse_args(PitchToken.PARTIAL, 3, pcdatasegs)
    assert isinstance(tones[0], Partial)
    assert tones[0].pcseg == c_third_partial.pcseg

@pytest.fixture
def octaves():
    """list of octaves to voice pitchclasses"""
    return [5] * 10

@pytest.fixture
def orders():
    """resolution order for octave voicings"""
    return ["horiz", "vert"] * 5

def test_octave_voicings(octaves, orders):
    """this should return a list of tuples"""
    ovoicings = make_octave_voicings(octaves, orders) 
    assert isinstance(ovoicings[0], OctaveVoicing)


@pytest.fixture
def ovoicings():
    """create an octave voicing list for use with test_voice_pitchclasses"""
    octaves = [4] * 10
    orders = ["horiz"] * 10
    return make_octave_voicings(octaves, orders)

@pytest.fixture
def d_thirdpartial():
    return Partial("d", PartialType.F3)

@pytest.fixture
def omiddle():
    return OctaveVoicing(4, "vert")

def test_resolve_pitch_for_partial(d_thirdpartial, omiddle):
    res_seg = resolve_pitch(d_thirdpartial.pcseg, omiddle)
    assert isinstance(res_seg, abjad.PitchSegment) 
    assert res_seg == abjad.PitchSegment("a'")


@pytest.fixture
def d_min():
    """fixture for a dminor chord, selector at index 1"""
    return ChordTone("d f a", 1)

def test_chord_tone_resolution_is_ok(d_min):
    """
    check that the the resolution method of the ChordTone class selects the
    correct chord tone
    """
    assert d_min.pcseg == abjad.PitchClassSegment("f")

@pytest.fixture
def fattrs():
    """fixture for testing pitch function attributes"""
    attrs = PitchFunAttrs(PitchToken.CHORDTONE, ("f a c", 1), 5)
    return attrs

def test_resolve_pitch_for_chord_tone(fattrs, omiddle):
    """
    pitch function attributes are useful for passing to resolve pitch
    function
    """
    pcseg = fattrs.args.pcseg
    res_seg = resolve_pitch(pcseg, omiddle)
    assert res_seg == abjad.PitchSegment("a'")


@pytest.fixture
def my_single_pquery():
    """  
    this is the type of structure that our queries could use
    """
    myvoicing = OctaveVoicing(4, "horiz")
    return PitchQuery("chordtone", 1, myvoicing)

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


def test_resolve_pitchselector_returns_chordtones(my_single_pquery, my_pitch_data):
    """
    currently this function is essentially returning nearly a full set of
    possible pitches from a query
    """
    pitch_segments = resolve_pitchselector(my_single_pquery, my_pitch_data)
    assert len(pitch_segments) == len(my_pitch_data.roots)
    assert isinstance(pitch_segments[0], abjad.PitchSegment)
    assert pitch_segments[0] == abjad.PitchSegment("g'")

@pytest.fixture
def my_partial_pquery():
    """
    construct a query that will be used to construct a set of harmonic
    overtones
    """
    myvoicing = OctaveVoicing(5, "horiz")
    return PitchQuery("partial", 5, myvoicing)


def test_resolve_pitchselector_returns_partials(my_partial_pquery,
        my_pitch_data):
    """
    this tests that our query works as expected when trying to form a set of
    partials over a given range of pitch class data segments
    """
    voiced_pitches = resolve_pitchselector(my_partial_pquery, my_pitch_data)
    assert voiced_pitches[2] == abjad.PitchSegment("g''")
