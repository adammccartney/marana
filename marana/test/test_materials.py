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
    

def test_blue_chord_slicing():
    blueSlice_6 = marana.chordalVoices["blue"][6][0:3]
    segment = abjad.PitchSegment("e''' fs''' cs'''")
    assert blueSlice_6 == segment

def test_green_chord_slicing():
    greenSlice_5 = marana.chordalVoices["green"][5][3:6]
    segment = abjad.PitchSegment("a'' b'' cs'''")
    assert greenSlice_5 == segment

def test_red_chord_slicing():
    redSlice_4 = marana.chordalVoices["red"][4][6:10]
    segment = abjad.PitchSegment("a' g' f'")
    assert redSlice_4 == segment

def test_black_chord_slicing():
    blackSlice_1 = marana.chordalVoices["black"][1][2:5]
    segment = abjad.PitchSegment("a,, a,, gs,,")
    assert blackSlice_1 == segment

def test_blue_tremolo():
    blue_tremolo_p1 = marana.tremoloVoices["blue"][5]["p1"]
    blue_tremolo_p2 = marana.tremoloVoices["blue"][5]["p2"]
    blue_tremolo_p3 = marana.tremoloVoices["blue"][5]["p3"]
    segment_1 = abjad.PitchSegment("e'' c'' fs'' cs'' cs'' a''")
    segment_2 = abjad.PitchSegment("d'' f'' e'' b' as'' gs''")
    segment_3 = abjad.PitchSegment("a'' cs''' bf'' c''' c''' d'''")
    assert blue_tremolo_p1 == segment_1
    assert blue_tremolo_p2 == segment_2
    assert blue_tremolo_p3 == segment_3

def test_green_tremolo():
    green_tremolo_p1 = marana.tremoloVoices["green"][4]["p1"]
    green_tremolo_p2 = marana.tremoloVoices["green"][4]["p2"]
    green_tremolo_p3 = marana.tremoloVoices["green"][4]["p3"]
    segment_1 = abjad.PitchSegment("g' e' fs' as' cs'' a'")
    segment_2 = abjad.PitchSegment("a' f' b' d'' cs'' fs''")
    segment_3 = abjad.PitchSegment("cs'' a' bf' c'' d'' f''")
    assert green_tremolo_p1 == segment_1
    assert green_tremolo_p2 == segment_2
    assert green_tremolo_p3 == segment_3

def test_red_tremolo():
    red_tremolo_p1 = marana.tremoloVoices["red"][3]["p1"]
    red_tremolo_p2 = marana.tremoloVoices["red"][3]["p2"]
    red_tremolo_p3 = marana.tremoloVoices["red"][3]["p3"]
    segment_1 = abjad.PitchSegment("g c' f' cs' e cs")
    segment_2 = abjad.PitchSegment("f a gs d gs as")
    segment_3 = abjad.PitchSegment("a f g ef f d")
    assert red_tremolo_p1 == segment_1
    assert red_tremolo_p2 == segment_2
    assert red_tremolo_p3 == segment_3


def test_black_tremolo():
    black_tremolo_p1 = marana.tremoloVoices["black"][2]["p1"]
    black_tremolo_p2 = marana.tremoloVoices["black"][2]["p2"]
    black_tremolo_p3 = marana.tremoloVoices["black"][2]["p3"]
    segment_1 = abjad.PitchSegment("c e as, cs a, cs")
    segment_2 = abjad.PitchSegment("a, d gs, b, fs, gs,")
    segment_3 = abjad.PitchSegment("f, a, ef, g, d, f,")
    assert black_tremolo_p1 == segment_1
    assert black_tremolo_p2 == segment_2
    assert black_tremolo_p3 == segment_3

def test_blue_melodies():
    blue_melody_p1_1 = marana.melodyVoices["blue"]["p1"][1]
    blue_melody_p1_2 = marana.melodyVoices["blue"]["p1"][2]
    blue_melody_p1_3 = marana.melodyVoices["blue"]["p1"][3]
    segment_1_1 = abjad.PitchSegment("e c fs as a d")
    segment_1_2 = abjad.PitchSegment("e' c' fs' as' a' d'")
    segment_1_3 = abjad.PitchSegment("b' g' cs'' es'' e'' a'")
    assert blue_melody_p1_1 == segment_1_1
    assert blue_melody_p1_2 == segment_1_2
    assert blue_melody_p1_3 == segment_1_3
    blue_melody_p2_4 = marana.melodyVoices["blue"]["p2"][4]
    segment_2_4 = abjad.PitchSegment("d'' a' d'' e'' gs'' fs'' a''")
    assert blue_melody_p2_4 == segment_2_4
    blue_melody_p3_5 = marana.melodyVoices["blue"]["p3"][5]
    segment_3_5 = abjad.PitchSegment("cs''' a'' e''' g'' fs'' b''")
    assert blue_melody_p3_5 == segment_3_5


def test_green_melodies():
    green_melody_p1_6 = marana.melodyVoices["green"]["p1"][6]
    green_melody_p1_8 = marana.melodyVoices["green"]["p1"][8]
    green_melody_p1_10 = marana.melodyVoices["green"]["p1"][10]
    segment_1_6 = abjad.PitchSegment("d''' d'''' es''' gs''' as''' b''' e''''")
    segment_1_8 = abjad.PitchSegment("g''' g'''' as''' cs'''' ds'''' e'''' a''''")
    segment_1_10 = abjad.PitchSegment("b''' b'''' css'''' es'''' fss'''' gs'''' cs'''''")
    assert green_melody_p1_6 == segment_1_6
    assert green_melody_p1_8 == segment_1_8
    assert green_melody_p1_10 == segment_1_10
    green_melody_p2_1 = marana.melodyVoices["green"]["p2"][1]
    segment_2_1 = abjad.PitchSegment("a a' gs b cs' gs' cs'")
    assert green_melody_p2_1 == segment_2_1
    green_melody_p3_2 = marana.melodyVoices["green"]["p3"][2]
    segment_3_2 = abjad.PitchSegment("cs' cs'' ef' g' a' g' c'")
    assert green_melody_p3_2 == segment_3_2


 
