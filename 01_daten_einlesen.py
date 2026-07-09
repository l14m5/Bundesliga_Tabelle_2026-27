# Bibliotheken instalieren und importieren

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)


# Exel hochladen aus Ordner data

datei = "data/Tabelle Bundesliga ML Projekt.xlsx"
print("Geladene Datei:", datei)


# Tabellenblätter einlesen und Blätter ausgeben

excel = pd.ExcelFile(datei)
print(excel.sheet_names)


# Reihenfolge der Tabellen ändern

saisons = [
    "Tabelle 16 17",
    "Tabelle 17 18",
    "Tabelle 18 19",
    "Tabelle 19 20",
    "Tabelle 20 21",
    "Tabelle 21 22",
    "Tabelle 22 23",
    "Tabelle 23 24",
    "Tabelle 24 25",
    "Tabelle 25 26"
]


# Gesamtdatensatz laden

# Alle Tabellen einlesen
daten = {}
alle_saisons = []

for saison in saisons:

    df_saison = pd.read_excel(
        datei,
        sheet_name=saison
    )

    # Leerzeichen aus Spaltennamen entfernen
    df_saison.columns = df_saison.columns.str.strip()

    # Saison als neue Spalte hinzufügen
    df_saison["Saison"] = saison

    # DataFrame im Dictionary speichern
    daten[saison] = df_saison

    # Für den Gesamtdatensatz merken
    alle_saisons.append(df_saison)

# Alle Saisons zusammenführen
df = pd.concat(
    alle_saisons,
    ignore_index=True
)

print(df.shape)


# Reihenfolge der Saisons festlegen
df["Saison"] = pd.Categorical(
    df["Saison"],
    categories=saisons,
    ordered=True
)

# Nach Verein und Saison sortieren
df = df.sort_values(
    ["Verein", "Saison"]
).reset_index(drop=True)

print(df.shape)
display(df.head())
