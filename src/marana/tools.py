#/usr/bin/python3
"""
marana.tools: a module containing some general tools for interfacing with abjad
and lilypond 
"""
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
