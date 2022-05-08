\version "2.22.0"
\language "english"

\include "./segments/stringcanon.ily"

\book {
  
  \paper {
    #(set-paper-size "a3")
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
    \header {piece = "marana, string sketch"}
  <<

  \new StaffGroup << %% strings
    
  \tempo 4 = 55
      
      \new Staff \with {
        instrumentName = #"Violin 1"
        shortInstrumentName = #"vln1"
        midiInstrument = #"violin"
      } <<
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "treble"
      \new Voice {
        \violinOne_segment_strings
      } %% end of vln notes
    >> %% end vln staff

      \new Staff \with {
        instrumentName = #"Violin 2"
        shortInstrumentName = #"vln2"
        midiInstrument = #"violin"
      } <<
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "treble"
      \new Voice {
        \violinTwo_segment_strings
      } %% end of vln two notes
    >> %% end of vln two staff


      \new Staff \with {
        instrumentName = #"Viola"
        shortInstrumentName = #"vla"
        midiInstrument = #"viola"
      } <<
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "alto"
      \new Voice {
        \viola_segment_strings
      } %% end of vla notes
    >> %% end of vla staff


      \new Staff \with {
        instrumentName = #"Cello"
        shortInstrumentName = #"vlc"
        midiInstrument = #"cello"
      } <<
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "bass"
      \new Voice {
        \cello_segment_strings
      } %% end of cello notes
    >> %% end of cello staff


      \new Staff \with {
        instrumentName = #"Contrabass"
        shortInstrumentName = #"Cb"
        midiInstrument = #"contrabass"
      } <<
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "bass"
      \new Voice {
        \contrabass_segment_strings
      } %% end of bsn notes
    >> %% end of bsn staff

    >> %% end strings 

  >> % score

  } % score
} % book
  
