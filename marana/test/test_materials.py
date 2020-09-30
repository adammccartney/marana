#import ide                       
import pathlib
import pytest
import sys


#abjad_ide = ide.AbjadIDE()
#scores = pathlib.Path(*pathlib.Path(__file__).parts[:-4])
#path = ide.Path(__file__, scores=scores)
#directories = path.materials.list_paths()


#@pytest.mark.parametrize("directory", directories)
#def test_materials_01(directory):
#    exit_code = abjad_ide.check_definition_py(directory)
#    if exit_code != 0:
#        sys.exit(exit_code)
#
#
#@pytest.mark.parametrize("directory", directories)
#def test_materials_02(directory):
#    exit_code = abjad_ide.make_illustration_pdf(directory, open_after=False)
#    if exit_code != 0:
#        sys.exit(exit_code)

import abjad
import marana

def test_blue_chord_voice_access():
    """checks that the dictionary of chord voices is set up correctly
       voice was defined once and transposed, misspelling will show 
       up in any octave
    """
    blueChordalVoice_5 = marana.chordalVoices["blue"][5]
    segment = abjad.PitchSegment("e'' fs'' cs'' d'' e'' as'' a'' c''' c'''")
    assert blueChordalVoice_5 == segment

def test_green_chord_voice_access():
    """ same as above on a different voice"""
    greenChordalVoice_4 = marana.chordalVoices["green"][4]
    segment = abjad.PitchSegment("g' fs' a' a' b' cs'' cs'' bf' d''")
    assert greenChordalVoice_4 == segment

def test_red_chord_voice_access():
    redChordalVoice_3 = marana.chordalVoices["red"][3]
    segment = abjad.PitchSegment("g cs' e f gs gs a g f")
    assert redChordalVoice_3 == segment

def test_black_chord_voice_access():
    blackChordalVoice_2 = marana.chordalVoices["black"][2]
    segment = abjad.PitchSegment("c as, a, a, gs, fs, f, ef, d,")
    assert blackChordalVoice_2 == segment
    
