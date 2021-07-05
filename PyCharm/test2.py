import librosa
import numpy as np
y, sr = librosa.load('../daten/Blues/Blues0.mp3')

mfccs_f = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

mfccs = [[] for i in range(len(mfccs_f))]
k = 0
for i in mfccs_f:
    mfccs[k].append(np.mean(i))
    k += 1

print(mfccs)

j = 1

for i in mfccs:
    globals()['mfcc%s' % j] = i
    j += 1

print(mfcc1)
print(mfcc2)
print(mfcc3)
print(mfcc4)
print(mfcc5)
print(mfcc6)
print(mfcc7)
print(mfcc8)
print(mfcc9)
print(mfcc10)
print(mfcc11)
print(mfcc12)
print(mfcc13)


print(mfcc1[0])