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
                          PartialType,
                          PcSegTuple,
                          PitchData,
                          PitchSegTuple,
                          PitchToken,
                          PitchQuery,
                          make_pitch_tuples,
                          make_pitchclass_segments) 


def make_octave_voicings(octaves: list[int], orders: list[str]):
    """
    Simple wrapper function to simply zip two lists of equal length, making an
    octave voicing 
    """
    assert len(octaves) == len(orders), "Lists must be of equal length"
    tups = list(zip(octaves, orders))
    ovoicings = [OctaveVoicing(o[0], o[1]) for o in tups] 
    return ovoicings

 
def parse_args(ptype: PitchToken, resolver: int, pitchclass_data_segments: list[PcSegTuple]):
    """
    extractor function 
    arguments in the tuple are generic selectors for either PARTIAL or
    CHORDTONE type objects. What is returned is a list comprehension whose
    contents is a list of Pitch objects

    TODO: this could be improved slightly
    """
    tones = None
    harmonies = [pcseg.harmony for pcseg in pitchclass_data_segments]
    roots = [pcseg.root for pcseg in pitchclass_data_segments]
    if ptype == PitchToken.PARTIAL:
        pnum = PartialType(resolver)
        tones = [Partial(r, pnum) for r in roots]
    if ptype == PitchToken.CHORDTONE:
        tones = [ChordTone(h, resolver) for h in harmonies]
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

    returns a list of voiced PitchSegments tuples
    """
    pitch_segments = []
    for (pc, ov) in zip(pitchclasses, ovoicings):
        pitch_segment = resolve_pitch(pc.pcseg, ov)
        pitch_segments.append(pitch_segment) 
    return pitch_segments


def resolve_pitchselector(pquery: PitchQuery, pdata: PitchData):
    """
    the arguments here are a pitch query and a pitch data object

    function returns an array of pitch segments 
    i.e. it resolves the pitch classes it parses in the first part 
    of the query according to the octave and resolution order

    this function is designed that we set up these two objects in a string at
    the level of main.py (pass them in via file for instance). This string is
    interpreted by calling python's exec function
    """
    roots = pdata.roots
    harmonies = pdata.harmonies
    pitchtuples = make_pitch_tuples(roots, harmonies)
    pcsegs = make_pitchclass_segments(pitchtuples)
    pitchclasses = parse_args(pquery.ptype, pquery.resolution, pcsegs) 
    seqlen = len(pitchclasses)
    octave = pquery.voicing.octave
    order = pquery.voicing.order
    octaves = [octave] * seqlen 
    orders = [order] * seqlen
    ovoicings = make_octave_voicings(octaves, orders)
    voiced_pitches = voice_pitchclasses(pitchclasses, ovoicings)
    return voiced_pitches
