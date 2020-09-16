import abjad

def default_on():
    """
    Notehead style default
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'default",
                         "before",
                                )

def altdefault_on():
    """
    Notehead style alternative default
    """
    return abjad.LilyPondLiteral(
                           "\\override Staff.NoteHead.style = #'altdefault",
                           "before",
                           )

def baroque_on():
    """
    Notehead style baroque   
    """
    return abjad.LilyPondLiteral(
                           "\\override Staff.NoteHead.style = #'baroque",
                           "before",
                           )
    
def neomensural_on():
    """
    Notehead style neomensural
    """
    return abjad.LilyPondLiteral(
                           "\\override Staff.NoteHead.style = #'neomensural",
                           "before",
                           )


def mensural_on():
    """
    Notehead style mensural
    """
    return abjad.LilyPondLiteral(
                           "\\override Staff.NoteHead.style = #'mensural",
                           "before",
                           )

def petrucci_on():
    """
    Notehead style petrucci   
    """
    return abjad.LilyPondLiteral(
                           "\\override Staff.NoteHead.style = #'petrucci",
                           "before",
                           )

    
def harmonic_on():
    """
    Notehead style clear rhombic
    """
    return abjad.LilyPondLiteral(
                           "\\override Staff.NoteHead.style = #'harmonic",
                           "before",
                           )

def harmonic_black_on():
    """
    Notehead style opaque rhombic
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'harmonic-black",
                         "before",
                         )

def harmonic_mixed_on():
    """
    Notehead style mixed rhombic
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'harmonic-mixed",
                         "before",
                         )

def diamond_on():
    """
    Notehead style diamond
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'diamond",
                         "before",
                         )

def cross_on():
    """
    Notehead style cross
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'cross",
                         "before",
                         )

def xcircle_on():
    """
    Notehead style xcircle
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'xcircle",
                         "before",
                         )

def triangle_on():
    """
    Notehead style triangle
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'triangle",
                         "before",
                         )

def slash_on():
    """
    Notehead style slash
    """
    return abjad.LilyPondLiteral(
                         "\\override Staff.NoteHead.style = #'slash",
                         "before",
                         )

def revert_notehead_style():
    """
    Reverts override, notehead style normal
    """
    return abjad.LilyPondLiteral("\\revert Staff.NoteHead.style",
                                  "before")


if __name__ == '__main__':
    import copy

    voice_one = r"a4 a2. a1 a\breve*1/2 a\longa*1/4"
    voice_two = copy.copy(voice_one) 
    voice_three = copy.copy(voice_one) 
    voice_four = copy.copy(voice_one) 
    voice_five = copy.copy(voice_one) 
    voice_six = copy.copy(voice_one) 
    voice_seven = copy.copy(voice_one) 
    voice_eight = copy.copy(voice_one) 
    voice_nine = copy.copy(voice_one) 
    voice_ten = copy.copy(voice_one) 
    voice_eleven = copy.copy(voice_one) 
    voice_twelve = copy.copy(voice_one) 
    voice_thirteen = copy.copy(voice_one) 
    voice_fourteen = copy.copy(voice_one) 
    voice_fifteen = copy.copy(voice_one) 
    
    staff = abjad.Staff([
                        voice_one, 
                        voice_two,
                        voice_three, 
                        voice_four,
                        voice_five,
                        voice_six,
                        voice_seven,
                        voice_eight,
                        voice_nine,
                        voice_ten,
                        voice_eleven,
                        voice_twelve,
                        voice_thirteen,
                        voice_fourteen,
                        voice_fifteen,
                        ])
    abjad.attach(default_on(), staff[0])
    abjad.attach(altdefault_on(), staff[1])
    abjad.attach(baroque_on(), staff[2])
    abjad.attach(neomensural_on(), staff[3])
    abjad.attach(mensural_on(), staff[4])
    abjad.attach(petrucci_on(), staff[5])
    abjad.attach(harmonic_on(), staff[6])
    abjad.attach(harmonic_black_on(), staff[7])
    abjad.attach(harmonic_mixed_on(), staff[8])
    abjad.attach(diamond_on(), staff[9])
    abjad.attach(cross_on(), staff[10])
    abjad.attach(xcircle_on(), staff[11])
    abjad.attach(triangle_on(), staff[12])
    abjad.attach(slash_on(), staff[13])
    abjad.attach(revert_notehead_style(), staff[14])
    abjad.f(staff)
    abjad.show(staff)
