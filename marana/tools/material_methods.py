import copy
import abjad
import rill


import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

def get_pitch_classes(pitch_segment):
    if isinstance(pitch_segment, abjad.PitchSegment):
        pitch_classes = pitch_segment.to_pitch_classes()
        return pitch_classes

def make_decimo_diad(root):
    """Makes a diad of a root + chromatic tenth returns a string"""
    if isinstance(root, abjad.NamedPitch):
        pitch = copy.deepcopy(root)
        upper_pitch = pitch.transpose(16)
        decimo = abjad.NamedPitch(upper_pitch) 
        diad = tuple((root, decimo))
        return diad
    # WARNING, error not getting returned
    else:
        ValueError("Expecting {root} to be an abjad.NamedPitch")

def make_diads(fuzzy_harmonies, interval_doubling=None):
    """
    Harmonizes with lookup table 
    Returns a list of tuples
    """
    from rill.materials.pitch.definition import diatonic_register_lookup

    harmonized_melodies = []
    if interval_doubling == None:
        for harmony in fuzzy_harmonies:
            harmonized_melody = []
            melody = harmony.pitches
            for pitch in melody:
                harmonized_melody.append(pitch)
        harmonized_melodies.append(harmonized_melody)
        print("harmonized_melodies: ", harmonized_melodies)
        return harmonized_melodies 
    else: 
        diatonic_lookup = diatonic_register_lookup[interval_doubling]
        for harmony in fuzzy_harmonies:
            melody = harmony.pitches
            harmonized_melody = []
            for pitch in melody:
                pitch_class = pitch.pitch_class
                harmonized_pitch = pitch + diatonic_lookup[pitch_class] 
                diad = (harmonized_pitch, pitch)
                harmonized_melody.append(diad)
            harmonized_melodies.append(tuple(harmonized_melody))
        return harmonized_melodies

def make_augmented_stream(progression):
    """Makes phrases and adds them to stream
    returns an instance of PhraseStream
    """
    augment_with_rest = None
    augmented_progression = []
    for harmony in progression: 
        augment_with_rest = harmony + (None,)
        augmented_progression.append(augment_with_rest)
    phrase_stream = PhraseStream(augmented_progression)
    return phrase_stream

def scale_range_double_octave(semitones):
    """takes a semitones val and fits to double octave range
    WARNING: currently all octaves are getting wrapped to unisons
    this is no problem for rill, as they are being used to lookup
    shortname values for harmonies
    """
    if (semitones >= -12) and (semitones <= 12):
        return semitones
    elif (semitones > 36) and (semitones <= 48):
        octave_transposed_semitones = semitones - 36 
        return octave_transposed_semitones
    elif (semitones > 24) and (semitones <= 36):
        octave_transposed_semitones = semitones - 24 
        return octave_transposed_semitones
    elif (semitones > 12) and (semitones <= 24):
        octave_transposed_semitones = semitones - 12 
        return octave_transposed_semitones
    elif (semitones >= -24) and (semitones < -12):
        octave_transposed_semitones = semitones + 12
        return octave_transposed_semitones
    elif (semitones >= -36) and (semitones < -24):
        octave_transposed_semitones = semitones + 24
        return octave_transposed_semitones
    elif (semitones >= -48) and (semitones < -36):
        octave_transposed_semitones = semitones + 36
        return octave_transposed_semitones
    else: 
        raise ValueError('outside transposible range')

def wrap_transposition(val):
    """
    Currently designed to return an int
    can be adapted to also return mircrotones
    returns a wrapped value
    """
    if (val < -12) or (val > 12):
        wrapval = scale_range_double_octave(val)
        return wrapval 
    else:
        return val


def deep_copy_harmonies_list(harmonies):
    copied_harmonies = []
    for i in range(len(harmonies)):
        new_harmony = copy.deepcopy(harmonies[i])
        copied_harmonies.append(new_harmony)
    return copied_harmonies

def transpose(fuzzy_harmonies, t_interval=0):
    """Takes a lits of fuzzy harmony objects
    returns a new list of related objects
    based on an interval argument
    """
    from rill.materials.pitch.definition import transposition_lookup
    
    wrapped_t_interval = wrap_transposition(t_interval)
    harmony_shortname_lookup = transposition_lookup[wrapped_t_interval]
    
    new_harmonies = deep_copy_harmonies_list(fuzzy_harmonies)
    
    transposed_harmonies = []
    for harmony in new_harmonies:
        transposed_name = harmony_shortname_lookup[harmony.shortname]
        transposed_segment = harmony.segment.transpose(n=t_interval)
        transposed_harmony = FuzzyHarmony(
                                 transposed_name, 
                                 transposed_segment, 
                                 )
        transposed_harmonies.append(transposed_harmony)
    return transposed_harmonies

def transpose_segment(pitch_segment, t_interval):
    """Takes a melodic fragment i.e. pitch segment
       makes a copy and transposes that copy
       returns the newly transposed fragment
       """
    copied_segment = copy.deepcopy(pitch_segment)
    transposed_segment = copied_segment.transpose(t_interval)
    return transposed_segment

