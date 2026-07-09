# Monte-Carlo-Simulation

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


# Wahrscheinlichkeiten berechnen

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
