#!/usr/bin/python3

# strings.py: script to generate string voices for a sketch for orchestral
# string section
from marana.tools import outputheader

def incrtup(tup: tuple, increment: int, modulus: int) -> tuple[int]: 
    """
    returns a new tuple that contains the values of tup incr by 1
    """
    nlist = []
    for i in tup:
        ret = (i + increment) % modulus
        nlist.append(ret)
    return tuple(nlist)


def permute(pitchset: dict, pattern: tuple, increment: int) -> list[tuple]:
    """  
    permute through the sets
    """
    rsets = []
    def itersets(mod: tuple[int]):
        """
        recursive function that iterates through the sets nperm times
        """
        if len(rsets) == len(pitchset): # permutations complete
            return                      # control to outer scope
        else:
            rsets.append(mod)
            # increment the set by 1
            # use the len of the pitchset to specify the modulus
            itersets(incrtup(mod, increment, len(pitchset))) 
    itersets(pattern)
    return rsets

##############################################################
# DATA 
##############################################################

PITCHSETS = {
        "BASIS" : {
                    0: "bf''",
                    1: "a''",
                    2: "g''",
                    3: "f''",
                    4: "e''",
                    5: "d''",
                    6: "c''",
                    7: "b'",
                    8: "a'",
                    9: "g'"
                    },
        }

"""
Modules are essentially collections of tone rows that are represented as tuples
of integers. These can be used to look up actualy pitch values from a pitchset.
Furthermore, they can be used in combination with the permute function to
create evolving melodic sequences.
"""
MODULES = {
           "A" : {
             "vla":    (3, 3, 5),
             "vlc":    (0, 1, 2),
             "kb":     (0, 0, 0)
             },
           "B" : {
             "vlnone": (0, 5, 9, 0),
             "vlc":    (0, 6, 4)
           }
          }


TEMPLATES = {
    "B": {
      "vlnone": "r2. {0}8( \\mf {1}8 {2}2.)-- {3}4:16 \\^\\ord ~ {3}3.:16\\^\\pont. \\> r4 r1",
      "vlc": "r2 {0}4 ~ {0}4 {1}2 r8 {2}8 \\^\\ord ~ {2}2.:16\\^\\pont. \\>"
    }
}




def createseqs(sequence: list[tuple], pitchset: dict) -> list[tuple]:
    """
    function that takes the newly minted sets and turns them into pitches that we
    can use to perform a lookup in the pitchset dictionary 
    """
    # for each melodic fragment in the sequence, perform a lookup 
    ptups = []
    for i in sequence:
        pset = []
        for j in i:
            pset.append(pitchset[j])
        ptups.append(tuple(pset))
    return ptups 


def filltemplate(template: str, pitchset: list[tuple]) -> list[str]:
    """
    and then use the values found to populate the templates.
    """
    # first check that the length of a pitchset tuple equals the number of
    # vacant slots in the template
    ret = []
    for item in pitchset:
        ret.append(template.format(*item))
    return ret
        


"""
define printer
"""


if __name__ == '__main__':
    vnonemods = permute(PITCHSETS["BASIS"], MODULES["B"]["vlnone"], 1)
    vcmods    = permute(PITCHSETS["BASIS"], MODULES["B"]["vlc"], -1)
    vnseqs = createseqs(vnonemods, PITCHSETS["BASIS"])
    vcseqs = createseqs(vcmods, PITCHSETS["BASIS"])
    vnphrases = filltemplate(TEMPLATES["B"]["vlnone"], vnseqs)
    vcphrases = filltemplate(TEMPLATES["B"]["vlc"], vcseqs)
    outputheader()
