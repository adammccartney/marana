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
      instrument = "tuba"
      subtitle = ""
      composer = "Adam McCartney"
      tagline = ""
    }

  \score {
  <<

    \new Staff \with {
      instrumentName = #"Tuba"
      shortInstrumentName = #"tb"
      midiInstrument = #"tuba"
    } <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "bass"
      \tempo 4 = 55
    \new Voice {
     \compressMMRests {
    \stringCanonGP
    \tuba_segment_chorale
    \tuba_segment_IYGH_A
    \tuba_segment_IYGH_B
    }
    } %% end of bsn notes
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
 
