import abjad

def ottava(num):
    """Makes ottava bracket returns lilypond literal"""
    if (num >= -2) and (num <= 2):
        return abjad.LilyPondLiteral(f"\\ottava #{num}", "before")
    else:
        return ValueError(f"{num} not in range: must be (range >= -2) or (range <= 2)")

if __name__ == '__main__':
    for i in range(5):
        print(ottava(i-2))
    for i in range(7):
        print(ottava(i-2))
