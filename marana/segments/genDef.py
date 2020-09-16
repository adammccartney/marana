import copy
import pathlib

import abjad
import marana

import marana.tools.FuzzyHarmony as FuzzyHarmony

from marana.tools.accents import tenuto as tenuto
from marana.tools.barlines import barline as barline
from marana.tools.clef import clef as clef
from marana.tools.FuzzyHarmony import Diad as Diad
from marana.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from marana.tools.material_methods import transpose_segment as transpose_segment
from marana.tools.tremolo import tremolo as tremolo

from abjad import NamedPitch as NamedPitch
from typing import List

#####################
# Setting up segment ### [A] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
score =marana.ScoreTemplate()
score_template = score()

segment_maker = marana.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=marana.build_path,
                                markup_leaves=False,
                                segment_name='segment_A',
                                rehearsal_mark=1,
                                tempo=((1, 4), 50),
                                time_signatures=[(4, 4)] * 44,
                                )

segment_maker.metronome_marks = [
        (0, marana.metronome_marks['50'], 5),
        ]

#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/


# ----- Diads
# -- sequences of notes for arpeggios


#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

rhythm_definition.notes = []

rhythm_definition.dynamics = [
             ]

rhythm_definition.markup = [
             ]


#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

auth_one_c = cm7_hrmns_kln_eing[2].segment
tr_arp_one = LegatoArpeggio(auth_one_c, seq_one)
monosynth_arp_one = tr_arp_one.stages 

auth_one_d = cm7_hrmns_kln_eing[3].segment
tr_arp_two = LegatoArpeggio(auth_one_d, seq_one)
monosynth_arp_two = tr_arp_two.stages 

diad_DA = Diad(d7_fifths_gr_kln[1])
diad_one = diad_DA.pitch_string

diad_AE = Diad(d7_fifths_kln_eing[0])
diad_two = diad_AE.pitch_string

