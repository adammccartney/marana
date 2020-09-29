
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
# Setting up segment ### [I] ###
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
                                segment_name='segment_I',
                                rehearsal_mark=9,
                                tempo=((1, 4), 50),
                                )

segment_maker.metronome_marks = [
        (0, marana.metronome_marks['50'], 5),
        ]

time_signatures= [(4, 4)] + [(3, 4)] + [(3, 4)] + [(4, 4)] + [(3, 4)] + [(3,4)]
maker.time_signatures = time_signatures

#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/


# ----- Diads
# -- sequences of notes for arpeggios


# -------------- Woodwinds ----------------------/
#-----------------------------------------------/

# Flute 
#-----------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "flute1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]


# Oboe
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "oboe1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]


# Bbclarinet
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Bbclarinet1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]



# bassoon  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "bassoon1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# -------------- Brass ---------------------------/
# fhorn1  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "fhorn1"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]


# fhorn3  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "fhorn3"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# trumpet1 
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "trumpet1"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]
# trombone1  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "trombone1"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]


###################################################
# -------------- Percussion ----------------------/
# timpani1 
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "timpani1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# vibraphone 
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "vibraphone"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# harp 
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "harp"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

###################################################
#----------------Strings -------------------------/
# violin1  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "violin1"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# violin2  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "violin2"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]


# viola  
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "viola1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# cello
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "cello1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]

# doublebass 
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "doublebass"
 
rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = [
        (0, marana.time_signature("4/4")),
        (1, marana.time_signature("3/4")),
        (3, marana.time_signature("4/4")),
        (4, marana.time_signature("3/4")),
]


# ---------------------------------------RUN SEGMENT

lilypond_file = segment_maker.run()
