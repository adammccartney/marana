#!/usr/bin/python3

"""
brassIYGH_A.py: script to generate a segment for the brass

usage: python3 brassIYGH_A.py > brassIYGH_A.ly
"""

from marana.tools import (
    convert,
    create_voice,
    create_pitch_map,
    generate_chunk,
    generate_phrases,
    outputheader,
    mapRests,
)

CALL_ROOTS = ["bf", "bf", "bf", "f"]
RESP_ROOTS = ["d", "g", "a,", "bf,", "d"]


# we're going to create a pitch map for each of the tones we want to
# articulate.

atups = [
    create_pitch_map("obOne", CALL_ROOTS, "1-1/7"),  # seventh
    create_pitch_map("obTwo", CALL_ROOTS, "1-1/3"),  # fifth
    create_pitch_map("clOne", CALL_ROOTS, "1-3/5"),  # third
    create_pitch_map("clTwo", CALL_ROOTS, "2"),
    create_pitch_map("tmp", CALL_ROOTS, "16"),
    create_pitch_map("va", CALL_ROOTS, "2-2/3"),  # fifth
    create_pitch_map("vc", CALL_ROOTS, "4"),
    create_pitch_map("kb", CALL_ROOTS, "8"),
]

call_dict = convert(atups, {})

btups = [
    create_pitch_map("fluteOne", CALL_ROOTS, "1-1/7"),
    create_pitch_map("fluteTwo", CALL_ROOTS, "1-1/3"),
    create_pitch_map("bsn", CALL_ROOTS, "16"),
    create_pitch_map("vibes", CALL_ROOTS, "1-3/5"),
    create_pitch_map("vnone", CALL_ROOTS, "1-1/7"),
    create_pitch_map("vntwo", CALL_ROOTS, "1-1/3"),
]

resp_dict = convert(btups, {})

# Then the templates will be filled with a consistent call to
# filltemplates(), which takes the newly created matrix as an arg

