#Bibliotheken instalieren und importieren

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)


#Exel einlesen

#Exel hochladen aus Ordner data
datei = "data/Tabelle Bundesliga ML Projekt.xlsx"

print("Geladene Datei:", datei)


#Tabellen laden

#Tabellenblätter einlesen und Blätter ausgeben
excel = pd.ExcelFile(datei)

print(excel.sheet_names)

#Reihenfolge der Tabellen ändern
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


#Gesamtdatensatz laden

#Alle Tabellen einlesen
daten = {}
alle_saisons = []

for saison in saisons:

    df_saison = pd.read_excel(
        datei,
        sheet_name=saison
    )

    #Leerzeichen aus Spaltennamen entfernen
    df_saison.columns = df_saison.columns.str.strip()

    #Saison als neue Spalte hinzufügen
    df_saison["Saison"] = saison

    #DataFrame im Dictionary speichern
    daten[saison] = df_saison

    #Für den Gesamtdatensatz merken
    alle_saisons.append(df_saison)

#Alle Saisons zusammenführen
df = pd.concat(
    alle_saisons,
    ignore_index=True
)

print(df.shape)

#Reihenfolge der Saisons festlegen
df["Saison"] = pd.Categorical(
    df["Saison"],
    categories=saisons,
    ordered=True
)

#Nach Verein und Saison sortieren
df = df.sort_values(
    ["Verein", "Saison"]
).reset_index(drop=True)

print(df.shape)
display(df.head())


#Trainingsdatensatz

#Trainingsdatensatz erstellen

#Originaldaten NICHT verändern
df_train = df.copy()

#Zielvariable erzeugen

df_train["Punkte_Saison"] = np.where(
    df_train["Aufsteiger"] == 1,
    df_train["Punkte 2.Bundesliga Vorjahr"],
    df_train["Punkte 1.Bundesliga Vorjahr"]
)

df_train["Zielpunkte"] = (
    df_train.groupby("Verein")["Punkte_Saison"]
            .shift(-1)
)

df_train = df_train.dropna(
    subset=["Zielpunkte"]
)

print(df_train["Saison"].value_counts())

#Anzahl der Saisons je Verein - nur zur Kontrolle, wegen Rechtschreibung
vereine = (
    df.groupby("Verein")["Saison"]
      .count()
      .sort_values()
)

print(vereine)


#Bundesliga Erfahrung

#Bundesliga-Erfahrung berechnen
df_train["Bundesliga_Erfahrung"] = 0

for verein in df_train["Verein"].unique():

    erfahrung = 0

    for index in df_train[df_train["Verein"] == verein].index:

        # Erfahrung vor dieser Saison speichern
        df_train.loc[index, "Bundesliga_Erfahrung"] = erfahrung

        # Nur Nicht-Aufsteiger zählen als Bundesliga-Erfahrungsjahr
        if df_train.loc[index, "Aufsteiger"] == 0:
            erfahrung += 1

print(
    df_train[
        ["Verein", "Saison", "Aufsteiger", "Bundesliga_Erfahrung"]
    ].head(40)
)


#Ligafaktor berechnen

#Ligafaktor berechnen aus historischen Daten
#Nur Aufsteiger betrachten
aufsteiger = df_train[df_train["Aufsteiger"] == 1].copy()

#Nur Datensätze verwenden, bei denen Zweitliga-Punkte vorhanden sind
aufsteiger = aufsteiger[
    aufsteiger["Punkte 2.Bundesliga Vorjahr"] > 0
]

#Verhältnis Bundesliga-Punkte / Zweitliga-Punkte
aufsteiger["Ligafaktor"] = (
    aufsteiger["Zielpunkte"] /
    aufsteiger["Punkte 2.Bundesliga Vorjahr"]
)

liga2_faktor = aufsteiger["Ligafaktor"].mean()

print("Berechneter Ligafaktor:", round(liga2_faktor,3))

#Ligagewichtung
#Punkte
df_train["Punkte 1.Bundesliga gewichtet"] = (
    df_train["Punkte 1.Bundesliga Vorjahr"]
)

df_train["Punkte 2.Bundesliga gewichtet"] = (
    df_train["Punkte 2.Bundesliga Vorjahr"] * liga2_faktor
)

#Tore
df_train["Tore 1.Bundesliga gewichtet"] = (
    df_train["Tore 1.Bundesliga Vorjahr"]
)

df_train["Tore 2.Bundesliga gewichtet"] = (
    df_train["Tore 2.Bundesliga Vorjahr"] * liga2_faktor
)

