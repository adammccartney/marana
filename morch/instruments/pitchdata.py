#!/usr/bin/python3
"""
instruments/pitchdata.py: this module contains data that is common to all
                          instruments
"""
from marana.pitch import PitchData

def create_pitch_data_segment():
    """
    return a small class with structured pitch data

    this is something that will likely be common across all scripts that use it
    within the context of a single segment of a piece
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

