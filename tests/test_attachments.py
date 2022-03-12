#!/usr/bin/python3
"""
test_tools.py: some small unit tests to check that the tools for marana are
working as expected
"""
import pytest
from abjad import Container, Dynamic, Voice, Staff

from marana.attachments import attach_dynamic_at_index, attach_hairpin
from marana.tools import strip_container

@pytest.fixture
def container():
    """    
    overengineered wrapper for abjad container
    """
    return Container("r4 c'2. r4 d'2. r4 e'2.")


def test_attach_dynamic_at_index(container):
    attach_dynamic_at_index(container, "p", 1)
    formatted = strip_container(container)
    assert formatted == "{r4 c'2. \\p r4 d'2. r4 e'2.}"


def test_attach_hairpin_three_part(container):
    attach_hairpin(container, "p < f")
    formatted = strip_container(container)
    assert formatted == "{r4 \\p \\< c'2. r4 d'2. r4 e'2. \\f}"


def test_attach_hairpin_two_part(container):
    attach_hairpin(container, "< !")
    formatted = strip_container(container)
    assert formatted == "{r4 \\< c'2. r4 d'2. r4 e'2. \\!}"

