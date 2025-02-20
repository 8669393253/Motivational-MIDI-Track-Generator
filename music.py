import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage

# Create a new MIDI file
mid = MidiFile()

# Add a track
track = MidiTrack()
mid.tracks.append(track)

# Function to add chords
def add_chord(track, notes, velocity, time):
    for note in notes:
        track.append(Message('note_on', note=note, velocity=velocity, time=0))  # Start note
    for note in notes:
        track.append(Message('note_off', note=note, velocity=velocity, time=time))  # End note

# Function to add melody
def add_melody(track, notes, velocity, time_per_note):
    for note in notes:
        track.append(Message('note_on', note=note, velocity=velocity, time=0))  # Start note
        track.append(Message('note_off', note=note, velocity=velocity, time=time_per_note))  # End note

# Tempo settings (bpm: 120)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120)))  # Correct usage of MetaMessage for tempo

# Adding Motivational Chords (Major chords)
chords = [
    [60, 64, 67],  # C Major (C, E, G)
    [62, 65, 69],  # D Minor (D, F, A)
    [64, 67, 71],  # E Minor (E, G, B)
    [65, 69, 72]   # F Major (F, A, C)
]

# Add a sequence of chords
for chord in chords:
    add_chord(track, chord, velocity=80, time=480)  # Add a chord and hold for a beat

# Adding Motivational Melody (Fast-paced notes)
melody = [72, 74, 76, 77, 79, 81, 83, 84]  # Simple uplifting melody notes
add_melody(track, melody, velocity=100, time_per_note=240)  # Fast-paced melody

# Save the file
mid.save('motivational_track.mid')

print("Motivational track generated and saved as 'motivational_track.mid'")
