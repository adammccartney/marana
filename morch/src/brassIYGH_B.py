#!/usr/bin/python3

"""
brassIYGH_A.py: script to generate a segment for the brass

usage: python3 brassIYGH_A.py > brassIYGH_A.ly
"""

from marana.tools import ( create_voice, outputheader, generate_chunk, mapRests )

CALLS = ["r8 bf8-. d'8 bf8-. f2",
         "r8 bf8-. g8 bf8-. f2",
         "r8 bf8-. a8 bf8-. c'2",
         "r8 f8-. bf8 c'8-. d'2",
         "r1"]

RESPS = ["r2 r8 bf8 d'8-. bf8",
         "f2 r8 bf8 g'8-. bf8", 
         "f2 r8 bf8 a8-. bf8",
         "c'2 r8 f8 bf8-. c'8", 
         "d'2 r2"]

idx_odd = [1, 3]
idx_even = [0, 2, 4]

rested_calls = mapRests(idx_even, CALLS)
rested_resps = mapRests(idx_even, RESPS)

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
    "chorus_aa": "r8 d'8-. ef'16-. ef'-. ef'-. ef'-. ef'16-. ef'-. ef'-. ef'-. ef'16-. ef'-. ef'-. ef'-.",
    "chorus_ab": "ef'16-. ef'-. ef'-. ef'-. d'16-. d'-. d'-. d'-. d'16-. d'-. d'-. d'-. d'16-. d'-. c'-. c'-.",
    "chorus_ac": "bf16-. bf-. d'8 d'4 d'4 c'4 ~",
    "chorus_ad": "c'4. ef'8 d'4 c'4",
    "chorus_ae": "bf4 f4 bf2",
    "chorus_eights_aa": "r8 d'8-. ef'8-. ef'-. ef'8-. ef'-. ef'8-. ef'-.",
    "chorus_eights_ab": "ef'8-. ef'-. d'8-. d'-. d'8-. d'-. d'8-. c'-.",
    "chorus_eights_ac": "bf8-. d'8 d'4 d'4 c'4 ~",
    "chorus_eights_ad": "c'4. ef'8 d'4 c'4",
    "chorus_eights_ae": "bf4 f4 bf2",
    "chorus_triplets_aa": """r4 \\tuplet 3/2 {ef'8 ef' ef'} \\tuplet 3/2 {ef'8 ef' ef'} 
                             \\tuplet 3/2 {ef'8 ef' ef'}""",
    "chorus_triplets_ab": """\\tuplet 3/2 {ef'8 ef' ef'} \\tuplet 3/2 {ef'8 ef' ef'} 
                             \\tuplet 3/2 {d'8 d' d'} \\tuplet 3/2 {d'8 d' d'}""",
    "chorus_triplets_ac": """\\tuplet 3/2 {bf8 bf bf} \\tuplet 3/2 {d'8 d' d'}
                             \\tuplet 3/2 {d'8 d' d'} \\tuplet 3/2 {c'8 c' c'}""",
    "chorus_triplets_ad": """\\tuplet 3/2 {c'8 c' c'} \\tuplet 3/2 {c'8 c' c'}
                             \\tuplet 3/2 {d'8 d' d'} \\tuplet 3/2 {ef'8 ef' ef'}""",
    "chorus_triplets_ae": """\\tuplet 3/2 {f'8 f' f'} \\tuplet 3/2 {f'8 f' f'} f'2""",
}

