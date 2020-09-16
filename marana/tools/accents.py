import abjad

def staccato():
    return abjad.LilyPondLiteral("-.", "after")

def tenuto():
    return abjad.LilyPondLiteral("--", "after")
