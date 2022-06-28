\version "2.22.0"
\language "english"

\include "./segments.ily"
\include "../macros.ily"

\book {
  
  \paper {
    #(set-paper-size "a4")
  line-width = 230\mm
  two-sided = ##t
  %inner-margin = 23\mm 
  %outer-margin = 25\mm 
  %ragged-right = ##f
  %ragged-last = ##f
  
  min-systems-per-page = #3
  max-systems-per-page = #12
  system-system-spacing.padding = #15  %fit staves closer together
  system-system-spacing.stretchability = #15  %how flexible the spacing is


 myStaffSize = #20
  #(define fonts
    (make-pango-font-tree "Times New Roman"
                          "Nimbus Sans"
                          "Luxi Mono"
                          
                           (/ myStaffSize 20))) 
  
  }
  \header {
      title = "marana"
      instrument = "harp"
      subtitle = ""
      composer = "Adam McCartney"
      tagline = ""
    }


  \score {
  <<

    \new Staff \with {
      instrumentName = #"harp"
      shortInstrumentName = #"hrp"
      midiInstrument = #"harp"
    } <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "treble"
    \new Voice {
      \harp_segment_strings
      \harp_segment_chorale
      \harp_segment_IYGH_A
      \harp_segment_IYGH_B
    } %% end of vln notes
  >> %% end of bsn staff

  >> % score
  \layout {
           indent = 1\cm
           % Increase the size of the bar number by 2
           \override Score.BarNumber.font-size = #2
           \set Score.markFormatter = #format-mark-box-alphabet
           \override Score.RehearsalMark.font-size = #5 
           \set Staff.barAlways = ##t
           \set Staff.defaultBarType = ""  
  }
 } % score
} % book
 