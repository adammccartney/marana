#!/usr/bin/python3

# strings.py: script to generate string voices for a sketch for orchestral
# string section
from marana.tools import generate_chunk, outputheader


##############################################################
# DATA
##############################################################

PITCHSETS = {
    "SOP_BISB": {
        0: ["bf''", "c'''"],
        1: ["g''", "a''"],
        2: ["f''", "g''"],
        3: ["a''", "bf''"],
        4: ["d'''", "e'''"],
        5: ["c'''", "d'''"],
        6: ["e'''", "f'''"],
        7: ["d'''", "e'''"],
        8: ["c'''", "d'''"],
        9: ["c'''", "d'''"],
    },
    "ALT_BISB": {
        0: ["bf'", "<e' c''>"],
        1: ["f'", "a'"],
        2: ["g'", "g'"],
        3: ["<a' bf'>", "f'"],
        4: ["bf'", "<a' e''>"],
        5: ["g'", "<g' d''>"],
        6: ["a'", "<c'' f''>"],
        7: ["g'", "<c'' e''>"],
        8: ["a'", "<c'' d''>"],
        9: ["g'", "<c'' d''>"],
    },
    "BASS_BISB": {
        0: ["bf,", "c"],
        1: ["f,", "a,"],
        2: ["g,", "f,"],
        3: ["f,", "a,"],
        4: ["bf,", "a,"],
        5: ["g,", "d,"],
        6: ["a", "f"],
        7: ["g,", "c"],
        8: ["a,", "c"],
        9: ["g,", "c"],
    },
    "SOPRANO": {
        0: "bf''",
        1: "a''",
        2: "g''",
        3: "f''",
        4: "e''",
        5: "d''",
        6: "c''",
        7: "b'!",
        8: "a'",
        9: "g'",
    },
    "ALTO": {
        0: "bf'",
        1: "a'",
        2: "g'",
        3: "f'",
        4: "e'",
        5: "d''",
        6: "c''",
        7: "b'!",
        8: "a'",
        9: "g'",
    },
    "TENOR": {
        0: "bf'",
        1: "a'",
        2: "g'",
        3: "f'",
        4: "e'",
        5: "d'",
        6: "c'",
        7: "b!",
        8: "a",
        9: "g",
    },
    "BASS": {
        0: "bf",
        1: "a",
        2: "g",
        3: "f",
        4: "e",
        5: "d",
        6: "c",
        7: "b,!",
        8: "a,",
        9: "g,",
    },
    "CONTRA": {
        0: "bf,",
        1: "a,",
        2: "g,",
        3: "f,",
        4: "e,",
        5: "d,",
        6: "c,",
        7: "b,,!",
        8: "a,,",
        9: "g,,",
    },
}

"""
Modules are essentially collections of tone rows that are represented as tuples
of integers. These can be used to look up actualy pitch values from a pitchset.
Furthermore, they can be used in combination with the permute function to
create evolving melodic sequences.
"""
MODULES = {
    "A": {
        "obOne": (3, 3, 5),
        "obTwo": (0, 1, 2),
        "clOne": (3, 3, 5),
        "clTwo": (0, 1, 2),
        "hnOne": (3, 3, 5),
        "hnTwo": (0, 0, 0),
        "hnThree": (0, 1, 2),
        "hnFour": (0, 0, 0),
        "trpOne": (3, 3, 5),
        "trpTwo": (0, 1, 2),
        "trb": (0, 0, 0),
        "tuba": (0, 1, 2),
        "tmp": (0, 0, 0),
        "va": (3, 3, 5),
        "vc": (0, 1, 2),
        "kb": (0, 0, 0),
    },
    "B": {
        "fluteOne": (0, 5),
        "fluteTwo": (0, 9),
        "bsn": (0, 6, 4),
        "vibes": (5, 6, 7),
        "harp": (0, 6, 4),
        "vnone": (0, 5, 9, 0),
        "vntwo": (5, 6, 7),
        "vc": (0, 6, 4),
    },
}


