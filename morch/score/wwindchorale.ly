\version "2.22.0"
\language "english"

\include "./segments/wwindChorale.ily"

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

\new StaffGroup << %% wwinds

  \tempo 4 = 55

  \tag #'flutes
  \new Staff \with {
    instrumentName = #"Flute 1, 2"
    shortInstrumentName = #"Fl. 1,2"
    midiInstrument = #"flute"
  } <<
    \accidentalStyle modern-cautionary 
    \clef "treble"
    \time 4/4
    \new Voice { 
      \voiceOne {
      \flOne_segment_chorale 
      } % end of flute Voice one notes
    } % end of flute voice one 
    \new Voice {
      \voiceTwo {
        \override Voice.DynamicText.stencil = ##f
        \flTwo_segment_chorale
      } % end of flute two voice notes
    } % end of flute voice two
  >> %% end of flute staff

  \tag #'oboes
  \new Staff \with {
    instrumentName = #"Oboe 1"
    shortInstrumentName = #"Ob. 1"
    midiInstrument = #"oboe"
  } <<
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
  \new Voice {
    \obOne_segment_chorale
  } %% end of oboe notes
>> %% end of oboe staff


  \new Staff \with {
    instrumentName = #"Oboe 2"
    shortInstrumentName = #"Ob. 2"
    midiInstrument = #"oboe"
  } <<
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
  \new Voice {
    \obTwo_segment_chorale
  } %% end of oboe notes
>> %% end of oboe two staff



  \tag #'clarinets
  \new Staff \with {
    instrumentName = #"Clarinet in Bb 1, 2"
    shortInstrumentName = #"Cl. 1,2"
    midiInstrument = #"clarinet"
  } <<
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
  \new Voice {
    \voiceOne {
      \clOne_segment_chorale 
    } % end of clarinet one notes
  } % end of clarinet 1, 2 voice one
  \new Voice {
    \voiceTwo {
      \override Voice.DynamicText.stencil = ##f
      \clTwo_segment_chorale
    } % end of clarinet two notes
  } % end of clarinet 1, 2 voice two


  \tag #'bassoon
  \new Staff \with {
    instrumentName = #"Bassoon"
    shortInstrumentName = #"Bsn."
    midiInstrument = #"bassoon"
  } <<
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "bass"
  \new Voice {
    \bsn_segment_chorale
  } %% end of bsn notes
>> %% end of bsn staff

  >> %% end wwind 
>> %% end wwind staff group

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
  
  
