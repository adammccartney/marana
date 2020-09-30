import abjad
import marana


voice = abjad.Voice("r1 c'2. d'2. r1 e'2. f'2.")
staff = abjad.Staff([voice])

time_signatures = ["4/4", "3/4"]

def handle_time_signatures(self):
    voice = voice
    leaves = abjad.select(voice).leaves()
    if not leaves:
        return
    

abjad.show(staff)
