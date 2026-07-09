# Trainingsdatensatz erstellen

# Originaldaten NICHT verändern
df_train = df.copy()

# Zielvariable erzeugen
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


# Anzahl der Saisons je Verein - zur Kontrolle

vereine = (
    df.groupby("Verein")["Saison"]
      .count()
      .sort_values()
)

print(vereine)
