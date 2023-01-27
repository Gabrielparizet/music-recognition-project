import librosa

filename = '/Users/gabrielparizet/Desktop/Projet Perso/music-recognition-project/mp3s/donato_dozzy_dj_say_your_eyes.mp3'

y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(f'The BPM of the audio file is {tempo}')