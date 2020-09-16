import abjad


class Diad(object):
    """
    Simple diad with a string representation
    Initialized with a tuple of abjad.NamedPitch objects
    """
    __slots__ = ( 
                 "_pitches", 
                 "_pitch_one",
                 "_pitch_string",
                 "_pitch_two",
                 )

    def __init__(self, pitches=None):
        self._pitches = pitches
        self._set_diad()

    def _set_diad(self):
        if self._pitches != None:
            self._pitch_one = str(self._pitches[0])
            self._pitch_two = str(self._pitches[1])
            pitch_string = f"{self._pitch_one} {self._pitch_two}"
            self._pitch_string = pitch_string
        else:
            self._pitch_one = ""
            self._pitch_two = ""
            self._pitch_string = ""

    @property
    def pitches(self) -> tuple:
        """Getter"""
        return self._pitches

    @property
    def pitch_string(self) -> str:
        return self._pitch_string

    @property 
    def lower(self) -> str:
        return self._pitch_one

    @property 
    def upper(self) -> str:
        return self._pitch_two

class FuzzyHarmony(object):
    """
    Stores a collection of notes in a PitchSegment
    Fuzzy because the names are used to roughly track
    the position in a given harmonic sequence and not
    to store precise information on the harmony.
    e.g.:
    bf_ii = key of bflat, minor harmony on ii degree 

    """

    __slots__ = (
            "_pitches", 
            "_pitch_list",  
            "_shortname",
            "segment", 
            )

    def __init__(self, shortname=str(), segment=None):
        self._shortname = shortname
        self.segment = abjad.PitchSegment(segment)
        self._set_pitches()
        self._make_list_pitches()

    def __repr__(self):
        """
        Simple string represenation of harmony
        Similiar layout to a dict
        """
        segment_str = str(self.segment)
        shortname_str = str(self.shortname)
        return '{}: {}'.format(shortname_str, segment_str)

    def _set_pitches(self):
        pitches = self.segment.to_pitches()
        self._pitches = tuple(pitches)

    def _make_list_pitches(self):
        """aliasing warning"""
        self._pitch_list = []
        for pitch in self.pitches:
            self._pitch_list.append(pitch.name)

    @property
    def pitches(self) -> tuple:
        """Gets pitches"""
        return self._pitches

    @property 
    def pitch_list(self):
        return self._pitch_list

    @property 
    def numbered_pitch_list(self):
        """Gets pitches from segment as numbered pitches"""
        pitch_list = self.pitch_list
        num_pitch_list = []
        for pitch in pitch_list:
            num_pitch = abjad.NumberedPitch(pitch)
            num_pitch_list.append(int(str(num_pitch)))
        return num_pitch_list

    @property
    def shortname(self):
        """gets shortname"""
        return self._shortname

class LegatoArpeggio(object):
    """
    Used to create string that is used for     
    """

    __slots__ = (
            "_arp_pitches",
            "_arp_strings",
            "_pitch_segment", 
            "_pitch_set",
            "_reordered_segment",
            "_reservoir",
            "_sequence", 
            )

    def __init__(self, pitch_segment=None, sequence=None):
        self._pitch_segment = pitch_segment or abjad.PitchSegment()
        self._sequence = sequence or tuple()
        self._reorder_segment()
        self._make_ascent()
        self._set_arp_pitches()
        self._set_arp_strings()

    def _make_ascent(self):
        """makes ascent from pitch set"""
        pitches = self._reordered_segment
        pitch_ascents = []
        for i in range(len(pitches)):
            ascent = tuple(pitches[: i + 1])
            print("ascent: ", ascent)
            pitch_ascents.append(ascent)
        self._reservoir = tuple(pitch_ascents)

    def _set_arp_pitches(self):
        """Sets a list of pitch strings"""
        self._arp_pitches = []
        for i in range(len(self._sequence)):
            arpeggio_stage = str(self._reordered_segment[i])
            arp_pitch_str = "{}".format(arpeggio_stage)
            self._arp_pitches.append(arp_pitch_str)

    def _set_arp_strings(self):
        """Sets strings from pitch segments"""
        self._arp_strings = []
        if len(self._reordered_segment) == len(self._sequence):
            for i in range(len(self._sequence)):
                arpeggio_stage = self._reservoir[i]
                arp_pitch_str = ' '.join(str(x) for x in arpeggio_stage)
                print("arp_pitch_str: ", arp_pitch_str)
                self._arp_strings.append(arp_pitch_str)
    
    def _reorder_segment(self):
        """Sets a reordered segment according to sequence"""
        pitches = []
        for i in range(len(self._sequence)):
            seq_val = self._sequence[i]
            pitches.append(self._pitch_segment[seq_val])
        self._reordered_segment = abjad.PitchSegment(pitches)
        print("Reordered pitches: ", self._reordered_segment)
    
    @property 
    def stages(self) -> list:
        return self._arp_strings

    @property 
    def pitches(self) -> list:
        return self._arp_pitches


