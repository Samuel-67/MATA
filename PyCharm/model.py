import tensorflow as tf
import  pandas as pd

daten = pd.read_csv('daten.csv')

print(daten.head())

daten_features = daten.drop(columns=['Genre'])
daten_labels = daten.pop('Genre')

print(daten_features.head())
