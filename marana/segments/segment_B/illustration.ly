\version "2.20.0"                                                              %! abjad.LilyPondFile._get_format_pieces()
\language "english"                                                            %! abjad.LilyPondFile._get_format_pieces()

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/stylesheet.ily"                                    %! abjad.LilyPondFile._get_formatted_includes()

\header {                                                                      %! abjad.LilyPondFile._get_formatted_blocks()
    title = ##f
    composer = ##f
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()

\score {                                                                       %! abjad.LilyPondFile._get_formatted_blocks()
    \context Score = "Score"                                                   %! marana.ScoreTemplate.__call__()
    \with                                                                      %! marana.ScoreTemplate.__call__()
    {                                                                          %! marana.ScoreTemplate.__call__()
        markFormatter = #format-mark-box-alphabet                              %! marana.ScoreTemplate.__call__()
    }                                                                          %! marana.ScoreTemplate.__call__()
    <<                                                                         %! marana.ScoreTemplate.__call__()
        \context MusicContext = "Music_Context"                                %! marana.ScoreTemplate.__call__()
        <<                                                                     %! marana.ScoreTemplate.__call__()
            \context StaffGroup = "Woodwind_Staff_Group"                       %! marana.ScoreTemplate.__call__()
            <<                                                                 %! marana.ScoreTemplate.__call__()
                \tag #'fluteOne
                \context Staff = "flute1"                                      %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "flute1_Markup_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "flute1_Music_Voice"                      %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "flute1_Dynamics_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'oboeOne
                \context Staff = "oboe1"                                       %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"oboe"                                   %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "oboe1_Markup_Voice"                      %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "oboe1_Music_Voice"                       %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "oboe1_Dynamics_Voice"                    %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'BbclarinetOne
                \context Staff = "Bbclarinet1"                                 %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"Bbclarinet"                             %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Markup_Voice"                %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Music_Voice"                 %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Dynamics_Voice"              %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'bassoonOne
                \context Staff = "bassoon1"                                    %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"bassoon"                                %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "bassoon1_Markup_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "bassoon1_Music_Voice"                    %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "bassoon1_Dynamics_Voice"                 %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
            >>                                                                 %! marana.ScoreTemplate.__call__()
            \context StaffGroup = "Brass_Staff_Group"                          %! marana.ScoreTemplate.__call__()
            <<                                                                 %! marana.ScoreTemplate.__call__()
                \tag #'fhornOne
                \context Staff = "fhorn1"                                      %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"fhorn"                                  %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "fhorn1_Markup_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "fhorn1_Music_Voice"                      %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "fhorn1_Dynamics_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'fhornThree
                \context Staff = "fhorn3"                                      %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"fhorn"                                  %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "fhorn3_Markup_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "fhorn3_Music_Voice"                      %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "fhorn3_Dynamics_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'trumpetOne
                \context Staff = "trumpet1"                                    %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"trumpet"                                %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "trumpet1_Markup_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "trumpet1_Music_Voice"                    %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "trumpet1_Dynamics_Voice"                 %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'tromboneOne
                \context Staff = "trombone1"                                   %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"trombone"                               %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "trombone1_Markup_Voice"                  %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "trombone1_Music_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "trombone1_Dynamics_Voice"                %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
            >>                                                                 %! marana.ScoreTemplate.__call__()
            \context StaffGroup = "Percussion_Staff_Group"                     %! marana.ScoreTemplate.__call__()
            <<                                                                 %! marana.ScoreTemplate.__call__()
                \tag #'timpaniOne
                \context Staff = "timpani1"                                    %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"timpani"                                %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "timpani1_Markup_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "timpani1_Music_Voice"                    %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "timpani1_Dynamics_Voice"                 %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'vibraphone
                \context Staff = "vibraphone"                                  %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"vibraphone"                             %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "vibraphone_Markup_Voice"                 %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "vibraphone_Music_Voice"                  %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "vibraphone_Dynamics_Voice"               %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
            >>                                                                 %! marana.ScoreTemplate.__call__()
            \tag #'harp
            \context Staff = "harp"                                            %! marana.ScoreTemplate.__call__()
            \with                                                              %! marana.ScoreTemplate.__call__()
            {                                                                  %! marana.ScoreTemplate.__call__()
                midiInstrument = #"harp"                                       %! marana.ScoreTemplate.__call__()
            }                                                                  %! marana.ScoreTemplate.__call__()
            <<                                                                 %! marana.ScoreTemplate.__call__()
                \context Voice = "harp_Markup_Voice"                           %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \stopTextSpan
                }                                                              %! marana.ScoreTemplate.__call__()
                \context Voice = "harp_Music_Voice"                            %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    \mark #2
                    r1
                    r1
                    r1
                    r1
                    r1
                }                                                              %! marana.ScoreTemplate.__call__()
                \context Voice = "harp_Dynamics_Voice"                         %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \!
                }                                                              %! marana.ScoreTemplate.__call__()
            >>                                                                 %! marana.ScoreTemplate.__call__()
            \context StaffGroup = "String_Staff_Group"                         %! marana.ScoreTemplate.__call__()
            <<                                                                 %! marana.ScoreTemplate.__call__()
                \tag #'violinOne
                \context Staff = "violin1"                                     %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "violin1_Markup_Voice"                    %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "violin1_Music_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "violin1_Dynamics_Voice"                  %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'violinTwo
                \context Staff = "violin2"                                     %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "violin2_Markup_Voice"                    %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "violin2_Music_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "violin2_Dynamics_Voice"                  %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'violaOne
                \context Staff = "viola1"                                      %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"viola"                                  %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "viola1_Markup_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "viola1_Music_Voice"                      %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "viola1_Dynamics_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'celloOne
                \context Staff = "cello1"                                      %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"cello"                                  %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "cello1_Markup_Voice"                     %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "cello1_Music_Voice"                      %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "cello1_Dynamics_Voice"                   %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
                \tag #'doublebassOne
                \context Staff = "doublebass"                                  %! marana.ScoreTemplate.__call__()
                \with                                                          %! marana.ScoreTemplate.__call__()
                {                                                              %! marana.ScoreTemplate.__call__()
                    midiInstrument = #"doublebass"                             %! marana.ScoreTemplate.__call__()
                }                                                              %! marana.ScoreTemplate.__call__()
                <<                                                             %! marana.ScoreTemplate.__call__()
                    \context Voice = "doublebass_Markup_Voice"                 %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \stopTextSpan
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "doublebass_Music_Voice"                  %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        \mark #2
                        r1
                        r1
                        r1
                        r1
                        r1
                    }                                                          %! marana.ScoreTemplate.__call__()
                    \context Voice = "doublebass_Dynamics_Voice"               %! marana.ScoreTemplate.__call__()
                    {                                                          %! marana.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        s1 * 1/1
                        \!
                    }                                                          %! marana.ScoreTemplate.__call__()
                >>                                                             %! marana.ScoreTemplate.__call__()
            >>                                                                 %! marana.ScoreTemplate.__call__()
        >>                                                                     %! marana.ScoreTemplate.__call__()
    >>                                                                         %! marana.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()