import abjad
import rill

# PitchSegments for section
cmin7_6 = rill.tetrads['bf_ii']
cmin7_64 = rill.invert_up(cmin7_6, 1)
cmin7_42 = rill.invert_up(cmin7_6, 2)
cmin7 = rill.invert_up(cmin7_6, 3)
print(type(cmin7_6), cmin7_64, cmin7_42, cmin7)

# As Harmony Objects
cm7_6 = rill.FuzzyHarmony('bf_ii', cmin7_6)
cm7_64 = rill.FuzzyHarmony('bf_ii', cmin7_64)
cm7_42 = rill.FuzzyHarmony('bf_ii', cmin7_42)
cm7 = rill.FuzzyHarmony('bf_ii', cmin7)

cm_harmonies = [cm7_6, cm7_64, cm7_42, cm7]

def generate_pitches(harmonies):
    for harmony in harmonies: 
        print(harmony)
        for pitch in harmony.pitches:
            print(pitch)

generate_pitches(cm_harmonies)

print("item access: ", cm7_6.pitches[1])


