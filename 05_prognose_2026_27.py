# Vorhersage 2026/27

# Daten der Saison 25/26 laden
df_2526 = daten["Tabelle 25 26"].copy()

# Leerzeichen aus den Spaltennamen entfernen
df_2526.columns = df_2526.columns.str.strip()

# Bundesliga-Erfahrung für Prognose berechnen
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


# Gewichtete Features für Prognose
df_2526["Punkte 1.Bundesliga gewichtet"] = df_2526["Punkte 1.Bundesliga Vorjahr"]
df_2526["Punkte 2.Bundesliga gewichtet"] = df_2526["Punkte 2.Bundesliga Vorjahr"] * liga2_faktor

df_2526["Tore 1.Bundesliga gewichtet"] = df_2526["Tore 1.Bundesliga Vorjahr"]
df_2526["Tore 2.Bundesliga gewichtet"] = df_2526["Tore 2.Bundesliga Vorjahr"] * liga2_faktor

df_2526["Gegentore 1.Bundesliga gewichtet"] = df_2526["Gegentore 1.Bundesliga Vorjahr"]
df_2526["Gegentore 2.Bundesliga gewichtet"] = df_2526["Gegentore 2.Bundesliga Vorjahr"] * liga2_faktor

X_2627 = df_2526[features].fillna(0)


# Punkte für die Saison 2026/27 vorhersagen
df_2526["Erwartete Punkte 26/27"] = modell.predict(X_2627)


# Nach erwarteten Punkten sortieren
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
