import abjad

def line_break():
    """
    Creates a line break in voice
    """
    return abjad.LilyPondLiteral("\\break", "after")


