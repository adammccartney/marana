#/usr/bin/python3
"""
marana.tools: a module containing some general tools for interfacing with abjad
and lilypond 
"""

import re
import abjad 

from collections import namedtuple
from typing import Callable
from abjad import Container, lilypond, Voice, Staff

def stringify_container(container: Container) -> str:
    """
    takes the contents of a container and turns it into a flat string
    """
    res = ""
    for item in container:
        res = res + str(item) + " "
    # trim last white space
    res = res.rstrip(" ")
    return res


INDENT = " " * 4

def strip_container(container: Container) -> str:
    """
    turns a container into a flat lilypond string
    """
    lystr = lilypond(container)
    res = lystr.replace("\n", "")
    res = res.replace("{" + INDENT, "{")
    res = res.replace(INDENT, " ")
    return res

def strip_voice(voice: Voice) -> str:
    """
    designed to turn a voice into a straight lilypond string
    """
    lystr = lilypond(voice)
    res = lystr.replace("\n", "")
    res = res.replace("\\new Voice", "")
    res = res.replace("{" + INDENT, "{")
    res = res.replace(INDENT, " ")
    return res

def strip_staff(staff: Staff) -> str:
    """
    same as above, designed to strip down a staff
    """
    lystr = lilypond(staff)
    res = lystr.replace("\n", "")
    res = res.replace("\\new Staff", "")
    res = res.replace("{" + INDENT, "{")
    res = res.replace(INDENT, " ")
    return res

def create_voice(phrase: str, offset: int):
    """
    will create a new voice that is a tranposition of the old voice at an
    offset of n semitones
    """
    voice = Voice(phrase)
    abjad.mutate.transpose(voice, offset)
    return voice

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



# create a map function that replaces the notes in deselected positions with
# rests
def mapRests(idxs: list[int], phrases: list[str]) -> list[str]:
    """
    takes an list of indexes onto which rests should be mapped
    along with an list of phrases, 
    assumes that the phrases are of equal length
    """
    def makeArray(phrase: str) -> list[str]:
        """
        makes an array out of a string
        """
        return phrase.split(" ")
    def makeRest(subject: str) -> str:
        """
        replaces any pitch info with a rest
        takes a lilypond string as input,
        returns a lilypond string as output
        """
        pre = re.compile(r"""([a-g])                          # pitch name
                             ([f]*|(qf)?|(qs)?|[s]*|t?q?[fs]) # accidental
                             (\'*|\,*)                        # zero or more octaves
                          """, re.VERBOSE)
        result = pre.sub("r", subject)  # replace pitch info with rest symbol
        return result
    pharr = [makeArray(p) for p in phrases]
    for p in pharr:
        for i in idxs:
            if (len(p) > 2):   # assume we want to operate on all but the last
                rested = makeRest(p[i])
                p[i] = rested
    result = [" ".join(p) for p in pharr]
    return result




