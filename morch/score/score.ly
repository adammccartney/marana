\version "2.22.0"
\language "english"

\include "./segments/stringcanon.ily"
\include "./segments/wwindChorale.ily"
\include "./segments/brassIYGH_A.ily"
\include "./segments/brassIYGH_B.ily"

%% MACROS

stringCanonGP = { R1*66 }
wwindChoraleGP = { R1*17 }
iyghBrassGP = { R1*20 }

\book {


    \header {
      title = "marana"
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
        \iyghBrassGP
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
          \iyghBrassGP
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
      \stringCanonGP
      \obOne_segment_chorale
      \iyghBrassGP
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
      \stringCanonGP
      \obTwo_segment_chorale
      \iyghBrassGP
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
      \stringCanonGP
      \clOne_segment_chorale 
      \iyghBrassGP
    } % end of clarinet 1, 2 voice one
  >>
    \new Staff \with {
      instrumentName = #"Clarinet in Bb 1"
      shortInstrumentName = #"Cl. 1"
      midiInstrument = #"clarinet"
    } <<
    \new Voice {
      \stringCanonGP
      \clTwo_segment_chorale
      \iyghBrassGP
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
      \stringCanonGP
      \bsn_segment_chorale
      \iyghBrassGP
    } %% end of bsn notes
  >> %% end of bsn staff

>> %% end wwind staff group

\new StaffGroup << %% brass


  \new Staff \with {
    instrumentName = #"French Horn 1,2"
    shortInstrumentName = #"F Horn. 1,2"
    midiInstrument = #"french horn"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
      \stringCanonGP
      \wwindChoraleGP
    \hrnOneTwo_segment_IYGH_A
    \hrnOneTwo_segment_IYGH_B
  } 


  \new Staff \with {
    instrumentName = #"French Horn 3,4"
    shortInstrumentName = #"F Horn. 3,4"
    midiInstrument = #"french horn"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "bass"
      \stringCanonGP
      \wwindChoraleGP
    \hrnThreeFour_segment_IYGH_A
    \hrnThreeFour_segment_IYGH_B
  } 


  \new Staff \with {
    instrumentName = #"Trumpet 1"
    shortInstrumentName = #"Trp. 1"
    midiInstrument = #"trumpet"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "treble"
      \stringCanonGP
      \wwindChoraleGP
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
      \stringCanonGP
      \wwindChoraleGP
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
      \stringCanonGP
      \wwindChoraleGP
    \trbOneTwo_segment_IYGH_A
    \trbOneTwo_segment_IYGH_B
  }

  \new Staff \with {
    instrumentName = #"Bass Trombone"
    shortInstrumentName = #"B.Trb."
    midiInstrument = #"trombone"
  }{
    \accidentalStyle modern-cautionary 
    
    \clef "bass"
      \stringCanonGP
      \wwindChoraleGP
    \btrb_segment_IYGH_A
    \btrb_segment_IYGH_B
  }

  \new Staff \with {
    instrumentName = #"Euphonium"
    shortInstrumentName = #"Euph."
    midiInstrument = #"tuba"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55
    \clef "bass"
      \stringCanonGP
      \wwindChoraleGP
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
      \wwindChoraleGP
      \iyghBrassGP
  }

  \new Staff \with {
    instrumentName = #"Timpani"
    shortInstrumentName = #"Timp."
    midiInstrument = #"timpani"
  }{
    \accidentalStyle modern-cautionary 
    \tempo 4 = 55 
    \clef "bass"
      \stringCanonGP
      \wwindChoraleGP
      \iyghBrassGP
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
      \wwindChoraleGP
      \iyghBrassGP
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
      \wwindChoraleGP
      \iyghBrassGP
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
      \wwindChoraleGP
      \iyghBrassGP
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
      \wwindChoraleGP
      \iyghBrassGP
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
      \wwindChoraleGP
      \iyghBrassGP
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
      \wwindChoraleGP
      \iyghBrassGP
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

} % score
} % book
  
