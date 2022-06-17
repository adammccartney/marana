#!/usr/bin/python3
"""
test_tools.py: some small unit tests to check that the tools for marana are
working as expected
"""
import pytest
import abjad
from abjad import Container, Dynamic, Voice, Staff

from marana.tools import ( 
                          get_registered_pitch,
                          create_pitch_map,
                          stringify_container, 
                          strip_container, 
                          strip_voice,
                          strip_staff, 
                          strip_braces
                          )


@pytest.fixture
def container():
    """  
    overengineered wrapper for abjad container
    """
    return Container("r4 c'2. r4 d'2. r4 e'2.")


def test_stringify_container_works_as_expected(container):
    """
    checks that strings coming out of this function are well formed
    """
    astr = stringify_container(container)
    assert isinstance(astr, str)
    assert astr == "r4 c'2. r4 d'2. r4 e'2."


def test_strip_voice(container):
    """
    tests that the string type returned from strip voice is formatted
    correctly
    """
    astr = stringify_container(container)
    voice = Voice(astr)
    dynamic = Dynamic("p")
    abjad.attach(dynamic, voice[1])
    sstr = strip_voice(voice)
    assert sstr == "{r4 c'2. \\p r4 d'2. r4 e'2.}"


def test_strip_staff(container):
    """
    tests that the string type returned from strip staff is formatted
    correctly
    """
    astr = stringify_container(container)
    staff = Staff(astr)
    dynamic = Dynamic("p")
    abjad.attach(dynamic, staff[1])
    sstr = strip_staff(staff)
    assert sstr == "{r4 c'2. \\p r4 d'2. r4 e'2.}"
    

def test_strip_container(container):
    """
    checks that we can get flat lilypond strings 
    """
    dynamic = Dynamic("f")
    abjad.attach(dynamic, container[3])
    sstr = strip_container(container)
    assert sstr == "{r4 c'2. r4 d'2. \\f r4 e'2.}"


def test_strip_braces_works():
    """
    checks that curley braces are stripped from beginning and end of string
    """
    f = "{a'}"
    assert strip_braces(f) == "a'" 


def test_strip_braces_rejects_malformed_start():
    """
    checks that function will only process strings with curley braces at
    beginning and end
    """
    f = "a'}"
    with pytest.raises(AssertionError) as excinfo:
        _ = strip_braces(f)
        assert "string to start with '{'" in str(excinfo)



def test_strip_braces_rejects_malformed_end():
    """
    checks that function will only process strings ending in curley braces
    """
    g = "{a'"
    with pytest.raises(AssertionError) as excinfo:
        _ = strip_braces(g)
        assert "string to end with '}'" in str(excinfo)

@pytest.fixture
def c():
    "life is simpler when you think in c"
    return "c"

def test_registered_pitch_works(c):
    """
    makes sure that our get registered pitch function creates the right
    transposition when it gets called and also returns a string with the
    correct form
    """
    x = get_registered_pitch(c, "2-2/3")
    assert x == "g'"


def test_registered_pitch_raises(c):
    """
    test our assertion is getting raised
    """
    with pytest.raises(AssertionError) as excinfo:
        _ = get_registered_pitch(c, "5-66")
        assert "Register not recognized" in str(excinfo)


@pytest.fixture
def roots():
    "life is simpler when you're connected to your roots"
    return ["c", "d", "e"]


def test_create_pitch_map(roots):
    """
    tests that a call to create pitch map returns a dict with the expected form
    """
    register = "2-2/3"  # fifth
    pitches = ["g'", "a'", "b'"]
    expected = ("fluteOne", pitches)
    assert create_pitch_map("fluteOne", roots, register) == expected




