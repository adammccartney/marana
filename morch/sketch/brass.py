#!/usr/bin/python3

"""
brass.py: script to generate a sketch for brass for the score morch (marana for
          orchestra). This script writes to stdout.

usage: python brass.py > brass.ly

"""

import abjad
from marana.tools import strip_voice
from collections import namedtuple
from typing import Callable

IYGH_PHRASES = {
    #######################################################################
    # data 
    #######################################################################
    "call_aa": "r8 bf8-. d'8 bf8 f2--",
    "call_ab": "r8 bf8-. g8 bf8 f2--",
    "call_ba": "r8 bf8-. a8 bf8 c'2--",
    "call_bb": "r8 f8-. bf8 c'8 d'2--",
    "call_bc": "r1",
    "resp_aa": "r2 r8 bf8-. d'8 bf8",
    "resp_ab": "f2-- r8 bf8-. g'8 bf8", 
    "resp_ba": "f2-- r8 bf8-. a8 bf8",
    "resp_bb": "c'2-- r8 f8-. bf8 c'8", 
    "resp_bc": "d'2-- r2", 
}

def create_voice(phrase: str, offset: int):
    """
    will create a new voice that is a tranposition of the old voice at an
    offset of n semitones
    """
    voice = abjad.Voice(phrase)
    abjad.mutate.transpose(voice, offset)
    return voice

def get_brass_section() -> dict:
    """  
    creates a dictionary of brass voices 
    """
    call_aa_octve = create_voice(IYGH_PHRASES["call_aa"], 12) # call aa up the octave
    call_ab_octve = create_voice(IYGH_PHRASES["call_ab"], 12) # call ab up the octave
    call_ba_octve = create_voice(IYGH_PHRASES["call_ba"], 12) # call ba up the octave
    call_bb_octve = create_voice(IYGH_PHRASES["call_bb"], 12) # call bb up the octave
    call_bc_octve = create_voice(IYGH_PHRASES["call_bc"], 12) # call bc up the octave
    call_aa = create_voice(IYGH_PHRASES["call_aa"], 0) # call aa
    call_ab = create_voice(IYGH_PHRASES["call_ab"], 0) # call ab
    call_ba = create_voice(IYGH_PHRASES["call_ba"], 0) # call ba
    call_bb = create_voice(IYGH_PHRASES["call_bb"], 0) # call bb
    call_bc = create_voice(IYGH_PHRASES["call_bc"], 0) # call bc
    call_aa_octvb = create_voice(IYGH_PHRASES["call_aa"], -12) # call aa octvb 
    call_ab_octvb = create_voice(IYGH_PHRASES["call_ab"], -12) # call ab octvb
    call_ba_octvb = create_voice(IYGH_PHRASES["call_ba"], -12) # call ba octvb
    call_bb_octvb = create_voice(IYGH_PHRASES["call_bb"], -12) # call bb octvb
    call_bc_octvb = create_voice(IYGH_PHRASES["call_bc"], -12) # call bc octvb
    resp_aa_octve = create_voice(IYGH_PHRASES["resp_aa"], 12) # response up oct
    resp_ab_octve = create_voice(IYGH_PHRASES["resp_ab"], 12) # response up oct
    resp_ba_octve = create_voice(IYGH_PHRASES["resp_ba"], 12) # response up oct
    resp_bb_octve = create_voice(IYGH_PHRASES["resp_bb"], 12) # response up oct
    resp_bc_octve = create_voice(IYGH_PHRASES["resp_bc"], 12) # response up oct
    resp_aa = create_voice(IYGH_PHRASES["resp_aa"], 0) # response up oct
    resp_ab = create_voice(IYGH_PHRASES["resp_ab"], 0) # response at pitch
    resp_ba = create_voice(IYGH_PHRASES["resp_ba"], 0) # response at pitch
    resp_bb = create_voice(IYGH_PHRASES["resp_bb"], 0) # response at pitch
    resp_bc = create_voice(IYGH_PHRASES["resp_bc"], 0) # response at pitch
    resp_aa_octvb = create_voice(IYGH_PHRASES["resp_aa"], -12) # response down oct
    resp_ab_octvb = create_voice(IYGH_PHRASES["resp_ab"], -12) # response down oct
    resp_ba_octvb = create_voice(IYGH_PHRASES["resp_ba"], -12) # response down oct
    resp_bb_octvb = create_voice(IYGH_PHRASES["resp_bb"], -12) # response down oct
    resp_bc_octvb = create_voice(IYGH_PHRASES["resp_bc"], -12) # response down oct

    brass = {
            "trpOneTwo": {
                "call_aa": call_aa_octve, 
                "call_ab": call_ab_octve,
                "call_ba": call_ba_octve,
                "call_bb": call_bb_octve,
                "call_bc": call_bc_octve
                },
            "trpThree": {
                "call_aa": call_aa, 
                "call_ab": call_ab,
                "call_ba": call_ba,
                "call_bb": call_bb,
                "call_bc": call_bc
                },
            "hrnOneTwo": {
                "resp_aa": resp_aa_octve, 
                "resp_ab": resp_ab_octve,
                "resp_ba": resp_ba_octve,
                "resp_bb": resp_bb_octve,
                "resp_bc": resp_bc_octve
                },
            "hrnThreeFour": {
                "resp_aa": resp_aa, 
                "resp_ab": resp_ab,
                "resp_ba": resp_ba,
                "resp_bb": resp_bb,
                "resp_bc": resp_bc
                },
            "tuba": {
                "resp_aa": resp_aa_octvb, 
                "resp_ab": resp_ab_octvb,
                "resp_ba": resp_ba_octvb,
                "resp_bb": resp_bb_octvb,
                "resp_bc": resp_bc_octvb
                },
            "trbOneTwo": {
                "call_aa": call_aa,
                "call_ab": call_ab,
                "call_ba": call_ba,
                "call_bb": call_bb,
                "call_bc": call_bc
                },
            "btrb": {
                "call_aa_octvb": call_aa_octvb,
                "call_ab_octvb": call_ab_octvb,
                "call_ba_octvb": call_ba_octvb,
                "call_bb_octvb": call_bb_octvb,
                "call_bc_octvb": call_bc_octvb
                }
            }
    return brass


