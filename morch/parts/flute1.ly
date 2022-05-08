\version "2.22.0"
\language "english"

\include "../segments/wwindChorale.ily"

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
    \header {piece = "marana, wwindChorale sketch, flute 1"}
  <<

  \new StaffGroup << %% wwinds

    \new Staff \with {
      instrumentName = #"Flute 1"
      shortInstrumentName = #"Fl. 1"
      midiInstrument = #"flute"
    } <<
      \accidentalStyle modern-cautionary 
      \clef "treble"
      \time 4/4
      \tempo 4 = 55
      \new Voice { 
        \flOne_segment_chorale 
      } % end of flute voice one 
    >> %% end of flute staff
  >> %% end wwind staff group

  >> % score

} % score
} % book
 
