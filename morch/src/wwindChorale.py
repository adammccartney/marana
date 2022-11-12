#!/usr/bin/python3

"""
wwindChorale.py: script to generate a short segment for woodwinds

usage: python3 wwindChorale.py > wwindChorale.ly
"""

import random
import heapq
from operator import itemgetter

from marana.tools import create_voice, outputheader, generate_chunk
from stringcanon import MACROS, printmacros

items = {2, 3}
total = 34


def createTraversal(items: set[int], total: int, seqlen: int) -> list[int] | int:
    """
    create a sequence of numbers such that the sum of the elements is equal to
    the total. This is really a graph traversal:
        The specific use case being targeted is a sequence of seven integers,
        each of which represents a number of repitition.
        Each reptition is at least 2.
    """
    # initialize sequence to null
    # then create a simple base number of repititions per harmony
    seq = [0] * seqlen
    val = random.sample(items, 1)
    seq = [i + val[0] for i in seq]
    result = sum(seq)
    while result < total:
        ridx = random.randrange(seqlen)
        val = random.sample(items, 1)
        seq[ridx] = seq[ridx] + val[0]
        result = sum(seq)
    # do some dirty tampering to round it down if we've overshot
    if result > total:
        # track the index of the largest value incase we need to decrement
        i_val = heapq.nlargest(1, enumerate(seq), key=itemgetter(1))
        idx = i_val[0][0]
        while result > total:
            seq[idx] = seq[idx] - 1
            result = sum(seq)
    return seq


# these two sequences were generated using createTraversal function
SEQ_ONE = [8, 4, 4, 2, 9, 2, 5]
SEQ_TWO = [2, 5, 4, 7, 7, 5, 4]


def make_bars_four_four(parent_list: list[list[str]]) -> list[str]:
    """
    takes in a raw sequence of music chunks (grouped in half note chunks)
    returns a flattened list of strings each containing a bar in four four
    """
    flatlist = [item for child_list in parent_list for item in child_list]
    # assume that we are dealing with chunks of halfnotes
    fours_chunks = [flatlist[x : x + 2] for x in range(0, len(flatlist), 2)]
    bars = [f"{x[0]} {x[1]}" for x in fours_chunks]
    return bars


FLUTE_ONE = [
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[0],  # 8
    ["r4 e''8-.\\fp r8"] * SEQ_ONE[1], # 4
    ["r4 e''8-.\\fp r8"] * SEQ_ONE[2], # 4
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[3],  # 2 
    ["r4 c''8-.\\fp r8"] * SEQ_ONE[4], # 9 
    ["r4 c''8-.\\fp r8"] * SEQ_ONE[5], # 2
    ["r4 b'8-.\\fp r8"] * SEQ_ONE[6],  # 5
]

FLUTE_ONE_BARS = make_bars_four_four(FLUTE_ONE)
# prepend dynamics to first bar

FLUTE_TWO = [
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[0],
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[1],
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[2],
    ["r4 e'8-.\\fp r8"] * SEQ_ONE[3],
    ["r4 f'8-.\\fp r8"] * SEQ_ONE[4],
    ["r4 f'8-.\\fp r8"] * SEQ_ONE[5],
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[6],
]

FLUTE_TWO_BARS = make_bars_four_four(FLUTE_TWO)

OB_SEQ = [7, 4, 8, 4, 4, 4, 4, 6, 6, 9, 4, 4, 4]
OBOE_ONE = [
    "r1",
    "r2. bf''4~ \\ppp",
    "bf''2. a''4~",
    "a''1~",
    "a''2. r4",  # end 8 start 4
    "r2. g''4~",
    "g''2. fs''4~",
    "fs''2. ef''4~",
    "ef''2. r4",
    "r1",
    "r4 d''2.~",
    "d''2. c''4~",
    "c''1",
    "c''1",
    "bf'1",
    "a'1",
    "g'1",
]  # should total 68 beats

OBOE_TWO_SEQ = [4, 2, 5, 4, 2]

OBOE_TWO = [
    "r1",
    # "r2 bf'16(\\ppp d'' bf' d'' bf' d'' bf' d''",
    """r4 
               \\featheredBeamRight 
               bf'16\\ppp[ d'' bf' d''
               bf'32 d'' bf' d''
               bf' d'' bf' d''
               bf' d'' bf' d''
               bf' d'' bf' d'']
               \\featheredBeamLeft
               bf'[ d'' bf' d''
               bf' d'' bf' d''
               bf' d'' bf' d''
               bf' d'' bf' d''
               bf'16 d'' bf' d'']
               r4
            """,
    """r2.
               \\featheredBeamRight
               bf'16[ d'' bf' d'']
               \\featheredBeamLeft
               bf'16[ d'' bf' d'']
               r2.
            """,
    """r4 
               \\featheredBeamRight
               g'16[ a' g' a'] 
               \\featheredBeamLeft
               g'16[ a' g' a'] 
               r4
            """,
    "r1",
    """\\featheredBeamRight
               ef'16[ fs' ef' fs' ef'16 fs' ef' fs']
               \\featheredBeamLeft
               ef'16[ fs' ef' fs' ef'16 fs' ef' fs']
            """,
    """r2 
               \\featheredBeamRight
               a'16[ c'' a' c'' 
               a'32 c'' a' c''
               a' c'' a' c'']
            """,
    """\\featheredBeamLeft
               a'32[ c'' a' c'' 
               a' c'' a' c'' 
               a'16 c'' a' c'' 
               a'16 c'' a' c''] r4
            """,
    """r4 
               \\featheredBeamRight
               a'16[ c'' a' c'' a'16 c'' a' c'' 
               a'32 c'' a' c''
               a' c'' a' c'']
            """,
    """\\featheredBeamLeft
               a'16[ c'' a' c''] 
               r2 
               \\featheredBeamRight
               c''32[ d'' c'' d''
               c'' d'' c'' d'']
            """,
    """\\featheredBeamLeft
               c''32[ d'' c'' d'' 
               c'' d'' c'' d''
               c''16 d'' c'' d''
               c''16 d'' c'' d'' c''16 d'' c'' d'']
            """,
    "r1",
    """\\featheredBeamRight
               bf'16[ d'' bf' d''] 
               \\featheredBeamLeft
               bf'16[ d'' bf' d''] 
               r2
            """,
    """r2 
               \\featheredBeamRight
               b'16[ d'' b' d'']
               \\featheredBeamLeft
               b'16[ d'' b' d'']
            """,
    """\\featheredBeamRight
               c''16[ d'' c'' d'' c''16 d'' c'' d'']
               \\featheredBeamLeft
               c''16[ d'' c'' d'' c''16 d'' c'' d'']
            """,
]


CLARINET_ONE = [
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[0],
    ["r4 cs''8-.\\fp r8"] * SEQ_ONE[1],
    ["r4 c''8-.\\fp r8"] * SEQ_ONE[2],
    ["r4 g'8-.\\fp r8"] * SEQ_ONE[3],
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[4],
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[5],
    ["r4 b'8-.\\fp r8"] * SEQ_ONE[6],
]

CLARINET_ONE_BARS = make_bars_four_four(CLARINET_ONE)

CLARINET_TWO = [
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[0],
    ["r4 a8-.\\fp r8"] * SEQ_ONE[1],
    ["r4 a8-.\\fp r8"] * SEQ_ONE[2],
    ["r4 c'8-.\\fp r8"] * SEQ_ONE[3],
    ["r4 e'8-.\\fp r8"] * SEQ_ONE[4],
    ["r4 d'8-.\\fp r8"] * SEQ_ONE[5],
    ["r4 a'8-.\\fp r8"] * SEQ_ONE[6],
]