TEMPLATES = {
    "A": {
        "obOne": "r4 {0}4--\\p ~ {1}4 {2}4--~ {2}2 r2",
        "obTwo": "r2 r4 {0}4--\\p {1}4 {2}4--~ {2}2",
        "clOne": "r4 {0}4--\\p~ {1}4 {2}4--~ {2}2 r2",
        "clTwo": "r2 r4 {0}4--\\p {1}4 {2}4--~ {2}2",
        "trpOne": "r2 {0}8-.\\fp {0}-. r4 {1}8-. {1}-. r4 r2",
        "trpTwo": "r2 {0}8-.\\fp {0}-. r4 {1}8-. {1}-. r4 r2",
        "hnOne": "r2 {0}8-. {0}-. r4 {1}8-. {1}-. r4 r2",
        "hnTwo": "r2 {0}8-. {0}-. r4 {1}8-. {1}-. r4 r2",
        "hnThree": "r2 {0}8-. {0}-. r4 {1}8-. {1}-. r4 r2",
        "hnFour": "r2 {0}8-. {0}-. r4 {1}8-. {1}-. r4 r2",
        "trb": "r2 {0}8-.\\fp {0}-. r4 {1}8-. {1}-. r4 r2",
        "tuba": "r2 {0}8-.\\fp {0}-. r4 {1}8-. {1}-. r4 r2",
        "tmp": "r4 {0}4--\\p {0}8-- {0}8-- {0}4-- {0}8-- {0}8-- {0}4-- {0}4-- r4",
        "va": "r4 {0}4--\\(\\pp {0}8-- {0}8--\\) {0}4--\\( {0}8-- {0}8--\\) {1}4--\\( {1}4--\\) r4",
        "vc": "r4 {0}4--\\(\\pp {0}8-- {0}8--\\) {1}4--\\( {1}8-- {1}8--\\) {2}4--\\( {2}4--\\) r4",
        "kb": "r4 {0}4--\\(\\pp {0}8-- {0}8--\\) {0}4--\\( {0}8-- {0}8--\\) {0}4--\\( {0}4--\\) r4",
    },
    "B": {
        "fluteOne": "r1 {0}2.\\p {1}4 {1}1",
        "fluteTwo": "r1 r2 {0}2\\p {1}1",
        "bsn": """\\repeat tremolo 16 {{ {0}32\\(\\pp\\< {1}\\) }}  |
                  \\repeat tremolo 16 {{ {2}32\\(\\f\\> {3}\\) }} |
                  \\repeat tremolo 16 {{ {4}32\\( {5}\\pp\\) }}  |""",
        "vibes": "{0}1^\\markup {{ sim. }} {1}1 {2}",
        "harp": """\\repeat tremolo 16 {{ {0}32\\(\\pp\\< {1}\\) }}  |
                   \\repeat tremolo 16 {{ {2}32\\(\\f\\> {3}\\) }} | 
                   \\repeat tremolo 16 {{ {4}32\\( {5}\\)\\pp }}  |""",
        "vnone": "r2. {0}8\\mp(^\\ord {1}8 {2}2.)-- {3}4:32 ^\\ord\\> ~ {3}2.:32^\\pont\\ppp r4",
        "vntwo": "r2. r8 {0}8\\p~^\\ord {0}2\\< {1}2\\> {2}2.:32\\ppp^\\pont r4",
        "vc": "r2. {0}4\\mp~^\\ord {0}4 {1}2\\> {2}4 ^\\ord ~ {2}2.:32^\\pont\\ppp r4",
    },
    # C phrases are phrases that link A and B
    "C": {},
}


