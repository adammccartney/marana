\version "2.22.0"
\language "english"

\include "./segments.ily"
\include "./macros.ily"

\book {


    \header {
      title = "marana"
      subtitle = "score in c"
      composer = "Adam McCartney"
      tagline = ""
  }
  
  \paper {
    #(set-paper-size "a3")
  line-width = 230\mm
  two-sided = ##t
  %inner-margin = 23\mm 
  %outer-margin = 25\mm 
  %ragged-right = ##f
  %ragged-last = ##f
  
  min-systems-per-page = #1
  max-systems-per-page = #2
  system-system-spacing.padding = #15  %fit staves closer together
  system-system-spacing.stretchability = #15  %how flexible the spacing is


  myStaffSize = #17
  #(define fonts
    (make-pango-font-tree "Times New Roman"
                          "Nimbus Sans"
                          "Luxi Mono"
                          
                           (/ myStaffSize 19))) 
  
  }

  \score {
  <<

    \new StaffGroup << %% wwinds


    \tag #'flutes
    \new Staff \with {
      instrumentName = #"Flute 1"
      shortInstrumentName = #"Fl. 1"
      midiInstrument = #"flute"
    } <<
      \accidentalStyle modern-cautionary 
      \clef "treble"
      \tempo 4 = 55
      
      \new Voice { 
      \fluteOne_segment_strings
      \flOne_segment_chorale 
      \piccoloChange
      \fluteOne_segment_IYGH_A
       
      \fluteOne_segment_IYGH_B
      } % end of flute voice one 
    >>
    \new Staff \with {
      instrumentName = #"Flute 2"
      shortInstrumentName = #"Fl. 2"
      midiInstrument = #"flute"
    } <<
      \accidentalStyle modern-cautionary 
      \clef "treble"
      \tempo 4 = 55
      \new Voice {
      \fluteTwo_segment_strings
      \flTwo_segment_chorale
      \piccoloChange
      \fluteTwo_segment_IYGH_A
      
      \fluteTwo_segment_IYGH_B
      } % end of flute voice two
    >> %% end of flute staff

    \tag #'oboes
    \new Staff \with {
      instrumentName = #"Oboe 1"
      shortInstrumentName = #"Ob. 1"
      midiInstrument = #"oboe"
    } <<
      \accidentalStyle modern-cautionary 
      \tempo 4 = 55
      \clef "treble"
    \new Voice {
      \obOne_segment_strings
      \obOne_segment_chorale
      \obOne_segment_IYGH_A
      
      \obOne_segment_IYGH_B
    } %% end of oboe notes
  >> %% end of oboe staff


    \new Staff \with {
      instrumentName = #"Oboe 2"
      shortInstrumentName = #"Ob. 2"
      midiInstrument = #"oboe"
    } <<
      \accidentalStyle modern-cautionary 
      \tempo 4 = 55
      \clef "treble"
    \new Voice {
      \obTwo_segment_strings
      \obTwo_segment_chorale
      \obTwo_segment_IYGH_A
      
      \obTwo_segment_IYGH_B
    } %% end of oboe notes
  >> %% end of oboe two staff

    \tag #'clarinets
    \new Staff \with {
      instrumentName = #"Clarinet in Bb 1"
      shortInstrumentName = #"Cl. 1"
      midiInstrument = #"clarinet"
    } <<
      \accidentalStyle modern-cautionary 
      \tempo 4 = 55
      \clef "treble"
    \new Voice {
      \clOne_segment_strings
      \clOne_segment_chorale 
      \clOne_segment_IYGH_A
      
      \clOne_segment_IYGH_B
    } % end of clarinet 1, 2 voice one
  >>
    \new Staff \with {
      instrumentName = #"Clarinet in Bb 2"
      shortInstrumentName = #"Cl. 2"
      midiInstrument = #"clarinet"
    } <<
    \new Voice {
      \clTwo_segment_strings
      \clTwo_segment_chorale
      \clTwo_segment_IYGH_A
      
      \clTwo_segment_IYGH_B
    } % end of clarinet 1, 2 voice two
  >> %% end clarinets

    \tag #'bassoon
    \new Staff \with {
      instrumentName = #"Bassoon"
      shortInstrumentName = #"Bsn."
      midiInstrument = #"bassoon"
    } <<
      \accidentalStyle modern-cautionary 
      
      \tempo 4 = 55
      \clef "bass"
    \new Voice {
      \bsn_segment_strings
      \bsn_segment_chorale
      \bsn_segment_IYGH_A
      
      \bsn_segment_IYGH_B
    } %% end of bsn notes
  >> %% end of bsn staff

>> %% end wwind staff group

\new StaffGroup << %% brass


  \new Staff \with {
    instrumentName = #"French Horn 1,2"
    shortInstrumentName = #"F Horn. 1,2"
    midiInstrument = #"french horn"
  } <<
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
    \new Voice {
      \voiceOne {
      \override Voice.RehearsalMark.stencil = ##f
      \hnOne_segment_strings
      \hrnOne_segment_chorale
      \hrnOne_segment_IYGH_A
      \hrnOne_segment_IYGH_B
    }
    }
    \new Voice {
      \voiceTwo {
      \override Voice.DynamicText.stencil = ##f
      \override Voice.TextScript.stencil = ##f
      \override Voice.RehearsalMark.stencil = ##f
      \hnTwo_segment_strings
      \hrnTwo_segment_chorale
      \hrnTwo_segment_IYGH_A
      \hrnTwo_segment_IYGH_B
    }
  }
>> %% end hn 1 2


  \new Staff \with {
    instrumentName = #"French Horn 3,4"
    shortInstrumentName = #"F Horn. 3,4"
    midiInstrument = #"french horn"
  } <<
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
    \new Voice {
      \voiceThree {
      \override Voice.RehearsalMark.stencil = ##f
      \hnThree_segment_strings
      \hrnThree_segment_chorale
      \hrnThree_segment_IYGH_A
      \hrnThree_segment_IYGH_B
    }
  }
  \new Voice {
    \voiceFour {
      \override Voice.DynamicText.stencil = ##f
      \override Voice.TextScript.stencil = ##f
      \override Voice.RehearsalMark.stencil = ##f
      \hnFour_segment_strings
      \hrnFour_segment_chorale
      \hrnFour_segment_IYGH_A
      \hrnFour_segment_IYGH_B
    }
  } 
 >> %% end hn 3 4
  \new Staff \with {
    instrumentName = #"Trumpet 1"
    shortInstrumentName = #"Trp. 1"
    midiInstrument = #"trumpet"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
    \override Voice.RehearsalMark.stencil = ##f
    \trpOne_segment_strings
    \trpOne_segment_chorale
    \trpOneTwo_segment_IYGH_A
    \trpOneTwo_segment_IYGH_B
  } 

  \new Staff \with {
    instrumentName = #"Trumpet 2"
    shortInstrumentName = #"Trp. 2"
    midiInstrument = #"trumpet"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
    \override Voice.RehearsalMark.stencil = ##f
    \trpTwo_segment_strings
    \trpTwo_segment_chorale
    \trpThree_segment_IYGH_A
    \trpThree_segment_IYGH_B
  } 

  \new Staff \with {
    instrumentName = #"Trombone 1"
    shortInstrumentName = #"Trb. 1"
    midiInstrument = #"trombone"
  }{
    \accidentalStyle modern-cautionary 
    
    \clef "bass"
    \override Voice.RehearsalMark.stencil = ##f
    \trb_segment_strings
    \trb_segment_chorale
    \trbOneTwo_segment_IYGH_A
    \trbOneTwo_segment_IYGH_B
  }

  \new Staff \with {
    instrumentName = #"Tuba"
    shortInstrumentName = #"Tb."
    midiInstrument = #"tuba"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "bass"
    \override Voice.RehearsalMark.stencil = ##f
    \transpose c' c {
      \tuba_segment_strings
    }
    \tuba_segment_chorale
    \tuba_segment_IYGH_A
    \tuba_segment_IYGH_B
  }

  >> %% brass