CLARINET_TWO_BARS = make_bars_four_four(CLARINET_TWO)

BASSOON = [
    "r1",
    "r1",
    "r4 r8 e'8(\\pp a' e' a--) e'(",
    "d'8 bf a e) a( e a4)",
    "r1",
    "r4 r8 e'8( a' e' a--) e'(",
    "bf8 g a e) a( e a4)",
    "r4 r8 e'8( a' e' a--) fs'(",
    "ef'8 e') a( e a e a4)",
    "r1",
    "r4 r8 g8( c' g c--) a(",
    "g8 c g,) c( g c c,4)",
    "r4 r8 c'8( f' c' f) c'(",
    "f8 e d f) c( f f,4)",
    "r1",
    "r4 r8 c'8( a d' a d)",
    "d'8( c' b a) d( a, d,4)",
]

HN1 = [
    "r1",
    "r4 bf'2.\\ppp ~",
    "bf'2. r4",
    "r2. bf'4\\ppp ~",
    "bf'4 2.",
    "r4 g'2\\ppp r4",
    "r1",
    "ef'1\\ppp",
    "r2 a'2\\ppp ~",
    "a'2. r4",
    "r4 a'2.\\ppp ~",
    "a'4 r2 c''4\\ppp ~",
    "c''1",
    "r1",
    "bf'2\\ppp r2",
    "r2 c''2\\ppp ~",
    "c''1"
]

HN2 = [
    "r1",
    "r4 d'2.\\ppp ~",
    "d'2. r4",
    "r2. d'4\\ppp ~",
    "d'4 2.",
    "r4 a'2\\ppp r4",
    "r1",
    "fs'1\\ppp",
    "r2 c'2\\ppp ~",
    "c'2. r4",
    "r4 d'2.\\ppp ~",
    "d'4 r2 d'4\\ppp ~",
    "d'1",
    "r1",
    "d'2\\ppp r2",
    "r2 c'2\\ppp ~",
    "c'1"
]

HN3 = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1"
]

HN4 = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1"
]

TRP1 = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1"
]

TRP2 = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1"
]

TRB = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1"
]

TUBA = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r1"
]





TIMP = [
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1",
    "R1"
]

VIBES = [
    "r1",
    "<d' bf'>8\\ppp^\\markup\"ord. med. mallets\" <d' bf'>8 <d' bf'>8 <d' bf'>8 r4 <d' bf'>8 <d' bf'>8",
    "<d' a' bf'>8 <d' a' bf'>8 <d' a' bf'>8 <d' a' bf'>8 r4 <d' a' bf'>8 <d' a' bf'>8",
    "<d' a' bf'>8 <d' a' bf'>8 <d' a' bf'>8 <d' a' bf'>8 r4 <d' a' bf'>8 <d' a' bf'>8",
    "<d' a' bf'>8 <d' a' bf'>8 <d' a' bf'>8 <d' a' bf'>8 r4 <d' a' bf'>8 <d' a' bf'>8",
    "<d' g' bf'>8 <d' g' bf'>8 <d' g' bf'>8 <d' g' bf'>8 r4 <d' g' bf'>8 <d' g' bf'>8",
    "r1",
    "r4 <ef' fs' a''>8 <ef' fs' a''>8 <ef' fs' a''>8 <ef' fs' a''>8 <ef' fs' a''>8 <ef' fs' a''>8",
    "r4 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8",
    "r4 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8",
    "r4 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8 <c' a' a''>8",
    "r4 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8",
    "r4 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8 <c' c'' d''>8",
    "r1",
    "r4 <d' bf' d''>8 <d' bf' d''>8 <d' bf' d''>8 <d' bf' d''>8 <d' bf' d''>8 <d' bf' d''>8",
    "r4 <d' d''>8 <d' d''>8 <d' d''>8 <d' d''>8 <d' d''>8 <d' d''>8",
    "r4 <c' c''>8 <c' c''>8 <c' c''>8 <c' c''>8 <c' c''>8 <c' c''>8",
]


HARP = [
    "<a a'>4\\f r4 <a' a''>4",
    "r4 <a a'>4 r4 <a' a''>4",
    "r4 <a a'>4 r4 <a' a''>4",
    "r4 <a a'>4 r4 <a' a''>4",
    "r4 <a a' cs'' e''>4 r4 <a' a'' cs''' e'''>4",
    "r4 <a a' cs'' e''>4 r4 <a' a'' cs''' e'''>4",
    "<a a' c'' e''>4 r4 <a' a'' c''' e'''>4",
    "r4 <a a' c'' e''>4 r4 <a' a'' c''' e'''>4",
    "r4 <c'' e'' g'' a''>4 r4 <c'' e'' g'' a''>4",
    "r4 <e'' f'' a'' c'''> r4 <e'' f'' a'' c'''>4",
    "r4 <e'' f'' a'' c'''> r4 <e'' f'' a'' c'''>4",
    "r4 <e'' f'' a'' c'''> r4 <e'' f'' a'' c'''>4",
    "r4 <e'' f'' a'' c'''> r4 <e'' f'' a'' c'''>4",
    "r4 <e'' f'' a'' c'''> r4 <d'' f'' a'' c'''>4",
    "r4 <e'' f'' a'' c'''> r4 <a' b' a'' b''>4",
    "r4 <a' b' a'' b''>4 r4 <a' b' a'' b''>4 ",
    "r4 <a' b' a'' b''>4 r4 <a' b' a'' b''>4 ",
]

VIOLIN_ONE = [
    "<a'' a'''>8\\pppp^\\markup\"Divisi. pizz.\" <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 r4 <a'' a'''>8 <a'' a'''>8",
    "<a'' a'''>8 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 r4 <a'' a'''>8 <a'' a'''>8",
    "<a'' a'''>8 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 r4 <a'' a'''>8 <a'' a'''>8",
    "<a'' a'''>8 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 r4 <a'' a'''>8 <a'' a'''>8",
    "<cs''' a'''>8 <cs''' a'''>8 <cs''' a'''>8 <cs''' a'''>8 r4 <cs''' a'''>8 <cs''' a'''>8",
    "<cs''' a'''>8 <cs''' a'''>8 <cs''' a'''>8 <cs''' a'''>8 r4 <cs''' a'''>8 <cs''' a'''>8",
    "r1",
    "r1",
    "r4 <g''' a'''>8 <g''' a'''>8 <g''' a'''>8 <g''' a'''>8 <g''' a'''>8 <g''' a'''>8",
    "r4 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8",
    "r4 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8",
    "r4 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8",
    "r4 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8",
    "r4 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8",
    "r4 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8 <f''' a'''>8",
    "r4 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8 <a'' a'''>8",
    "r1^\\markup\"Unisoni. arco.\" "
]

