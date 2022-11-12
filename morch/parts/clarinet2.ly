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
      instrument = "clarinet in Bb two"
      subtitle = "transposing part, sounds 2vb"
      composer = "Adam McCartney"
      tagline = ""
    }
  \score {
  <<

    \new Staff \with {
      instrumentName = #"Clarinet Bb 2"
      shortInstrumentName = #"Cl. 2"
      midiInstrument = #"clarinet"
    } <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "treble"
      \tempo 4 = 55
    \new Voice {
    \compressMMRests {
      \transpose bf c'
      \clTwo_segment_strings
      \clTwo_segment_chorale
      \clTwo_segment_IYGH_A
      \clTwo_segment_IYGH_B
}
    } % end of clarinet 1, 2 voice one
  >> %% end wwind staff group

  >> % score
  \layout {
           indent = 2\cm
           % Increase the size of the bar number by 2
           \override Score.BarNumber.font-size = #2
           \set Score.markFormatter = #format-mark-box-alphabet
           \override Score.RehearsalMark.font-size = #5 
           \set Staff.barAlways = ##t
           \set Staff.defaultBarType = ""  
  }
 } % score
} % book
 
