#!/usr/bin/python3
"""
marana.attachments: methods for handling attachments of dynamic and markup info 
"""
from abjad import attach, hairpin, Container, Dynamic


def attach_dynamic_at_index(container: Container, dynamic: str, index: int) -> None:
    """
    Creates a dynamic in the form of an abjad.Dynamic and attaches it to the
    container at index

    modifies the contents of container
    """
    dyn = Dynamic(dynamic)
    attach(dyn, container[index])


def attach_hairpin(container: Container, descriptor: str) -> None:
    """
    Attaches a hairpin spanner to the container

    modifies the contents of container
    """
    hairpin(descriptor, container[:])
