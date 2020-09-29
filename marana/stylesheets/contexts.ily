% marana 2020

\layout {
% GLOBAL SKIPS
    \context {
        \name GlobalSkips
        \type Engraver_group
        \consists Script_engraver
        \consists Text_engraver
        %\consists \alternateTextSpannerEngraver

        \override TextScript.font-size = 6

        \override TextSpanner.font-size = 6
        }

    % GLOBAL RESTS
    \context {
        \name GlobalRests
        \type Engraver_group
        \consists Multi_measure_rest_engraver

        \override MultiMeasureRest.transparent = ##t

        \override MultiMeasureRestText.staff-padding = 2
        \override MultiMeasureRestText.font-size = 3
        \override MultiMeasureRestText.outside-staff-priority = 0
        \override MultiMeasureRestText.padding = 0
        }

    % PAGE LAYOUT
    \context {
        \name PageLayout
        \type Engraver_group
        \consists Text_engraver
        \consists \alternateTextSpannerEngraver

        \override TextSpanner.font-size = 6
        }


    % GLOBAL CONTEXT
    \context {
        \name GlobalContext
        \type Engraver_group
        \consists Axis_group_engraver
        \consists Bar_number_engraver
        \consists Mark_engraver
        % prevents LilyPond cyclic chain in pure-Y-offset callbacks warning:
        \consists Staff_collecting_engraver
        %\consists Time_signature_engraver
        \accepts GlobalSkips
        \accepts GlobalRests
        \accepts PageLayout

        % Y-extent = ##f 
        \override BarNumber.Y-extent = ##f
        \override BarNumber.font-size = 1

    }

    % VOICE
    \context {
        \Voice
        \remove Forbid_line_break_engraver

        \override MultiMeasureRest.transparent = ##t
    }

    % STAFF
    \context {
        \Staff
        \accepts GlobalRests

        \remove Time_signature_engraver

        \override BarLine.transparent = ##t
    }

    % remove after rebuild:
    \context {
        \PianoStaff
        \override StaffGrouper.staff-staff-spacing.minimum-distance = 14
    }

    % MUSIC CONTEXT
    \context {
        \ChoirStaff
        \name MusicContext
        \type Engraver_group
        \alias ChoirStaff
        systemStartDelimiter = #'SystemStartBar
    }

    % SCORE
    \context {
        \Score
        \accepts GlobalContext
        \accepts MusicContext
        \remove Bar_number_engraver
        \remove Metronome_markup_engraver
        \remove System_start_delimiter_engraver

        \override Beam.breakable = ##t
        \override Beam.damping = 99

        \override Glissando.breakable = ##t
        \override Glissando.thickness = 3

        \override Hairpin.to-barline = ##f

        \override NoteCollision.merge-differently-dotted = ##t

        \override NoteColumn.ignore-collision = ##t

        %%%\shape #'((-2 . 0) (-1 . 0) (-0.5 . 0) (0 . 0)) RepeatTie                 
        \override RepeatTie.X-extent = ##f
        % these do not work for all repeat ties:
        \override RepeatTie.details.note-head-gap = #-0.5
        \override RepeatTie.extra-offset = #'(-0.5 . 0)

        \override SpacingSpanner.strict-grace-spacing = ##t
        \override SpacingSpanner.strict-note-spacing = ##t
        \override SpacingSpanner.uniform-stretching = ##t

        \override StemTremolo.beam-width = 1.5
        \override StemTremolo.slope = 0.5

        \override TextScript.font-name = #"Palatino"
        % DISCOVERY: overriding TextScript.X-extent = ##f
        %            makes LilyPond ignore self-alignment-X tweaks;
        %            probably should never be done at stylesheet level.
        % NOTE:      may be best to override NO text script properties.

        %\override TimeSignature.stencil = ##f

        \override TupletBracket.breakable = ##t
        \override TupletBracket.full-length-to-extent = ##f

        \override TupletNumber.font-size = 0.333
        \override TupletNumber.text = #tuplet-number::calc-fraction-text

        autoBeaming = ##f
        proportionalNotationDuration = #(ly:make-moment 1 11)
        tupletFullLength = ##t
    }
}
