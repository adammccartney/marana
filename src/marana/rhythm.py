#!/usr/bin/python3
from enum import Enum, auto
from abjadext.rmakers import Talea

class RhythmToken(Enum):
    TALEA = auto()

class RhythmData:
    """
    Small class to hold rhythm data
    """
    def __init__(self, counts, denominator, time_signature_pairs):
        self.counts = counts
        self.denominator = denominator
        self.time_signature_pairs = time_signature_pairs


class RhythmQuery:
    """
    A rhythm query is a simple struct for holding information used to interpret
    rhythm data in a structured way. It's almost like a constructor in that it
    works closely with attributes of RhythmData and an interpretation command 

    attributes:
        rtype (rhythmtype)
    """

    def __init__(self, rtype: str):
        self.checkrtype(rtype)

    def checkrtype(self, rtype: str):
        if rtype not in {"talea"}:
            raise ValueError("Uknown rhythm type requested")
        if rtype == "talea":
            self.rtype = RhythmToken.TALEA




