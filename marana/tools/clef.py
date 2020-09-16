import abjad

def clef(name):
    """
    Makes a clef before a specific leaf
    """
    clef = abjad.Clef(name)
    if isinstance(clef, abjad.Clef):
        return abjad.LilyPondLiteral(f"{format(clef, 'lilypond')}", "before")
                
if __name__ == '__main__':
    clef = clef('bass')
    abjad.f(clef)