class Progression(object):
    """
    Harmonic Progression
    Contains a number of FuzzyHarmonies in a tuple 
    """

    def __init__(self, harmonies):
        self._harmonies = tuple(harmonies)

    ### NON-MODIFYING MEMBER FUNCTIONS ###
    def get_progression(self):
        """returns a tuple of harmonies"""
        return self._harmonies

    def get_harmony(self, index):
        """returns a specific harmony"""
        progression = self.get_progression()
        for harmony in progression:
            return progression[index]

def replace_and_make_new_progression(progression, index, fuzzy_harmony):
    """
    Takes three arguments
    progression to copy
    index to change
    fuzzy_harmony to insert
    
    makes new progression, similar to the old 
    but containing fuzzy_harmony inserted at index
    """
    new_progression = progression.get_progression()
    progression_list = []
    for i in range(len(new_progression)):
        progression_list.append(new_progression[i])
    progression_list[index] = fuzzy_harmony
    new_progression = tuple(progression_list)
    return new_progression

def get_global_minima(pitch_segment):
    """
    returns global minima of a pitch segment
    as a single member list containing an abjad.Pitch()
    """
    result = []
    bottom_index = 0
    minima = pitch_segment[bottom_index]
    if 3 <= len(pitch_segment):        # works for triads and above
        for i in range(len(pitch_segment)):
            new_min = pitch_segment[i]
            if minima > new_min:
                minima = new_min
        result.append(minima)
        global_minima = abjad.NamedPitch(result[bottom_index]) # could build check
        return global_minima   

def invert_up(segment, inversion):
    """
    inverts a chord upwards
    assumes segment is within octave range
    returns new pitch segment

    Warning: no sanity check on transposition at the moment
    i.e. you can invert 433 times and still generate strings
    that represent pitches
    """
    interval = 12
    new_segment = segment
    
    if inversion < 0:
        print("Inversion needs to be a positive int")
    for i in range(inversion):
        segment = new_segment
        lowest_note = get_global_minima(segment) #call global_minima to find lowest note
        set_ = abjad.PitchSet(
                items=[lowest_note.name],
                item_class=abjad.NamedPitch,
                )
        transposed_set = set_.transpose(interval)  #transposed note is lowest note.tranpose("+P8")
        transposed_pitch = None
        for i in transposed_set:
            transposed_pitch = abjad.NamedPitch(i)
        new_pitches = []
        segment_len = len(segment)
        section = range(1, segment_len)    # trim lowest note
        for i in section:                 
            new_pitches.append(segment[i])
        new_pitches.append(transposed_pitch) # append transposed 
        new_segment = abjad.PitchSegment(new_pitches) # make new segment
    return new_segment

def get_global_maxima(pitch_segment):
    """
    returns the highest abjad.NamedPitch in a PitchSegment
    """
    result = []
    top_index = -1
    maxima = pitch_segment[top_index]         # last item in list is top of segment
    if 3 <= len(pitch_segment):        # works for triads and above
        for i in range(len(pitch_segment)):
            new_max = pitch_segment[i]
            if maxima < new_max:
                maxima = new_max
        result.append(maxima)
        global_maxima = abjad.NamedPitch(result[top_index]) # could build check
        return global_maxima  

def invert_down(segment, inversion):
    """
    inverts a chord downwards
    assumes segment is within octave range
    returns new pitch segment

    Warning: no sanity check on transposition at the moment
    i.e. you can invert -433 times and still generate strings
    that represent pitches
    """

    if inversion > 0:
        print("Inversion needs to be a negative int")
    interval = -12
    new_segment = segment
    for i in range(abs(inversion)):
        segment = new_segment
        highest_note = get_global_maxima(segment) #call global_minima to find lowest note
        set_ = abjad.PitchSet(
                items=[highest_note.name],
                item_class=abjad.NamedPitch,
                )
        transposed_set = set_.transpose(interval)  #transposed note is lowest note.tranpose("+P8")
        transposed_pitch = None
        for i in transposed_set:
            transposed_pitch = abjad.NamedPitch(i)   # initialize as named pitch
        new_pitches = []
        segment_len = len(segment)
        section = range(0, segment_len - 1)    # trim lowest note
        new_pitches.append(transposed_pitch) # append transposed 
        for i in section:                 
            new_pitches.append(segment[i])
        new_segment = abjad.PitchSegment(new_pitches) # make new segment
    return new_segment