VIOLIN_TWO = [
    "<a' a''>8\\pppp^\\markup\"Divisi. pizz.\" <a' a''>8 <a' a''>8 <a' a''>8 r4 <a' a''>8 <a' a''>8",
    "<a' a''>8 <a' a''>8 <a' a''>8 <a' a''>8 r4 <a' a''>8 <a' a''>8",
    "<a' a''>8 <a' a''>8 <a' a''>8 <a' a''>8 r4 <a' a''>8 <a' a''>8",
    "<a' a''>8 <a' a''>8 <a' a''>8 <a' a''>8 r4 <a' a''>8 <a' a''>8",
    "<e' cs''>8 <e' cs''>8 <e' cs''>8 <e' cs''>8 r4 <e' cs''>8 <e' cs''>8",
    "<e' cs''>8 <e' cs''>8 <e' cs''>8 <e' cs''>8 r4 <e' cs''>8 <e' cs''>8",
    "r1",
    "r1",
    "r4 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8",
    "r4 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8",
    "r4 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8",
    "r4 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8 <e' e''>8",
    "r4 <d' e''>8 <d' e''>8 <d' e''>8 <d' e''>8 <d' e''>8 <d' e''>8",
    "r4 <c' e''>8 <c' e''>8 <c' e''>8 <c' e''>8 <c' e''>8 <c' e''>8",
    "r4 <c' e''>8 <c' e''>8 <c' e''>8 <c' e''>8 <c' e''>8 <c' e''>8",
    "r4 <a' e''>8 <a' e''>8 <a' e''>8 <a' e''>8 <a' e''>8 <a' e''>8",
    "r1^\\markup\"Unisoni. arco.\" "
]

VIOLA = [
    "r1",
    "r1",
    "r1",
    "r1",
    "r1",
    "r4 r8 e''8(\\pp a'' e'' a'--) e''(",
    "bf'8 g' a' e') a'( e' a'4)",
    "r4 r8 e''8( a'' e'' a'--) fs''(",
    "ef''8 e'') a'( e' a' e' a'4)",
    "r1",
    "r1",
    "r1",
    "r4 r8 c''8(\\pp f'' c'' f') c''(",
    "f'8 e' d' f') c'( f' f4)",
    "r1",
    "r4 r8 c''8( a' d'' a' d')",
    "d''8( c'' b' a') d'( a d4)",
    ]


CELLO = [
        "r1",
        "r1",
        "r1",
        "r1",
        "r1",
        "r1",
        "r1",
        "r2 r4 e'4(\\pp",
        "a' e' a--) fs'(",
        "ef'4 e') a( e",
        "a4 e a2)",
        "r1",
        "r1",
        "r2 r4 c'4(",
        "f'4 c' f) c'(",
        "f4 e d f)",
        "c4( f f,2)",
        "r1",
        "r1",
]


CONTRABASS = [
    "r1",
    "r4^\\markup\"Divisi\" <d bf>2.\\ppp ~",
    "<d bf>2. r4",
    "r2. <d bf>4\\ppp ~",
    "<d bf>4 2.",
    "r4 <a, g>2\\ppp r4",
    "r1",
    "<fs, ef>1\\ppp",
    "r2 <c a>2\\ppp ~",
    "<c a>2. r4",
    "r4 <c a>2.\\ppp ~",
    "<c a>4 r2 <d c'>4\\ppp ~",
    "<d c'>1",
    "r1",
    "<d bf>2\\ppp r2",
    "r2 <d b>2\\ppp",
    "<c c'>1"
]


REST = ["R1" * 17]

COMMON_TIME = "\\time 4/4"


# segment is 17 bars long

CHORALE_PHRASES = {
    #######################################################################
    # data
    #######################################################################
    "chorale_Sa": FLUTE_ONE_BARS[0],
    "chorale_Sb": FLUTE_ONE_BARS[1],
    "chorale_Sc": FLUTE_ONE_BARS[2],
    "chorale_Sd": FLUTE_ONE_BARS[3],
    "chorale_Se": FLUTE_ONE_BARS[4],
    "chorale_Sf": FLUTE_ONE_BARS[5],
    "chorale_Sg": FLUTE_ONE_BARS[6],
    "chorale_Sh": FLUTE_ONE_BARS[7],
    "chorale_Si": FLUTE_ONE_BARS[8],
    "chorale_Sj": FLUTE_ONE_BARS[9],
    "chorale_Sk": FLUTE_ONE_BARS[10],
    "chorale_Sl": FLUTE_ONE_BARS[11],
    "chorale_Sm": FLUTE_ONE_BARS[12],
    "chorale_Sn": FLUTE_ONE_BARS[13],
    "chorale_So": FLUTE_ONE_BARS[14],
    "chorale_Sp": FLUTE_ONE_BARS[15],
    "chorale_Sq": FLUTE_ONE_BARS[16],
    "chorale_Aa": FLUTE_TWO_BARS[0],
    "chorale_Ab": FLUTE_TWO_BARS[1],
    "chorale_Ac": FLUTE_TWO_BARS[2],
    "chorale_Ad": FLUTE_TWO_BARS[3],
    "chorale_Ae": FLUTE_TWO_BARS[4],
    "chorale_Af": FLUTE_TWO_BARS[5],
    "chorale_Ag": FLUTE_TWO_BARS[6],
    "chorale_Ah": FLUTE_TWO_BARS[7],
    "chorale_Ai": FLUTE_TWO_BARS[8],
    "chorale_Aj": FLUTE_TWO_BARS[9],
    "chorale_Ak": FLUTE_TWO_BARS[10],
    "chorale_Al": FLUTE_TWO_BARS[11],
    "chorale_Am": FLUTE_TWO_BARS[12],
    "chorale_An": FLUTE_TWO_BARS[13],
    "chorale_Ao": FLUTE_TWO_BARS[14],
    "chorale_Ap": FLUTE_TWO_BARS[15],
    "chorale_Aq": FLUTE_TWO_BARS[16],
    "chorale_Ta": CLARINET_ONE_BARS[0],
    "chorale_Tb": CLARINET_ONE_BARS[1],
    "chorale_Tc": CLARINET_ONE_BARS[2],
    "chorale_Td": CLARINET_ONE_BARS[3],
    "chorale_Te": CLARINET_ONE_BARS[4],
    "chorale_Tf": CLARINET_ONE_BARS[5],
    "chorale_Tg": CLARINET_ONE_BARS[6],
    "chorale_Th": CLARINET_ONE_BARS[7],
    "chorale_Ti": CLARINET_ONE_BARS[8],
    "chorale_Tj": CLARINET_ONE_BARS[9],
    "chorale_Tk": CLARINET_ONE_BARS[10],
    "chorale_Tl": CLARINET_ONE_BARS[11],
    "chorale_Tm": CLARINET_ONE_BARS[12],
    "chorale_Tn": CLARINET_ONE_BARS[13],
    "chorale_To": CLARINET_ONE_BARS[14],
    "chorale_Tp": CLARINET_ONE_BARS[15],
    "chorale_Tq": CLARINET_ONE_BARS[16],
    "chorale_Ba": CLARINET_TWO_BARS[0],
    "chorale_Bb": CLARINET_TWO_BARS[1],
    "chorale_Bc": CLARINET_TWO_BARS[2],
    "chorale_Bd": CLARINET_TWO_BARS[3],
    "chorale_Be": CLARINET_TWO_BARS[4],
    "chorale_Bf": CLARINET_TWO_BARS[5],
    "chorale_Bg": CLARINET_TWO_BARS[6],
    "chorale_Bh": CLARINET_TWO_BARS[7],
    "chorale_Bi": CLARINET_TWO_BARS[8],
    "chorale_Bj": CLARINET_TWO_BARS[9],
    "chorale_Bk": CLARINET_TWO_BARS[10],
    "chorale_Bl": CLARINET_TWO_BARS[11],
    "chorale_Bm": CLARINET_TWO_BARS[12],
    "chorale_Bn": CLARINET_TWO_BARS[13],
    "chorale_Bo": CLARINET_TWO_BARS[14],
    "chorale_Bp": CLARINET_TWO_BARS[15],
    "chorale_Bq": CLARINET_TWO_BARS[16],
}


