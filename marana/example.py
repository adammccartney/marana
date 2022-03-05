#!/usr/bin/python3
from marana.pitch import OctaveVoicing, PitchData, PitchQuery
from marana.parser import resolve_pitchselector

def segment_pitch_data():
    """
    return a small class with structured pitch data
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


def resolve_query_sequence():
    """
    an example routine to show how we could resolve a sequence of pitch queries 
    takes no args
    returns a sequence of pitch segments 
    """
    pitch_data = segment_pitch_data()
    query_one = PitchQuery("chordtone", 1, OctaveVoicing(4, "horiz"))
    pitch_segments = resolve_pitchselector(query_one, pitch_data)
    # TODO: implement a routine here to assign rhythmic data
    return pitch_segments