#Gegentore
df_train["Gegentore 1.Bundesliga gewichtet"] = (
    df_train["Gegentore 1.Bundesliga Vorjahr"]
)

df_train["Gegentore 2.Bundesliga gewichtet"] = (
    df_train["Gegentore 2.Bundesliga Vorjahr"] * liga2_faktor
)


#Features auswählen

features = [

    #Tabellenplatz
    "Platzierung 1.Bundesliga Vorjahr",
    "Platzierung 2.Bundesliga Vorjahr",

    #Punkte
    "Punkte 1.Bundesliga Vorjahr",
    "Punkte 2.Bundesliga Vorjahr",
    "Punkte 1.Bundesliga gewichtet",
    "Punkte 2.Bundesliga gewichtet",

    #Tore
    "Tore 1.Bundesliga Vorjahr",
    "Tore 2.Bundesliga Vorjahr",
    "Tore 1.Bundesliga gewichtet",
    "Tore 2.Bundesliga gewichtet",

    #Gegentore
    "Gegentore 1.Bundesliga Vorjahr",
    "Gegentore 2.Bundesliga Vorjahr",
    "Gegentore 1.Bundesliga gewichtet",
    "Gegentore 2.Bundesliga gewichtet",

    #Mannschaft
    "Marktwert",
    "Kadergroese",
    "Durchschnittsalter",
    "Zugaenge",
    "Abgaenge",
    "Trainerwechsel",

    #Sonstiges
    "Aufsteiger",
    "Bundesliga_Erfahrung"
]

#Fehlenden Feature-Werte auffüllen
df_train[features] = df_train[features].fillna(0)

print(df_train[features].isnull().sum())


#Trainingsdaten und Testdaten

#Trainings- und Testdaten erstellen
#Trainingsdaten:
#Saison 16/17 bis 23/24

train = df_train[
    df_train["Saison"] != "Tabelle 24 25"
]

#Testdaten:
#Saison 24/25

test = df_train[
    df_train["Saison"] == "Tabelle 24 25"
]

X_train = train[features]
y_train = train["Zielpunkte"]

X_test = test[features]
y_test = test["Zielpunkte"]

print("Trainingsdaten:", X_train.shape)
print("Testdaten:", X_test.shape)


#Random Forest trainieren

from sklearn.ensemble import RandomForestRegressor

modell = RandomForestRegressor(

    n_estimators=1000,
    max_depth=10,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42

)

modell.fit(
    X_train,
    y_train
)

print("Modell erfolgreich trainiert!")

#Modell bewerten
from sklearn.metrics import mean_absolute_error, r2_score

test_vorhersage = modell.predict(X_test)

mae = mean_absolute_error(y_test, test_vorhersage)
r2 = r2_score(y_test, test_vorhersage)

print(f"MAE: {mae:.2f} Punkte")
print(f"R²: {r2:.3f}")

#Feature Wichtigkeit

importance = pd.DataFrame({
    "Feature": features,
    "Wichtigkeit": modell.feature_importances_
})

importance = importance.sort_values(
    "Wichtigkeit",
    ascending=False
)

display(importance)

#Ausgeben, wie viele Teams im Datensatz fehlen 
print(df_train["Saison"].value_counts().sort_index())


#Vorhersagen 26/27

#Daten der Saison 25/26 laden
df_2526 = daten["Tabelle 25 26"].copy()

#Leerzeichen aus den Spaltennamen entfernen
df_2526.columns = df_2526.columns.str.strip()

#Bundesliga-Erfahrung für Prognose berechnen
erfahrung_werte = {}

for verein in df["Verein"].unique():

    verein_daten = df[df["Verein"] == verein]

    erfahrung = 0

    for _, zeile in verein_daten.iterrows():

        if zeile["Saison"] == "Tabelle 25 26":
            break

        if zeile["Aufsteiger"] == 0:
            erfahrung += 1

    erfahrung_werte[verein] = erfahrung

df_2526["Bundesliga_Erfahrung"] = (
    df_2526["Verein"].map(erfahrung_werte).fillna(0)
)

#Gewichtete Features für Prognose
df_2526["Punkte 1.Bundesliga gewichtet"] = df_2526["Punkte 1.Bundesliga Vorjahr"]
df_2526["Punkte 2.Bundesliga gewichtet"] = df_2526["Punkte 2.Bundesliga Vorjahr"] * liga2_faktor

