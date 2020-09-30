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
    ])),
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


melody_voice = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        ("p1", abjad.OrderedDict([
            (1, abjad.PitchSegment("e c fs as a d")),
            (2, abjad.PitchSegment("e' c' fs' as' a' d'")),
            (3, abjad.PitchSegment("b' g' cs' f' e' as'")),
            (4, abjad.PitchSegment("e'' c'' fs'' as'' a'' ds''")),
            (5, abjad.PitchSegment("gs'' e'' as'' d''' cs''' g''")),
            (6, abjad.PitchSegment("b'' g'' cs'' f'' e'' as''")),
            (8, abjad.PitchSegment("e''' c''' fs''' as''' a''' ds'''")),
            (10, abjad.PitchSegment("gs''' e''' as''' d'''' cs'''' g'''")),
            ])
        ),
        ("p2", abjad.OrderedDict([
            (1, abjad.PitchSegment("d a, d e gs fs a")),
            ])
        ),
        ("p3", abjad.OrderedDict([
            (1, abjad.PitchSegment("a f c' ef f g")),
            ])
         ),
    ])),
    ("green", abjad.OrderedDict([
        ("p1", abjad.OrderedDict([
            (1, abjad.PitchSegment("g g' as cs' ds' e' a'")),
            ])
         ),
        ("p2", abjad.OrderedDict([
            (1, abjad.PitchSegment("a a' gs b cs' gs' cs'")),
            ])
         ),
        ("p3", abjad.OrderedDict([
            (1, abjad.PitchSegment("cs cs' ef g a g c")),
        ])
         ),
    ])
])


tremolo_voice = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        (2, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("e, c, fs, cs, cs, a,")),
            ("p2", abjad.PitchSegment("d, f, e, b,, as, gs,")),
            ("p3", abjad.PitchSegment("a, cs bf, c c d")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("e c fs cs cs a")),
            ("p2", abjad.PitchSegment("d f e b, as gs")),
            ("p3", abjad.PitchSegment("a cs' bf c' c' d'")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("e' c' fs' cs' cs' a'")),
            ("p2", abjad.PitchSegment("d' f' e' b as' gs'")),
            ("p3", abjad.PitchSegment("a' cs'' bf' c'' c'' d''")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("e'' c'' fs'' cs'' cs'' a''")),
            ("p2", abjad.PitchSegment("d'' f'' e'' b' as'' gs''")),
            ("p3", abjad.PitchSegment("a'' cs''' bf'' c''' c''' d'''")),
            ])
         ),
        (6, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("e''' c''' fs''' cs''' cs''' a'''")),
            ("p2", abjad.PitchSegment("d''' f''' e''' b'' as''' gs'''")),
            ("p3", abjad.PitchSegment("a''' cs'''' bf''' c'''' c'''' d''''")),
            ])
         ),
    ])),
    ("green", abjad.OrderedDict([
        (2, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g, e, fs, as, cs a,")),
            ("p2", abjad.PitchSegment("a, f, b, d cs fs,")),
            ("p3", abjad.PitchSegment("cs a, bf, c d f")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g e fs as cs' a")),
            ("p2", abjad.PitchSegment("a f b d' cs' fs'")),
            ("p3", abjad.PitchSegment("cs' a bf c' d' f'")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g' e' fs' as' cs'' a'")),
            ("p2", abjad.PitchSegment("a' f' b' d'' cs'' fs''")),
            ("p3", abjad.PitchSegment("cs'' a' bf' c'' d'' f''")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g'' e'' fs'' as'' cs''' a''")),
            ("p2", abjad.PitchSegment("a'' f'' b'' d''' cs''' fs'''")),
            ("p3", abjad.PitchSegment("cs''' a'' bf'' c''' d''' f'''")),
            ])
         ),
        (6, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g'' e'' fs'' as'' cs''' a''")),
            ("p2", abjad.PitchSegment("a'' f'' b'' d''' cs''' fs'''")),
            ("p3", abjad.PitchSegment("cs''' a'' bf'' c''' d''' f'''")),
            ])
         ),
    ])),
    ("red", abjad.OrderedDict([
        (1, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g,, c, f, cs, e,, cs,,")),
            ("p2", abjad.PitchSegment("f,, a,, gs,, d,, gs,, as,,")),
            ("p3", abjad.PitchSegment("a,, f,, g,, ef,, f,, d,,")),
            ])
         ),
        (2, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g, c f cs e, cs,")),
            ("p2", abjad.PitchSegment("f, a, gs, d, gs, as,")),
            ("p3", abjad.PitchSegment("a, f, g, ef, f, d,")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g c' f' cs' e cs")),
            ("p2", abjad.PitchSegment("f a gs d gs as")),
            ("p3", abjad.PitchSegment("a f g ef f d")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g' c'' f'' cs'' e' cs'")),
            ("p2", abjad.PitchSegment("f' a' gs' d' gs' as'")),
            ("p3", abjad.PitchSegment("a' f' g' ef' f' d'")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("g'' c''' f''' cs''' e'' cs''")),
            ("p2", abjad.PitchSegment("f'' a'' gs'' d'' gs'' as''")),
            ("p3", abjad.PitchSegment("a'' f'' g'' ef'' f'' d''")),
            ])
         ),
    ])),
    ("black", abjad.OrderedDict([
        (2, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("c e as, cs a, cs")),
            ("p2", abjad.PitchSegment("a, d gs, b, fs, gs,")),
            ("p3", abjad.PitchSegment("f, a, ef, g, d, f,")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("c' e' as cs' a cs'")),
            ("p2", abjad.PitchSegment("a d' gs b fs gs")),
            ("p3", abjad.PitchSegment("f a ef g d f")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("c'' e'' as' cs'' a' cs''")),
            ("p2", abjad.PitchSegment("a' d'' gs' b' fs' gs'")),
            ("p3", abjad.PitchSegment("f' a' ef' g' d' f'")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("p1", abjad.PitchSegment("c''' e''' as'' cs''' a'' cs'''")),
            ("p2", abjad.PitchSegment("a'' d''' gs'' b'' fs'' gs''")),
            ("p3", abjad.PitchSegment("f'' a'' ef'' g'' d'' f''")),
            ])
         ),
    ])),
])
