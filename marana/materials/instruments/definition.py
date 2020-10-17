import abjad

from marana.materials.instruments import markups as markups

instruments = abjad.OrderedDict(
    [
        #Woodwind
        (
            "flute 1",
            abjad.Flute(
                markup=markups.instrument("Flute 1"),
                short_markup=markups.short_instrument("fl.1"),
                ),
            ),
        (
            "oboe 1",
            abjad.Oboe(
                markup=markups.instrument("Oboe 1"),
                short_markup=markups.short_instrument("ob.1"),
                ),
            ),
        (
            "Bbclarinet 1",
            abjad.ClarinetInBFlat(
                markup=markups.instrument("Bb Clarinet 1"),
                short_markup=markups.short_instrument("Bbcl.1"),
                ),
            ),
        (
            "bassoon 1",
            abjad.Bassoon(
                markup=markups.instrument("Bassoon 1"),
                short_markup=markups.short_instrument("bsn.1"),
                ),
            ),
        # Brass
        (
            "fhorn 1",
            abjad.FrenchHorn(
                markup=markups.instrument("F Horn 1"),
                short_markup=markups.short_instrument("fhrn.1"),
                ),
            ),
        (
            "fhorn 3",
            abjad.FrenchHorn(
                markup=markups.instrument("F Horn 3"),
                short_markup=markups.short_instrument("fhrn.3"),
                ),
            ),
        (
            "trumpet 1",
            abjad.Trumpet(
                markup=markups.instrument("Trumpet 1"),
                short_markup=markups.short_instrument("trp.1"),
                ),
            ),
        (
            "trombone 1",
            abjad.TenorTrombone(
                markup=markups.instrument("Trombone 1"),
                short_markup=markups.short_instrument("trb.1"),
                ),
            ),
        # Percussion 
        (
            "timpani 1",
            abjad.Percussion(
                markup=markups.instrument("Timpani 1"),
                short_markup=markups.short_instrument("timp.1"),
                ),
            ),
        (
            "vibraphone",
            abjad.Percussion(
                markup=markups.instrument("Vibraphone"),
                short_markup=markups.short_instrument("vibes"),
                ),
            ),
        # Strings 
        (
            "harp",
            abjad.Harp(
                markup=markups.instrument("Harp"),
                short_markup=markups.short_instrument("hrp"),
                ),
            ),
        (
            "violin 1",
            abjad.Violin(
                markup=markups.instrument("Violin 1"),
                short_markup=markups.short_instrument("vln.1"),
                ),
            ),
        (
            "violin 2",
            abjad.Violin(
                markup=markups.instrument("Violin 2"),
                short_markup=markups.short_instrument("vln.1"),
                ),
            ),
        (
            "viola 1",
            abjad.Viola(
                markup=markups.instrument("Viola 1"),
                short_markup=markups.short_instrument("vla.1"),
                ),
            ),
        (
            "cello 1",
            abjad.Cello(
                markup=markups.instrument("Cello 1"),
                short_markup=markups.short_instrument("vlc.1"),
                ),
            ),
        (
            "doublebass",
            abjad.Contrabass(
                markup=markups.instrument("Double Bass"),
                short_markup=markups.short_instrument("db"),
                ),
            ),
        ]
    )

if __name__ == '__main__':
    for key, item in instruments.items():
        print(key, item)