df_2526["Tore 1.Bundesliga gewichtet"] = df_2526["Tore 1.Bundesliga Vorjahr"]
df_2526["Tore 2.Bundesliga gewichtet"] = df_2526["Tore 2.Bundesliga Vorjahr"] * liga2_faktor

df_2526["Gegentore 1.Bundesliga gewichtet"] = df_2526["Gegentore 1.Bundesliga Vorjahr"]
df_2526["Gegentore 2.Bundesliga gewichtet"] = df_2526["Gegentore 2.Bundesliga Vorjahr"] * liga2_faktor

X_2627 = df_2526[features].fillna(0)

#Punkte für die Saison 2026/27 vorhersagen
df_2526["Erwartete Punkte 26/27"] = modell.predict(X_2627)

#Nach erwarteten Punkten sortieren
prognose = df_2526.sort_values(
    "Erwartete Punkte 26/27",
    ascending=False
).reset_index(drop=True)

prognose["Prognose Platz"] = prognose.index + 1

display(
    prognose[
        ["Prognose Platz", "Verein", "Erwartete Punkte 26/27"]
    ]
)


#Monte-Carlo Simulation

#Monte-Carlo-Simulation
np.random.seed(42)

anzahl_simulationen = 1000
standardabweichung = 5

simulationen = []

for sim in range(anzahl_simulationen):

    saison = prognose.copy()

    saison["Simulierte Punkte"] = np.random.normal(
        saison["Erwartete Punkte 26/27"],
        standardabweichung
    )

    saison["Simulierte Punkte"] = saison["Simulierte Punkte"].clip(lower=0)

    saison = saison.sort_values(
        "Simulierte Punkte",
        ascending=False
    ).reset_index(drop=True)

    saison["Simulierter Platz"] = saison.index + 1

    saison["Simulation"] = sim + 1

    simulationen.append(
        saison[
            [
                "Simulation",
                "Verein",
                "Simulierter Platz",
                "Simulierte Punkte"
            ]
        ]
    )

alle_simulationen = pd.concat(
    simulationen,
    ignore_index=True
)

display(alle_simulationen.head())

#Wahrscheinlichkeiten berechnen
wahrscheinlichkeiten = pd.DataFrame({
    "Verein": prognose["Verein"]
})

wahrscheinlichkeiten["Meister"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: (alle_simulationen[
        (alle_simulationen["Verein"] == team) &
        (alle_simulationen["Simulierter Platz"] == 1)
    ].shape[0] / anzahl_simulationen) * 100
)

wahrscheinlichkeiten["Champions League"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: (alle_simulationen[
        (alle_simulationen["Verein"] == team) &
        (alle_simulationen["Simulierter Platz"] <= 4)
    ].shape[0] / anzahl_simulationen) * 100
)

wahrscheinlichkeiten["Europa League"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: (alle_simulationen[
        (alle_simulationen["Verein"] == team) &
        (alle_simulationen["Simulierter Platz"] == 5)
    ].shape[0] / anzahl_simulationen) * 100
)

wahrscheinlichkeiten["Conference League"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: (alle_simulationen[
        (alle_simulationen["Verein"] == team) &
        (alle_simulationen["Simulierter Platz"] == 6)
    ].shape[0] / anzahl_simulationen) * 100
)

wahrscheinlichkeiten["Relegation"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: (alle_simulationen[
        (alle_simulationen["Verein"] == team) &
        (alle_simulationen["Simulierter Platz"] == 16)
    ].shape[0] / anzahl_simulationen) * 100
)

wahrscheinlichkeiten["Abstieg"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: (alle_simulationen[
        (alle_simulationen["Verein"] == team) &
        (alle_simulationen["Simulierter Platz"] >= 17)
    ].shape[0] / anzahl_simulationen) * 100
)

wahrscheinlichkeiten["Durchschnittlicher Platz"] = wahrscheinlichkeiten["Verein"].apply(
    lambda team: alle_simulationen[
        alle_simulationen["Verein"] == team
    ]["Simulierter Platz"].mean()
)

ergebnisse = prognose[
    ["Prognose Platz", "Verein", "Erwartete Punkte 26/27"]
].merge(
    wahrscheinlichkeiten,
    on="Verein"
)

ergebnisse = ergebnisse.sort_values(
    "Durchschnittlicher Platz"
).reset_index(drop=True)

ergebnisse["Prognose Platz"] = ergebnisse.index + 1

ergebnisse = ergebnisse.round(2)

display(ergebnisse)
