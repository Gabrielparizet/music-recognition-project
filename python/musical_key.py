#%%
# Import pandas, numpy, matplotlib, seaborn, glob, librosa, librosa.display, IPython and itertools
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd 

from itertools import cycle


# Display style settings.
sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cylce = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])


# Store our audio file in the audio_file variable.
audio_file = '/Users/gabrielparizet/Desktop/Projet Perso/music-recognition-project/audio_files/donato_dozzy_dj_say_your_eyes.wav'


# Using librosa.load, we extract y as the raw data of our audiofile, and sr as the sample rate of our audio file.
y, sr = librosa.load(audio_file)


# Print the first ten value of our raw data y, which is an array:
print(f'y: {y[:10]}')
# Print the shape of y:
print(f'shape y: {y.shape}')
# Print our sample rate, sr:
print(f'sr: {sr}')


# Display a graph of our audio file
pd.Series(y).plot(figsize=(10,5), lw=1, title='Raw Audio', color=color_pal[1])
plt.show()

"""
# Spectogram of the sound in Decibel as D
D = librosa.stft(y)
# Spectogram of the sound in Decibel
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
S_db.shape


# Plot the transformed audio data
fig, ax = plt.subplots(figsize=(10, 5))
img = librosa.display.specshow(S_db, x_axis='time', y="decibel", ax=ax)



"""
# %%
