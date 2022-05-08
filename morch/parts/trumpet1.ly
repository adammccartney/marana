\version "2.22.0"
\language "english"

\include "../segments/brassIYGH_A.ily"
\include "../segments/brassIYGH_B.ily"

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

  \score {
    \header {piece = "marana, if you get to heaven sketch, trumpet 1 (sounds 2vb)"}
  <<

    \new Staff \with {
      instrumentName = #"Trumpet 1"
      shortInstrumentName = #"trp 1"
      midiInstrument = #"trumpet"
    } <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "treble"
      \tempo 4 = 55
    \new Voice {
      \transpose bf c'
      \trpOneTwo_segment_IYGH_A
      \trpOneTwo_segment_IYGH_B
    } %% end of vln notes
  >> %% end of bsn staff

  >> % score
 } % score
} % book
 