TEMPLATE_MAP = {
    "obOne": """r8 {0}8\\fp ~ {0}4. r8\\ppp r4
                    r8 {1}8\\fp ~ {1}4. r8\\ppp r4
                    r8 {2}8\\fp ~ {2}4. r8\\ppp r4
                    r8 {3}8\\fp ~ {3}4. r8\\ppp r4
                    r1
                 """,
    "obTwo": """r8 {0}8\\fp ~ {0}4. r8\\ppp r4
                    r8 {1}8\\fp ~ {1}4. r8\\ppp r4
                    r8 {2}8\\fp ~ {2}4. r8\\ppp r4
                    r8 {3}8\\fp ~ {3}4. r8\\ppp r4
                    r1
                 """,
    "clOne": """r8 {0}8\\fp ~ {0}2~ {0}4\\ppp
                    r8 {1}8\\fp ~ {1}2~ {1}4\\ppp
                    r8 {2}8\\fp ~ {2}2~ {2}4\\ppp
                    r8 {3}8\\fp ~ {3}2~ {3}4\\ppp
                    r1                 
                 """,
    "clTwo": """r8 {0}8\\fp ~ {0}2~ {0}4\\ppp
                    r8 {1}8\\fp ~ {1}2~ {1}4\\ppp
                    r8 {2}8\\fp ~ {2}2~ {2}4\\ppp
                    r8 {3}8\\fp ~ {3}2~ {3}4\\ppp
                    r1
                 """,
    "tmp": """r8 {0}8-.\\f r2.
                 r8 {1}8-.\\f r2.
                 r8 {2}8-.\\f r2.
                 r8 {3}8-.\\f r2.
                 r1
                 """,
    "va": """r8 {0}8\\fp ~ {0}2. ~
                 {0}8\\ppp {1}8\\fp ~ {1}2. ~
                 {1}8\\ppp {2}8\\fp ~ {2}2. ~
                 {2}8\\ppp {3}8\\fp ~ {3}2. ~
                 {3}1\\ppp
                 """,
    "vc": """r8 {0}8\\fp ~ {0}2. ~
                 {0}8\\ppp {1}8\\fp ~ {1}2. ~
                 {1}8\\ppp {2}8\\fp ~ {2}2. ~
                 {2}8\\ppp {3}8\\fp ~ {3}2. ~
                 {3}1\\ppp
                 """,
    "kb": """r8 {0}8\\fp ~ {0}2. ~
                 {0}8\\ppp {1}8\\fp ~ {1}2. ~
                 {1}8\\ppp {2}8\\fp ~ {2}2. ~
                 {2}8\\ppp {3}8\\fp ~ {3}2. ~
                 {3}1\\ppp
                 """,
    "fluteOne": """r2. {0}4\\fp ~ 
                  {0}4\\ppp r2 {1}4\\fp ~
                  {1}4\\ppp r2 {2}4\\fp ~
                  {2}4\\ppp r2 {3}4\\fp ~
                  {3}4\\ppp r2.
                  """,
    "fluteTwo": """r2. {0}4\\fp ~ 
                  {0}4.\\ppp r8 r4 {1}4\\fp ~
                  {1}4.\\ppp r8 r4 {2}4\\fp ~
                  {2}4.\\ppp r8 r4 {3}4\\fp ~
                  {3}4.\\ppp r8 r2
                  """,
    "bsn": """r2. {0}4\\fp ~ 
                {0}2\\ppp r4 {1}4\\fp ~
                {1}2\\ppp r4 {2}4\\fp ~
                {2}2\\ppp r4 {3}4\\fp ~
                {3}2\\ppp r2
                """,
    "vibes": """r2. {0}4\\f ~ 
                  {0}2. {1}4\\f ~
                  {1}2. {2}4\\f ~
                  {2}2. {3}4\\f ~
                  {3}2 r2
                  """,
    "vnone": """r2. {0}4\\fp ~ 
                  {0}2\\ppp r4 {1}4\\fp ~
                  {1}2\\ppp r4 {2}4\\fp ~
                  {2}2\\ppp r4 {3}4\\fp ~
                  {3}2\\ppp r2
                  """,
    "vntwo": """r2. {0}4\\fp ~ 
                  {0}2\\ppp r4 {1}4\\fp ~
                  {1}2\\ppp r4 {2}4\\fp ~
                  {2}2\\ppp r4 {3}4\\fp ~
                  {3}2\\ppp r2
                  """,
}


CALLS = [
    "r8 bf8-.\\sfp d'8 bf8-. f2",
    "r8 bf8-.\\sfp g8 bf8-. f2",
    "r8 bf8-.\\sfp a8 bf8-. c'2",
    "r8 f8-.\\sfp bf8 c'8-. d'2",
    "r1",
]

RESPS = [
    "r2 r8 bf8 d'8-.\\sfp bf8",
    "f2 r8 bf8 g'8-.\\sfp bf8",
    "f2 r8 bf8 a8-.\\sfp bf8",
    "c'2 r8 f8 bf8-.\\sfp c'8",
    "d'2 r2",
]

idx_odd = [2, 3, 4]
idx_even = [0, 2, 4]

rested_calls = mapRests(idx_odd, CALLS)
rested_resps = mapRests(idx_even, RESPS)

call_phrases = generate_phrases(call_dict, TEMPLATE_MAP)
resp_phrases = generate_phrases(resp_dict, TEMPLATE_MAP)

