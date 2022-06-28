\version "2.22.0"
\language "english"

VIOLA = {
     r1
     r1
     r1
     r1
     r1
     r4 r8 e''8(\pp a'' e'' a'--) e''(
     bf'8 g' a' e') a'( e' a'4)
     r4 r8 e''8( a'' e'' a'--) fs''(
     ef''8 e'') a'( e' a' e' a'4)
     r1
     r4 r8 g'8( c'' g' c'--) a'(
     g'8 c' g) c'( g' c' c4)
     r4 r8 c''8( f'' c'' f') c''(
     f'8 e' d' f') c'( f' f4)
     r1
     r4 r8 c''8( a' d'' a' d')
     d''8( c'' b' a') d'( a d4)
}

\score {
  
    \new Staff \with {
      instrumentName = #"Flute 2"
      shortInstrumentName = #"Fl. 2"
      midiInstrument = #"flute"
    } << \new Voice {
      r1 c1 d1 
      e1 \break
      \set Staff.InstrumentName = "Piccolo"
      \set Staff.shortInstrumentName = "Picc."
      f1 
         }
>>
}

\layout {}