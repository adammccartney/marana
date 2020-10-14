#!/usr/bin/python

import abjad

""" A simple script to generate pitch material """


def get_harmonics(pitch_segment):
    """ Given an abjad PitchSegment,
        print segments at harmonics (1, 2, 3, 4, 5, 6, 8, 10)"""
    h1 = pitch_segment.transpose(0)
    h2 = pitch_segment.transpose(12)
    h3 = pitch_segment.transpose(19)
    h4 = pitch_segment.transpose(24)
    h5 = pitch_segment.transpose(28)
    h6 = pitch_segment.transpose(31)
    h8 = pitch_segment.transpose(36)
    h10 = pitch_segment.transpose(40)
    harmonics = [h1, h2, h3, h4, h5, h6, h8, h10]
    return harmonics


def print_dict_entries(harmonics_list):
    """ Takes an array of harmonicy
        melody segment on the x-axis
        harmonics on the y-axis"""
    for i in range(len(harmonics_list)):
        print(f"({i+1}, abjad.PitchSegment({str(harmonics_list[i])})),")


if __name__ == '__main__':
    blue_melody_p1 = abjad.PitchSegment("e c fs as a d")
    blue_melody_p2 = abjad.PitchSegment("d a, d e gs fs a")
    blue_melody_p3 = abjad.PitchSegment("a f c' ef f g")
    green_melody_p1 = abjad.PitchSegment("g g' as cs' ds' e' a'")
    green_melody_p2 = abjad.PitchSegment("a a' gs b cs' gs' cs'")
    green_melody_p3 = abjad.PitchSegment("cs cs' ef g a g c")
    print("TEST:", str(green_melody_p3))
    melodies = [blue_melody_p1, blue_melody_p2, blue_melody_p3, green_melody_p1,
                green_melody_p2, green_melody_p3]
    for i in range(len(melodies)):
        print(f"{i+1}th Melody:")
        harmonics = get_harmonics(melodies[i])
        print_dict_entries(harmonics)


              
