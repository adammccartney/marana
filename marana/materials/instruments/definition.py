import abjad
import mccartney

instruments = abjad.OrderedDict(
    [
        #Woodwind
        (
            "flute 1",
            abjad.Flute(
                markup=mccartney.markups.instrument("Flute 1"),
                short_markup=mccartney.markups.short_instrument("fl.1"),
                ),
            ),
        (
            "oboe 1",
            abjad.Oboe(
                markup=mccartney.markups.instrument("Oboe 1"),
                short_markup=mccartney.markups.short_instrument("ob.1"),
                ),
            ),
        (
            "Bbclarinet 1",
            abjad.ClarinetInBFlat(
                markup=mccartney.markups.instrument("Bb Clarinet 1"),
                short_markup=mccartney.markups.short_instrument("Bbcl.1"),
                ),
            ),
        (
            "bassoon 1",
            abjad.Bassoon(
                markup=mccartney.markups.instrument("Bassoon 1"),
                short_markup=mccartney.markups.short_instrument("bsn.1"),
                ),
            ),
        # Brass
        (
            "fhorn 1",
            abjad.FrenchHorn(
                markup=mccartney.markups.instrument("F Horn 1"),
                short_markup=mccartney.markups.short_instrument("fhrn.1"),
                ),
            ),
        (
            "fhorn 3",
            abjad.FrenchHorn(
                markup=mccartney.markups.instrument("F Horn 3"),
                short_markup=mccartney.markups.short_instrument("fhrn.3"),
                ),
            ),
        (
            "trumpet 1",
            abjad.Trumpet(
                markup=mccartney.markups.instrument("Trumpet 1"),
                short_markup=mccartney.markups.short_instrument("trp.1"),
                ),
            ),
        (
            "trombone 1",
            abjad.TenorTrombone(
                markup=mccartney.markups.instrument("Trombone 1"),
                short_markup=mccartney.markups.short_instrument("trb.1"),
                ),
            ),
        # Percussion 
        (
            "timpani 1",
            abjad.Percussion(
                markup=mccartney.markups.instrument("Timpani 1"),
                short_markup=mccartney.markups.short_instrument("timp.1"),
                ),
            ),
        (
            "vibraphone",
            abjad.Percussion(
                markup=mccartney.markups.instrument("Vibraphone"),
                short_markup=mccartney.markups.short_instrument("vibes"),
                ),
            ),
        # Strings 
        (
            "harp",
            abjad.Harp(
                markup=mccartney.markups.instrument("Harp"),
                short_markup=mccartney.markups.short_instrument("hrp"),
                ),
            ),
        (
            "violin 1",
            abjad.Violin(
                markup=mccartney.markups.instrument("Violin 1"),
                short_markup=mccartney.markups.short_instrument("vln.1"),
                ),
            ),
        (
            "violin 2",
            abjad.Violin(
                markup=mccartney.markups.instrument("Violin 2"),
                short_markup=mccartney.markups.short_instrument("vln.1"),
                ),
            ),
        (
            "viola 1",
            abjad.Viola(
                markup=mccartney.markups.instrument("Viola 1"),
                short_markup=mccartney.markups.short_instrument("vla.1"),
                ),
            ),
        (
            "cello 1",
            abjad.Cello(
                markup=mccartney.markups.instrument("Cello 1"),
                short_markup=mccartney.markups.short_instrument("vlc.1"),
                ),
            ),
        (
            "doublebass",
            abjad.Contrabass(
                markup=mccartney.markups.instrument("Double Bass"),
                short_markup=mccartney.markups.short_instrument("db"),
                ),
            ),
        ]
    )
