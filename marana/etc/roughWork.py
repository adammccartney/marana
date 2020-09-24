#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing ground for some 
       helper functions"""

def print_test():
    print("this is a test!")


test_list = [
    'flute',
    'oboe',
    'clarinet',
    'bassoon',
    'horn',
    'trumpet',
    'trombone',
    'violin',
    'viola',
    'cello',
    'doublebass'
    ]

def sort_instruments_by_clef(voice_list, target):
        if isinstance(voice_list, list):
            for i in range(len(voice_list)):
                target.append(voice_list[i])
            return target
        else:
            single_voice = voice_list
            target.append(single_voice)
            return target

def set_clefs_and_print_results(instr_list):
    treble, alto, bass = [], [], []
    tmp_lst = instr_list[0:2]
    print(tmp_lst)
    sort_instruments_by_clef(tmp_lst, treble)
    tmp_lst = instr_list[3]
    sort_instruments_by_clef(tmp_lst, bass)
    tmp_lst = instr_list[4:6]
    sort_instruments_by_clef(tmp_lst, treble)
    tmp_lst = instr_list[6]
    sort_instruments_by_clef(tmp_lst, bass)
    tmp_lst = instr_list[7]
    sort_instruments_by_clef(tmp_lst, treble)
    tmp_lst = instr_list[8]
    sort_instruments_by_clef(tmp_lst, alto)
    tmp_lst = instr_list[9:11]
    sort_instruments_by_clef(tmp_lst, bass)
    print("treble: ", treble, '\n', "alto: ", alto, '\n', "bass: ", bass)


music_voices = [ "flute1_Music_Voice", 
                "oboe1_Music_Voice",
                "Bbclarinet1_Music_Voice",
                "bassoon1_Music_Voice",
                "fhorn1_Music_Voice",
                "fhorn3_Music_Voice",
                "trumpet1_Music_Voice",
                "trombone1_Music_Voice",
                "timpani1_Music_Voice",
                "vibraphone_Music_Voice",
                "harp_Music_Voice",
                "violin1_Music_Voice",
                "violin2_Music_Voice",
                "viola1_Music_Voice",
                "cello1_Music_Voice",
                "doublebass_Music_Voice",
            ] 
    
def sort_instruments_by_clef(voice_list, target):
    if isinstance(voice_list, list):
        for i in range(len(voice_list)):
            target.append(voice_list[i])
        return target
    else:
        single_voice = voice_list
        target.append(single_voice)
        return target

def configure_score():
    voices  = music_voices # list of voices
    treble, alto, bass = [], [], []
    temp = voices[0:3] # fl, ob, cl
    print(temp)
    sort_instruments_by_clef(temp, treble)
    temp = voices[3] # bassoon
    sort_instruments_by_clef(temp, bass)
    temp = voices[4:7] # hrn1, hrn3, trp
    sort_instruments_by_clef(temp, treble)
    temp = voices[8] # timpani
    sort_instruments_by_clef(temp, bass)
    temp = voices[9:13] # vibraphone, harp, vln1, vln2
    sort_instruments_by_clef(temp, treble)
    temp = voices[13] # viola
    sort_instruments_by_clef(temp, alto) # cello, db
    temp = voices[14:16] # cello, db
    sort_instruments_by_clef(temp, bass)
    print("treble: ", treble, '\n', "alto: ", alto, '\n', "bass: ", bass)
   

    
if __name__ == "__main__":
    print("hello test")
    print_test()
    set_clefs_and_print_results(test_list)
    configure_score()
