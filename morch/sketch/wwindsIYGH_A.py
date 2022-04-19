#!/usr/bin/python3

"""
wwindsIYGH_A.py: script to generate a segment for the woodwinds

usage: python3 wwindsIYGH_A.py > wwindsIYGH_A.ly
"""
import abjad
from marana.tools import strip_voice
from collections import namedtuple
from typing import Callable


CALLS = ["r8 bf8 d'8-. bf8 f2--",
         "r8 bf8 g8-. bf8 f2--",
         "r8 bf8 a8-. bf8 c'2--",
         "r8 f8 bf8-. c'8 d'2--",
         "r1"]

RESPS = ["r2 r8 bf8-. d'8 bf8",
         "f2-- r8 bf8-. g'8 bf8", 
         "f2-- r8 bf8-. a8 bf8",
         "c'2-- r8 f8-. bf8 c'8", 
         "d'2-- r2"]


ORNAMENT = ["r8 \\tuplet 3/2 { fs''16 g'' a'' } bf''2.:16",
            "ef''4:16 fs''4:16 g''2:16",
            "r1",
            "r8 \\tuplet 3/2 {ef''16 fs'' g''} a''2.:16",
            "r8 f''4:16 g''4:16 a''4:16"]


MELODY = ["r4 fs'2 r4",
          "bf'2 r4 f'4",
          "r4 d'2 r4",
          "bf2 r2",
          "bf2 r2"]


DESC_CHORUS = ["r1",
               "r1",
               "r1",
               "r1",
               """\\tuplet 5/4 {bf''8 a''8 g''8 fs''8 ef''8 }
                  \\tuplet 5/4 { d''8 c''8 bf'8 a'8 g'8 }"""]


IYGH_PHRASES = {
    #######################################################################
    # data 
    #######################################################################
    "call_aa": ORNAMENT[0],
    "call_ab": ORNAMENT[1],
    "call_ba": ORNAMENT[2],
    "call_bb": ORNAMENT[3],
    "call_bc": ORNAMENT[4],
    "resp_aa": MELODY[0],
    "resp_ab": MELODY[1],
    "resp_ba": MELODY[2],
    "resp_bb": MELODY[3],
    "resp_bc": MELODY[4],
    "chorus_aa": DESC_CHORUS[0],
    "chorus_ab": DESC_CHORUS[1],
    "chorus_ac": DESC_CHORUS[2],
    "chorus_ad": DESC_CHORUS[3],
    "chorus_ae": DESC_CHORUS[4],
    }
    



def create_voice(phrase: str, offset: int):
    """
    will create a new voice that is a tranposition of the old voice at an
    offset of n semitones
    """
    voice = abjad.Voice(phrase)
    abjad.mutate.transpose(voice, offset)
    return voice

def get_wwind_section() -> dict:
    """  
    creates a dictionary of woodwind voices 
    """
    call_aa = create_voice(IYGH_PHRASES["call_aa"], 0) # call aa
    call_ab = create_voice(IYGH_PHRASES["call_ab"], 0) # call ab
    call_ba = create_voice(IYGH_PHRASES["call_ba"], 0) # call ba
    call_bb = create_voice(IYGH_PHRASES["call_bb"], 0) # call bb
    call_bc = create_voice(IYGH_PHRASES["call_bc"], 0) # call bc
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
    chorus_aa = create_voice(IYGH_PHRASES["chorus_aa"], 0) # chorus 
    chorus_ab = create_voice(IYGH_PHRASES["chorus_ab"], 0) # chorus 
    chorus_ac = create_voice(IYGH_PHRASES["chorus_ac"], 0) # chorus 
    chorus_ad = create_voice(IYGH_PHRASES["chorus_ad"], 0) # chorus 
    chorus_ae = create_voice(IYGH_PHRASES["chorus_ae"], 0) # chorus 
    chorus_aa_octvb = create_voice(IYGH_PHRASES["chorus_aa"], -12) # chorus down the octave
    chorus_ab_octvb = create_voice(IYGH_PHRASES["chorus_ab"], -12) # chorus down the octave
    chorus_ac_octvb = create_voice(IYGH_PHRASES["chorus_ac"], -12) # chorus down the octave
    chorus_ad_octvb = create_voice(IYGH_PHRASES["chorus_ad"], -12) # chorus down the octave
    chorus_ae_octvb = create_voice(IYGH_PHRASES["chorus_ae"], -12) # chorus down the octave


    wwinds = {
            "flOneTwo": {
                "call_aa": call_aa, 
                "call_ab": call_ab,
                "call_ba": call_ba,
                "call_bb": call_bb,
                "call_bc": call_bc,
                "chorus_aa": chorus_aa,
                "chorus_ab": chorus_ab,
                "chorus_ac": chorus_ac,
                "chorus_ad": chorus_ad,
                "chorus_ae": chorus_ae,
                },
            "obOneTwo": {
                "resp_aa": resp_aa, 
                "resp_ab": resp_ab,
                "resp_ba": resp_ba,
                "resp_bb": resp_bb,
                "resp_bc": resp_bc,
                "chorus_aa": chorus_aa,
                "chorus_ab": chorus_ab,
                "chorus_ac": chorus_ac,
                "chorus_ad": chorus_ad,
                "chorus_ae": chorus_ae,
                },
            "clOneTwo": {
                "resp_aa": resp_aa, 
                "resp_ab": resp_ab,
                "resp_ba": resp_ba,
                "resp_bb": resp_bb,
                "resp_bc": resp_bc,
                "chorus_aa": chorus_aa_octvb,
                "chorus_ab": chorus_ab_octvb,
                "chorus_ac": chorus_ac_octvb,
                "chorus_ad": chorus_ad_octvb,
                "chorus_ae": chorus_ae_octvb,
                },
            "bassoon": {
                "resp_aa": resp_aa_octvb, 
                "resp_ab": resp_ab_octvb,
                "resp_ba": resp_ba_octvb,
                "resp_bb": resp_bb_octvb,
                "resp_bc": resp_bc_octvb,
                "chorus_aa": chorus_aa_octvb,
                "chorus_ab": chorus_ab_octvb,
                "chorus_ac": chorus_ac_octvb,
                "chorus_ad": chorus_ad_octvb,
                "chorus_ae": chorus_ae_octvb,
                },
            }
    return wwinds


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
    instruments = ["flOneTwo", "obOneTwo", "clOneTwo", "bassoon"]
    segment = "verseOne"
    generate_chunk(get_wwind_section, instruments, segment)