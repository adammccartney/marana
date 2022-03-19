#!/usr/bin/python3
"""
examples/hrn3.py: and isorhythmic module for horn
"""
from marana.attachments import attach_dynamic_at_index, attach_tie
from marana.isorhythm import add_pitches
from marana.pitch import OctaveVoicing, PitchQuery
from marana.parser import resolve_pitchselector, resolve_rhythmselector
from marana.rhythm import RhythmData, RhythmQuery
from marana.tools import strip_container

from pitchdata import create_pitch_data_segment

def create_rhythm_data_segment():
    """
    return a small class with structured rhythm data

    this will be specific to the voice at hand
    """
    #######################################################################
    # data 
    #######################################################################
    lcounts = [-4, -1, 1, 2, 4, -1, 1, 2, 4, -4]
    tspairs = [(4, 4)] * 3
    ldenominator = 8
    rdata = RhythmData(counts=lcounts, denominator=ldenominator, 
                       time_signature_pairs=tspairs)
    return rdata


def resolve_query_sequence():
    """
    an example routine to show how we could resolve a sequence of pitch queries 
    takes no args, returns a list of abjad.Container objects
    """
    pitch_data = create_pitch_data_segment()
    pquery_one = PitchQuery("partial", 1, OctaveVoicing(3, "horiz"))
    sel_one = resolve_pitchselector(pquery_one, pitch_data)
    lone = len(sel_one)
    sel_matrix = [sel_one]
    rdata = create_rhythm_data_segment()
    rquery_one = RhythmQuery("talea") 
    music = []
    for i in range(0, lone):
        phrase = [sel_matrix[0][i]]
        basic_rhythm = resolve_rhythmselector(rquery_one, rdata)
        pitched_rhythm = add_pitches(basic_rhythm, phrase)
        music.append(pitched_rhythm)
    return music


def make_attachments(music_containers):
    """git merge exclude one directorygit merge exclude one directory
    applies attachments to music 
    """
    for container in music_containers:
        attach_dynamic_at_index(container, "pp", 2)
        attach_tie(container, 3)
        attach_dynamic_at_index(container, "pp", 6)
        attach_tie(container, 7)

def printf(container, name):
    """

    """
    fstr = strip_container(container)
    print(f"hrnthree_{name} = ", fstr)

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
