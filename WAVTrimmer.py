import librosa
import os

content = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\WAVTrimmer\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") :
            cline = str(file)
            content.append(cline)

for elem in content:
    outstr = "30" + elem
    print("")
    print("Encoding: " + outstr)
    y, sr = librosa.load(elem, duration=30.0)
    librosa.output.write_wav(outstr, y, sr)

print("")

print("Your files are now available in the same folder as the code.")