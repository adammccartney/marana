\version "2.22.0"
\language "english"

\include "../segments.ily"

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
    \header {piece = "marana"}
  <<

    \new Staff \with {
      instrumentName = #"Bass Trombone"
      shortInstrumentName = #"B Trb"
      midiInstrument = #"trombone"
    } <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "bass"
    \new Voice {
      \btrb_segment_chorale
    } %% end of bsn notes
  >> %% end of bsn staff

  >> % score
 } % score
} % book
 
