#!/python

import abjad

""" testing to find a data structure for the pitch material used in chords """


chord_voice = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        (0, abjad.PitchSegment("e,,, fs,,, cs,,, d,,, e,,, as,,, a,,,, c,, c,,")),
        (1, abjad.PitchSegment("e,, fs,, cs,, d,, e,, as,, a,,, c, c,")),
        (2, abjad.PitchSegment("e, fs, cs, d, e, as, a,, c c")),
        (3, abjad.PitchSegment("e fs cs d e as a, c' c'")),
        (4, abjad.PitchSegment("e' fs' cs' d' e' as' a c'' c''")),
        (5, abjad.PitchSegment("e'' fs'' cs'' d'' e'' as'' a' c''' c'''")),
        (6, abjad.PitchSegment("e''' fs''' cs''' d''' e''' as''' a'' c'''' c''''")),
        (7, abjad.PitchSegment("e'''' fs'''' cs'''' d'''' e'''' as'''' a''' c''''' c'''''")),
        (8, abjad.PitchSegment("e''''' fs''''' cs''''' d''''' e''''' as''''' a'''' c'''''' c''''''")),
    ])
    ),
])
