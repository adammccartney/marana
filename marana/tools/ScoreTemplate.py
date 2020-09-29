import abjad
import marana

class ScoreTemplate(abjad.ScoreTemplate):
    """
    Makes a simple score template for symphony orchestra 
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    _always_make_global_rests = True

    _global_rests_in_topmost_staff = True
    
    def __init__(self):
        super(ScoreTemplate, self).__init__()
        self.voice_abbreviations.update(
            {"fl1": "flute1_Music_Voice",
             "ob1": "oboe1_Music_Voice",
             "Bbcl1": "Bbclarinet1_Music_Voice",
             "bsn1": "bassoon1_Music_Voice",
             "hrn1": "fhorn1_Music_Voice",
             "hrn3": "fhorn3_Music_Voice",
             "trp1": "trumpet1_Music_Voice",
             "trb1": "trombone1_Music_Voice",
             "tmp1": "timpani1_Music_Voice",
             "hrp": "harp_Music_Voice",
             "vln1": "violin1_Music_Voice",
             "vln2": "violin2_Music_Voice",
             "vla1": "viola1_Music_Voice",
             "vlc1": "cello1_Music_Voice",
             "db": "doublebass_Music_Voice",
             }
            )

    ### SPECIAL METHODS ###

    def __call__(self) -> abjad.Score:
        """
        Calls score template.
        """
        site = "marana.ScoreTemplate.__call__()"
        tag = abjad.Tag(site)

        # GLOBAL CONTEXT
        global_context = self._make_global_context()

        # Woodwind
        ## Flutes
        markup_voice = abjad.Voice(name="flute1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="flute1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="flute1_Dynamics_Voice", tag=tag)
        flute_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="flute1",
            tag=tag,
        )
        abjad.annotate(
            flute_staff,
            "default_instrument",
            marana.instruments["flute 1"],
        )
        abjad.annotate(flute_staff, "default_clef", abjad.Clef("treble"))
        fluteOne_tag = abjad.LilyPondLiteral(r"\tag #'fluteOne", format_slot='before')
        abjad.attach(fluteOne_tag, flute_staff)
        abjad.setting(flute_staff).midi_instrument = abjad.scheme.Scheme(
                'flute', force_quotes=True)

        ## Oboe
        markup_voice = abjad.Voice(name="oboe1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="oboe1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="oboe1_Dynamics_Voice", tag=tag)
        oboe_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="oboe1",
            tag=tag,
        )
        abjad.annotate(
            oboe_staff,
            "default_instrument",
            marana.instruments["oboe 1"],
        )
        abjad.annotate(oboe_staff, "default_clef", abjad.Clef("treble"))
        oboeOne_tag = abjad.LilyPondLiteral(r"\tag #'oboeOne", format_slot='before')
        abjad.attach(oboeOne_tag, oboe_staff)
        abjad.setting(oboe_staff).midi_instrument = abjad.scheme.Scheme(
                'oboe', force_quotes=True)

        ## Bb Clarinet
        markup_voice = abjad.Voice(name="Bbclarinet1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Bbclarinet1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Bbclarinet1_Dynamics_Voice", tag=tag)
        Bbclarinet_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Bbclarinet1",
            tag=tag,
        )
        abjad.annotate(
            Bbclarinet_staff,
            "default_instrument",
            marana.instruments["Bbclarinet 1"],
        )
        abjad.annotate(Bbclarinet_staff, "default_clef", abjad.Clef("treble"))
        BbclarinetOne_tag = abjad.LilyPondLiteral(r"\tag #'BbclarinetOne", format_slot='before')
        abjad.attach(BbclarinetOne_tag, Bbclarinet_staff)
        abjad.setting(Bbclarinet_staff).midi_instrument = abjad.scheme.Scheme(
                'Bbclarinet', force_quotes=True)

        ## Bassoon
        markup_voice = abjad.Voice(name="bassoon1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="bassoon1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="bassoon1_Dynamics_Voice", tag=tag)
        bassoon_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="bassoon1",
            tag=tag,
        )
        abjad.annotate(
            bassoon_staff,
            "default_instrument",
            marana.instruments["bassoon 1"],
        )
        abjad.annotate(bassoon_staff, "default_clef", abjad.Clef("treble"))
        bassoonOne_tag = abjad.LilyPondLiteral(r"\tag #'bassoonOne", format_slot='before')
        abjad.attach(bassoonOne_tag, bassoon_staff)
        abjad.setting(bassoon_staff).midi_instrument = abjad.scheme.Scheme(
                'bassoon', force_quotes=True)

        # Brass
        ## f horn 1
        markup_voice = abjad.Voice(name="fhorn1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="fhorn1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="fhorn1_Dynamics_Voice", tag=tag)
        fhorn_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="fhorn1",
            tag=tag,
        )
        abjad.annotate(
            fhorn_staff,
            "default_instrument",
            marana.instruments["fhorn 1"],
        )
        abjad.annotate(fhorn_staff, "default_clef", abjad.Clef("treble"))
        fhornOne_tag = abjad.LilyPondLiteral(r"\tag #'fhornOne", format_slot='before')
        abjad.attach(fhornOne_tag, fhorn_staff)
        abjad.setting(fhorn_staff).midi_instrument = abjad.scheme.Scheme(
                'fhorn', force_quotes=True)

        ## f horn 3
        markup_voice = abjad.Voice(name="fhorn3_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="fhorn3_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="fhorn3_Dynamics_Voice", tag=tag)
        fhorn_lstaff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="fhorn3",
            tag=tag,
        )
        abjad.annotate(
            fhorn_lstaff,
            "default_instrument",
            marana.instruments["fhorn 3"],
        )
        abjad.annotate(fhorn_lstaff, "default_clef", abjad.Clef("treble"))
        fhornThree_tag = abjad.LilyPondLiteral(r"\tag #'fhornThree", format_slot='before')
        abjad.attach(fhornThree_tag, fhorn_lstaff)
        abjad.setting(fhorn_lstaff).midi_instrument = abjad.scheme.Scheme(
                'fhorn', force_quotes=True)

        ## Trumpets
        markup_voice = abjad.Voice(name="trumpet1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="trumpet1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="trumpet1_Dynamics_Voice", tag=tag)
        trumpet_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="trumpet1",
            tag=tag,
        )
        abjad.annotate(
            trumpet_staff,
            "default_instrument",
            marana.instruments["trumpet 1"],
        )
        abjad.annotate(trumpet_staff, "default_clef", abjad.Clef("treble"))
        trumpetOne_tag = abjad.LilyPondLiteral(r"\tag #'trumpetOne", format_slot='before')
        abjad.attach(trumpetOne_tag, trumpet_staff)
        abjad.setting(trumpet_staff).midi_instrument = abjad.scheme.Scheme(
                'trumpet', force_quotes=True)


        ## Trombones
        markup_voice = abjad.Voice(name="trombone1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="trombone1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="trombone1_Dynamics_Voice", tag=tag)
        trombone_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="trombone1",
            tag=tag,
        )
        abjad.annotate(
            trombone_staff,
            "default_instrument",
            marana.instruments["trombone 1"],
        )
        abjad.annotate(trombone_staff, "default_clef", abjad.Clef("treble"))
        tromboneOne_tag = abjad.LilyPondLiteral(r"\tag #'tromboneOne", format_slot='before')
        abjad.attach(tromboneOne_tag, trombone_staff)
        abjad.setting(trombone_staff).midi_instrument = abjad.scheme.Scheme(
                'trombone', force_quotes=True)
       
        # Percussion
        ## Timpani
        markup_voice = abjad.Voice(name="timpani1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="timpani1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="timpani1_Dynamics_Voice", tag=tag)
        timpani_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="timpani1",
            tag=tag,
        )
        abjad.annotate(
            timpani_staff,
            "default_instrument",
            marana.instruments["timpani 1"],
        )
        abjad.annotate(timpani_staff, "default_clef", abjad.Clef("treble"))
        timpaniOne_tag = abjad.LilyPondLiteral(r"\tag #'timpaniOne", format_slot='before')
        abjad.attach(timpaniOne_tag, timpani_staff)
        abjad.setting(timpani_staff).midi_instrument = abjad.scheme.Scheme(
                'timpani', force_quotes=True)


        ## Vibraphone
        markup_voice = abjad.Voice(name="vibraphone_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="vibraphone_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="vibraphone_Dynamics_Voice", tag=tag)
        vibraphone_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="vibraphone",
            tag=tag,
        )
        abjad.annotate(
            vibraphone_staff,
            "default_instrument",
            marana.instruments["vibraphone"],
        )
        abjad.annotate(vibraphone_staff, "default_clef", abjad.Clef("treble"))
        vibraphone_tag = abjad.LilyPondLiteral(r"\tag #'vibraphone", format_slot='before')
        abjad.attach(vibraphone_tag, vibraphone_staff)
        abjad.setting(vibraphone_staff).midi_instrument = abjad.scheme.Scheme(
                'vibraphone', force_quotes=True)
        
        # Strings
        ## Harp
        markup_voice = abjad.Voice(name="harp_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="harp_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="harp_Dynamics_Voice", tag=tag)
        harp_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="harp",
            tag=tag,
        )
        abjad.annotate(
            harp_staff,
            "default_instrument",
            marana.instruments["harp"],
        )
        abjad.annotate(harp_staff, "default_clef", abjad.Clef("treble"))
        harp_tag = abjad.LilyPondLiteral(r"\tag #'harp", format_slot='before')
        abjad.attach(harp_tag, harp_staff)
        abjad.setting(harp_staff).midi_instrument = abjad.scheme.Scheme(
                'harp', force_quotes=True)
        
        ## Violin 1
        markup_voice = abjad.Voice(name="violin1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="violin1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="violin1_Dynamics_Voice", tag=tag)
        violinOne_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="violin1",
            tag=tag,
        )
        abjad.annotate(
           violinOne_staff,
            "default_instrument",
            marana.instruments["violin 1"],
        )
        abjad.annotate(violinOne_staff, "default_clef", abjad.Clef("treble"))
        violinOne_tag = abjad.LilyPondLiteral(r"\tag #'violinOne", format_slot='before')
        abjad.attach(violinOne_tag, violinOne_staff)
        abjad.setting(violinOne_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)


        ## Violin 2
        markup_voice = abjad.Voice(name="violin2_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="violin2_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="violin2_Dynamics_Voice", tag=tag)
        violinTwo_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="violin2",
            tag=tag,
        )
        abjad.annotate(
            violinTwo_staff,
            "default_instrument",
            marana.instruments["violin 2"],
        )
        abjad.annotate(violinTwo_staff, "default_clef", abjad.Clef("treble"))
        violinTwo_tag = abjad.LilyPondLiteral(r"\tag #'violinTwo", format_slot='before')
        abjad.attach(violinTwo_tag, violinTwo_staff)
        abjad.setting(violinTwo_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        ## Viola
        markup_voice = abjad.Voice(name="viola1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="viola1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="viola1_Dynamics_Voice", tag=tag)
        viola_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="viola1",
            tag=tag,
        )
        abjad.annotate(
            viola_staff,
            "default_instrument",
            marana.instruments["viola 1"],
        )
        abjad.annotate(viola_staff, "default_clef", abjad.Clef("alto"))
        violaOne_tag = abjad.LilyPondLiteral(r"\tag #'violaOne", format_slot='before')
        abjad.attach(violaOne_tag, viola_staff)
        abjad.setting(viola_staff).midi_instrument = abjad.scheme.Scheme(
                'viola', force_quotes=True)

        ## Cello
        markup_voice = abjad.Voice(name="cello1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="cello1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="cello1_Dynamics_Voice", tag=tag)
        cello_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="cello1",
            tag=tag,
        )
        abjad.annotate(
            cello_staff,
            "default_instrument",
            marana.instruments["cello 1"],
        )
        abjad.annotate(cello_staff, "default_clef", abjad.Clef("bass"))
        celloOne_tag = abjad.LilyPondLiteral(r"\tag #'celloOne", format_slot='before')
        abjad.attach(celloOne_tag, cello_staff)
        abjad.setting(cello_staff).midi_instrument = abjad.scheme.Scheme(
                'cello', force_quotes=True)


        ## Doubleobass
        markup_voice = abjad.Voice(name="doublebass_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="doublebass_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="doublebass_Dynamics_Voice", tag=tag)
        doublebass_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="doublebass",
            tag=tag,
        )
        abjad.annotate(
            doublebass_staff,
            "default_instrument",
            marana.instruments["doublebass"],
        )
        abjad.annotate(doublebass_staff, "default_clef", abjad.Clef("bass"))
        doublebassOne_tag = abjad.LilyPondLiteral(r"\tag #'doublebassOne", format_slot='before')
        abjad.attach(doublebassOne_tag, doublebass_staff)
        abjad.setting(doublebass_staff).midi_instrument = abjad.scheme.Scheme(
                'doublebass', force_quotes=True)

        # Define staff groups
        ## Woodwind Staff Group
        woodwind_staff_group = abjad.StaffGroup(
                [flute_staff, oboe_staff, Bbclarinet_staff, bassoon_staff],
                simultaneous=True,
                lilypond_type="StaffGroup",
                name="Woodwind_Staff_Group",
                tag=tag,
                )
         
        ## Brass Staff Group
        brass_staff_group = abjad.StaffGroup(
                [fhorn_staff, fhorn_lstaff, trumpet_staff, trombone_staff],
                simultaneous=True,
                lilypond_type="StaffGroup",
                name="Brass_Staff_Group",
                tag=tag,
                )
         
        ## Percussion Staff Group
        percussion_staff_group = abjad.StaffGroup(
                [timpani_staff, vibraphone_staff],
                simultaneous=True,
                lilypond_type="StaffGroup",
                name="Percussion_Staff_Group",
                tag=tag,
                )
        
        ## String Staff Group
        string_staff_group = abjad.StaffGroup(
                [violinOne_staff, violinTwo_staff, viola_staff, cello_staff, doublebass_staff],
                simultaneous=True,
                lilypond_type="StaffGroup",
                name="String_Staff_Group",
                tag=tag,
                )
        
        # Music Context
        music_context = abjad.Context(
                [
                    woodwind_staff_group,
                    brass_staff_group,
                    percussion_staff_group,
                    harp_staff,
                    string_staff_group,
                ],
                lilypond_type="MusicContext",
                simultaneous=True,
                name="Music_Context",
                tag=tag,
                )

        # Score
        score = abjad.Score(
                [music_context], name="Score", tag=tag
                )
        return score
    
    ### PRIVATE METHODS ###

    def _make_global_context(self):
        site = "abjad.ScoreTemplate._make_global_context()"
        tag = abjad.Tag(site)
        global_rests = abjad.Context(
            lilypond_type="GlobalRests", name="Global_Rests", tag=tag,
        )
        global_skips = abjad.Context(
            lilypond_type="GlobalSkips", name="Global_Skips", tag=tag,
        )
        global_context = abjad.Context(
            [global_rests, global_skips],
            lilypond_type="GlobalContext",
            simultaneous=True,
            name="Global_Context",
            tag=tag,
        )
        return global_context


    ### PUBLIC PROPERTIES ###

    @property
    def voice_abbreviations(self):
        """Gets voice abbreviations""" 
        return super(ScoreTemplate, self).voice_abbreviations


if __name__ == '__main__':
    score = ScoreTemplate()
    score_template = score()
    abjad.f(score_template)
