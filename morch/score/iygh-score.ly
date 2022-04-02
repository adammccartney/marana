\version "2.22.0"
\language "english"

\include "brass.ly"

instrument = ""
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
<<

\new StaffGroup << %% brass

  \new Staff \with {
    instrumentName = #"French Horn 1,2"
    shortInstrumentName = #"F Horn. 1,2"
    midiInstrument = #"french horn"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
    \hrnOneTwo_verseOne
  } 


  \new Staff \with {
    instrumentName = #"French Horn 3,4"
    shortInstrumentName = #"F Horn. 3,4"
    midiInstrument = #"french horn"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "bass"
    \hrnThreeFour_verseOne
  } 


  \new Staff \with {
    instrumentName = #"Trumpet 1,2"
    shortInstrumentName = #"Trp. 1,2"
    midiInstrument = #"trumpet"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
    \trpOneTwo_verseOne
  } 

  \new Staff \with {
    instrumentName = #"Trumpet 3"
    shortInstrumentName = #"Trp. 3"
    midiInstrument = #"trumpet"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
    \trpThree_verseOne
  } 

  \new Staff \with {
    instrumentName = #"Trombone 1,2"
    shortInstrumentName = #"Trb. 1,2"
    midiInstrument = #"trombone"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "bass"
    \trbOneTwo_verseOne
  }

  \new Staff \with {
    instrumentName = #"Bass Trombone"
    shortInstrumentName = #"B.Trb."
    midiInstrument = #"trombone"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "bass"
    \btrb_verseOne
  }

  \new Staff \with {
    instrumentName = #"Tuba"
    shortInstrumentName = #"Tb."
    midiInstrument = #"tuba"
  }{
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "bass"
    \tuba_verseOne
  }

  >> %% brass

>> % score


	\header {piece = "marana brass sketch (22) iygh"}
	
	
	\layout {
	  
	   indent = 1\cm
           % Increase the size of the bar number by 2
           \override Score.BarNumber.font-size = #2
        
           \set Score.markFormatter = #format-mark-box-alphabet
           \override Score.RehearsalMark.font-size = #5 
           \set Staff.barAlways = ##t
           \set Staff.defaultBarType = "" 
           
           \context {
                     \Score
                     \RemoveEmptyStaves
                    }
  
           \context {
                     \Staff
                    \RemoveEmptyStaves

     % To use the setting globally, uncomment the following line:

     \override VerticalAxisGroup #'remove-first = ##t
                    }
          
                
	        }
	        
	
	\midi {  
	  \context {                         %
          \Staff                             %
          \remove "Staff_performer"          % Creating single
          }                                  % midi channel 
          \context {                        % for each 
          \Voice                            % voice
          \consists "Staff_performer"      %  
                   }
	  \tempo 4 = 60} 
                    }
  }
  
  
