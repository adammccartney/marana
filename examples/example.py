#!/usr/bin/python3
from marana.isorhythm import add_pitches
from marana.pitch import OctaveVoicing, PitchData, PitchQuery
from marana.parser import resolve_pitchselector, resolve_rhythmselector
from marana.rhythm import RhythmData, RhythmQuery

def create_pitch_data_segment():
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

def create_rhythm_data_segment():
    """
    return a small class with structured rhythm data
    """
    #######################################################################
    # data 
    #######################################################################
    lcounts = [-1, 3] * 3
    tspairs = [(4, 4)] * 3
    ldenominator = 4
    rdata = RhythmData(counts=lcounts, denominator=ldenominator, 
                       time_signature_pairs=tspairs)
    return rdata

def resolve_query_sequence():
    """
    an example routine to show how we could resolve a sequence of pitch queries 
    takes no args
    returns a sequence of pitch segments 
    """
    pitch_data = create_pitch_data_segment()
    pquery_one = PitchQuery("chordtone", 1, OctaveVoicing(4, "horiz"))
    pitch_selection = resolve_pitchselector(pquery_one, pitch_data)
    rdata = create_rhythm_data_segment()
    rquery_one = RhythmQuery("talea") 
    basic_rhythm = resolve_rhythmselector(rquery_one, rdata)
    pitched_rhythm = add_pitches(basic_rhythm, pitch_selection[:3])
    return pitched_rhythm


