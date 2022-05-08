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
  <<

  \new StaffGroup << %% strings
    
  \tempo 4 = 55
      
      \new Staff \with {
        instrumentName = #"Violin 1"
        shortInstrumentName = #"vln1"
        midiInstrument = #"violin"
      }{ 
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "treble"
        \violinOne_segment_strings
      }

      \new Staff \with {
        instrumentName = #"Violin 2"
        shortInstrumentName = #"vln2"
        midiInstrument = #"violin"
      }{ 
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "treble"
        \violinTwo_segment_strings
      } %% end of vln two notes


      \new Staff \with {
        instrumentName = #"Viola"
        shortInstrumentName = #"vla"
        midiInstrument = #"viola"
      }{ 
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "alto"
        \viola_segment_strings
      } %% end of vla notes


      \new Staff \with {
        instrumentName = #"Cello"
        shortInstrumentName = #"vlc"
        midiInstrument = #"cello"
      }{ 
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "bass"
        \cello_segment_strings
      } %% end of cello notes


      \new Staff \with {
        instrumentName = #"Contrabass"
        shortInstrumentName = #"Cb"
        midiInstrument = #"contrabass"
      }{ 
        \accidentalStyle modern-cautionary 
        \time 4/4
        \clef "bass"
        \contrabass_segment_strings
      } %% end of bsn notes

    >> %% end strings 

  >> % score

    \header {piece = "marana, string sketch"}
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

