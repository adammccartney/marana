#!/usr/bin/python

import abjad

"""
  Dictionary of chord voices used:
      Breaking line length style rules, as there seems to be trouble
      initializing the PitchSegment objects otherwise
"""


chord_voice = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "e,,, fs,,, cs,,, d,,, e,,, as,,, a,,, c,, c,,"
        )),
        (1, abjad.PitchSegment(
            "e,, fs,, cs,, d,, e,, as,, a,, c, c,"
        )),
        (2, abjad.PitchSegment(
            "e, fs, cs, d, e, as, a, c c"
        )),
        (3, abjad.PitchSegment(
            "e fs cs d e as a c' c'"
        )),
        (4, abjad.PitchSegment(
            "e' fs' cs' d' e' as' a' c'' c''"
        )),
        (5, abjad.PitchSegment(
            "e'' fs'' cs'' d'' e'' as'' a'' c''' c'''"
        )),
        (6, abjad.PitchSegment(
            "e''' fs''' cs''' d''' e''' as''' a''' c'''' c''''"
        )),
        (7, abjad.PitchSegment(
            "e'''' fs'''' cs'''' d'''' e'''' as'''' a'''' c''''' c'''''"
        )),
        (8,
         abjad.PitchSegment(
             "e''''' fs''''' cs''''' d''''' e''''' as''''' a''''' c'''''' c''''''"
         )),
    ])
    ),
    ("green", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "g,,, fs,,, a,,, a,,, b,,, cs,, cs,, bf,,, d,,"
        )),
        (1, abjad.PitchSegment(
            "g,, fs,, a,, a,, b,, cs, cs, bf,, d,"
        )),
        (2, abjad.PitchSegment(
            "g, fs, a, a, b, cs cs bf, d"
        )),
        (3, abjad.PitchSegment(
            "g fs a a b cs' cs' bf d'"
        )),
        (4, abjad.PitchSegment(
            "g' fs' a' a' b' cs'' cs'' bf' d''"
        )),
        (5, abjad.PitchSegment(
            "g'' fs'' a'' a'' b'' cs''' cs''' bf'' d'''"
        )),
        (6,
         abjad.PitchSegment(
             "g''' fs''' a''' a''' b''' cs'''' cs'''' bf''' d''''"
         )),
        (7,
         abjad.PitchSegment(
             "g'''' fs'''' a'''' a'''' b'''' cs''''' cs''''' bf'''' d'''''"
         )),
        (8,
         abjad.PitchSegment(
             "g''''' fs''''' a''''' a''''' b''''' cs'''''' cs'''''' bf''''' d''''''"
         )),
    ])),
    ("red", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "g,,, cs,, e,,, f,,, gs,,, gs,,, a,,, g,,, f,,,"
        )),
        (1, abjad.PitchSegment(
            "g,, cs, e,, f,, gs,, gs,, a,, g,, f,,"
        )),
        (2, abjad.PitchSegment(
            "g, cs e, f, gs, gs, a, g, f,"
            )),
        (3, abjad.PitchSegment(
            "g cs' e f gs gs a g f"
        )),
        (4, abjad.PitchSegment(
            "g' cs'' e' f' gs' gs' a' g' f'"
            )),
        (5, abjad.PitchSegment(
            "g'' cs''' e'' f'' gs'' gs'' a'' g'' f''"
            )),
        (6, abjad.PitchSegment(
            "g''' cs'''' e''' f''' gs''' gs''' a''' g''' f'''"
            )),
        (7, abjad.PitchSegment(
            "g'''' cs''''' e'''' f'''' gs'''' gs'''' a'''' g'''' f''''"
            )),
        (8, abjad.PitchSegment(
            "g''''' cs'''''' e''''' f''''' gs''''' gs''''' a''''' g''''' f'''''"
            )),
    ])),
    ("black", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "c,, as,,, a,,, a,,, gs,,, fs,,, f,,, ef,,, d,,,"
            )),
        (1, abjad.PitchSegment(
            "c, as,, a,, a,, gs,, fs,, f,, ef,, d,,"
            )),
        (2, abjad.PitchSegment(
            "c as, a, a, gs, fs, f, ef, d,"
            )),
        (3, abjad.PitchSegment(
            "c' as a a gs fs f ef d"
            )),
        (4, abjad.PitchSegment(
            "c'' as' a' a' gs' fs' f' ef' d'"
            )),
        (5, abjad.PitchSegment(
            "c''' as'' a'' a'' gs'' fs'' f'' ef'' d''"
            )),
        (6, abjad.PitchSegment(
            "c'''' as''' a''' a''' gs''' fs''' f''' ef''' d'''"
            )),
        (7, abjad.PitchSegment(
            "c''''' as'''' a'''' a'''' gs'''' fs'''' f'''' ef'''' d''''"
            )),
        (8, abjad.PitchSegment(
            "c'''''' as''''' a''''' a''''' gs''''' fs''''' f''''' ef''''' d'''''"
            )),
    ])),
])