\new StaffGroup << %% perc

  \new Staff \with {
    instrumentName = #"Vibraphone"
    shortInstrumentName = #"Vibes."
    midiInstrument = #"vibraphone"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
      \vibes_segment_strings
      \vibes_segment_chorale
      \vibes_segment_IYGH_A
      \vibes_segment_IYGH_B
  }

  \new Staff \with {
    instrumentName = #"Timpani"
    shortInstrumentName = #"Timp."
    midiInstrument = #"timpani"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55 
    \clef "bass"
      \tmp_segment_strings
      \timp_segment_chorale
      \tmp_segment_IYGH_A
      \tmp_segment_IYGH_B
  }
>> %% end perc 


  \new Staff \with {
    instrumentName = #"Harp"
    shortInstrumentName = #"Harp."
    midiInstrument = #"harp"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55 
    \clef "treble"
      \harp_segment_strings
      \harp_segment_chorale
      \harp_segment_IYGH_A
      \harp_segment_IYGH_B
  }


  \new StaffGroup << %% strings
    
      \new Staff \with {
        instrumentName = #"Violin 1"
        shortInstrumentName = #"vln1"
        midiInstrument = #"violin"
      }{ 
        \accidentalStyle modern-cautionary 
        \tempo 4 = 55 
        \clef "treble"
        \violinOne_segment_strings
        \violinOne_segment_chorale
        \vnone_segment_IYGH_A
        
        \vnone_segment_IYGH_B
      }

      \new Staff \with {
        instrumentName = #"Violin 2"
        shortInstrumentName = #"vln2"
        midiInstrument = #"violin"
      }{ 
        \accidentalStyle modern-cautionary 
        \tempo 4 = 55 
        \clef "treble"
        \violinTwo_segment_strings
        \violinTwo_segment_chorale
        \vntwo_segment_IYGH_A
        
        \vntwo_segment_IYGH_B
      } %% end of vln two notes


      \new Staff \with {
        instrumentName = #"Viola"
        shortInstrumentName = #"vla"
        midiInstrument = #"viola"
      }{ 
        \accidentalStyle modern-cautionary 
        \tempo 4 = 55 
        \clef "alto"
        \viola_segment_strings
        \viola_segment_chorale
        \va_segment_IYGH_A
        
        \va_segment_IYGH_B
      } %% end of vla notes


      \new Staff \with {
        instrumentName = #"Cello"
        shortInstrumentName = #"vlc"
        midiInstrument = #"cello"
      }{ 
        \accidentalStyle modern-cautionary 
        \tempo 4 = 55 
        \clef "bass"
        \cello_segment_strings
        \cello_segment_chorale
        \vc_segment_IYGH_A
        
        \vc_segment_IYGH_B
      } %% end of cello notes


      \new Staff \with {
        instrumentName = #"Contrabass"
        shortInstrumentName = #"Cb"
        midiInstrument = #"contrabass"
      }{ 
        \accidentalStyle modern-cautionary 
       \tempo 4 = 55 
        \clef "bass"
        \contrabass_segment_strings
        \contrabass_segment_chorale
        \kb_segment_IYGH_A
        
        \kb_segment_IYGH_B
      } %% end of bsn notes

    >> %% end strings 
  >> %% end score
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
                     \compressEmptyMeasures
                    }
  
           \context {
                     \Staff

     % To use the setting globally, uncomment the following line:
     \override VerticalAxisGroup #'remove-first = ##t
                    }
          
                
	        }
            \midi {}
} % score
} % book

  
