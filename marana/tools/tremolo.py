import abjad

def tremolo(speed):
    """
    Makes a tremolo mark on single leaf.
    """
    if isinstance(speed, int):
        while (speed == 8) or (speed == 16) or (speed == 32) or (speed == 64):
            return abjad.LilyPondLiteral(f":{speed}", "after")
    else:
        raise ValueError("int(4 ||  8 || 16 || 32 || 64) expected")


if __name__ == '__main__':

    one = tremolo(32)
    abjad.f(one)
    one = tremolo(8)
    abjad.f(one)
    one = tremolo(16)
    abjad.f(one)
    one = tremolo(64)
    abjad.f(one)
    #one = tremolo(99)
    #abjad.f(one)
    #one = tremolo('32')
    #abjad.f(one)
