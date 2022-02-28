# marana/parser.py
#!/usr/bin/python3
"""
This module that provides a simple parser to parse 'modular expressions'
a modular expression is an invented term that refers to a specific style of
musical idea

    basically, what we want to try here is to load an instruction that causes a
    parse operation and returns a voice with structured pitch data

    The data is queried using lists of selectors

     [({token_type: partial,
        attributes: {args: (root), octave: 4}},
       {token_type: harm,
        attributes: {args: (2), octave: 4}}),

    ({token_type: partial,
      attributes: (root), octave: 4}},
     {token_type: harm,
      attributes: {args: (2), octave: 4}})]


A pitch query is made up of a list of one or more objects with the following
structure: 

     [({pitch_type: partial,
        attributes: {resolver: (root), 
                     voice_selector: { octave: int, 
                                       resolver: str }}})]

"""


from abjad import PitchClassSegment, PitchClassSegment, PitchSegment
from marana.pitch import (Partial, 
                          ChordTone, 
                          OctaveVoicing, 
                          PitchSegTuple,
                          PitchTuple) 


def make_octave_voicings(octaves: list[int], orders: list[str]):
    """
    Simple wrapper function to simply zip two lists of equal length, making an
    octave voicing 
    """
    assert len(octaves) == len(orders), "Lists must be of equal length"
    tups = list(zip(octaves, orders))
    ovoicings = [OctaveVoicing(o[0], o[1]) for o in tups] 
    return ovoicings

 
def parse_args(args: tuple, pitchclass_data_segments: list[PitchTuple]):
    """
    extractor function 
    arguments in the tuple are generic selectors for either PARTIAL or
    CHORDTONE type objects. What is returned is a list comprehension whose
    contents is a list of Pitch objects
    """
    tones = None
    harmonies = [pcseg.harmony for pcseg in pitchclass_data_segments]
    roots = [pcseg.root for pcseg in pitchclass_data_segments]
    if (len(args) == 1): # chordtone selector
        i = args[0]
        tones = [ChordTone(h, i) for h in harmonies]
    if (len(args) == 2): # root, partial pair
        p = args[1]
        tones = [Partial(r, p) for r in roots]
    assert tones is not None
    return tones


def resolve_pitch(pcseg: PitchClassSegment, ovoicing: OctaveVoicing):
    """
    pitchclass: Partial|ChordTone
    ovoicing is a list of octave voicings

    returns a PitchSegment

    """
    order = ovoicing.order
    octave = ovoicing.octave
    ret = None
    assert order in {"vert", "horiz"}, "direction should be vert or horiz"
    if (order == "vert"):
        ret = pcseg.voice_vertically(octave)
    elif (order == "horiz"):
        ret = pcseg.voice_horizontally(octave)
    assert ret is not None, "res should be bound"
    assert isinstance(ret, PitchSegment), "res should be instance PitchSegment"
    return ret 


def voice_pitchclasses(pitchclasses, ovoicings: list[OctaveVoicing]) -> list[PitchSegTuple]:
    """
    takes a list of pitchclasses and a list of OctaveVoicings, voices the pitchclasses
    according to the members of the OctaveVoicing  

    arguments: pitchclasses: list[Partial] | list[ChordTone]

    returns a list of voiced PitchSegments
    """
    pitch_segments = []
    for (pc, ov) in zip(pitchclasses, ovoicings):
        root_pseg = resolve_pitch(pc.root, ov)
        harmony_pseg = resolve_pitch(pc.harmony, ov)
        psegtuple = PitchSegTuple(root_pseg, harmony_pseg)
        pitch_segments.append(psegtuple)
    return pitch_segments

def parse_pitch_attrs(attrs: dict, pitchclass_data: list[PitchTuple]):
    """
    parse the attributes of pitch selector
    attributes are:
        pitch_selector_args: the args specify what type of Pitch object will be formed
        octave: the octave specifies what octave the pitch will be voices at
        order: the order in which the pitches will be resolved within the octave

    returns an array of PitchSegments
    """
    pitchclass_selector_args = attrs['args']
    pitchclasses = parse_args(pitchclass_selector_args, pitchclass_data) 
    octave = attrs['octave']
    octaves = [octave] * len(pitchclasses)  # we want to zip these later
    order = attrs['order']
    orders = [order] * len(pitchclasses)    # same here
    ovoicings = make_octave_voicings(octaves, orders)
    voiced_pitches = voice_pitchclasses(pitchclasses, ovoicings)
    return voiced_pitches


def parse_pselector(pselector: tuple):
    """
    takes a tuple of pitch selectors and resolves to pitches, returns a
    tuple of lilypond pitch strings
    """
    num_items = len(pselector)
    for ps in pselector:
        if ps["token_type"] == "partial":
            print("resolve the args as partial")
        if ps["token_type"] == "chordtone":
            print("resolve the args as chord tone")
    return num_items


def parse_input(input: tuple):  # returns a flat array of lilypond pitch strings
    num_items = len(input)
    for n in input:
        for k in n:
            pselector_tup = None
            voicing_flag = None
            if k == "selector":
                pselector_tup = n[k]
            if k == "voicing":
                voicing_flag = n[k]
    return num_items
