import abjad

def grace_before(note):
    """Makes a grace note flageolet command returns a string"""
    if isinstance(note, str):
        return abjad.LilyPondLiteral(f"\\grace {note}", "before")
    else:
        return ValueError(f"Grace note {note} needs to be a string format")

def grace_flageolet_before(note):
    """Makes a grace note flageolet command returns a string"""
    if isinstance(note, str):
        return abjad.LilyPondLiteral(f"\\grace {note}\\flageolet", "before")
    else:
        return ValueError(f"Grace note {note} needs to be a string format")

def grace_after(note):
    """Makes a grace note flageolet command returns a string"""
    if isinstance(note, str):
        return abjad.LilyPondLiteral(f"\\grace {note}", "after")
    else:
        return ValueError(f"Grace note {note} needs to be a string format")

def grace_flageolet_after(note):
    """Makes a grace note flageolet command returns a string"""
    if isinstance(note, str):
        return abjad.LilyPondLiteral(f"\\grace {note}\\flageolet", "after")
    else:
        return ValueError(f"Grace note {note} needs to be a string format")

if __name__ == '__main__':
    print(str(grace_before("c'8")))
    print(str(grace_flageolet_before("fs'''16")))
    print(str(grace_after("d'''16[ f''']")))
    print(str(grace_flageolet_after("a'''16[ cs'''']")))