rhythm_definition.notes = [
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r4"),
        (melody_one_a_oct_down[0], abjad.Duration(3, 4), marana.tie(), clef('bass')),
        #------------Bar 13
        (melody_one_a_oct_down[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_one_a[0], abjad.Duration(2, 4)), 
        (melody_one_a_oct_down[1], abjad.Duration(1,4)), 
        (melody_one_a_oct_down[3], abjad.Duration(1)), 
        (melody_one_a_oct_down[2], abjad.Duration(1), tremolo(32), clef('treble')), 
        (monosynth_arp_one[0], abjad.Duration(1, 2), tremolo(32), marana.tie()),
        (monosynth_arp_one[1], abjad.Duration(1, 2), tremolo(32), marana.tie()),
        #------------Bar 17
        (monosynth_arp_one[1], abjad.Duration(1, 4), tremolo(32), marana.tie()),
        (monosynth_arp_one[2], abjad.Duration(3, 4), tremolo(32), marana.tie()),
        (monosynth_arp_one[3], abjad.Duration(1), tremolo(32), marana.tie()),
        (monosynth_arp_one[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (monosynth_arp_two[0], abjad.Duration(1, 2), tremolo(32), marana.tie()),
        (monosynth_arp_two[1], abjad.Duration(1, 2), tremolo(32), marana.tie()),
        #------------Bar 21
        (monosynth_arp_two[1], abjad.Duration(1, 4), tremolo(32), marana.tie()),
        (monosynth_arp_two[2], abjad.Duration(3, 4), tremolo(32), marana.tie()),
        (monosynth_arp_two[3], abjad.Duration(1), tremolo(32), marana.tie()),
        (monosynth_arp_two[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        ("r1"),
        #-----------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 29
        ("r1"),
        (diad_one, abjad.Duration(1), tremolo(32), marana.tie(), clef('bass')),
        (diad_one, abjad.Duration(1), tremolo(32), marana.tie()),
        (diad_one, abjad.Duration(1), tremolo(32), marana.tie()),
        #-----------Bar 33
        (diad_one, abjad.Duration(1), tremolo(32), marana.tie()),
        (diad_one, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        (diad_two, abjad.Duration(1), tremolo(32), marana.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), marana.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), marana.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), marana.tie()),
        #-----------Bar 41
        (diad_two, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
        ("r1"),
        ]

rhythm_definition.dynamics = [
        (12, abjad.Dynamic('ppp')),
        (18, '>'),
        (20, '<'),
        (23, '>'),
        (24, abjad.Dynamic('ppp')),
        (26, '<'),
        (29, '>'),
        (31, abjad.Dynamic('niente')),
        (39, abjad.Dynamic('niente')),
        (40, '<'),
        (42, '>'),
        (44, abjad.Dynamic('niente')),
        (46, abjad.Dynamic('niente')),
        (47, '<'),
        (49, '>', 3.5),
        (51, abjad.Dynamic('niente')),
       ]

rhythm_definition.markup = [
        (18, marana.markup.mx(), 1.5),
        ]


#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

plag_one_a = gm7_hrmns_zw_dr[0].segment
plag_one_a_arp = LegatoArpeggio(plag_one_a, seq_one)
rh_arp_one = plag_one_a_arp.stages

plag_one_b = gm7_hrmns_zw_dr[1].segment
plag_one_b_arp = LegatoArpeggio(plag_one_b, seq_two)
rh_arp_two = plag_one_b_arp.stages

rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (rh_arp_one[0], abjad.Duration(1, 2), marana.tie()),
        (rh_arp_one[1], abjad.Duration(3, 4), marana.tie()),
        (rh_arp_one[2], abjad.Duration(1, 4), marana.tie()),
        (rh_arp_one[2], abjad.Duration(2, 4), marana.tie()),
        (rh_arp_one[3], abjad.Duration(2, 4), marana.tie()),
        (rh_arp_one[3], abjad.Duration(1), marana.tie()), 
        # ------------------------------------------ Bar 6
        (rh_arp_two[2], abjad.Duration(1), marana.tie()),
        (rh_arp_two[2], abjad.Duration(1,2), marana.tie()),
        (rh_arp_two[3], abjad.Duration(1,2), marana.tie()),
        (rh_arp_two[3], abjad.Duration(1), marana.tie()),
        #------------Bar 9
        (rh_arp_two[3], abjad.Duration(1, 4), marana.tie()),
        (rh_arp_two[1], abjad.Duration(3, 4), marana.tie()),
        (rh_arp_two[0], abjad.Duration(1), marana.tie()),
        (rh_arp_two[0], abjad.Duration(1), marana.tie()),
        (rh_arp_two[0], abjad.Duration(1)),
        #------------Bar 13
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 17
        ("r1"),
        ("r1"),
        ("r1"),       
        ("r1"),
        #------------Bar 21
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 29
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 41
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        ]


rhythm_definition.dynamics = [ 
                    (0, abjad.Dynamic('ppp'), 2.5)
                       ]

rhythm_definition.markup = []


#--------------/
# LH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

auth_one_a = cm7_hrmns_kln_eing[0].segment
auth_one_a_arp= LegatoArpeggio(auth_one_a, seq_one)
lh_arp_one = auth_one_a_arp.stages

auth_two_a = d7_hrmns_gr_kln[0].segment
auth_two_a_arp = LegatoArpeggio(auth_two_a, seq_three)
lh_arp_two = auth_two_a_arp.stages

auth_two_b = d7_hrmns_gr_kln[1].segment
auth_two_b_arp = LegatoArpeggio(auth_two_b, seq_three)
lh_arp_three = auth_two_b_arp.stages

rhythm_definition.notes = [
        (lh_arp_one[0], abjad.Duration(1, 2), marana.tie()),
        (lh_arp_one[1], abjad.Duration(1, 2), marana.tie()),
        (lh_arp_one[1], abjad.Duration(1, 4), marana.tie()),
        (lh_arp_one[2], abjad.Duration(3, 4), marana.tie()),
        (lh_arp_one[3], abjad.Duration(1), marana.tie()),
        (lh_arp_one[3], abjad.Duration(3, 4)), 
        ("r4"),
        # ------------------------------------------ Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 13
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 17
        ("r1"),
        ("r1"),
        ("r1"),       
        ("r1"),
        #------------Bar 21
        ("r1"),
        ("r2"),
        (lh_arp_two[0], abjad.Duration(1, 2), marana.tie()),
        (lh_arp_two[1], abjad.Duration(3, 4), marana.tie()),
        (lh_arp_two[2], abjad.Duration(1, 4), marana.tie()),
        (lh_arp_two[2], abjad.Duration(2, 4), marana.tie()),
        (lh_arp_two[3], abjad.Duration(2, 4), marana.tie()),
        #------------ Bar 25
        (lh_arp_two[3], abjad.Duration(1), marana.tie()), 
        (lh_arp_three[3], abjad.Duration(1), marana.tie()),
        (lh_arp_three[3], abjad.Duration(1,2), marana.tie()),
        (lh_arp_three[2], abjad.Duration(1,2), marana.tie()),
        (lh_arp_three[2], abjad.Duration(1), marana.tie()),
        #------------Bar 29
        (lh_arp_three[2], abjad.Duration(1, 4), marana.tie()),
        (lh_arp_three[1], abjad.Duration(3, 4), marana.tie()),
        (lh_arp_three[0], abjad.Duration(1)),
        ("r1"),  
        ("r1"),
        #-----------Bar 33
        (diad_one, abjad.Duration(1), marana.tie()),
        (diad_one, abjad.Duration(1), marana.tie()),
        (diad_one, abjad.Duration(1), marana.tie()),
        (diad_one, abjad.Duration(1), marana.tie()),
        #-----------Bar 37
        (diad_one, abjad.Duration(1)),
        ("r1"),
        ("r1"),
        (diad_two, abjad.Duration(1), marana.tie()),
        #-----------Bar 41
        (diad_two, abjad.Duration(1), marana.tie()),
        (diad_two, abjad.Duration(1), marana.tie()), 
        (diad_two, abjad.Duration(1), marana.tie()),
        (diad_two, abjad.Duration(1), barline("||")),
        ]


rhythm_definition.dynamics = [
        (47, abjad.Dynamic('pp')),
        (48, '>'),
        (51, abjad.Dynamic('niente')),
        ]

rhythm_definition.markup = []

# ---------------------------------------RUN SEGMENT

lilypond_file = segment_maker.run()
