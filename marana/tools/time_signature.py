import abjad 

def time_signature(ts_string):
    """
    Makes a time signature on a single leaf.
    WARNING: no checks ... 
    """
    return abjad.LilyPondLiteral(f"\\time {ts_string}", "before")

if __name__ == '__main__':
    voice = r"c'1 d'2 f'4 f'2 e'2"
    staff = abjad.Staff(voice)
    abjad.attach(time_signature("3/4"), staff[1])
    abjad.attach(time_signature("4/4"), staff[3])
    abjad.f(staff)


