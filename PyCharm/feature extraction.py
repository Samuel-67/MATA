import librosa
import numpy as np
import csv
import os
from tqdm import tqdm

# sorgt dafür das die arrays ohne minimierung ausgegeben werden. (normalerweise wird es abgekürzt damit es nicht zu lang ist)
# --> ohne das werden nur erste drei werte angegenen dann ... und dann die letzten drei. damit es kürzer ist.
np.set_printoptions(threshold=np.inf)


# y, sr = librosa.load('../daten/Blues/Blues0.mp3')

#tracks_ordner = "../daten/death metal/"
tracks_ordner_arr = ["../daten/500progenre/death metal/", "../daten/500progenre/blues/", "../daten/500progenre/edm/", "../daten/500progenre/hiphop/", "../daten/500progenre/reggae/"]
#genre = 'death metal'
genre_arr = ["death metal", "blues", "edm", "hiphop", "reggea"]
genreid_arr = [1,2,3,4,5] # deathmetal = 1, blues = 2 usw.
zieldatei ="daten4.csv"

n = 0

def getfeatures(y, sr):

    getfeatures.tempo, beat = librosa.beat.beat_track(y=y, sr=sr)

    #getfeatures.mfccs gibt für jeden einzelnen Frame den koeffizienten an d.h. pro koeffizient jeder Frame

    mfccs_f = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    #durchschnitt von jedem Koeffizienten ausrechen (sodasss nicht für jeden Koeffizienten ein wert pro frma evorliegt)
    # Aufbau von mfccs_f ist: mit werte ist gemeint ein wert pro frame
    # mfccs_f = [[Werte Koeffizient 1][Werte Koeffizient 2][Werte Koeffizient 3][Werte Koeffizient 4][Werte Koeffizient 5]]
    getfeatures.mfccs = [[] for i in range(len(mfccs_f))]
    k = 0
    for i in mfccs_f:
        getfeatures.mfccs[k].append(np.mean(i))
        k += 1

    # für jeden mfcc eine variable (mfcc1, mfcc2 usw.) zuordnen:
    j = 1
    for i in getfeatures.mfccs:
        globals()['mfcc%s' % j] = i
        j += 1

    # spectral rolloff
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr) [0]
    getfeatures.rolloff_durchschnitt = np.mean(rolloff, axis=0)

    # spectral centroid
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr) [0]
    getfeatures.centroid_durchschnitt = np.mean(centroid)

    # durchschnittliche RMS-Energie:
    rms = librosa.feature.rms(y=y)
    getfeatures.rms_durchschnitt = np.mean(rms)

    #zero crossing rate (anzahl im ganzen ausschnitt)
    zero_crossings = librosa.zero_crossings(y)
    getfeatures.zcr = sum(zero_crossings)

    #spectral bandwith:
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr) [0]
    getfeatures.spec_bw_durchschnitt = np.mean(spec_bw)


    #spectral flatness:
    spec_flatness = librosa.feature.spectral_flatness(y=y) [0]
    getfeatures.spec_flatness_durchschnitt = np.mean(spec_flatness)


def csvschreiben(genre, BPM, rolloff, centroid, rms_durchschnitt, zcr, spec_bw, spec_flatness, mfcc1, mfcc2, mfcc3, mfcc4, mfcc5, mfcc6, mfcc7, mfcc8, mfcc9, mfcc10, mfcc11 ,mfcc12, mfcc13):
    with open(zieldatei, 'a', newline='') as datei:
        writer = csv.writer(datei)
        writer.writerow([genre, BPM, rolloff, centroid, rms_durchschnitt, zcr, spec_bw, spec_flatness, mfcc1, mfcc2, mfcc3, mfcc4, mfcc5, mfcc6, mfcc7, mfcc8, mfcc9, mfcc10, mfcc11 ,mfcc12, mfcc13])

with open(zieldatei, 'w', newline='') as datei:
    writer = csv.writer(datei)
    writer.writerow(["genre", "bpm", "rolloff", "centroid", "rms", "zcr", "spec_bw", "spec_flatness", "mfcc1", "mfcc2", "mfcc3", "mfcc4", "mfcc5", "mfcc6", "mfcc7", "mfcc8", "mfcc9", "mfcc10", "mfcc11" ,"mfcc12", "mfcc13"])

for e in tracks_ordner_arr:
    tracks_ordner = e
    genre = genreid_arr[n]
    n += 1

    pbar = tqdm(total=100)

    for x in os.listdir(tracks_ordner):
        y, sr = librosa.load(tracks_ordner + x)
        getfeatures(y, sr)
        csvschreiben(genre, getfeatures.tempo, getfeatures.rolloff_durchschnitt, getfeatures.centroid_durchschnitt, getfeatures.rms_durchschnitt, getfeatures.zcr, getfeatures.spec_bw_durchschnitt, getfeatures.spec_flatness_durchschnitt, mfcc1[0], mfcc2[0], mfcc3[0], mfcc4[0], mfcc5[0], mfcc6[0], mfcc7[0], mfcc8[0], mfcc9[0], mfcc10[0], mfcc11[0], mfcc12[0], mfcc13[0])
        i = len(os.listdir(tracks_ordner))
        pbar.update(100/i)

