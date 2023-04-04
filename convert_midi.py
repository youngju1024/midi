import collections
import datetime
import glob
import numpy as np
import pathlib
import pandas as pd
import pretty_midi
import seaborn as sns
import os
import hashlib

from note_seq import abc_parser
from note_seq import midi_io
from note_seq import musicxml_reader
import tensorflow.compat.v1 as tf
from IPython import display
from matplotlib import pyplot as plt
from typing import Dict, List, Optional, Sequence, Tuple


def midi_to_notes(midi_file: str) -> pd.DataFrame:
  pm = pretty_midi.PrettyMIDI(midi_file)
  instrument = pm.instruments[0]
  notes = collections.defaultdict(list)

  # Sort the notes by start time
  sorted_notes = sorted(instrument.notes, key=lambda note: note.start)
  prev_start = sorted_notes[0].start

  for note in sorted_notes:
    start = note.start
    end = note.end
    notes['pitch'].append(note.pitch)
    notes['start'].append(start)
    notes['end'].append(end)
    notes['step'].append(start - prev_start)
    notes['duration'].append(end - start)
    notes['velocity'].append(note.velocity)
    prev_start = start

  return pd.DataFrame({name: np.array(value) for name, value in notes.items()})

def notes_to_midi(
  notes: pd.DataFrame,
  out_file: str, 
  instrument_name: str,
) -> pretty_midi.PrettyMIDI:

  pm = pretty_midi.PrettyMIDI()
  instrument = pretty_midi.Instrument(is_drum=True,
      program=pretty_midi.instrument_name_to_program(
          instrument_name))

  for i, note in notes.iterrows():
    note = pretty_midi.Note(
        velocity=int(note['velocity']),
        pitch=int(note['pitch']),
        start=float(note['start']),
        end=float(note['end']),
    )
    instrument.notes.append(note)

  pm.instruments.append(instrument)
  pm.write(out_file)
  return pm

def plot_distributions(notes: pd.DataFrame, drop_percentile=2.5):
  plt.figure(figsize=[15, 5])
  plt.subplot(1, 3, 1)
  sns.histplot(notes, x="pitch", bins=20)

  plt.subplot(1, 3, 2)
  max_step = np.percentile(notes['step'], 100 - drop_percentile)
  sns.histplot(notes, x="step", bins=np.linspace(0, max_step, 21))

  plt.subplot(1, 3, 3)
  max_duration = np.percentile(notes['duration'], 100 - drop_percentile)
  sns.histplot(notes, x="duration", bins=np.linspace(0, max_duration, 21))
  
def plot_piano_roll(notes: pd.DataFrame, count: Optional[int] = None):
  if count:
    title = f'First {count} notes'
  else:
    title = f'Whole track'
    count = len(notes['pitch'])
  plt.figure(figsize=(20, 4))
  plot_pitch = np.stack([notes['pitch'], notes['pitch']], axis=0)
  plot_start_stop = np.stack([notes['start'], notes['end']], axis=0)
  plt.plot(
      plot_start_stop[:, :count], plot_pitch[:, :count], color="b", marker=".")
  plt.xlabel('Time [s]')
  plt.ylabel('Pitch')
  _ = plt.title(title)

output = 'music.tfrecord'

_SAMPLING_RATE = 16000

filenames = glob.glob('midi/**/*.mid*',recursive=True)

pm = pretty_midi.PrettyMIDI(filenames[1])
for key in pm.key_signature_changes:
  print(key)
print(filenames[1])
'''
print('Number of instruments:', len(pm.instruments))
instrument = pm.instruments[0]
instrument_name = pretty_midi.program_to_instrument_name(instrument.program)
print('Instrument name:', instrument_name)

print(filenames[1])
raw_notes = midi_to_notes(filenames[1])
print(raw_notes['pitch'].unique())

raw_notes_list = raw_notes.values.tolist()


for f in filenames:
  pm = pretty_midi.PrettyMIDI(f)
  tempo_times, tempo = pm.get_tempo_changes()
  raw_notes = midi_to_notes(f)
  n = 0.
  for note in raw_notes:

  raw_notes.

#print(r_notes)
#plot_piano_roll(raw_notes)
#plt.show()
#plot_distributions(raw_notes)
#plt.show()

example_file = 'example.midi'
#example_pm = notes_to_midi(
#    raw_notes, out_file=example_file, instrument_name=instrument_name)
'''