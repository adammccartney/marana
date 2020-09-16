import abjad

def tie():
    """
    Makes a tie on a single leaf.
    """
    return abjad.LilyPondLiteral("~", "after")

if __name__ == '__main__':
    voice = r"c'4 d'2 f'4 f'2 e'2"
    staff = abjad.Staff(voice)
    abjad.attach(tie(), staff[2])
    abjad.f(staff)

