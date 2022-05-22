#!/usr/bin/python3

# strings.py: script to generate string voices for a sketch for orchestral
# string section
from marana.tools import ( generate_chunk,
                           outputheader
                           )


##############################################################
# DATA 
##############################################################

PITCHSETS = {
        "FLUTE_BIS" : {
                    0: ["bf''", "b''"],
                    1: ["g''", "a''"],
                    2: ["f''", "g''"],
                    3: ["a''", "bf''"],
                    4: ["d'''", "e'''"],
                    5: ["c'''", "d'''"],
                    6: ["e'''", "f'''"],
                    7: ["d'''", "e'''"],
                    8: ["c'''", "d'''"],
                    9: ["c'''", "d'''"]
            },
        "HARP_BISB" : {
                    0: ["bf'", "<e' b'>"],
                    1: ["f'", "a'"],
                    2: ["g'", "g'"],
                    3: ["f'", "<a' bf'>"],
                    4: ["bf'", "<a' e''>"],
                    5: ["g'", "<g' d''>"],
                    6: ["a'", "<c'' f''>"],
                    7: ["g'", "<b' e''>"],
                    8: ["a'", "<c'' d''>"],
                    9: ["g'", "<c'' d''>"]
                    },
        "SOPRANO" : {
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
         "TENOR": {
                    0: "bf'",
                    1: "a'",
                    2: "g'",
                    3: "f'",
                    4: "e'",
                    5: "d'",
                    6: "c'",
                    7: "b",
                    8: "a",
                    9: "g"
             },
         "BASS": {
                    0: "bf",
                    1: "a",
                    2: "g",
                    3: "f",
                    4: "e",
                    5: "d",
                    6: "c",
                    7: "b,",
                    8: "a,",
                    9: "g,"
             },
         "CONTRA": {
                    0: "bf,",
                    1: "a,",
                    2: "g,",
                    3: "f,",
                    4: "e,",
                    5: "d,",
                    6: "c,",
                    7: "b,,",
                    8: "a,,",
                    9: "g,,"
             }
        }

"""
Modules are essentially collections of tone rows that are represented as tuples
of integers. These can be used to look up actualy pitch values from a pitchset.
Furthermore, they can be used in combination with the permute function to
create evolving melodic sequences.
"""
MODULES = {
           "A" : {
             "va":    (3, 3, 5),
             "vc":    (0, 1, 2),
             "kb":    (0, 0, 0)
             },
           "B" : {
             "vnone": (0, 5, 9, 0),
             "vntwo": (5, 6, 7),
             "vc":    (0, 6, 4)
           }
          }


TEMPLATES = {
    "A": {
        "va": "r4 {0}4--\\p^\\tasto\\( {0}8-- {0}8--\\) {0}4--\\( {0}8-- {0}8--\\) {1}4--\\( {1}4--\\) r4",
        "vc": "r4 {0}4--\\p^\\tasto\\( {0}8-- {0}8--\\) {1}4--\\( {1}8-- {1}8--\\) {2}4--\\( {2}4--\\) r4",
        "kb": "r4 {0}4--\\p^\\tasto\\( {0}8-- {0}8--\\) {0}4--\\( {0}8-- {0}8--\\) {0}4--\\( {0}4--\\) r4"
    },
    "B": {
      "vnone": "r2. {0}8\\mp(^\\ord^\\espress {1}8 {2}2.)-- {3}4:16 ^\\ord\\> ~ {3}2.:16^\\pont\\ppp r4",
      "vntwo": "r2. r8 {0}8\\p~^\\ord^\\espress {0}2\\< {1}2\\> {2}2.:16\\ppp r4",
      "vc": "r2. {0}4\\mp~^\\ord^\\espress {0}4 {1}2\\> {2}4 ^\\ord ~ {2}2.:16^\\pont\\ppp r4"
    }
}


# lilypond macros used for the string section
MACROS = {
    "TEXT_SPAN_ORD": "textSpanOrd = { \\override TextSpanner.bound-details.left.text = \"Ord. -> Pont.\" } ",
    "TEXT_SPAN_PONT": "textSpanPont = { \\override TextSpanner.bound-details.left.text = \"Sul Pont.\" }",
    "TEXT_SPAN_TASTO": "textSpanTasto = { \\override TextSpanner.bound-details.left.text = \"Sul Tasto\" }",
    "ORD": "ord = \\markup { ord. }",
    "TASTO": "tasto = \\markup { sul tasto }",
    "PONT": "pont = \\markup{ sul pont.  }",
    "START_REPEAT": "startRepeat = {\\set Score.repeatCommands = #'(start-repeat)}",
    "END_REPEAT": "endRepeat = {\\set Score.repeatCommands = #'(end-repeat)}",
    "BEAM_ACCEL": "beamAccel = { \\override Beam.grow-direction = #RIGHT }",
    "BEAM_DECCEL": "beamDeccel = { \\override Beam.grow-direction = #LEFT }",
    "BEAM_NEUTRAL": "beamNeutral = { \\override Beam.grow-direction = #f }",
    "BOW_TREM": "bowTrem = \\markup{ bow tremolo }",
    "START_RIT": "startRit = { \\override TextSpanner.bound-details.left.text= \\markup { \\upright \"rit.\" } }",
    "ESSPRESSIVO": "espress = \\markup { espressivo }"
    }

################################################################


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


def filltemplates(template: str, pitchset: list[tuple]) -> list[str]:
    """ 
    Populate a lilypond style format string with notes from the pitchsets
    """
    # first check that the length of a pitchset tuple equals the number of
    # vacant slots in the template
    ret = []
    for item in pitchset:
        ret.append(template.format(*item))
    return ret


def createMusicChunk(section: str, name: str, pamount: int) -> list[str]:
    """
    parse the section and (instrument) name
    populate set of templates based on musical logic of segment
    """
    nameError =  "Name should be one of 'vnone', 'vntwo', 'va', 'vc', 'kb'"
    assert name in {"vnone", "vntwo", "va", "vc", "kb"}, nameError
    sectionError = "Section should be one of 'A', 'B'"
    assert section in {"A", "B"}, sectionError
    if (section == "A") and (name == "va"):
        register = "TENOR"
    elif (section == "A") and ((name == "vc") or (name == "kb")):
        register = "BASS"
    elif (section == "B") and ((name == "vnone") or (name == "vntwo")):
        register = "SOPRANO"
    elif (section == "B") and (name == "vc"):
        register = "TENOR"
    else:
        register = None  
    assert register is not None, "Error: register not defined"
    mods = permute(PITCHSETS[register], MODULES[section][name], pamount)
    seqs = createseqs(mods, PITCHSETS[register]) 
    return filltemplates(TEMPLATES[section][name], seqs)
        

def get_segment() -> dict:
    """
    get segment fetches all the music phrases that occur per instrument
    it's essentally an organizer function, it just sets up a dictionary that we
    can later use to retrieve musical phrases along with variable names for
    these phrases
    """
    va_A = createMusicChunk("A", "va", -1)
    vc_A = createMusicChunk("A", "vc", -1)
    kb_A = createMusicChunk("A", "kb", -1)

    vnone_B = createMusicChunk("B", "vnone", 1) 
    vntwo_B = createMusicChunk("B", "vntwo", 1)
    vc_B = createMusicChunk("B", "vc", -1)

    SECT_A_REST = "r1 r1" # two bar rest 
    SECT_B_REST = "r1 r1 r1" # three bar rest

    METER_2_4 = "\\time 2/4"
    METER_4_4 = "\\time 4/4"

    # periods are six bars long, alternate between section type A and B
    phrases = {
            "violinOne": {
                "mm01": METER_2_4,
                "mm01_02": SECT_A_REST,
                "mm03_04": SECT_A_REST,
                "mm05_06": SECT_A_REST,
                "mm07": METER_4_4,
                "mm07_09": vnone_B[0],
                "mm10_12": vnone_B[1],
                "mm13": METER_2_4,
                "mm13_14": SECT_A_REST,
                "mm15_16": SECT_A_REST,
                "mm17_18": SECT_A_REST,
                "mm19": METER_4_4,
                "mm19_21": vnone_B[2],
                "mm22_24": vnone_B[3],
                "mm25": METER_2_4,
                "mm25_26": SECT_A_REST,
                "mm27_28": SECT_A_REST,
                "mm29_30": SECT_A_REST,
                "mm31": METER_4_4,
                "mm31_33": vnone_B[4],
                "mm34_36": vnone_B[5],
                "mm37": METER_2_4,
                "mm37_38": SECT_A_REST,
                "mm39_40": SECT_A_REST,
                "mm41_42": SECT_A_REST,
                "mm43": METER_4_4,
                "mm43_45": vnone_B[6],
                "mm46_48": vnone_B[7],
                "mm49": METER_2_4,
                "mm49_50": SECT_A_REST,
                "mm51_52": SECT_A_REST,
                "mm53_54": SECT_A_REST,
                "mm55": METER_4_4,
                "mm55_57": vnone_B[8],
                "mm58_60": vnone_B[9],
                "mm61": METER_2_4,
                "mm61_62": SECT_A_REST,
                "mm63_64": SECT_A_REST,
                "mm65_66": SECT_A_REST
            },
            "violinTwo": {
                "mm01": METER_2_4,
                "mm01_02": SECT_A_REST,
                "mm03_04": SECT_A_REST,
                "mm05_06": SECT_A_REST,
                "mm07": METER_4_4,
                "mm07_09": vntwo_B[0],
                "mm10_12": vntwo_B[1],
                "mm13": METER_2_4,
                "mm13_14": SECT_A_REST,
                "mm15_16": SECT_A_REST,
                "mm17_18": SECT_A_REST,
                "mm19": METER_4_4,
                "mm19_21": vntwo_B[2],
                "mm22_24": vntwo_B[3],
                "mm25": METER_2_4,
                "mm25_26": SECT_A_REST,
                "mm27_28": SECT_A_REST,
                "mm29_30": SECT_A_REST,
                "mm31": METER_4_4,
                "mm31_33": vntwo_B[4],
                "mm34_36": vntwo_B[5],
                "mm37": METER_2_4,
                "mm37_38": SECT_A_REST,
                "mm39_40": SECT_A_REST,
                "mm41_42": SECT_A_REST,
                "mm43": METER_4_4,
                "mm43_45": vntwo_B[6],
                "mm46_48": vntwo_B[7],
                "mm49": METER_2_4,
                "mm49_50": SECT_A_REST,
                "mm51_52": SECT_A_REST,
                "mm53_54": SECT_A_REST,
                "mm55": METER_4_4,
                "mm55_57": vntwo_B[8],
                "mm58_60": vntwo_B[9],
                "mm61": METER_2_4,
                "mm61_62": SECT_A_REST,
                "mm63_64": SECT_A_REST,
                "mm65_66": SECT_A_REST
                },
            "viola": {
                "mm01": METER_2_4,
                "mm01_02": va_A[0],
                "mm03_04": va_A[0],
                "mm05_06": va_A[0],
                "mm07": METER_4_4,
                "mm07_09": SECT_B_REST,
                "mm10_12": SECT_B_REST,
                "mm13": METER_2_4,
                "mm13_14": va_A[1],
                "mm15_16": va_A[1],
                "mm17_18": va_A[2],
                "mm19": METER_4_4,
                "mm19_21": SECT_B_REST,
                "mm22_24": SECT_B_REST,
                "mm25": METER_2_4,
                "mm25_26": va_A[3],
                "mm27_28": va_A[3],
                "mm29_30": va_A[4],
                "mm31": METER_4_4,
                "mm31_33": SECT_B_REST,
                "mm34_36": SECT_B_REST,
                "mm37": METER_2_4,
                "mm37_38": va_A[5],
                "mm39_40": va_A[5],
                "mm41_42": va_A[6],
                "mm43": METER_4_4,
                "mm43_45": SECT_B_REST,
                "mm46_48": SECT_B_REST,
                "mm49": METER_2_4,
                "mm49_50": va_A[7],
                "mm51_52": va_A[7],
                "mm53_54": va_A[8],
                "mm55": METER_4_4,
                "mm55_57": SECT_B_REST,
                "mm58_60": SECT_B_REST,
                "mm61": METER_2_4,
                "mm61_62": va_A[9],
                "mm63_64": va_A[9],
                "mm65_66": va_A[9]
            },
            "cello": {
                "mm01": METER_2_4,
                "mm01_02": vc_A[0],
                "mm03_04": vc_A[0],
                "mm05_06": vc_A[0],
                "mm07": METER_4_4,
                "mm07_09": vc_B[0],
                "mm10_12": vc_B[1],
                "mm13": METER_2_4,
                "mm13_14": vc_A[1],
                "mm15_16": vc_A[1],
                "mm17_18": vc_A[2],
                "mm19": METER_4_4,
                "mm19_21": vc_B[2],
                "mm22_24": vc_B[3],
                "mm25": METER_2_4,
                "mm25_26": vc_A[3],
                "mm27_28": vc_A[3],
                "mm29_30": vc_A[4],
                "mm31": METER_4_4,
                "mm31_33": vc_B[4],
                "mm34_36": vc_B[5],
                "mm37": METER_2_4,
                "mm37_38": vc_A[5],
                "mm39_40": vc_A[5],
                "mm41_42": vc_A[6],
                "mm43": METER_4_4,
                "mm43_45": vc_B[6],
                "mm46_48": vc_B[7],
                "mm49": METER_2_4,
                "mm49_50": vc_A[7],
                "mm51_52": vc_A[7],
                "mm53_54": vc_A[8],
                "mm55": METER_4_4,
                "mm55_57": vc_B[8],
                "mm58_60": vc_B[9],
                "mm61": METER_2_4,
                "mm61_62": vc_A[9],
                "mm63_64": vc_A[9],
                "mm65_66": vc_A[9]
            },
            "contrabass": {
                "mm01": METER_2_4,
                "mm01_02": kb_A[0],
                "mm03_04": kb_A[0],
                "mm05_06": kb_A[0],
                "mm07": METER_4_4,
                "mm07_09": SECT_B_REST,
                "mm10_12": SECT_B_REST,
                "mm13": METER_2_4,
                "mm13_14": kb_A[1],
                "mm15_16": kb_A[1],
                "mm17_18": kb_A[2],
                "mm19": METER_4_4,
                "mm19_21": SECT_B_REST,
                "mm22_24": SECT_B_REST,
                "mm25": METER_2_4,
                "mm25_26": kb_A[3],
                "mm27_28": kb_A[3],
                "mm29_30": kb_A[4],
                "mm31": METER_4_4,
                "mm31_33": SECT_B_REST,
                "mm34_36": SECT_B_REST,
                "mm37": METER_2_4,
                "mm37_38": kb_A[5],
                "mm39_40": kb_A[5],
                "mm41_42": kb_A[6],
                "mm43": METER_4_4,
                "mm43_45": SECT_B_REST,
                "mm46_48": SECT_B_REST,
                "mm49": METER_2_4,
                "mm49_50": kb_A[7],
                "mm51_52": kb_A[7],
                "mm53_54": kb_A[8],
                "mm55": METER_4_4,
                "mm55_57": SECT_B_REST,
                "mm58_60": SECT_B_REST,
                "mm61": METER_2_4,
                "mm61_62": kb_A[9],
                "mm63_64": kb_A[9],
                "mm65_66": kb_A[9]
            }
    }
    return phrases
    

"""
define printer
"""

def printmacros():
    """
    outputs a selection of lilypond macro definitions to stdout
    """
    print("\n%% Macros " + "%" * 62 + "\n")
    lines = [macro for macro in MACROS.values()]
    for l in lines:
        print(l)
    print("\n" + "%" * 72)


if __name__ == '__main__':

    outputheader()
    printmacros()
    instruments = ["violinOne", "violinTwo", "viola", "cello", "contrabass"]
    segment = "segment_strings"
    generate_chunk(get_segment, instruments, segment)

