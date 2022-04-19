#!/usr/bin/python3

"""
maprests.py: quick throwaway script to work out how to write a function that creates
             material strings based on array storage
"""

import re

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