IYGH_PHRASES = {
    #######################################################################
    # data
    #######################################################################
    "call_aa": rested_calls[0],
    "call_ab": rested_calls[1],
    "call_ba": rested_calls[2],
    "call_bb": rested_calls[3],
    "call_bc": rested_calls[4],
    "resp_aa": rested_resps[0],
    "resp_ab": rested_resps[1],
    "resp_ba": rested_resps[2],
    "resp_bb": rested_resps[3],
    "resp_bc": rested_resps[4],
    "chorus_aa": "r8 d'8-.\\ppp ef'16-.( ef'-. ef'-. ef'-. ef'16-. ef'-. ef'-. ef'-. ef'16-. ef'-. ef'-. ef'-.",
    "chorus_ab": "ef'16-. ef'-. ef'-. ef'-.) d'16-.( d'-. d'-. d'-. d'16-. d'-. d'-. d'-. d'16-. d'-. c'-. c'-.",
    "chorus_ac": "bf16-. bf-.) d'8 d'4-- d'4-- c'4 ~",
    "chorus_ad": "c'4. ef'8\\mp d'4 c'4",
    "chorus_ae": "bf4 f4 bf2",
    "chorus_eights_aa": "r8 d'8-.\\p ef'8-.( ef'-. ef'8-. ef'-. ef'8-. ef'-.",
    "chorus_eights_ab": "ef'8-. ef'-.) d'8-.( d'-. d'8-. d'-. d'8-. c'-.",
    "chorus_eights_ac": "bf8-. d'8-.) d'4-- d'4-- c'4 ~",
    "chorus_eights_ad": "c'4. ef'8 d'4 c'4",
    "chorus_eights_ae": "bf4 f4 bf2",
    "chorus_triplets_aa": """r4 \\tuplet 3/2 {ef'8-.\\pp( ef'-. ef'-.} \\tuplet 3/2 {ef'8-. ef'-. ef'-.} 
                             \\tuplet 3/2 {ef'8-. ef'-. ef'-.}""",
    "chorus_triplets_ab": """\\tuplet 3/2 {ef'8-. ef'-. ef'-.} \\tuplet 3/2 {ef'8-. ef'-. ef'-.)} 
                             \\tuplet 3/2 {d'8-.( d'-. d'-.} \\tuplet 3/2 {d'8-. d'-. d'-.)}""",
    "chorus_triplets_ac": """\\tuplet 3/2 {bf8-.( bf-. bf-.} \\tuplet 3/2 {d'8-. d'-. d'-.}
                             \\tuplet 3/2 {d'8-. d'-. d'-.)} \\tuplet 3/2 {c'8-.( c'-. c'-.}""",
    "chorus_triplets_ad": """\\tuplet 3/2 {c'8-. c'-. c'-.} \\tuplet 3/2 {c'8-. c'-. c'-.)}
                             \\tuplet 3/2 {d'8-.( d'-. d'-.} \\tuplet 3/2 {ef'8-. ef'-. ef'-.}""",
    "chorus_triplets_ae": """\\tuplet 3/2 {f'8-. f'-. f'-.} \\tuplet 3/2 {f'8-. f'-. f'-.)} f'2\\mf""",
}


