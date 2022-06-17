#!/usr/bin/python3

"""
wwindChorale.py: script to generate a short segment for woodwinds

usage: python3 wwindChorale.py > wwindChorale.ly
"""

import random
import heapq
from operator import itemgetter

from marana.tools import ( create_voice, 
                           outputheader, 
                           generate_chunk )

items = { 2, 3 }
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
    while (result < total):
        ridx = random.randrange(seqlen)
        val = random.sample(items, 1)
        seq[ridx] = seq[ridx] + val[0]
        result = sum(seq)
    # do some dirty tampering to round it down if we've overshot
    if (result > total):
        # track the index of the largest value incase we need to decrement
        i_val = heapq.nlargest(1, enumerate(seq), key=itemgetter(1))
        idx = i_val[0][0]
        while (result > total):
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
    fours_chunks = [flatlist[x:x+2] for x in range(0, len(flatlist), 2)]
    bars = [f"{x[0]} {x[1]}" for x in fours_chunks]
    return bars


FLUTE_ONE = [["r4 a'4--"] * SEQ_ONE[0], 
             ["r4 e''4--"] * SEQ_ONE[1],
             ["r4 e''4--"] * SEQ_ONE[2],
             ["r4 a'4--"] * SEQ_ONE[3],
             ["r4 c''4--"] * SEQ_ONE[4],
             ["r4 c''4--"] * SEQ_ONE[5],
             ["r4 b'4--"] * SEQ_ONE[6]]

FLUTE_ONE_BARS = make_bars_four_four(FLUTE_ONE)
# prepend dynamics to first bar
FLUTE_ONE_BARS[0] = "r4 a'4--\\mp r4 a'4--"

FLUTE_TWO = [["r4 a'4--"] * SEQ_ONE[0], 
             ["r4 a'4--"] * SEQ_ONE[1],
             ["r4 a'4--"] * SEQ_ONE[2],
             ["r4 e'4--"] * SEQ_ONE[3],
             ["r4 f'4--"] * SEQ_ONE[4],
             ["r4 f'4--"] * SEQ_ONE[5],
             ["r4 a'4--"] * SEQ_ONE[6]]

FLUTE_TWO_BARS = make_bars_four_four(FLUTE_TWO)
FLUTE_TWO_BARS[0] = "r4 a'4--\\mp r4 a'4--"

OB_SEQ = [7, 4, 8, 4, 4, 4, 4, 6, 6, 9, 4, 4, 4]
OBOE_ONE = ["r1",
            "r2. bf''4~ \\ppp",
            "bf''2. a''4~",
            "a''1~",
            "a''2. r4", # end 8 start 4
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
            "g'1"
            ] # should total 68 beats 

OBOE_TWO_SEQ = [4, 2, 5, 4, 2]

OBOE_TWO = ["r1",
            "r2 bf'16(\\ppp d'' bf' d'' bf' d'' bf' d''",
            """bf'16 d'' bf' d'' bf' d'' bf' d''
               bf'16 d'' bf' d'') r4""",
            "r2. bf'16( d'' bf' d''",
            "bf'16 d'' bf' d'') r2.",
            "r4 g'16( a' g' a' g'16 a' g' a') r4",
            "r1",
            """ef'16( fs' ef' fs' ef'16 fs' ef' fs' 
               ef'16 fs' ef' fs' ef'16 fs' ef' fs')""",
            "r2 a'16( c'' a' c'' a'16 c'' a' c''",
            """a'16 c'' a' c'' a'16 c'' a' c'' 
               a'16 c'' a' c'') r4""",
            """r4 a'16( c'' a' c'' a'16 c'' a' c'' 
                a'16 c'' a' c''""",
            "a'16 c'' a' c'') r2 c''16( d'' c'' d''",
            """c''16 d'' c'' d'' c''16 d'' c'' d''
               c''16 d'' c'' d'' c''16 d'' c'' d'')""",
            "r1",
            "bf'16( d'' bf' d'' bf'16 d'' bf' d'') r2",
            "r2 b'16( d'' b' d'' b'16 d'' b' d'')",
            """c''16( d'' c'' d'' c''16 d'' c'' d''
               c''16 d'' c'' d'' c''16 d'' c'' d'')""",
            ]


CLARINET_ONE = [["r4 a'4--"] * SEQ_ONE[0], 
                ["r4 cs''4--"] * SEQ_ONE[1],
                ["r4 c''4--"] * SEQ_ONE[2],
                ["r4 g'4--"] * SEQ_ONE[3],
                ["r4 a'4--"] * SEQ_ONE[4],
                ["r4 a'4--"] * SEQ_ONE[5],
                ["r4 b'4--"] * SEQ_ONE[6]]

