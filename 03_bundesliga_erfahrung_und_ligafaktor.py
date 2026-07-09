# Bundesliga-Erfahrung berechnen

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


#Ligafaktor berechnen aus historischen Daten

# Nur Aufsteiger betrachten
aufsteiger = df_train[df_train["Aufsteiger"] == 1].copy()

# Nur Datensätze verwenden, bei denen Zweitliga-Punkte vorhanden sind
aufsteiger = aufsteiger[
    aufsteiger["Punkte 2.Bundesliga Vorjahr"] > 0
]

# Verhältnis Bundesliga-Punkte / Zweitliga-Punkte
aufsteiger["Ligafaktor"] = (
    aufsteiger["Zielpunkte"] /
    aufsteiger["Punkte 2.Bundesliga Vorjahr"]
)

liga2_faktor = aufsteiger["Ligafaktor"].mean()

print("Berechneter Ligafaktor:", round(liga2_faktor,3))


#Ligagewichtung

# Punkte
df_train["Punkte 1.Bundesliga gewichtet"] = (
    df_train["Punkte 1.Bundesliga Vorjahr"]
)

df_train["Punkte 2.Bundesliga gewichtet"] = (
    df_train["Punkte 2.Bundesliga Vorjahr"] * liga2_faktor
)

# Tore
df_train["Tore 1.Bundesliga gewichtet"] = (
    df_train["Tore 1.Bundesliga Vorjahr"]
)

df_train["Tore 2.Bundesliga gewichtet"] = (
    df_train["Tore 2.Bundesliga Vorjahr"] * liga2_faktor
)

# Gegentore
df_train["Gegentore 1.Bundesliga gewichtet"] = (
    df_train["Gegentore 1.Bundesliga Vorjahr"]
)

df_train["Gegentore 2.Bundesliga gewichtet"] = (
    df_train["Gegentore 2.Bundesliga Vorjahr"] * liga2_faktor
)


#Features auswählen

features = [

    # Tabellenplatz
    "Platzierung 1.Bundesliga Vorjahr",
    "Platzierung 2.Bundesliga Vorjahr",

    # Punkte
    "Punkte 1.Bundesliga Vorjahr",
    "Punkte 2.Bundesliga Vorjahr",
    "Punkte 1.Bundesliga gewichtet",
    "Punkte 2.Bundesliga gewichtet",

    # Tore
    "Tore 1.Bundesliga Vorjahr",
    "Tore 2.Bundesliga Vorjahr",
    "Tore 1.Bundesliga gewichtet",
    "Tore 2.Bundesliga gewichtet",

    # Gegentore
    "Gegentore 1.Bundesliga Vorjahr",
    "Gegentore 2.Bundesliga Vorjahr",
    "Gegentore 1.Bundesliga gewichtet",
    "Gegentore 2.Bundesliga gewichtet",

    # Mannschaft
    "Marktwert",
    "Kadergroese",
    "Durchschnittsalter",
    "Zugaenge",
    "Abgaenge",
    "Trainerwechsel",

    # Sonstiges
    "Aufsteiger",
    "Bundesliga_Erfahrung"
]

#Fehlenden Feature-Werte auffüllen
df_train[features] = df_train[features].fillna(0)

print(df_train[features].isnull().sum())