def get_brass_section() -> dict:
    """  
    creates a dictionary of brass voices 
    """
    call_aa_octve = create_voice(IYGH_PHRASES["call_aa"], 12) # call aa up the octave
    call_ab_octve = create_voice(IYGH_PHRASES["call_ab"], 12) # call ab up the octave
    call_ba_octve = create_voice(IYGH_PHRASES["call_ba"], 12) # call ba up the octave
    call_bb_octve = create_voice(IYGH_PHRASES["call_bb"], 12) # call bb up the octave
    call_bc_octve = create_voice(IYGH_PHRASES["call_bc"], 12) # call bc up the octave
    call_aa = create_voice(IYGH_PHRASES["call_aa"], 0) # call aa
    call_ab = create_voice(IYGH_PHRASES["call_ab"], 0) # call ab
    call_ba = create_voice(IYGH_PHRASES["call_ba"], 0) # call ba
    call_bb = create_voice(IYGH_PHRASES["call_bb"], 0) # call bb
    call_bc = create_voice(IYGH_PHRASES["call_bc"], 0) # call bc
    call_aa_octvb = create_voice(IYGH_PHRASES["call_aa"], -12) # call aa octvb 
    call_ab_octvb = create_voice(IYGH_PHRASES["call_ab"], -12) # call ab octvb
    call_ba_octvb = create_voice(IYGH_PHRASES["call_ba"], -12) # call ba octvb
    call_bb_octvb = create_voice(IYGH_PHRASES["call_bb"], -12) # call bb octvb
    call_bc_octvb = create_voice(IYGH_PHRASES["call_bc"], -12) # call bc octvb
    resp_aa_octve = create_voice(IYGH_PHRASES["resp_aa"], 12) # response up oct
    resp_ab_octve = create_voice(IYGH_PHRASES["resp_ab"], 12) # response up oct
    resp_ba_octve = create_voice(IYGH_PHRASES["resp_ba"], 12) # response up oct
    resp_bb_octve = create_voice(IYGH_PHRASES["resp_bb"], 12) # response up oct
    resp_bc_octve = create_voice(IYGH_PHRASES["resp_bc"], 12) # response up oct
    resp_aa = create_voice(IYGH_PHRASES["resp_aa"], 0) # response up oct
    resp_ab = create_voice(IYGH_PHRASES["resp_ab"], 0) # response at pitch
    resp_ba = create_voice(IYGH_PHRASES["resp_ba"], 0) # response at pitch
    resp_bb = create_voice(IYGH_PHRASES["resp_bb"], 0) # response at pitch
    resp_bc = create_voice(IYGH_PHRASES["resp_bc"], 0) # response at pitch
    resp_aa_octvb = create_voice(IYGH_PHRASES["resp_aa"], -12) # response down oct
    resp_ab_octvb = create_voice(IYGH_PHRASES["resp_ab"], -12) # response down oct
    resp_ba_octvb = create_voice(IYGH_PHRASES["resp_ba"], -12) # response down oct
    resp_bb_octvb = create_voice(IYGH_PHRASES["resp_bb"], -12) # response down oct
    resp_bc_octvb = create_voice(IYGH_PHRASES["resp_bc"], -12) # response down oct
    chorus_aa_octve = create_voice(IYGH_PHRASES["chorus_aa"], 12) # chorus up the octave
    chorus_ab_octve = create_voice(IYGH_PHRASES["chorus_ab"], 12) # chorus up the octave
    chorus_ac_octve = create_voice(IYGH_PHRASES["chorus_ac"], 12) # chorus up the octave
    chorus_ad_octve = create_voice(IYGH_PHRASES["chorus_ad"], 12) # chorus up the octave
    chorus_ae_octve = create_voice(IYGH_PHRASES["chorus_ae"], 12) # chorus up the octave
    chorus_aa = create_voice(IYGH_PHRASES["chorus_aa"], 0) # chorus 
    chorus_ab = create_voice(IYGH_PHRASES["chorus_ab"], 0) # chorus 
    chorus_ac = create_voice(IYGH_PHRASES["chorus_ac"], 0) # chorus 
    chorus_ad = create_voice(IYGH_PHRASES["chorus_ad"], 0) # chorus 
    chorus_ae = create_voice(IYGH_PHRASES["chorus_ae"], 0) # chorus 
    chorus_eights_aa = create_voice(IYGH_PHRASES["chorus_eights_aa"], 0) # chorus_eights 
    chorus_eights_ab = create_voice(IYGH_PHRASES["chorus_eights_ab"], 0) # chorus_eights 
    chorus_eights_ac = create_voice(IYGH_PHRASES["chorus_eights_ac"], 0) # chorus_eights 
    chorus_eights_ad = create_voice(IYGH_PHRASES["chorus_eights_ad"], 0) # chorus_eights 
    chorus_eights_ae = create_voice(IYGH_PHRASES["chorus_eights_ae"], 0) # chorus_eights 
    chorus_eights_aa_octvb = create_voice(IYGH_PHRASES["chorus_eights_aa"], -12) # chorus_eights down the octave
    chorus_eights_ab_octvb = create_voice(IYGH_PHRASES["chorus_eights_ab"], -12) # chorus_eights down the octave
    chorus_eights_ac_octvb = create_voice(IYGH_PHRASES["chorus_eights_ac"], -12) # chorus_eights down the octave
    chorus_eights_ad_octvb = create_voice(IYGH_PHRASES["chorus_eights_ad"], -12) # chorus_eights down the octave
    chorus_eights_ae_octvb = create_voice(IYGH_PHRASES["chorus_eights_ae"], -12) # chorus_eights down the octave

    chorus_triplets_aa = create_voice(IYGH_PHRASES["chorus_triplets_aa"], 0) # chorus triplets 

    chorus_triplets_ab = create_voice(IYGH_PHRASES["chorus_triplets_ab"], 0) # chorus triplets 

    chorus_triplets_ac = create_voice(IYGH_PHRASES["chorus_triplets_ac"], 0) # chorus triplets 
    chorus_triplets_ad = create_voice(IYGH_PHRASES["chorus_triplets_ad"], 0) # chorus triplets 
    chorus_triplets_ae = create_voice(IYGH_PHRASES["chorus_triplets_ae"], 0) # chorus triplets 
    chorus_triplets_aa_octvb = create_voice(IYGH_PHRASES["chorus_triplets_aa"], -12) # chorus triplets 
    chorus_triplets_ab_octvb = create_voice(IYGH_PHRASES["chorus_triplets_ab"], -12) # chorus triplets 
    chorus_triplets_ac_octvb = create_voice(IYGH_PHRASES["chorus_triplets_ac"], -12) # chorus triplets 
    chorus_triplets_ad_octvb = create_voice(IYGH_PHRASES["chorus_triplets_ad"], -12) # chorus triplets 
    chorus_triplets_ae_octvb = create_voice(IYGH_PHRASES["chorus_triplets_ae"], -12) # chorus triplets 


    brass = {
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
                },
            "trpThree": {
                "call_aa": call_aa, 
                "call_ab": call_ab,
                "call_ba": call_ba,
                "call_bb": call_bb,
                "call_bc": call_bc,
                "chorus_aa": chorus_aa,
                "chorus_ab": chorus_ab,
                "chorus_ac": chorus_ac,
                "chorus_ad": chorus_ad,
                "chorus_ae": chorus_ae,
                },
            "hrnOneTwo": {
                "resp_aa": resp_aa_octve, 
                "resp_ab": resp_ab_octve,
                "resp_ba": resp_ba_octve,
                "resp_bb": resp_bb_octve,
                "resp_bc": resp_bc_octve,
                "chorus_aa": chorus_triplets_aa,
                "chorus_ab": chorus_triplets_ab,
                "chorus_ac": chorus_triplets_ac,
                "chorus_ad": chorus_triplets_ad,
                "chorus_ae": chorus_triplets_ae,
                },
            "hrnThreeFour": {
                "resp_aa": resp_aa, 
                "resp_ab": resp_ab,
                "resp_ba": resp_ba,
                "resp_bb": resp_bb,
                "resp_bc": resp_bc,
                "chorus_aa": chorus_triplets_aa_octvb,
                "chorus_ab": chorus_triplets_ab_octvb,
                "chorus_ac": chorus_triplets_ac_octvb,
                "chorus_ad": chorus_triplets_ad_octvb,
                "chorus_ae": chorus_triplets_ae_octvb,
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
                }
            }
    return brass

if __name__ == '__main__':
    outputheader()
    instruments = ["hrnOneTwo", "hrnThreeFour", "trpOneTwo", "trpThree",
                   "trbOneTwo", "btrb", "tuba"]
    segment = "segment_B"
    generate_chunk(get_brass_section, instruments, segment)