CLARINET_ONE_BARS = make_bars_four_four(CLARINET_ONE)
CLARINET_ONE_BARS[0] = "r4 a'4--\\mp r4 a'4--"

CLARINET_TWO = [["r4 a'4--"] * SEQ_ONE[0], 
                ["r4 a4--"] * SEQ_ONE[1],
                ["r4 a4--"] * SEQ_ONE[2],
                ["r4 c'4--"] * SEQ_ONE[3],
                ["r4 e'4--"] * SEQ_ONE[4],
                ["r4 d'4--"] * SEQ_ONE[5],
                ["r4 a'4--"] * SEQ_ONE[6]]

CLARINET_TWO_BARS = make_bars_four_four(CLARINET_TWO)
CLARINET_ONE_BARS[0] = "r4 a'4--\\mp r4 a'4--"

BASSOON = ["r1",
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
           "d'8( c' b a) d( a, d,4)"
           ]

CELLO = ["r1", 
         "r1", 
         "r1", 
         "r1", 
         "r1",
         "r1", 
         "r1",
         "r4 r8 e'8( a' e' a--) fs'(",
         "ef'8 e') a( e a e a4)",
         "r1",
         "r1",
         "r1",
         "r4 r8 c'8( f' c' f) c'(",
         "f8 e d f) c( f f,4)",
         "r1",
         "r4 r8 c'8( a d' a d)",
         "d'8( c' b a) d( a, d,4)"
         ]

REST = ["r1" * 17]
           


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
    "chorale_Bq": CLARINET_TWO_BARS[16]
    }


def get_segment() -> dict:
    """  
    does exactly what it says on the tin

    chorale := a fairly full chordal texture
    desc    := descant melody
    basn    := bassoon melody

    The whole section is laid out in a 17 bar chunk
    """
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
    orn_a =create_voice(OBOE_TWO[0], 0)
    orn_b =create_voice(OBOE_TWO[1], 0)
    orn_c =create_voice(OBOE_TWO[2], 0)
    orn_d =create_voice(OBOE_TWO[3], 0)
    orn_e =create_voice(OBOE_TWO[4], 0)
    orn_f =create_voice(OBOE_TWO[5], 0)
    orn_g =create_voice(OBOE_TWO[6], 0)
    orn_h =create_voice(OBOE_TWO[7], 0)
    orn_i =create_voice(OBOE_TWO[8], 0)
    orn_j =create_voice(OBOE_TWO[9], 0)
    orn_k =create_voice(OBOE_TWO[10], 0)
    orn_l =create_voice(OBOE_TWO[11], 0)
    orn_m =create_voice(OBOE_TWO[12], 0)
    orn_n =create_voice(OBOE_TWO[13], 0)
    orn_o =create_voice(OBOE_TWO[14], 0)
    orn_p =create_voice(OBOE_TWO[15], 0)
    orn_q =create_voice(OBOE_TWO[16], 0)
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
    rest = create_voice(REST[0], 0)
    

    wwinds = {
            "flOne": {
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
                "desc_q": desc_q
                },
            "obTwo": {
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
                "orn_p": orn_p,
                "orn_q": orn_q
                },
            "clOne": {
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
                "chorale_Bq": chorale_Bq
                },
            "bsn": {
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
            "hrnOneTwo": {
                "rest": rest
                },
            "hrnThreeFour": {
                "rest": rest
                },
            "trpOne": {
                "rest": rest
                },
            "trpTwo": {
                "rest": rest
                },
            "trb": {
                "rest": rest
                },
            "btrb": {
                "rest": rest
                },
            "tuba": {
                "rest": rest
                },
            "harp": {
                "rest": rest
                },
            "percussion": {
                "rest": rest
                },
            "violinOne": {
                "rest": rest
                },
            "violinTwo": {
                "rest": rest
                },
            "viola": {
                "rest": rest
                },
            "cello": {
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
                "rest": rest
                }
            }
    return wwinds

if __name__ == '__main__':
    outputheader()
    instruments = ["flOne", "flTwo", "obOne", "obTwo", "clOne", "clTwo", "bsn",
                   "hrnOneTwo", "hrnThreeFour", "trpOne", "trpTwo", "trb", "btrb", "tuba",
                   "harp", "percussion",
                   "violinOne", "violinTwo", "viola", "cello", "contrabass"
            ]
    segment = "segment_chorale"
    generate_chunk(get_segment, instruments, segment)
