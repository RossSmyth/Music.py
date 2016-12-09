import winsound

scale = 440
ratio = 1.05946
notes = {
		 'A': 0,
         'A#': 1,
         'B': 2,
		 'C': 3,
		 'C#': 4,
		 'D': 5,
		 'D#': 6,
		 'E': 7,
		 'F': 8,
		 'F#': 9,
		 'G': 10,
		 'G#': 11,
		 }

tempered_notes = {}

for note in notes:
	freq = scale * ratio ** notes.get(note)
	tempered_notes[note] = int(freq)

def play_note(note, duration=500):
	"""Plays the notes for a certain duration"""
	winsound.Beep(tempered_notes.get(note), duration)

def frequency(note):
	"""Finds the frequency of a note"""
	pitch_level = note[1]
	name = note[0]
	
	step = 12 * pitch_level + notes[name]
	
	return 110 * 2 ** (step / 12)
	
def play_note_list(note_list):
	"""Plays the list of notes"""
	for note in note_list:
		freq = frequency(note)
		play_note(freq)

song = input("Notes in order:")

note_list = song.split()

note_final_list = []
i = 0
for note in note_list:
	if len(note) > 2:
		note_final_list.insert(i, [note[:2], int(note[2:])])
	else:
		note_final_list.insert(i, [note[:1], int(note[1:])])
	i += 1

