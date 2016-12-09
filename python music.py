import winsound

scale = 440
ratio = 1.05946
notes = {'A2': -11,
		 'A#2': -10,
		 'C2': -9,
         'C#2': -8,
         'D2': -7,
         'D#2': -6,
         'E2': -5,
         'F2': -4,
         'F#2':-2,
         'G2': -2,
         'G#2': -1,
		 'A3': -11,
		 'A#3': -10,
		 'C3': -9,
         'C#3': -8,
         'D3': -7,
         'D#3': -6,
         'E3': -5,
         'F3': -4,
         'F#3':-2,
         'G3': -2,
         'G#3': -1,
         'A4': 0,
         'A#4': 1,
         'B4': 2,
		 'C4': 3,
		 'C#4': 4,
		 'D4': 5,
		 'D#4': 6,
		 'E4': 7,
		 'F4': 8,
		 'F#4': 9,
		 'G4': 10,
		 'G#4': 11,
		 'A5:': 12,
		 'A#5': 13,
		 'B5': 14
		 }

tempered_notes = {}

for note in notes:
    freq = scale * ratio ** notes.get(note)
    tempered_notes[note] = int(freq)

def play_note(note, duration=500):
    winsound.Beep(tempered_notes.get(note), duration)

song = input("Notes in order:")
for note in song.split():
    play_note(note)