#!/usr/bin/python3
"""
test_tools.py: some small unit tests to check that the tools for marana are
working as expected
"""
import pytest
import abjad
from abjad import Container, Dynamic, Voice, Staff

from marana.tools import stringify_container, strip_container, strip_voice, strip_staff


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