def get_brass_section() -> dict:
    """
    creates a dictionary of brass voices
    """

    call_aa_15ve = create_voice(IYGH_PHRASES["call_aa"], 24)  # call aa up the 15ave

    call_ab_15ve = create_voice(IYGH_PHRASES["call_ab"], 24)  # call ab up the 15ave
    call_ba_15ve = create_voice(IYGH_PHRASES["call_ba"], 24)  # call ba up the 15ave
    call_bb_15ve = create_voice(IYGH_PHRASES["call_bb"], 24)  # call bb up the 15ave
    call_bc_15ve = create_voice(IYGH_PHRASES["call_bc"], 24)  # call bc up the 15ave
    call_aa_octve = create_voice(IYGH_PHRASES["call_aa"], 12)  # call aa up the octave
    call_ab_octve = create_voice(IYGH_PHRASES["call_ab"], 12)  # call ab up the octave
    call_ba_octve = create_voice(IYGH_PHRASES["call_ba"], 12)  # call ba up the octave
    call_bb_octve = create_voice(IYGH_PHRASES["call_bb"], 12)  # call bb up the octave
    call_bc_octve = create_voice(IYGH_PHRASES["call_bc"], 12)  # call bc up the octave
    call_aa_5ve = create_voice(IYGH_PHRASES["call_aa"], 7)  # call aa
    call_ab_5ve = create_voice(IYGH_PHRASES["call_ab"], 7)  # call ab
    call_ba_5ve = create_voice(IYGH_PHRASES["call_ba"], 7)  # call ba
    call_bb_5ve = create_voice(IYGH_PHRASES["call_bb"], 7)  # call bb
    call_bc_5ve = create_voice(IYGH_PHRASES["call_bc"], 7)  # call bc
    call_aa = create_voice(IYGH_PHRASES["call_aa"], 0)  # call aa
    call_ab = create_voice(IYGH_PHRASES["call_ab"], 0)  # call ab
    call_ba = create_voice(IYGH_PHRASES["call_ba"], 0)  # call ba
    call_bb = create_voice(IYGH_PHRASES["call_bb"], 0)  # call bb
    call_bc = create_voice(IYGH_PHRASES["call_bc"], 0)  # call bc
    call_aa_octvb = create_voice(IYGH_PHRASES["call_aa"], -12)  # call aa octvb
    call_ab_octvb = create_voice(IYGH_PHRASES["call_ab"], -12)  # call ab octvb
    call_ba_octvb = create_voice(IYGH_PHRASES["call_ba"], -12)  # call ba octvb
    call_bb_octvb = create_voice(IYGH_PHRASES["call_bb"], -12)  # call bb octvb
    call_bc_octvb = create_voice(IYGH_PHRASES["call_bc"], -12)  # call bc octvb
    resp_aa_octve = create_voice(IYGH_PHRASES["resp_aa"], 12)  # response up oct
    resp_ab_octve = create_voice(IYGH_PHRASES["resp_ab"], 12)  # response up oct
    resp_ba_octve = create_voice(IYGH_PHRASES["resp_ba"], 12)  # response up oct
    resp_bb_octve = create_voice(IYGH_PHRASES["resp_bb"], 12)  # response up oct
    resp_bc_octve = create_voice(IYGH_PHRASES["resp_bc"], 12)  # response up oct
    resp_aa_fifve = create_voice(IYGH_PHRASES["resp_aa"], 7)  # response up fifth
    resp_ab_fifve = create_voice(IYGH_PHRASES["resp_ab"], 7)  # response up fifth
    resp_ba_fifve = create_voice(IYGH_PHRASES["resp_ba"], 7)  # response up fifth
    resp_bb_fifve = create_voice(IYGH_PHRASES["resp_bb"], 7)  # response up fifth
    resp_bc_fifve = create_voice(IYGH_PHRASES["resp_bc"], 7)  # response up fifth
    resp_aa = create_voice(IYGH_PHRASES["resp_aa"], 0)  # response up oct
    resp_ab = create_voice(IYGH_PHRASES["resp_ab"], 0)  # response at pitch
    resp_ba = create_voice(IYGH_PHRASES["resp_ba"], 0)  # response at pitch
    resp_bb = create_voice(IYGH_PHRASES["resp_bb"], 0)  # response at pitch
    resp_bc = create_voice(IYGH_PHRASES["resp_bc"], 0)  # response at pitch
    resp_aa_fourvb = create_voice(IYGH_PHRASES["resp_aa"], -5)  # response fourth below
    resp_ab_fourvb = create_voice(IYGH_PHRASES["resp_ab"], -5)  # response fourth below
    resp_ba_fourvb = create_voice(IYGH_PHRASES["resp_ba"], -5)  # response fourth below
    resp_bb_fourvb = create_voice(IYGH_PHRASES["resp_bb"], -5)  # response fourth below
    resp_bc_fourvb = create_voice(IYGH_PHRASES["resp_bc"], -5)  # response fourth below
    resp_aa_octvb = create_voice(IYGH_PHRASES["resp_aa"], -12)  # response down oct
    resp_ab_octvb = create_voice(IYGH_PHRASES["resp_ab"], -12)  # response down oct
    resp_ba_octvb = create_voice(IYGH_PHRASES["resp_ba"], -12)  # response down oct
    resp_bb_octvb = create_voice(IYGH_PHRASES["resp_bb"], -12)  # response down oct
    resp_bc_octvb = create_voice(IYGH_PHRASES["resp_bc"], -12)  # response down oct
    chorus_aa_octve = create_voice(
        IYGH_PHRASES["chorus_aa"], 12
    )  # chorus up the octave
    chorus_ab_octve = create_voice(
        IYGH_PHRASES["chorus_ab"], 12
    )  # chorus up the octave
    chorus_ac_octve = create_voice(
        IYGH_PHRASES["chorus_ac"], 12
    )  # chorus up the octave
    chorus_ad_octve = create_voice(
        IYGH_PHRASES["chorus_ad"], 12
    )  # chorus up the octave
    chorus_ae_octve = create_voice(
        IYGH_PHRASES["chorus_ae"], 12
    )  # chorus up the octave
    chorus_aa = create_voice(IYGH_PHRASES["chorus_aa"], 0)  # chorus
    chorus_ab = create_voice(IYGH_PHRASES["chorus_ab"], 0)  # chorus
    chorus_ac = create_voice(IYGH_PHRASES["chorus_ac"], 0)  # chorus
    chorus_ad = create_voice(IYGH_PHRASES["chorus_ad"], 0)  # chorus
    chorus_ae = create_voice(IYGH_PHRASES["chorus_ae"], 0)  # chorus
    chorus_eights_aa = create_voice(
        IYGH_PHRASES["chorus_eights_aa"], 0
    )  # chorus_eights
    chorus_eights_ab = create_voice(
        IYGH_PHRASES["chorus_eights_ab"], 0
    )  # chorus_eights
    chorus_eights_ac = create_voice(
        IYGH_PHRASES["chorus_eights_ac"], 0
    )  # chorus_eights
    chorus_eights_ad = create_voice(
        IYGH_PHRASES["chorus_eights_ad"], 0
    )  # chorus_eights
    chorus_eights_ae = create_voice(
        IYGH_PHRASES["chorus_eights_ae"], 0
    )  # chorus_eights
    chorus_eights_aa_octvb = create_voice(
        IYGH_PHRASES["chorus_eights_aa"], -12
    )  # chorus_eights down the octave
    chorus_eights_ab_octvb = create_voice(
        IYGH_PHRASES["chorus_eights_ab"], -12
    )  # chorus_eights down the octave
    chorus_eights_ac_octvb = create_voice(
        IYGH_PHRASES["chorus_eights_ac"], -12
    )  # chorus_eights down the octave
    chorus_eights_ad_octvb = create_voice(
        IYGH_PHRASES["chorus_eights_ad"], -12
    )  # chorus_eights down the octave
    chorus_eights_ae_octvb = create_voice(
        IYGH_PHRASES["chorus_eights_ae"], -12
    )  # chorus_eights down the octave

    chorus_triplets_aa_fifve = create_voice(
        IYGH_PHRASES["chorus_triplets_aa"], 7
    )  # chorus triplets
    chorus_triplets_ab_fifve = create_voice(
        IYGH_PHRASES["chorus_triplets_ab"], 7
    )  # chorus triplets
    chorus_triplets_ac_fifve = create_voice(
        IYGH_PHRASES["chorus_triplets_ac"], 7
    )  # chorus triplets
    chorus_triplets_ad_fifve = create_voice(
        IYGH_PHRASES["chorus_triplets_ad"], 7
    )  # chorus triplets
    chorus_triplets_ae_fifve = create_voice(
        IYGH_PHRASES["chorus_triplets_ae"], 7
    )  # chorus triplets

    chorus_triplets_aa = create_voice(
        IYGH_PHRASES["chorus_triplets_aa"], 0
    )  # chorus triplets

    chorus_triplets_ab = create_voice(
        IYGH_PHRASES["chorus_triplets_ab"], 0
    )  # chorus triplets

    chorus_triplets_ac = create_voice(
        IYGH_PHRASES["chorus_triplets_ac"], 0
    )  # chorus triplets
    chorus_triplets_ad = create_voice(
        IYGH_PHRASES["chorus_triplets_ad"], 0
    )  # chorus triplets
    chorus_triplets_ae = create_voice(
        IYGH_PHRASES["chorus_triplets_ae"], 0
    )  # chorus triplets

    chorus_triplets_aa_fifvb = create_voice(
        IYGH_PHRASES["chorus_triplets_aa"], -5
    )  # chorus triplets
    chorus_triplets_ab_fifvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ab"], -5
    )  # chorus triplets
    chorus_triplets_ac_fifvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ac"], -5
    )  # chorus triplets
    chorus_triplets_ad_fifvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ad"], -5
    )  # chorus triplets
    chorus_triplets_ae_fifvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ae"], -5
    )  # chorus triplets

    chorus_triplets_aa_octvb = create_voice(
        IYGH_PHRASES["chorus_triplets_aa"], -12
    )  # chorus triplets
    chorus_triplets_ab_octvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ab"], -12
    )  # chorus triplets
    chorus_triplets_ac_octvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ac"], -12
    )  # chorus triplets
    chorus_triplets_ad_octvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ad"], -12
    )  # chorus triplets
    chorus_triplets_ae_octvb = create_voice(
        IYGH_PHRASES["chorus_triplets_ae"], -12
    )  # chorus triplets

    TEMPO_FAST = "\\tempo 4 = 116"
    FINAL_BARLINE = '\\bar "|."'
    FIVE_BAR_REST = "r1 r1 r1 r1 r1"

    instruments = {
        "fluteOne": {
            "resp": resp_phrases["fluteOne"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "fluteTwo": {
            "resp": resp_phrases["fluteTwo"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "clOne": {
            "call": call_phrases["clOne"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "clTwo": {
            "call": call_phrases["clTwo"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "obOne": {
            "call": call_phrases["obOne"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "obTwo": {
            "call": call_phrases["obTwo"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "bsn": {
            "resp": resp_phrases["bsn"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "trpOneTwo": {
            "call_aa": call_aa_octve,
            "call_ab": call_ab_octve,
            "call_ba": call_ba_octve,
            "call_bb": call_bb_octve,
            "call_bc": call_bc_octve,
            "chorus_aa": chorus_aa_octve,
            "chorus_ab": chorus_ab_octve,
            "chorus_ac": chorus_ac_octve,
            "chorus_ad": chorus_ad_octve,
            "chorus_ae": chorus_ae_octve,
            "final_barline": FINAL_BARLINE,
        },
        "trpThree": {
            "call_aa": call_aa_5ve,
            "call_ab": call_ab_5ve,
            "call_ba": call_ba_5ve,
            "call_bb": call_bb_5ve,
            "call_bc": call_bc_5ve,
            "chorus_aa": chorus_triplets_aa,
            "chorus_ab": chorus_triplets_ab,
            "chorus_ac": chorus_triplets_ac,
            "chorus_ad": chorus_triplets_ad,
            "chorus_ae": chorus_triplets_ae,
            "final_barline": FINAL_BARLINE,
        },
        "hrnOne": {
            "resp_aa": resp_aa_octve,
            "resp_ab": resp_ab_octve,
            "resp_ba": resp_ba_octve,
            "resp_bb": resp_bb_octve,
            "resp_bc": resp_bc_octve,
            "chorus_aa": chorus_triplets_aa_fifve,
            "chorus_ab": chorus_triplets_ab_fifve,
            "chorus_ac": chorus_triplets_ac_fifve,
            "chorus_ad": chorus_triplets_ad_fifve,
            "chorus_ae": chorus_triplets_ae_fifve,
            "final_barline": FINAL_BARLINE,
        },
        "hrnTwo": {
            "resp_aa": resp_aa,
            "resp_ab": resp_ab,
            "resp_ba": resp_ba,
            "resp_bb": resp_bb,
            "resp_bc": resp_bc,
            "chorus_aa": chorus_triplets_aa_fifvb,
            "chorus_ab": chorus_triplets_ab_fifvb,
            "chorus_ac": chorus_triplets_ac_fifvb,
            "chorus_ad": chorus_triplets_ad_fifvb,
            "chorus_ae": chorus_triplets_ae_fifvb,
            "final_barline": FINAL_BARLINE,
        },
        "hrnThree": {
            "resp_aa": resp_aa_fifve,
            "resp_ab": resp_ab_fifve,
            "resp_ba": resp_ba_fifve,
            "resp_bb": resp_bb_fifve,
            "resp_bc": resp_bc_fifve,
            "chorus_aa": chorus_triplets_aa,
            "chorus_ab": chorus_triplets_ab,
            "chorus_ac": chorus_triplets_ac,
            "chorus_ad": chorus_triplets_ad,
            "chorus_ae": chorus_triplets_ae,
            "final_barline": FINAL_BARLINE,
        },
        "hrnFour": {
            "resp_aa": resp_aa_fourvb,
            "resp_ab": resp_ab_fourvb,
            "resp_ba": resp_ba_fourvb,
            "resp_bb": resp_bb_fourvb,
            "resp_bc": resp_bc_fourvb,
            "chorus_aa": chorus_triplets_aa_octvb,
            "chorus_ab": chorus_triplets_ab_octvb,
            "chorus_ac": chorus_triplets_ac_octvb,
            "chorus_ad": chorus_triplets_ad_octvb,
            "chorus_ae": chorus_triplets_ae_octvb,
            "final_barline": FINAL_BARLINE,
        },
        "tuba": {
            "resp_aa": resp_aa_octvb,
            "resp_ab": resp_ab_octvb,
            "resp_ba": resp_ba_octvb,
            "resp_bb": resp_bb_octvb,
            "resp_bc": resp_bc_octvb,
            "chorus_aa": chorus_triplets_aa_octvb,
            "chorus_ab": chorus_triplets_ab_octvb,
            "chorus_ac": chorus_triplets_ac_octvb,
            "chorus_ad": chorus_triplets_ad_octvb,
            "chorus_ae": chorus_triplets_ae_octvb,
            "final_barline": FINAL_BARLINE,
        },
        "trbOneTwo": {
            "call_aa": call_aa,
            "call_ab": call_ab,
            "call_ba": call_ba,
            "call_bb": call_bb,
            "call_bc": call_bc,
            "chorus_eights_aa": chorus_eights_aa,
            "chorus_eights_ab": chorus_eights_ab,
            "chorus_eights_ac": chorus_eights_ac,
            "chorus_eights_ad": chorus_eights_ad,
            "chorus_eights_ae": chorus_eights_ae,
            "final_barline": FINAL_BARLINE,
        },
        "btrb": {
            "call_aa_octvb": call_aa_octvb,
            "call_ab_octvb": call_ab_octvb,
            "call_ba_octvb": call_ba_octvb,
            "call_bb_octvb": call_bb_octvb,
            "call_bc_octvb": call_bc_octvb,
            "chorus_eights_aa": chorus_eights_aa_octvb,
            "chorus_eights_ab": chorus_eights_ab_octvb,
            "chorus_eights_ac": chorus_eights_ac_octvb,
            "chorus_eights_ad": chorus_eights_ad_octvb,
            "chorus_eights_ae": chorus_eights_ae_octvb,
            "final_barline": FINAL_BARLINE,
        },
        "tmp": {
            "call": call_phrases["tmp"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "vibes": {
            "resp": resp_phrases["vibes"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "harp": {
                "rest_i": FIVE_BAR_REST,
                "rest_ii": FIVE_BAR_REST,
                "final_barline": FINAL_BARLINE,
        },
        "vnone": {
            "resp": resp_phrases["vnone"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "vntwo": {
            "resp": resp_phrases["vntwo"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "va": {
            "call": call_phrases["va"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "vc": {
            "call": call_phrases["vc"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
        "kb": {
            "call": call_phrases["kb"],
            "rest": FIVE_BAR_REST,
            "final_barline": FINAL_BARLINE,
        },
    }
    return instruments


if __name__ == "__main__":
    outputheader()
    instruments = [
        "fluteOne",
        "fluteTwo",
        "clOne",
        "clTwo",
        "obOne",
        "obTwo",
        "bsn",
        "hrnOne",
        "hrnTwo",
        "hrnThree",
        "hrnFour",
        "trpOneTwo",
        "trpThree",
        "trbOneTwo",
        "btrb",
        "tuba",
        "tmp",
        "harp",
        "vibes",
        "vnone",
        "vntwo",
        "va",
        "vc",
        "kb",
    ]
    segment = "segment_IYGH_B"
    generate_chunk(get_brass_section, instruments, segment)