def get_segment() -> dict:
    """
    does exactly what it says on the tin

    chorale := a fairly full chordal texture
    desc    := descant melody
    basn    := bassoon melody
    chords  := chords

    The whole section is laid out in a 17 bar chunk
    """
    time_sig = COMMON_TIME
    chorale_Sa = create_voice(CHORALE_PHRASES["chorale_Sa"], 0)
    chorale_Sb = create_voice(CHORALE_PHRASES["chorale_Sb"], 0)
    chorale_Sc = create_voice(CHORALE_PHRASES["chorale_Sc"], 0)
    chorale_Sd = create_voice(CHORALE_PHRASES["chorale_Sd"], 0)
    chorale_Se = create_voice(CHORALE_PHRASES["chorale_Se"], 0)
    chorale_Sf = create_voice(CHORALE_PHRASES["chorale_Sf"], 0)
    chorale_Sg = create_voice(CHORALE_PHRASES["chorale_Sg"], 0)
    chorale_Sh = create_voice(CHORALE_PHRASES["chorale_Sh"], 0)
    chorale_Si = create_voice(CHORALE_PHRASES["chorale_Si"], 0)
    chorale_Sj = create_voice(CHORALE_PHRASES["chorale_Sj"], 0)
    chorale_Sk = create_voice(CHORALE_PHRASES["chorale_Sk"], 0)
    chorale_Sl = create_voice(CHORALE_PHRASES["chorale_Sl"], 0)
    chorale_Sm = create_voice(CHORALE_PHRASES["chorale_Sm"], 0)
    chorale_Sn = create_voice(CHORALE_PHRASES["chorale_Sn"], 0)
    chorale_So = create_voice(CHORALE_PHRASES["chorale_So"], 0)
    chorale_Sp = create_voice(CHORALE_PHRASES["chorale_Sp"], 0)
    chorale_Sq = create_voice(CHORALE_PHRASES["chorale_Sq"], 0)
    chorale_Aa = create_voice(CHORALE_PHRASES["chorale_Aa"], 0)
    chorale_Ab = create_voice(CHORALE_PHRASES["chorale_Ab"], 0)
    chorale_Ac = create_voice(CHORALE_PHRASES["chorale_Ac"], 0)
    chorale_Ad = create_voice(CHORALE_PHRASES["chorale_Ad"], 0)
    chorale_Ae = create_voice(CHORALE_PHRASES["chorale_Ae"], 0)
    chorale_Af = create_voice(CHORALE_PHRASES["chorale_Af"], 0)
    chorale_Ag = create_voice(CHORALE_PHRASES["chorale_Ag"], 0)
    chorale_Ah = create_voice(CHORALE_PHRASES["chorale_Ah"], 0)
    chorale_Ai = create_voice(CHORALE_PHRASES["chorale_Ai"], 0)
    chorale_Aj = create_voice(CHORALE_PHRASES["chorale_Aj"], 0)
    chorale_Ak = create_voice(CHORALE_PHRASES["chorale_Ak"], 0)
    chorale_Al = create_voice(CHORALE_PHRASES["chorale_Al"], 0)
    chorale_Am = create_voice(CHORALE_PHRASES["chorale_Am"], 0)
    chorale_An = create_voice(CHORALE_PHRASES["chorale_An"], 0)
    chorale_Ao = create_voice(CHORALE_PHRASES["chorale_Ao"], 0)
    chorale_Ap = create_voice(CHORALE_PHRASES["chorale_Ap"], 0)
    chorale_Aq = create_voice(CHORALE_PHRASES["chorale_Aq"], 0)
    chorale_Ta = create_voice(CHORALE_PHRASES["chorale_Ta"], 0)
    chorale_Tb = create_voice(CHORALE_PHRASES["chorale_Tb"], 0)
    chorale_Tc = create_voice(CHORALE_PHRASES["chorale_Tc"], 0)
    chorale_Td = create_voice(CHORALE_PHRASES["chorale_Td"], 0)
    chorale_Te = create_voice(CHORALE_PHRASES["chorale_Te"], 0)
    chorale_Tf = create_voice(CHORALE_PHRASES["chorale_Tf"], 0)
    chorale_Tg = create_voice(CHORALE_PHRASES["chorale_Tg"], 0)
    chorale_Th = create_voice(CHORALE_PHRASES["chorale_Th"], 0)
    chorale_Ti = create_voice(CHORALE_PHRASES["chorale_Ti"], 0)
    chorale_Tj = create_voice(CHORALE_PHRASES["chorale_Tj"], 0)
    chorale_Tk = create_voice(CHORALE_PHRASES["chorale_Tk"], 0)
    chorale_Tl = create_voice(CHORALE_PHRASES["chorale_Tl"], 0)
    chorale_Tm = create_voice(CHORALE_PHRASES["chorale_Tm"], 0)
    chorale_Tn = create_voice(CHORALE_PHRASES["chorale_Tn"], 0)
    chorale_To = create_voice(CHORALE_PHRASES["chorale_To"], 0)
    chorale_Tp = create_voice(CHORALE_PHRASES["chorale_Tp"], 0)
    chorale_Tq = create_voice(CHORALE_PHRASES["chorale_Tq"], 0)
    chorale_Ba = create_voice(CHORALE_PHRASES["chorale_Ba"], 0)
    chorale_Bb = create_voice(CHORALE_PHRASES["chorale_Bb"], 0)
    chorale_Bc = create_voice(CHORALE_PHRASES["chorale_Bc"], 0)
    chorale_Bd = create_voice(CHORALE_PHRASES["chorale_Bd"], 0)
    chorale_Be = create_voice(CHORALE_PHRASES["chorale_Be"], 0)
    chorale_Bf = create_voice(CHORALE_PHRASES["chorale_Bf"], 0)
    chorale_Bg = create_voice(CHORALE_PHRASES["chorale_Bg"], 0)
    chorale_Bh = create_voice(CHORALE_PHRASES["chorale_Bh"], 0)
    chorale_Bi = create_voice(CHORALE_PHRASES["chorale_Bi"], 0)
    chorale_Bj = create_voice(CHORALE_PHRASES["chorale_Bj"], 0)
    chorale_Bk = create_voice(CHORALE_PHRASES["chorale_Bk"], 0)
    chorale_Bl = create_voice(CHORALE_PHRASES["chorale_Bl"], 0)
    chorale_Bm = create_voice(CHORALE_PHRASES["chorale_Bm"], 0)
    chorale_Bn = create_voice(CHORALE_PHRASES["chorale_Bn"], 0)
    chorale_Bo = create_voice(CHORALE_PHRASES["chorale_Bo"], 0)
    chorale_Bp = create_voice(CHORALE_PHRASES["chorale_Bp"], 0)
    chorale_Bq = create_voice(CHORALE_PHRASES["chorale_Bq"], 0)
    desc_a = create_voice(OBOE_ONE[0], 0)
    desc_b = create_voice(OBOE_ONE[1], 0)
    desc_c = create_voice(OBOE_ONE[2], 0)
    desc_d = create_voice(OBOE_ONE[3], 0)
    desc_e = create_voice(OBOE_ONE[4], 0)
    desc_f = create_voice(OBOE_ONE[5], 0)
    desc_g = create_voice(OBOE_ONE[6], 0)
    desc_h = create_voice(OBOE_ONE[7], 0)
    desc_i = create_voice(OBOE_ONE[8], 0)
    desc_j = create_voice(OBOE_ONE[9], 0)
    desc_k = create_voice(OBOE_ONE[10], 0)
    desc_l = create_voice(OBOE_ONE[11], 0)
    desc_m = create_voice(OBOE_ONE[12], 0)
    desc_n = create_voice(OBOE_ONE[13], 0)
    desc_o = create_voice(OBOE_ONE[14], 0)
    desc_p = create_voice(OBOE_ONE[15], 0)
    desc_q = create_voice(OBOE_ONE[16], 0)
    orn_a = OBOE_TWO[0]
    orn_b = OBOE_TWO[1]
    orn_c = OBOE_TWO[2]
    orn_d = OBOE_TWO[3]
    orn_e = OBOE_TWO[4]
    orn_f = OBOE_TWO[5]
    orn_g = OBOE_TWO[6]
    orn_h = OBOE_TWO[7]
    orn_i = OBOE_TWO[8]
    orn_j = OBOE_TWO[9]
    orn_k = OBOE_TWO[10]
    orn_l = OBOE_TWO[11]
    orn_m = OBOE_TWO[12]
    orn_n = OBOE_TWO[13]
    orn_o = OBOE_TWO[14]
    bsn_a = create_voice(BASSOON[0], 0)
    bsn_b = create_voice(BASSOON[1], 0)
    bsn_c = create_voice(BASSOON[2], 0)
    bsn_d = create_voice(BASSOON[3], 0)
    bsn_e = create_voice(BASSOON[4], 0)
    bsn_f = create_voice(BASSOON[5], 0)
    bsn_g = create_voice(BASSOON[6], 0)
    bsn_h = create_voice(BASSOON[7], 0)
    bsn_i = create_voice(BASSOON[8], 0)
    bsn_j = create_voice(BASSOON[9], 0)
    bsn_k = create_voice(BASSOON[10], 0)
    bsn_l = create_voice(BASSOON[11], 0)
    bsn_m = create_voice(BASSOON[12], 0)
    bsn_n = create_voice(BASSOON[13], 0)
    bsn_o = create_voice(BASSOON[14], 0)
    bsn_p = create_voice(BASSOON[15], 0)
    bsn_q = create_voice(BASSOON[16], 0)

    hn1_a = HN1[0]
    hn1_b = HN1[1]
    hn1_c = HN1[2]
    hn1_d = HN1[3]
    hn1_e = HN1[4]
    hn1_f = HN1[5]
    hn1_g = HN1[6]
    hn1_h = HN1[7]
    hn1_i = HN1[8]
    hn1_j = HN1[9]
    hn1_k = HN1[10]
    hn1_l = HN1[11]
    hn1_m = HN1[12]
    hn1_n = HN1[13]
    hn1_o = HN1[14]
    hn1_p = HN1[15]
    hn1_q = HN1[16]
    
    hn2_a = HN2[0]
    hn2_b = HN2[1]
    hn2_c = HN2[2]
    hn2_d = HN2[3]
    hn2_e = HN2[4]
    hn2_f = HN2[5]
    hn2_g = HN2[6]
    hn2_h = HN2[7]
    hn2_i = HN2[8]
    hn2_j = HN2[9]
    hn2_k = HN2[10]
    hn2_l = HN2[11]
    hn2_m = HN2[12]
    hn2_n = HN2[13]
    hn2_o = HN2[14]
    hn2_p = HN2[15]
    hn2_q = HN2[16]
    
    hn3_a = create_voice(HN3[0], 0)
    hn3_b = create_voice(HN3[1], 0)
    hn3_c = create_voice(HN3[2], 0)
    hn3_d = create_voice(HN3[3], 0)
    hn3_e = create_voice(HN3[4], 0)
    hn3_f = create_voice(HN3[5], 0)
    hn3_g = create_voice(HN3[6], 0)
    hn3_h = create_voice(HN3[7], 0)
    hn3_i = create_voice(HN3[8], 0)
    hn3_j = create_voice(HN3[9], 0)
    hn3_k = create_voice(HN3[10], 0)
    hn3_l = create_voice(HN3[11], 0)
    hn3_m = create_voice(HN3[12], 0)
    hn3_n = create_voice(HN3[13], 0)
    hn3_o = create_voice(HN3[14], 0)
    hn3_p = create_voice(HN3[15], 0)
    hn3_q = create_voice(HN3[16], 0)
    
    hn4_a = create_voice(HN4[0], 0)
    hn4_b = create_voice(HN4[1], 0)
    hn4_c = create_voice(HN4[2], 0)
    hn4_d = create_voice(HN4[3], 0)
    hn4_e = create_voice(HN4[4], 0)
    hn4_f = create_voice(HN4[5], 0)
    hn4_g = create_voice(HN4[6], 0)
    hn4_h = create_voice(HN4[7], 0)
    hn4_i = create_voice(HN4[8], 0)
    hn4_j = create_voice(HN4[9], 0)
    hn4_k = create_voice(HN4[10], 0)
    hn4_l = create_voice(HN4[11], 0)
    hn4_m = create_voice(HN4[12], 0)
    hn4_n = create_voice(HN4[13], 0)
    hn4_o = create_voice(HN4[14], 0)
    hn4_p = create_voice(HN4[15], 0)
    hn4_q = create_voice(HN4[16], 0)
    
    trp1_a = create_voice(TRP1[0], 0)
    trp1_b = create_voice(TRP1[1], 0)
    trp1_c = create_voice(TRP1[2], 0)
    trp1_d = create_voice(TRP1[3], 0)
    trp1_e = create_voice(TRP1[4], 0)
    trp1_f = create_voice(TRP1[5], 0)
    trp1_g = create_voice(TRP1[6], 0)
    trp1_h = create_voice(TRP1[7], 0)
    trp1_i = create_voice(TRP1[8], 0)
    trp1_j = create_voice(TRP1[9], 0)
    trp1_k = create_voice(TRP1[10], 0)
    trp1_l = create_voice(TRP1[11], 0)
    trp1_m = create_voice(TRP1[12], 0)
    trp1_n = create_voice(TRP1[13], 0)
    trp1_o = create_voice(TRP1[14], 0)
    trp1_p = create_voice(TRP1[15], 0)
    trp1_q = create_voice(TRP1[16], 0)
    
    trp2_a = create_voice(TRP2[0], 0)
    trp2_b = create_voice(TRP2[1], 0)
    trp2_c = create_voice(TRP2[2], 0)
    trp2_d = create_voice(TRP2[3], 0)
    trp2_e = create_voice(TRP2[4], 0)
    trp2_f = create_voice(TRP2[5], 0)
    trp2_g = create_voice(TRP2[6], 0)
    trp2_h = create_voice(TRP2[7], 0)
    trp2_i = create_voice(TRP2[8], 0)
    trp2_j = create_voice(TRP2[9], 0)
    trp2_k = create_voice(TRP2[10], 0)
    trp2_l = create_voice(TRP2[11], 0)
    trp2_m = create_voice(TRP2[12], 0)
    trp2_n = create_voice(TRP2[13], 0)
    trp2_o = create_voice(TRP2[14], 0)
    trp2_p = create_voice(TRP2[15], 0)
    trp2_q = create_voice(TRP2[16], 0)
    
    trb_a = create_voice(TRB[0], 0)
    trb_b = create_voice(TRB[1], 0)
    trb_c = create_voice(TRB[2], 0)
    trb_d = create_voice(TRB[3], 0)
    trb_e = create_voice(TRB[4], 0)
    trb_f = create_voice(TRB[5], 0)
    trb_g = create_voice(TRB[6], 0)
    trb_h = create_voice(TRB[7], 0)
    trb_i = create_voice(TRB[8], 0)
    trb_j = create_voice(TRB[9], 0)
    trb_k = create_voice(TRB[10], 0)
    trb_l = create_voice(TRB[11], 0)
    trb_m = create_voice(TRB[12], 0)
    trb_n = create_voice(TRB[13], 0)
    trb_o = create_voice(TRB[14], 0)
    trb_p = create_voice(TRB[15], 0)
    trb_q = create_voice(TRB[16], 0)
    
    
    tuba_a = create_voice(TUBA[0], 0)
    tuba_b = create_voice(TUBA[1], 0)
    tuba_c = create_voice(TUBA[2], 0)
    tuba_d = create_voice(TUBA[3], 0)
    tuba_e = create_voice(TUBA[4], 0)
    tuba_f = create_voice(TUBA[5], 0)
    tuba_g = create_voice(TUBA[6], 0)
    tuba_h = create_voice(TUBA[7], 0)
    tuba_i = create_voice(TUBA[8], 0)
    tuba_j = create_voice(TUBA[9], 0)
    tuba_k = create_voice(TUBA[10], 0)
    tuba_l = create_voice(TUBA[11], 0)
    tuba_m = create_voice(TUBA[12], 0)
    tuba_n = create_voice(TUBA[13], 0)
    tuba_o = create_voice(TUBA[14], 0)
    tuba_p = create_voice(TUBA[15], 0)
    tuba_q = create_voice(TUBA[16], 0)

    
    vibes_a = create_voice(VIBES[0], 0)
    vibes_b = create_voice(VIBES[1], 0)
    vibes_c = create_voice(VIBES[2], 0)
    vibes_d = create_voice(VIBES[3], 0)
    vibes_e = create_voice(VIBES[4], 0)
    vibes_f = create_voice(VIBES[5], 0)
    vibes_g = create_voice(VIBES[6], 0)
    vibes_h = create_voice(VIBES[7], 0)
    vibes_i = create_voice(VIBES[8], 0)
    vibes_j = create_voice(VIBES[9], 0)
    vibes_k = create_voice(VIBES[10], 0)
    vibes_l = create_voice(VIBES[11], 0)
    vibes_m = create_voice(VIBES[12], 0)
    vibes_n = create_voice(VIBES[13], 0)
    vibes_o = create_voice(VIBES[14], 0)
    vibes_p = create_voice(VIBES[15], 0)
    vibes_q = create_voice(VIBES[16], 0)

    
    timp_a = create_voice(TIMP[0], 0)
    timp_b = create_voice(TIMP[1], 0)
    timp_c = create_voice(TIMP[2], 0)
    timp_d = create_voice(TIMP[3], 0)
    timp_e = create_voice(TIMP[4], 0)
    timp_f = create_voice(TIMP[5], 0)
    timp_g = create_voice(TIMP[6], 0)
    timp_h = create_voice(TIMP[7], 0)
    timp_i = create_voice(TIMP[8], 0)
    timp_j = create_voice(TIMP[9], 0)
    timp_k = create_voice(TIMP[10], 0)
    timp_l = create_voice(TIMP[11], 0)
    timp_m = create_voice(TIMP[12], 0)
    timp_n = create_voice(TIMP[13], 0)
    timp_o = create_voice(TIMP[14], 0)
    timp_p = create_voice(TIMP[15], 0)
    timp_q = create_voice(TIMP[16], 0)
    
    
    chord_a = create_voice(HARP[0], 0)
    chord_b = create_voice(HARP[1], 0)
    chord_c = create_voice(HARP[2], 0)
    chord_d = create_voice(HARP[3], 0)
    chord_e = create_voice(HARP[4], 0)
    chord_f = create_voice(HARP[5], 0)
    chord_g = create_voice(HARP[6], 0)
    chord_h = create_voice(HARP[7], 0)
    chord_i = create_voice(HARP[8], 0)
    chord_j = create_voice(HARP[9], 0)
    chord_k = create_voice(HARP[10], 0)
    chord_l = create_voice(HARP[11], 0)
    chord_m = create_voice(HARP[12], 0)
    chord_n = create_voice(HARP[13], 0)
    chord_o = create_voice(HARP[14], 0)
    chord_p = create_voice(HARP[15], 0)
    chord_q = create_voice(HARP[16], 0)
    
    vn1_a = VIOLIN_ONE[0]
    vn1_b = VIOLIN_ONE[1]
    vn1_c = create_voice(VIOLIN_ONE[2], 0)
    vn1_d = create_voice(VIOLIN_ONE[3], 0)
    vn1_e = create_voice(VIOLIN_ONE[4], 0)
    vn1_f = create_voice(VIOLIN_ONE[5], 0)
    vn1_g = create_voice(VIOLIN_ONE[6], 0)
    vn1_h = create_voice(VIOLIN_ONE[7], 0)
    vn1_i = create_voice(VIOLIN_ONE[8], 0)
    vn1_j = create_voice(VIOLIN_ONE[9], 0)
    vn1_k = create_voice(VIOLIN_ONE[10], 0)
    vn1_l = create_voice(VIOLIN_ONE[11], 0)
    vn1_m = create_voice(VIOLIN_ONE[12], 0)
    vn1_n = create_voice(VIOLIN_ONE[13], 0)
    vn1_o = create_voice(VIOLIN_ONE[14], 0)
    vn1_p = create_voice(VIOLIN_ONE[15], 0)
    vn1_q = create_voice(VIOLIN_ONE[16], 0)

    vn2_a = create_voice(VIOLIN_TWO[0], 0)
    vn2_b = create_voice(VIOLIN_TWO[1], 0)
    vn2_c = create_voice(VIOLIN_TWO[2], 0)
    vn2_d = create_voice(VIOLIN_TWO[3], 0)
    vn2_e = create_voice(VIOLIN_TWO[4], 0)
    vn2_f = create_voice(VIOLIN_TWO[5], 0)
    vn2_g = create_voice(VIOLIN_TWO[6], 0)
    vn2_h = create_voice(VIOLIN_TWO[7], 0)
    vn2_i = create_voice(VIOLIN_TWO[8], 0)
    vn2_j = create_voice(VIOLIN_TWO[9], 0)
    vn2_k = create_voice(VIOLIN_TWO[10], 0)
    vn2_l = create_voice(VIOLIN_TWO[11], 0)
    vn2_m = create_voice(VIOLIN_TWO[12], 0)
    vn2_n = create_voice(VIOLIN_TWO[13], 0)
    vn2_o = create_voice(VIOLIN_TWO[14], 0)
    vn2_p = create_voice(VIOLIN_TWO[15], 0)
    vn2_q = create_voice(VIOLIN_TWO[16], 0)

    
    va_a = create_voice(VIOLA[0], 0)
    va_b = create_voice(VIOLA[1], 0)
    va_c = create_voice(VIOLA[2], 0)
    va_d = create_voice(VIOLA[3], 0)
    va_e = create_voice(VIOLA[4], 0)
    va_f = create_voice(VIOLA[5], 0)
    va_g = create_voice(VIOLA[6], 0)
    va_h = create_voice(VIOLA[7], 0)
    va_i = create_voice(VIOLA[8], 0)
    va_j = create_voice(VIOLA[9], 0)
    va_k = create_voice(VIOLA[10], 0)
    va_l = create_voice(VIOLA[11], 0)
    va_m = create_voice(VIOLA[12], 0)
    va_n = create_voice(VIOLA[13], 0)
    va_o = create_voice(VIOLA[14], 0)
    va_p = create_voice(VIOLA[15], 0)
    va_q = create_voice(VIOLA[16], 0)
    vc_a = create_voice(CELLO[0], 0)
    vc_b = create_voice(CELLO[1], 0)
    vc_c = create_voice(CELLO[2], 0)
    vc_d = create_voice(CELLO[3], 0)
    vc_e = create_voice(CELLO[4], 0)
    vc_f = create_voice(CELLO[5], 0)
    vc_g = create_voice(CELLO[6], 0)
    vc_h = create_voice(CELLO[7], 0)
    vc_i = create_voice(CELLO[8], 0)
    vc_j = create_voice(CELLO[9], 0)
    vc_k = create_voice(CELLO[10], 0)
    vc_l = create_voice(CELLO[11], 0)
    vc_m = create_voice(CELLO[12], 0)
    vc_n = create_voice(CELLO[13], 0)
    vc_o = create_voice(CELLO[14], 0)
    vc_p = create_voice(CELLO[15], 0)
    vc_q = create_voice(CELLO[16], 0)    

    cb_a = CONTRABASS[0]
    cb_b = CONTRABASS[1]
    cb_c = CONTRABASS[2]
    cb_d = CONTRABASS[3]
    cb_e = CONTRABASS[4]
    cb_f = CONTRABASS[5]
    cb_g = CONTRABASS[6]
    cb_h = CONTRABASS[7]
    cb_i = CONTRABASS[8]
    cb_j = CONTRABASS[9]
    cb_k = CONTRABASS[10]
    cb_l = CONTRABASS[11]
    cb_m = CONTRABASS[12]
    cb_n = CONTRABASS[13]
    cb_o = CONTRABASS[14]
    cb_p = CONTRABASS[15]
    cb_q = CONTRABASS[16]
    
    rmark = "\\mark #6"

    harp_ped_one = "r4_\\markup { \\harp-pedal #\"-ovo-|----\" }" 
    harp_ped_two = "r4_\\markup { \\harp-pedal #\"-o--|----\" }"

    instruments = {
        "flOne": {
            "time_sig": time_sig,
            "rmark": rmark,
            "chorale_Sa": chorale_Sa,
            "chorale_Sb": chorale_Sb,
            "chorale_Sc": chorale_Sc,
            "chorale_Sd": chorale_Sd,
            "chorale_Se": chorale_Se,
            "chorale_Sf": chorale_Sf,
            "chorale_Sg": chorale_Sg,
            "chorale_Sh": chorale_Sh,
            "chorale_Si": chorale_Si,
            "chorale_Sj": chorale_Sj,
            "chorale_Sk": chorale_Sk,
            "chorale_Sl": chorale_Sl,
            "chorale_Sm": chorale_Sm,
            "chorale_Sn": chorale_Sn,
            "chorale_So": chorale_So,
            "chorale_Sp": chorale_Sp,
            "chorale_Sq": chorale_Sq,
        },
        "flTwo": {
            "time_sig": time_sig,
            "rmark": rmark,
            "chorale_Aa": chorale_Aa,
            "chorale_Ab": chorale_Ab,
            "chorale_Ac": chorale_Ac,
            "chorale_Ad": chorale_Ad,
            "chorale_Ae": chorale_Ae,
            "chorale_Af": chorale_Af,
            "chorale_Ag": chorale_Ag,
            "chorale_Ah": chorale_Ah,
            "chorale_Ai": chorale_Ai,
            "chorale_Aj": chorale_Aj,
            "chorale_Ak": chorale_Ak,
            "chorale_Al": chorale_Al,
            "chorale_Am": chorale_Am,
            "chorale_An": chorale_An,
            "chorale_Ao": chorale_Ao,
            "chorale_Ap": chorale_Ap,
            "chorale_Aq": chorale_Aq,
        },
        "obOne": {
            "time_sig": time_sig,
            "rmark": rmark,
            "desc_a": desc_a,
            "desc_b": desc_b,
            "desc_c": desc_c,
            "desc_d": desc_d,
            "desc_e": desc_e,
            "desc_f": desc_f,
            "desc_g": desc_g,
            "desc_h": desc_h,
            "desc_i": desc_i,
            "desc_j": desc_j,
            "desc_k": desc_k,
            "desc_l": desc_l,
            "desc_m": desc_m,
            "desc_n": desc_n,
            "desc_o": desc_o,
            "desc_p": desc_p,
            "desc_q": desc_q,
        },
        "obTwo": {
            "time_sig": time_sig,
            "rmark": rmark,
            "orn_a": orn_a,
            "orn_b": orn_b,
            "orn_c": orn_c,
            "orn_d": orn_d,
            "orn_e": orn_e,
            "orn_f": orn_f,
            "orn_g": orn_g,
            "orn_h": orn_h,
            "orn_i": orn_i,
            "orn_j": orn_j,
            "orn_k": orn_k,
            "orn_l": orn_l,
            "orn_m": orn_m,
            "orn_n": orn_n,
            "orn_o": orn_o,
        },
        "clOne": {
            "time_sig": time_sig,
            "rmark": rmark,
            "chorale_Ta": chorale_Ta,
            "chorale_Tb": chorale_Tb,
            "chorale_Tc": chorale_Tc,
            "chorale_Td": chorale_Td,
            "chorale_Te": chorale_Te,
            "chorale_Tf": chorale_Tf,
            "chorale_Tg": chorale_Tg,
            "chorale_Th": chorale_Th,
            "chorale_Ti": chorale_Ti,
            "chorale_Tj": chorale_Tj,
            "chorale_Tk": chorale_Tk,
            "chorale_Tl": chorale_Tl,
            "chorale_Tm": chorale_Tm,
            "chorale_Tn": chorale_Tn,
            "chorale_To": chorale_To,
            "chorale_Tp": chorale_Tp,
            "chorale_Tq": chorale_Tq,
        },
        "clTwo": {
            "time_sig": time_sig,
            "rmark": rmark,
            "chorale_Ba": chorale_Ba,
            "chorale_Bb": chorale_Bb,
            "chorale_Bc": chorale_Bc,
            "chorale_Bd": chorale_Bd,
            "chorale_Be": chorale_Be,
            "chorale_Bf": chorale_Bf,
            "chorale_Bg": chorale_Bg,
            "chorale_Bh": chorale_Bh,
            "chorale_Bi": chorale_Bi,
            "chorale_Bj": chorale_Bj,
            "chorale_Bk": chorale_Bk,
            "chorale_Bl": chorale_Bl,
            "chorale_Bm": chorale_Bm,
            "chorale_Bn": chorale_Bn,
            "chorale_Bo": chorale_Bo,
            "chorale_Bp": chorale_Bp,
            "chorale_Bq": chorale_Bq,
        },
        "bsn": {
            "time_sig": time_sig,
            "rmark": rmark,
            "rmark": rmark,
            "bsn_a": bsn_a,
            "bsn_b": bsn_b,
            "bsn_c": bsn_c,
            "bsn_d": bsn_d,
            "bsn_e": bsn_e,
            "bsn_f": bsn_f,
            "bsn_g": bsn_g,
            "bsn_h": bsn_h,
            "bsn_i": bsn_i,
            "bsn_j": bsn_j,
            "bsn_k": bsn_k,
            "bsn_l": bsn_l,
            "bsn_m": bsn_m,
            "bsn_n": bsn_n,
            "bsn_o": bsn_o,
            "bsn_p": bsn_p,
            "bsn_q": bsn_q,
        },
        "hrnOne" : {
            "time_sig": time_sig,
            "rmark": rmark,
            "hn1_a": hn1_a,
            "hn1_b": hn1_b,
            "hn1_c": hn1_c,
            "hn1_d": hn1_d,
            "hn1_e": hn1_e,
            "hn1_f": hn1_f,
            "hn1_g": hn1_g,
            "hn1_h": hn1_h,
            "hn1_i": hn1_i,
            "hn1_j": hn1_j,
            "hn1_k": hn1_k,
            "hn1_l": hn1_l,
            "hn1_m": hn1_m,
            "hn1_n": hn1_n,
            "hn1_o": hn1_o,
            "hn1_p": hn1_p,
            "hn1_q": hn1_q
        },
        "hrnTwo": {
            "time_sig": time_sig,
            "rmark": rmark,
            "hn2_a": hn2_a,
            "hn2_b": hn2_b,
            "hn2_c": hn2_c,
            "hn2_d": hn2_d,
            "hn2_e": hn2_e,
            "hn2_f": hn2_f,
            "hn2_g": hn2_g,
            "hn2_h": hn2_h,
            "hn2_i": hn2_i,
            "hn2_j": hn2_j,
            "hn2_k": hn2_k,
            "hn2_l": hn2_l,
            "hn2_m": hn2_m,
            "hn2_n": hn2_n,
            "hn2_o": hn2_o,
            "hn2_p": hn2_p,
            "hn2_q": hn2_q
        },
        "hrnThree" : {
            "time_sig": time_sig,
            "rmark": rmark,
            "hrnThree_GP": "R1*17",
        },
        "hrnFour": {
            "time_sig": time_sig,
            "rmark": rmark,
            "hrnFour_GP": "R1*17",
        },
        "trpOne": {
            "time_sig": time_sig,
            "rmark": rmark,
            "trpOne_GP": "R1*17"
        },
        "trpTwo": {
            "time_sig": time_sig,
            "rmark": rmark,
            "trpTwo_GP": "R1*17"
        },
        "trb": {
            "time_sig": time_sig,
            "rmark": rmark,
            "trb_GP": "R1*17"
        },
        "tuba": {
            "time_sig": time_sig,
            "rmark": rmark,
            "tuba_GP": "R1*17",
                 },
        "harp": {
            "time_sig": time_sig,
            "rmark": rmark,
            "harp_ped_one": harp_ped_one,
            "chord_a": chord_a,
            "chord_b": chord_b,
            "chord_c": chord_c,
            "chord_d": chord_d,
            "chord_e": chord_e,
            "chord_f": chord_f,
            "harp_ped_two": harp_ped_two,
            "chord_g": chord_g,
            "chord_h": chord_h,
            "chord_i": chord_i,
            "chord_j": chord_j,
            "chord_k": chord_k,
            "chord_l": chord_l,
            "chord_m": chord_m,
            "chord_n": chord_n,
            "chord_o": chord_o,
            "chord_p": chord_p,
            "chord_q": chord_q,
        },
        "vibes": {
                "time_sig": time_sig, 
                "rmark": rmark,
                "vibes_a": vibes_a,
                "vibes_b": vibes_b,
                "vibes_c": vibes_c,
                "vibes_d": vibes_d,
                "vibes_e": vibes_e,
                "vibes_f": vibes_f,
                "vibes_g": vibes_g,
                "vibes_h": vibes_h,
                "vibes_i": vibes_i,
                "vibes_j": vibes_j,
                "vibes_k": vibes_k,
                "vibes_l": vibes_l,
                "vibes_m": vibes_m,
                "vibes_n": vibes_n,
                "vibes_o": vibes_o,
                "vibes_p": vibes_p,
                "vibes_q": vibes_q,
                },
        "timp": {
                "time_sig": time_sig, 
                "rmark": rmark,
                 "timp_GP": "R1*17"
                },
        "violinOne": {
                "time_sig": time_sig, 
                "rmark": rmark,
                "vn1_a": vn1_a,
                "vn1_b": vn1_b,
                "vn1_c": vn1_c,
                "vn1_d": vn1_d,
                "vn1_e": vn1_e,
                "vn1_f": vn1_f,
                "vn1_g": vn1_g,
                "vn1_h": vn1_h,
                "vn1_i": vn1_i,
                "vn1_j": vn1_j,
                "vn1_k": vn1_k,
                "vn1_l": vn1_l,
                "vn1_m": vn1_m,
                "vn1_n": vn1_n,
                "vn1_o": vn1_o,
                "vn1_p": vn1_p,
                "vn1_q": vn1_q,
                },
        "violinTwo": {
                "time_sig": time_sig, 
                "rmark": rmark,
                "vn2_a": vn2_a,
                "vn2_b": vn2_b,
                "vn2_c": vn2_c,
                "vn2_d": vn2_d,
                "vn2_e": vn2_e,
                "vn2_f": vn2_f,
                "vn2_g": vn2_g,
                "vn2_h": vn2_h,
                "vn2_i": vn2_i,
                "vn2_j": vn2_j,
                "vn2_k": vn2_k,
                "vn2_l": vn2_l,
                "vn2_m": vn2_m,
                "vn2_n": vn2_n,
                "vn2_o": vn2_o,
                "vn2_p": vn2_p,
                "vn2_q": vn2_q,
                },
        "viola": {
                "time_sig": time_sig, 
                "rmark": rmark,
                "va_a": va_a,
                "va_b": va_b,
                "va_c": va_c,
                "va_d": va_d,
                "va_e": va_e,
                "va_f": va_f,
                "va_g": va_g,
                "va_h": va_h,
                "va_i": va_i,
                "va_j": va_j,
                "va_k": va_k,
                "va_l": va_l,
                "va_m": va_m,
                "va_n": va_n,
                "va_o": va_o,
                "va_p": va_p,
                "va_q": va_q,
        },
        "cello": {
            "time_sig": time_sig,
            "rmark": rmark,
            "vc_a": vc_a,
            "vc_b": vc_b,
            "vc_c": vc_c,
            "vc_d": vc_d,
            "vc_e": vc_e,
            "vc_f": vc_f,
            "vc_g": vc_g,
            "vc_h": vc_h,
            "vc_i": vc_i,
            "vc_j": vc_j,
            "vc_k": vc_k,
            "vc_l": vc_l,
            "vc_m": vc_m,
            "vc_n": vc_n,
            "vc_o": vc_o,
            "vc_p": vc_p,
            "vc_q": vc_q,
        },
        "contrabass": {
                "time_sig": time_sig,
                "rmark": rmark,
                "cb_a": cb_a,
                "cb_b": cb_b,
                "cb_c": cb_c,
                "cb_d": cb_d,
                "cb_e": cb_e,
                "cb_f": cb_f,
                "cb_g": cb_g,
                "cb_h": cb_h,
                "cb_i": cb_i,
                "cb_j": cb_j,
                "cb_k": cb_k,
                "cb_l": cb_l,
                "cb_m": cb_m,
                "cb_n": cb_n,
                "cb_o": cb_o,
                "cb_p": cb_p,
                "cb_q": cb_q,
        },
        }
    return instruments


if __name__ == "__main__":
    outputheader()
    printmacros(MACROS)
    instruments = [
        "flOne",
        "flTwo",
        "obOne",
        "obTwo",
        "clOne",
        "clTwo",
        "bsn",
        "hrnOne",
        "hrnTwo",
        "hrnThree",
        "hrnFour",
        "trpOne",
        "trpTwo",
        "trb",
        "tuba",
        "harp",
        "vibes",
        "timp",
        "violinOne",
        "violinTwo",
        "viola",
        "cello",
        "contrabass",
    ]
    segment = "segment_chorale"
    generate_chunk(get_segment, instruments, segment)
