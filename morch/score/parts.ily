
\book {
    \bookOutputSuffix "flute1"
    \header {
        subtitle = "flute 1 part"
    }
    \score {
        \header {piece = "Largo"}
        \keepWithTag #'(fluteOne)
        \include "./segments.ily"
    }
}

\book {
    \bookOutputSuffix "flute2"
    \header {
        subtitle = "flute 2 part"
    }
    \score {
        \keepWithTag #'(fluteTwo)
        \include "./segments.ily"
    }
}


\book {
    \bookOutputSuffix "oboe1"
    \header {
        subtitle = "oboe 1 part"
    }
    \score {
        \keepWithTag #'(oboeOne)
        \include "./segments.ily"
    }
}


\book {
    \bookOutputSuffix "oboe2"
    \header {
        subtitle = "oboe 2 part"
    }
    \score {
        \keepWithTag #'(oboeTwo)
        \include "./segments.ily"
    }
}