# lilypond macros used for the string section
MACROS = {
    "TEXT_SPAN_ORD": 'textSpanOrd = { \\override TextSpanner.bound-details.left.text = "Ord. -> Pont." } ',
    "TEXT_SPAN_PONT": 'textSpanPont = { \\override TextSpanner.bound-details.left.text = "Sul Pont." }',
    "TEXT_SPAN_TASTO": 'textSpanTasto = { \\override TextSpanner.bound-details.left.text = "Sul Tasto" }',
    "ORD": "ord = \\markup { ord. }",
    "TASTO": "tasto = \\markup { sul tasto }",
    "PONT": "pont = \\markup{ sul pont.  }",
    "START_REPEAT": "startRepeat = {\\set Score.repeatCommands = #'(start-repeat)}",
    "END_REPEAT": "endRepeat = {\\set Score.repeatCommands = #'(end-repeat)}",
    "BEAM_ACCEL": "beamAccel = { \\override Beam.grow-direction = #RIGHT }",
    "BEAM_DECCEL": "beamDeccel = { \\override Beam.grow-direction = #LEFT }",
    "BEAM_NEUTRAL": "beamNeutral = { \\override Beam.grow-direction = #f }",
    "BOW_TREM": "bowTrem = \\markup{ bow tremolo }",
    "START_RIT": 'startRit = { \\override TextSpanner.bound-details.left.text= \\markup { \\upright "rit." } }',
    "ESSPRESSIVO": "espress = \\markup { espressivo }",
    "BOWED": "arco = \\markup { arco }",
    "MOT": "motoron = \\markup { motor on }",
    "LV": "lv = \\markup { l.v.}",
    "PED": "ped = \\markup { pedal depressed }",
    "CON_SORD": "consord = \\markup {con sord.}",
    "VIA_SORD": "viasord = \\markup {via sord.}",
    "FEATHERED_BEAM_RIGHT": "featheredBeamRight = { \\override Beam.grow-direction = #RIGHT }",
    "FEATHERED_BEAM_LEFT": "featheredBeamLeft = { \\override Beam.grow-direction = #LEFT }",
    "VIA_SORD": "viaSord = \\markup \"via sord.\"",
    "MEDMALLETS": "mmallets = \\markup { med. mallets }",
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
        if len(rsets) == len(pitchset):  # permutations complete
            return  # control to outer scope
        else:
            rsets.append(mod)
            # increment the set by 1
            # use the len of the pitchset to specify the modulus
            itersets(incrtup(mod, increment, len(pitchset)))

    itersets(pattern)
    return rsets


def isPolyphonic(ptups: list[tuple]) -> bool:
    """
    Simply looks at the structure of the material in the list of pitch tuples
    and decides if the content should be considered Polyphonic or not

    Assumes that all values in a ptups list are of the same type
    """
    ret = False
    sample = ptups[0][0]  # use the first val in list as sample
    if type(sample) is list:
        ret = True
    return ret


def convertTuple(x: tuple[list]) -> tuple[str]:
    """
    converts a tuple containing a list of strings to a simple tuple containing
    those strings. It basically takes all elements of the inner lists and
    unifies them in a tuple by removing the list parenthesis.
    """
    flatlist = []
    for innerlist in x:
        flatlist = flatlist + innerlist
    return flatlist


def createseqs(sequence: list[tuple], pitchset: dict) -> list[tuple]:
    """
    function that takes the newly minted sets and turns them into pitches that we
    can use to perform a lookup in the pitchset dictionary

    guarantees to return a flat list of tuples that contain pitches

    otherwise for each melodic fragment in the sequence, perform a simple lookup

    if the instrument requires pitch material that is polyphonic, the lookup
    function will need to further flatten the list that is returned on lookup
    """
    ptups = []
    for i in sequence:
        pset = []
        for j in i:
            pset.append(pitchset[j])
        ptups.append(tuple(pset))
    ret = []
    if isPolyphonic(ptups):
        ret = [convertTuple(t) for t in ptups]
    else:
        ret = ptups
    return ret


def filltemplates(template: str, pitchset: list[tuple]) -> list[str]:
    """
    Populate a lilypond style format string with notes from the pitchsets
    """
    # first check that the length of a pitchset tuple equals the number of
    # vacant slots in the template
    ret = []
    for item in pitchset:
        ret.append(template.format(*item))  # format string passed *args
    return ret


def playsSoprano(instrument: str) -> bool:
    """
    checks if an instrument should be playing soprano
    """
    if instrument in {
        "obOne",
        "obTwo",
        "clOne",
        "clTwo",
        "trpOne",
        "trpTwo",
        "vnone",
        "vntwo",
    }:
        return True
    else:
        return False


def playsAlto(instrument: str) -> bool:
    if instrument in {"hnOne", "hnThree"}:
        return True
    else:
        return False


def playsTenor(instrument: str) -> bool:
    if instrument in {"hnTwo", "hnFour", "tuba", "va"}:
        return True
    else:
        return False


def playsBass(instrument: str) -> bool:
    if instrument in {"trb", "tmp", "vc", "kb"}:
        return True
    else:
        return False


def playsSopranoBisbgl(instrument: str) -> bool:
    """
    checks if instrument should be playing soprano bisb figures
    """
    if instrument in {"fluteOne", "fluteTwo"}:
        return True
    else:
        return False


def playsAltoBisbgl(instrument: str) -> bool:
    """
    check if plays alto
    """
    if instrument in {"harp", "vibes"}:
        return True
    else:
        return False


def createMusicChunk(section: str, name: str, pamount: int) -> list[str]:
    """
    parse the section and (instrument) name
    populate set of templates based on musical logic of segment

    pamaout is an integer value that dermines the level of increment per round
    of permutation. e.g. a value of -1 means the set of integers being permuted
    will be decremented by 1 on each iteration. This essentially amounts to
    moving backwards or forwards (striding) through the sets.
    """
    instrument_names = [
        "fluteOne",
        "fluteTwo",
        "obOne",
        "obTwo",
        "clOne",
        "clTwo",
        "bsn",
        "hnOne",
        "hnTwo",
        "hnThree",
        "hnFour",
        "trpOne",
        "trpTwo",
        "trb",
        "tuba",
        "vibes",
        "tmp",
        "harp",
        "vnone",
        "vntwo",
        "va",
        "vc",
        "kb",
    ]
    nameError = f"Name should be one of: {instrument_names}"
    assert name in set(instrument_names), nameError
    sectionError = "Section should be one of 'A', 'B'"
    assert section in {"A", "B"}, sectionError
    if (section == "A") and playsSoprano(name):
        register = "SOPRANO"
    elif (section == "A") and playsAlto(name):
        register = "ALTO"
    elif (section == "A") and playsTenor(name):
        register = "TENOR"
    elif (section == "A") and playsBass(name):
        register = "BASS"
    elif (section == "B") and playsSoprano(name):
        register = "SOPRANO"
    elif (section == "B") and playsSopranoBisbgl(name):
        register = "SOP_BISB"
    elif (section == "B") and playsAltoBisbgl(name):
        register = "ALT_BISB"
    elif (section == "B") and (name == "vc"):
        register = "TENOR"
    elif (section == "B") and (name == "bsn"):
        register = "BASS_BISB"
    else:
        register = None
    assert register is not None, "Error: register not defined"
    modes = permute(PITCHSETS[register], MODULES[section][name], pamount)
    seqs = createseqs(modes, PITCHSETS[register])
    return filltemplates(TEMPLATES[section][name], seqs)


def get_segment() -> dict:
    """
    get segment fetches all the music phrases that occur per instrument
    it's essentally an organizer function, it just sets up a dictionary that we
    can later use to retrieve musical phrases along with variable names for
    these phrases
    """
    obOne_A = createMusicChunk("A", "obOne", -1)
    obTwo_A = createMusicChunk("A", "obTwo", -1)
    clOne_A = createMusicChunk("A", "clOne", -1)
    clTwo_A = createMusicChunk("A", "clTwo", -1)

    trpOne_A = createMusicChunk("A", "trpOne", -1)
    trpTwo_A = createMusicChunk("A", "trpTwo", -1)
    trb_A = createMusicChunk("A", "trb", -1)
    tuba_A = createMusicChunk("A", "tuba", -1)

    tmp_A = createMusicChunk("A", "tmp", -1)
    va_A = createMusicChunk("A", "va", -1)
    vc_A = createMusicChunk("A", "vc", -1)
    kb_A = createMusicChunk("A", "kb", -1)

    fluteOne_B = createMusicChunk("B", "fluteOne", 1)
    fluteTwo_B = createMusicChunk("B", "fluteTwo", -1)
    bsn_B = createMusicChunk("B", "bsn", 1)
    vibes_B = createMusicChunk("B", "vibes", 1)
    vibes_B[0] = "g'1\\p^\\arco^\\ped^\\motoron <g' d''>1 a'1" # once override
    harp_B = createMusicChunk("B", "harp", 1)
    vnone_B = createMusicChunk("B", "vnone", 1)
    vntwo_B = createMusicChunk("B", "vntwo", 1)
    vc_B = createMusicChunk("B", "vc", -1)

    SECT_A_REST = "R2*4"  # two bar rest
    SECT_B_REST = "R1*3"  # three bar rest

    INIT_HARP_PEDAL = "r2_\\markup { \\harp-pedal #\"--^|----\" } r2 r2 r2"

    PAGE_BREAK = "\\break"

    METER_2_4 = "\\time 2/4"
    METER_4_4 = "\\time 4/4"

    RMARKS = [
        "\\mark #1",
        "\\mark #2",
        "\\mark #3",
        "\\mark #4",
        "\\mark #5",
    ]

    # periods are six bars long, alternate between section type A and B
    phrases = {
        "fluteOne": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "break": PAGE_BREAK,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "break": PAGE_BREAK,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": "g''1\\pp ~ g'' e''~",
            "mm34_36": "e'' d''~ d''",
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "break": PAGE_BREAK,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": fluteOne_B[4],
            "mm52_54": fluteOne_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "break": PAGE_BREAK,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": fluteOne_B[6],
            "mm70_72": fluteOne_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "break": PAGE_BREAK,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": fluteOne_B[8],
            "mm88_90": fluteOne_B[9],
            "break": PAGE_BREAK,
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
            "break": PAGE_BREAK,
        },
        "fluteTwo": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": "r1 g''1\\pp ~ g''",
            "mm34_36": "e''1 ~ e'' c''",
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": fluteTwo_B[4],
            "mm52_54": fluteTwo_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": fluteTwo_B[6],
            "mm70_72": fluteTwo_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": fluteTwo_B[8],
            "mm88_90": fluteTwo_B[9],
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "obOne": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": "r1 r2 g''2\\ppp ~ g''1 ~",
            "mm16_18": "g''2 a''2 ~ a''1 r1",
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": "d''1\\ppp ~ d'' c''~",
            "mm52_54": "c'' bf'~ bf'",
            "mm55": METER_2_4,
            "mm55_58": obOne_A[5],
            "mm59_62": obOne_A[5],
            "mm63_66": obOne_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "obTwo": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": "r1 r1 d''\\ppp ~",
            "mm16_18": "d''1 ~ d''1 r1",
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": "r1 d''1\\ppp ~d''1",
            "mm52_54": "c''1 ~ c''1 r1",
            "mm55": METER_2_4,
            "mm55_58": obTwo_A[5],
            "mm59_62": obTwo_A[5],
            "mm63_66": obTwo_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": obTwo_A[7],
            "mm77_80": obTwo_A[7],
            "mm81_84": obTwo_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "clOne": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": "g''1\\ppp~ g''1 a''1 ~",
            "mm16_18": "a''1 f''1~ f''1",
            "mm19": METER_2_4,
            "mm19_22": clOne_A[1],
            "mm23_26": clOne_A[1],
            "mm27_30": clOne_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": "f1\\ppp ~ f1 g1 ~",
            "mm70_72": "g1 bf ~bf",
            "mm73": METER_2_4,
            "mm73_76": clOne_A[7],
            "mm77_80": clOne_A[7],
            "mm81_84": clOne_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": clOne_A[9],
            "mm95_98": clOne_A[9],
            "mm99_102": clOne_A[9],
        },
        "clTwo": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": "r1 d''1\\ppp~ d''1",
            "mm16_18": "g''1~ g''1~ g''1",
            "mm19": METER_2_4,
            "mm19_22": clTwo_A[1],
            "mm23_26": clTwo_A[1],
            "mm27_30": clTwo_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": "r1 f1\\ppp ~ f1",
            "mm70_72": "a1 ~ a1 r1",
            "mm73": METER_2_4,
            "mm73_76": clTwo_A[7],
            "mm77_80": clTwo_A[7],
            "mm81_84": clTwo_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": clTwo_A[9],
            "mm95_98": clTwo_A[9],
            "mm99_102": clTwo_A[9],
        },
        "bsn": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": bsn_B[2],
            "mm34_36": bsn_B[3],
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": bsn_B[4],
            "mm52_54": bsn_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": bsn_B[6],
            "mm70_72": bsn_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": bsn_B[8],
            "mm88_90": bsn_B[9],
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "hnOne": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": "d''2\\ppp^\\markup\"Con sord.\" ~ d'' ~ d'' ~ d''",
            "mm23_26": "bf'2~ bf' bf' ~ bf'",
            "mm27_30": "a'2 ~ a' ~ a' ~ a'",
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": "bf'2\\ppp ~ bf' ~ bf' ~ bf'",
            "mm41_44": "b'2~ b' ~ b' ~ b'",
            "mm45_48": "g'2~ g' ~ g' g'",
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": "a'2\\ppp ~ a' a' a'",
            "mm59_62": "g'2 ~ g' ~ g' ~ g'",
            "mm63_66": "g'2 ~ g' ~ g' ~ g'",
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": "d''2\\ppp ~ d'' ~ d'' ~ d''",
            "mm77_80": "d''2 ~ d'' ~ d'' ~ d''",
            "mm81_84": "c''2 ~ c'' ~ c'' ~c''",
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": "a'2\\ppp~ a'~ a' a'",
            "mm95_98": "g'2 ~ g'~ g'~ g'",
            "mm99_102": "f'2~ f' ~ f'~ f'",
        },
        "hnTwo": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": "g'2\\ppp^\\markup\"Con sord.\"~ g'~ g' ~ g'",
            "mm23_26": "g'2~ g'2 ~ g'2 ~g'2",
            "mm27_30": "g'2~ g'2 ~ g'2 ~g'2",
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": "bf2\\ppp ~ bf ~ bf ~ bf",
            "mm41_44": "bf2 ~ bf ~ bf ~ bf",
            "mm45_48": "bf2 ~ bf ~ bf ~ bf",
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": "d'2\\ppp ~ d' ~ d' ~ d'",
            "mm59_62": "d'2 ~ d' ~ d' ~ d'",
            "mm63_66": "e'2 ~ e' ~ e' ~ e'",
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": "f'2\\ppp ~ f' ~ f' ~ f'",
            "mm77_80": "f'2 ~ f' ~f' ~ f'",
            "mm81_84": "f'2 ~ f' ~f' ~ f'",
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": "a2\\ppp~ a~ a~ a",
            "mm95_98": "a2~ a ~ a~ a",
            "mm99_102": "a2~ a~ a~ a",
        },
        "hnThree": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": "d'1\\ppp^\\markup\"Con sord.\" ~d' ~ d'",
            "mm34_36": "bf ~ bf ~ bf",
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": "f'1\\ppp ~ f'1 ~ f'1",
            "mm52_54": "e'1 ~ e'1 ~ e'1 ",
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": "a'1\\ppp ~ a' ~ a'",
            "mm70_72": "b' ~ b' ~ b'",
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": "bf'1\\ppp ~ bf' ~bf'",
            "mm88_90": "a'1 ~ a'1 ~ a'",
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "hnFour": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": "g1\\ppp^\\markup\"Con sord.\" ~ g~ g",
            "mm34_36": "g ~ g ~ g",
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": "bf1\\ppp ~ bf1 ~ bf1",
            "mm52_54": "bf1 ~ bf1 ~ bf1 ",
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": "f'1\\ppp ~ f' ~ f'",
            "mm70_72": "f' ~ f' ~ f'",
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": "a1\\ppp ~a ~a",
            "mm88_90": "a1~ a ~ a",
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "trpOne": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": """r2 | g''8-.\\fp^\\consord g''8-. r4 | 
                          g''8-. g''-. r4 | r2""",
            "mm23_26": trpOne_A[1],
            "mm27_30": trpOne_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": trpOne_A[3],
            "mm41_44": trpOne_A[3],
            "mm45_48": trpOne_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": trpOne_A[5],
            "mm59_62": trpOne_A[5],
            "mm63_66": trpOne_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": trpOne_A[7],
            "mm77_80": trpOne_A[7],
            "mm81_84": trpOne_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": trpOne_A[8],
            "mm95_98": trpOne_A[9],
            "mm99_102": trpOne_A[9],
        },
        "trpTwo": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": """r2 | g'8-.\\fp^\\consord g'-. r4 |
                          bf''8-. bf''8-. r4 | r2""",
            "mm23_26": trpTwo_A[1],
            "mm27_30": trpTwo_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": trpTwo_A[3],
            "mm41_44": trpTwo_A[3],
            "mm45_48": trpTwo_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": trpTwo_A[5],
            "mm59_62": trpTwo_A[5],
            "mm63_66": trpTwo_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": trpTwo_A[7],
            "mm77_80": trpTwo_A[7],
            "mm81_84": trpTwo_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": trpTwo_A[8],
            "mm95_98": trpTwo_A[9],
            "mm99_102": trpTwo_A[9],
        },
        "trb": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": """r2 | g,8-.\\fp^\\consord g,8-. r4 |
                          g,8-. g,8 r4 | r2""",
            "mm23_26": trb_A[1],
            "mm27_30": trb_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": trb_A[3],
            "mm41_44": trb_A[3],
            "mm45_48": trb_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": trb_A[5],
            "mm59_62": trb_A[5],
            "mm63_66": trb_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": trb_A[7],
            "mm77_80": trb_A[7],
            "mm81_84": trb_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": trb_A[8],
            "mm95_98": trb_A[9],
            "mm99_102": trb_A[9],
        },
        "tuba": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": """r2 | g8-.\\fp^\\consord g8-. r4 |
                          g8-. g8 r4 | r2""",
            "mm23_26": tuba_A[1],
            "mm27_30": tuba_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": tuba_A[3],
            "mm41_44": tuba_A[3],
            "mm45_48": tuba_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": tuba_A[5],
            "mm59_62": tuba_A[5],
            "mm63_66": tuba_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": tuba_A[7],
            "mm77_80": tuba_A[7],
            "mm81_84": tuba_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": tuba_A[8],
            "mm95_98": tuba_A[9],
            "mm99_102": tuba_A[9],
        },
        "vibes": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": vibes_B[0],
            "mm16_18": vibes_B[1],
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": vibes_B[2],
            "mm34_36": vibes_B[3],
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": vibes_B[4],
            "mm52_54": vibes_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": vibes_B[6],
            "mm70_72": vibes_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": vibes_B[8],
            "mm88_90": vibes_B[9],
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "tmp": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": tmp_A[3],
            "mm41_44": tmp_A[3],
            "mm45_48": tmp_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": tmp_A[5],
            "mm59_62": tmp_A[5],
            "mm63_66": tmp_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": tmp_A[7],
            "mm77_80": tmp_A[7],
            "mm81_84": tmp_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": tmp_A[9],
            "mm95_98": tmp_A[9],
            "mm99_102": tmp_A[9],
        },
        "harp": {
            "mm01": METER_2_4,
            "mm01_04": INIT_HARP_PEDAL,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": harp_B[1],
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": harp_B[2],
            "mm34_36": harp_B[3],
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": harp_B[4],
            "mm52_54": harp_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": harp_B[6],
            "mm70_72": harp_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": harp_B[8],
            "mm88_90": harp_B[9],
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "violinOne": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": vnone_B[0],
            "mm16_18": vnone_B[1],
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": vnone_B[2],
            "mm34_36": vnone_B[3],
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": vnone_B[4],
            "mm52_54": vnone_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": vnone_B[6],
            "mm70_72": vnone_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": vnone_B[8],
            "mm88_90": vnone_B[9],
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "violinTwo": {
            "mm01": METER_2_4,
            "mm01_04": SECT_A_REST,
            "mm05_08": SECT_A_REST,
            "mm09_12": SECT_A_REST,
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": vntwo_B[0],
            "mm16_18": vntwo_B[1],
            "mm19": METER_2_4,
            "mm19_22": SECT_A_REST,
            "mm23_26": SECT_A_REST,
            "mm27_30": SECT_A_REST,
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": vntwo_B[2],
            "mm34_36": vntwo_B[3],
            "mm37": METER_2_4,
            "mm37_40": SECT_A_REST,
            "mm41_44": SECT_A_REST,
            "mm45_48": SECT_A_REST,
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": vntwo_B[4],
            "mm52_54": vntwo_B[5],
            "mm55": METER_2_4,
            "mm55_58": SECT_A_REST,
            "mm59_62": SECT_A_REST,
            "mm63_66": SECT_A_REST,
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": vntwo_B[6],
            "mm70_72": vntwo_B[7],
            "mm73": METER_2_4,
            "mm73_76": SECT_A_REST,
            "mm77_80": SECT_A_REST,
            "mm81_84": SECT_A_REST,
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": vntwo_B[8],
            "mm88_90": vntwo_B[9],
            "mm91": METER_2_4,
            "mm91_94": SECT_A_REST,
            "mm95_98": SECT_A_REST,
            "mm99_102": SECT_A_REST,
        },
        "viola": {
            "mm01": METER_2_4,
            "mm01_04": """r4 g'4--\\(\\p^\\tasto |
                          g'8-- g'--\\) g'4--\\( |
                          g'8-- g'8--\\) g'4--\\( |
                          g'4-- r4\\)
                       """,
            "mm05_08": va_A[0],
            "mm09_12": va_A[0],
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": va_A[1],
            "mm23_26": va_A[1],
            "mm27_30": va_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": va_A[3],
            "mm41_44": va_A[3],
            "mm45_48": va_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": va_A[5],
            "mm59_62": va_A[5],
            "mm63_66": va_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": va_A[7],
            "mm77_80": va_A[7],
            "mm81_84": va_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": va_A[9],
            "mm95_98": va_A[9],
            "mm99_102": va_A[9],
        },
        "cello": {
            "mm01": METER_2_4,
            "mm01_04": """r4 bf4--\\(\\p^\\tasto |
                          bf8-- bf--\\) a4--\\( |
                          a8-- a8--\\) g4--\\( |
                          g4-- r4\\)""",
            "mm05_08": vc_A[0],
            "mm09_12": vc_A[0],
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": vc_B[0],
            "mm16_18": vc_B[1],
            "mm19": METER_2_4,
            "mm19_22": vc_A[1],
            "mm23_26": vc_A[1],
            "mm27_30": vc_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": vc_B[2],
            "mm34_36": vc_B[3],
            "mm37": METER_2_4,
            "mm37_40": vc_A[3],
            "mm41_44": vc_A[3],
            "mm45_48": vc_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": vc_B[4],
            "mm52_54": vc_B[5],
            "mm55": METER_2_4,
            "mm55_58": vc_A[5],
            "mm59_62": vc_A[5],
            "mm63_66": vc_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": vc_B[6],
            "mm70_72": vc_B[7],
            "mm73": METER_2_4,
            "mm73_76": vc_A[7],
            "mm77_80": vc_A[7],
            "mm81_84": vc_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": vc_B[8],
            "mm88_90": vc_B[9],
            "mm91": METER_2_4,
            "mm91_94": vc_A[9],
            "mm95_98": vc_A[9],
            "mm99_102": vc_A[9],
        },
        "contrabass": {
            "mm01": METER_2_4,
            "mm01_04": """r4 bf4--\\(\\p^\\tasto |
                          bf8-- bf--\\) bf4--\\( |
                          bf8-- bf8--\\) bf4--\\( |
                          bf4-- r4\\)""",
            "mm05_08": kb_A[0],
            "mm09_12": kb_A[0],
            "mm13": METER_4_4,
            "rmark1": RMARKS[0],
            "mm13_15": SECT_B_REST,
            "mm16_18": SECT_B_REST,
            "mm19": METER_2_4,
            "mm19_22": kb_A[1],
            "mm23_26": kb_A[1],
            "mm27_30": kb_A[2],
            "mm31": METER_4_4,
            "rmark2": RMARKS[1],
            "mm31_33": SECT_B_REST,
            "mm34_36": SECT_B_REST,
            "mm37": METER_2_4,
            "mm37_40": kb_A[3],
            "mm41_44": kb_A[3],
            "mm45_48": kb_A[4],
            "mm49": METER_4_4,
            "rmark3": RMARKS[2],
            "mm49_51": SECT_B_REST,
            "mm52_54": SECT_B_REST,
            "mm55": METER_2_4,
            "mm55_58": kb_A[5],
            "mm59_62": kb_A[5],
            "mm63_66": kb_A[6],
            "mm67": METER_4_4,
            "rmark4": RMARKS[3],
            "mm67_69": SECT_B_REST,
            "mm70_72": SECT_B_REST,
            "mm73": METER_2_4,
            "mm73_76": kb_A[7],
            "mm77_80": kb_A[7],
            "mm81_84": kb_A[8],
            "mm85": METER_4_4,
            "rmark5": RMARKS[4],
            "mm85_87": SECT_B_REST,
            "mm88_90": SECT_B_REST,
            "mm91": METER_2_4,
            "mm91_94": kb_A[9],
            "mm95_98": kb_A[9],
            "mm99_102": kb_A[9],
        },
    }
    return phrases


"""
define printer
"""


def printmacros(macros_dict):
    """
    outputs a selection of lilypond macro definitions to stdout
    """
    print("\n%% Macros " + "%" * 62 + "\n")
    lines = [macro for macro in macros_dict.values()]
    for l in lines:
        print(l)
    print("\n" + "%" * 72)


if __name__ == "__main__":

    outputheader()
    printmacros(MACROS)
    instruments = [
        "fluteOne",
        "fluteTwo",
        "obOne",
        "obTwo",
        "clOne",
        "clTwo",
        "bsn",
        "hnOne",
        "hnTwo",
        "hnThree",
        "hnFour",
        "trpOne",
        "trpTwo",
        "trb",
        "tuba",
        "vibes",
        "tmp",
        "harp",
        "violinOne",
        "violinTwo",
        "viola",
        "cello",
        "contrabass",
    ]
    segment = "segment_strings"
    generate_chunk(get_segment, instruments, segment)
