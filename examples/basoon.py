#!/usr/bin/python3
"""
examples/basoon.py: an example of how we would script a real bassoon voice
using the marana library
"""
from marana.attachments import attach_dynamic_at_index
from marana.isorhythm import add_pitches
from marana.pitch import OctaveVoicing, PitchData, PitchQuery
from marana.parser import resolve_pitchselector, resolve_rhythmselector
from marana.rhythm import RhythmData, RhythmQuery
from marana.tools import strip_container

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

def create_rhythm_data_segment():
    """
    return a small class with structured rhythm data

    this will be specific to the voice at hand
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
    takes no args, returns a list of abjad.Container objects
    """
    pitch_data = create_pitch_data_segment()
    pquery_one = PitchQuery("partial", 4, OctaveVoicing(4, "horiz"))
    pquery_two = PitchQuery("partial", 3, OctaveVoicing(3, "horiz"))
    pquery_three = PitchQuery("partial", 2, OctaveVoicing(3, "horiz"))
    sel_one = resolve_pitchselector(pquery_one, pitch_data)
    sel_two = resolve_pitchselector(pquery_two, pitch_data)
    sel_three = resolve_pitchselector(pquery_three, pitch_data)
    lone = len(sel_one)
    ltwo = len(sel_two)
    lthree = len(sel_three)
    serror = "Will throw range error, try to make length of selections equal"
    assert lone == ltwo, serror
    assert lone == lthree, serror 
    assert ltwo == lthree, serror
    sel_matrix = [sel_one, sel_two, sel_three]
    rdata = create_rhythm_data_segment()
    rquery_one = RhythmQuery("talea") 
    music = []
    for i in range(0, lone):
        phrase = [sel_matrix[0][i], sel_matrix[1][i], sel_matrix[2][i]]
        basic_rhythm = resolve_rhythmselector(rquery_one, rdata)
        pitched_rhythm = add_pitches(basic_rhythm, phrase)
        music.append(pitched_rhythm)
    return music


def make_attachments(music_containers):
    """
    applies attachments to music 
    """
    for container in music_containers:
        attach_dynamic_at_index(container, "fp", 1)
        attach_dynamic_at_index(container, "fp", 3)
        attach_dynamic_at_index(container, "fp", 5)

def printf(container, name):
    """

    """
    fstr = strip_container(container)
    print(f"basoon_{name} = ", fstr)

def outputf(music_containers):
    """
    outputs music as formatted strings
    """
    print("\\version \"2.22.0\"")
    print("\\language \"english\"")
    print("\n")
    i = 0
    phrases = "abcdefghijk"
    for c in music_containers:
        printf(c, phrases[i])
        i += 1


if __name__ == '__main__':
    music = resolve_query_sequence()
    make_attachments(music)
    outputf(music)