if __name__ == '__main__':

    neg_P8 = -12
    neg_Ma7 = -11
    neg_mi7 = -10
    neg_Ma6 = -9
    neg_mi6 = -8
    neg_P5 = -7
    neg_TT = -6
    neg_P4 = -5
    neg_Ma3 = -4
    neg_mi3 = -3
    neg_Ma2 = -2
    neg_mi2 = -1
    unison = 0
    mi2 = 1 
    Ma2 = 2 
    mi3 = 3 
    Ma3 = 4 
    P4 = 5
    TT = 6
    P5 = 7
    mi6 = 8
    Ma6 = 9
    mi7 = 10
    Ma7 = 11
    P8 = 12

    intervals = [
                neg_P8,
                neg_Ma7,
                neg_mi7,
                neg_Ma6,
                neg_mi6,
                neg_P5,
                neg_TT,
                neg_P4,
                neg_Ma3,
                neg_mi3,
                neg_Ma2,
                neg_mi2,
                unison,
                mi2, 
                Ma2, 
                mi3, 
                Ma3, 
                P4,
                TT,
                P5,
                mi6,
                Ma6,
                mi7,
                Ma7,
                P8,
      ]

    ex_neg_P8 = [-12, -24, -36]
    ex_neg_Ma7 = [-11, -23, -35]
    ex_neg_mi7 = [-10, -22, -34]
    ex_neg_Ma6 = [-9, -21, -33]
    ex_neg_mi6 = [-8, -20, -32]
    ex_neg_P5 = [-7, -19, -31]
    ex_neg_TT = [-6, -18, -30]
    ex_neg_P4 = [-5, -17, -29]
    ex_neg_Ma3 = [-4, -16, -28]
    ex_neg_mi3 = [-3, -15, -27]
    ex_neg_Ma2 = [-2, -14, -26]
    ex_neg_mi2 = [-1, -13, -25]
    ex_unison = [0]
    ex_mi2 = [1, 13, 25]
    ex_Ma2 = [2, 14, 26]
    ex_mi3 = [3, 15, 27]
    ex_Ma3 = [4, 16, 28]
    ex_P4 = [5, 17, 29]
    ex_TT = [6, 18, 30]
    ex_P5 = [7, 19, 31]
    ex_mi6 = [8, 20, 32]
    ex_Ma6 = [9, 21, 33]
    ex_mi7 = [10, 22, 34]
    ex_Ma7 = [11, 23, 35]
    ex_P8 = [12, 24, 36]
       
    interval_ex = [ 
            ex_neg_P8, 
            ex_neg_Ma7,
            ex_neg_mi7,
            ex_neg_Ma6,
            ex_neg_mi6,
            ex_neg_P5,
            ex_neg_TT,
            ex_neg_P4,
            ex_neg_Ma3,
            ex_neg_mi3,
            ex_neg_Ma2,
            ex_neg_mi2,
            ex_unison,
            ex_mi2,
            ex_Ma2,
            ex_mi3,
            ex_Ma3,
            ex_P4,
            ex_TT,
            ex_P5,
            ex_mi6,
            ex_Ma6,
            ex_mi7,
            ex_Ma7,
            ex_P8, 
        ]


            
    ### Test mode_twelve() for values within negative octave 
    

#    start_value = -12
#    counter = 0
#    for i in range(0, 25): 
#        if intervals[i] == scale_range_double_octave(start_value):
#            print(True)
#            start_value += 1
#            counter += 1
#            print(f"{counter} tests completed")
#    else:
#        False
#        print(f"{intervals[i]} != ", scale_range_double_octave(start_value))
#
 
 #   ### Test mode_twelve() for values within negative double octave 

 #   for i in range(len(interval_ex)):
 #       extensions = interval_ex[i]
 #       interval_check = intervals[i]
 #       for st_val in range(len(extensions)):
 #           if scale_range_double_octave(extensions[st_val]) == interval_check:
 #               print(True)
 #           else:
 #               print(False)
 #               print(
 #                       f"""
 #                       extensions = {extensions[st_val]} \n
 #                       {scale_range_double_octave(extensions[st_val])} != """, 
 #                       interval_check
 #                       )

 #   ### Test wrap_transposition for negative values 

 #   test_val = -47
 #   for i in range(48):
 #       wrapped_interval = wrap_transposition(test_val)
 #       print(f"Negative Wrapped val {i}: ", wrapped_interval)
 #       test_val += 1

 #   ### Test wrap_transposition for positive values 

 #   test_val = 0
 #   for i in range(48):
 #       wrapped_interval = wrap_transposition(test_val)
 #       print(f"Positive Wrapped val {i}: ", wrapped_interval)
 #       test_val += 1


    # Test copy function in transpose() on FuzzyHarmony object

    harmony = rill.FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"))
    second_harmony = rill.FuzzyHarmony('g_v', abjad.PitchSegment("g' b' d' f'"))
    copied_harmony = copy.deepcopy(harmony)
    copied_second = copy.deepcopy(second_harmony)
    harmonies = [harmony, second_harmony]
    copied_harmonies = [copied_harmony, copied_second]
    if harmony == copied_harmony:
        print(True)
    else:
        print(False)
    
    if harmony is copied_harmony:
        print(True)
    else:
        print(False)
    
    if harmonies == copied_harmonies:
        print(True)
    else:
        print(False)
    
    if harmonies is copied_harmonies:
        print(True)
    else:
        print(False)

    second_copy = deep_copy_harmonies_list(harmonies)
    for i in range(len(second_copy)):
        print(f"Copied harmony {second_copy[i]}")
    
    transposed_up_fifth = transpose(harmonies, 7)
    for harmony in range(len(transposed_up_fifth)):
        print("transposed harmony: ", transposed_up_fifth[harmony])

    middle_c = abjad.NamedPitch("c'")
    diad = make_decimo_diad(middle_c)
    print("Diad: ", diad)
    any_pitch = 'gasdasd'
    diad = make_decimo_diad(any_pitch)
    print("Diad: ", diad)

    from rill.tools.FuzzyHarmony import Diad as Diad

    d_first_oct = abjad.NamedPitch("d'")
    decimo = make_decimo_diad(d_first_oct)
    diad = Diad(decimo)
    print(diad.upper)
    print(diad.lower)
