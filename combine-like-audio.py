import csv
from pydub import AudioSegment


with open('key.csv', newline='') as csvkey:
    lookup = {}
    combo_list = []
    filename_list = []
    reader = csv.reader(csvkey)
    for x in reader:
        combo_list.append(x[2])
        filename_list.append(x[0])
        lookup[x[0]] = x[2]
    combo_list = sorted(set(combo_list))
    audio_files = {}
    for n in combo_list:
        audio_files[n] = AudioSegment.empty()
    for n in filename_list:
        audio_files[lookup[n]] = audio_files[lookup[n]] + AudioSegment.silent(duration=100) + AudioSegment.from_wav(n + ".wav")
    for n in audio_files:
        audio_files[n].export("combination-"+n+".wav", format = "wav")
        
