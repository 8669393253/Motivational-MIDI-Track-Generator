# Motivational MIDI Track Generator

This Python script generates a MIDI file with an uplifting and motivational sequence of chords and melody. It uses the `mido` library to create the MIDI file, add notes, and set the tempo.

## Features
- **Chords**: The script adds a series of major and minor chords that create a harmonic and motivational background.
- **Melody**: A fast-paced melody is added to give the track an uplifting feel.
- **Tempo**: The track is set to a moderate tempo of 120 beats per minute (BPM), which is commonly used for energetic, motivational music.

## Requirements
- Python 3.x
- The `mido` library, which can be installed via pip:

  pip install mido


## How It Works
1. **Chords**: The script defines a list of chords, including:
   - C Major (C, E, G)
   - D Minor (D, F, A)
   - E Minor (E, G, B)
   - F Major (F, A, C)
   
   These chords are added to the track with a velocity of 80 and held for one beat.

2. **Melody**: A simple melody is defined with the notes:
   - C5, D5, E5, F5, G5, A5, B5, C6
   
   The melody is played with a velocity of 100, and each note is held for half a beat (240 ticks).

3. **Tempo**: The track is set to a tempo of 120 BPM, providing a moderate pace for both the chords and melody.

4. **MIDI File**: After generating the track, the script saves the MIDI file as `motivational_track.mid`.

## How to Run
1. Make sure you have Python installed (Python 3.x recommended).
2. Install the `mido` library:

   pip install mido

3. Save the Python script (e.g., `motivational_track.py`) to your computer.
4. Run the script:

   python motivational_track.py

5. The script will generate a file called `motivational_track.mid` in the same directory.

## Customization
- You can modify the list of chords and the melody to create your own unique motivational track.
- Adjust the `velocity` and `time` parameters to change the dynamics and timing of the notes.
- Change the `tempo` to create a faster or slower track.

## Example Output
After running the script, you will find a file called `motivational_track.mid` in your directory. This file can be opened with any MIDI player or digital audio workstation (DAW) software for playback and editing.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