NamedVoice = namedtuple("NamedVoice", ['voice', 'name', 'parent'])

def get_named_voices(group: dict, instrument: str) -> list[NamedVoice]:
    """
    returns a list of NamedVoice tuples 
    """
    voices = group[instrument] 
    keys = voices.keys()
    names = [instrument + "_" + k for k in keys]
    namedvoices = []
    for k, n in zip(keys, names):
        namedvoice = NamedVoice(voices[k], n, instrument)
        namedvoices.append(namedvoice)
    return namedvoices


def printf(voice, name):
    """
    prints a voice with name
    """
    fstr = strip_voice(voice)
    print(f"{name} = ", fstr)


def outputheader():
    print("\\version \"2.22.0\"")
    print("\\language \"english\"")


def outputf(namedvoices: list[NamedVoice]) -> None:
    """
    outputs the lilypond voices for segment
    writes to stdout
    """
    print("\n")
    print(f"%% {namedvoices[0].parent}")
    print("%%" * 28)

    for nv in namedvoices:
        printf(nv.voice, nv.name)


def output_aggregate_voice(namedvoices: list[NamedVoice], segment: str) -> None:
    """
    creates a context voice for the voices in the namedvoices list
    writes the format string to stdout
    """
    print("\n")
    parent = namedvoices[0].parent
    padding = " " * 4
    print(f"{parent}_{segment} = {{")
    for nv in namedvoices:
        print(f"{padding}\\{nv.name}")
    print("}")
    print("%%" * 28)


def generate_chunk(sectionGetter: Callable[[], dict] , 
                   instruments: list[str], 
                   segment: str) -> None:
    """
    Wrapper function,
    first gets an instrumental section (a tree of instruments and the music
    they play), then iterates over the array of instrument names and creates
    lilypond musical output based on the values stored in the section tree

    writes to stdout
    """
    section = sectionGetter()
    for i in instruments:
        nvoice = get_named_voices(section, i)
        outputf(nvoice)
        output_aggregate_voice(nvoice, segment)


if __name__ == '__main__':
    outputheader()
    instruments = ["hrnOneTwo", "hrnThreeFour", "trpOneTwo", "trpThree",
                   "trbOneTwo", "btrb", "tuba"]
    segment = "verseOne"
    generate_chunk(get_brass_section, instruments, segment)
