\version "2.22.0"
\language "english"

\score {
  \new StaffGroup <<
  \new Staff <<
    \accidentalStyle modern-cautionary 
    \time 4/4
    \clef "treble"
    \new Voice {
      bf'16 a'8 g'16 f' e' d'8 c'16 bf a g g'16 f' e' d' ~ |
      d' c' bf a g g' f' e' d'8 c'16 bf a g g'16 f' | 
      e' d'8 c'16 bf a g g'16 f' e' d'8 c'16 bf a g |
      bf'16 a'8 g'16 f' e' d'8 c'16 bf a g g'16 f' e' d' ~ |
      d' c' bf a g g' f' e' d'8 c'16 bf a g g'16 f' | 
      e' d'8 c'16 bf a g g'16 f' e' d'8 c'16 bf a g
    }
    >>
    \new Staff <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "treble"
      \new Voice {
      bf'8 a'4 g'8 f' e' d'4 c'8 bf a g g'8 f' e' d' ~ |
      d' c' bf a g g' f' e' d'4 c'8 bf a g g'8 f' | 
      e' d'4 c'8 bf a g g'8 f' e' d'4 c'8 bf a g |
      
    }
    >>
      \new Staff <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "treble"
      \new Voice {
      bf'4 a'2 g'4 f' e' d'2 c'4 bf a g g'4 f' e' d' ~ |
      d' c' bf a g g' f' e' d'2 c'4 bf a g g'4 f' | 
      e' d'2 c'4 bf a g g'4 f' e' d'2 c'4 bf a g
    }
    >>
         \new Staff <<
      \accidentalStyle modern-cautionary 
      \time 4/4
      \clef "treble"
      \new Voice {
      bf'1 ~ bf' ~ bf' 
      a'1 ~ a'1 ~ a'1 ~
      a'1 ~ a'1 ~ a'1
    }
    >>
  >> %% staffgroup
}