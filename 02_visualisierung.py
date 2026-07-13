# Bundesliga-Tabelle

tabelle = ergebnisse[
    [
        "Prognose Platz",
        "Verein",
        "Erwartete Punkte 26/27",
        "Meister",
        "Champions League",
        "Europa League",
        "Conference League",
        "Relegation",
        "Abstieg"
    ]
].copy()

tabelle = tabelle.round(2)

def zeilenfarbe(row):

    platz = row["Prognose Platz"]

# Meister Gold
    if platz == 1:
        return ["background-color: #FFD700"] * len(row)
# Champions League Grün
    elif platz <= 4:
        return ["background-color: #C6EFCE"] * len(row)
# Europa League Blau
    elif platz == 5:
        return ["background-color: #BDD7EE"] * len(row)
# Conference League Hellblau
    elif platz == 6:
        return ["background-color: #DDEBF7"] * len(row)
# Relegation Orange
    elif platz == 16:
        return ["background-color: #FCE4D6"] * len(row)
# Abstieg Rot
    elif platz >= 17:
        return ["background-color: #F4CCCC"] * len(row)
# Mittelfeld Weiß
    else:
        return ["background-color: #FFFFFF"] * len(row)


styled_tabelle = (
    tabelle.style
    .apply(zeilenfarbe, axis=1)
    .format({
        "Erwartete Punkte 26/27": "{:.2f}",
        "Meister": "{:.1f} %",
        "Champions League": "{:.1f} %",
        "Europa League": "{:.1f} %",
        "Conference League": "{:.1f} %",
        "Relegation": "{:.1f} %",
        "Abstieg": "{:.1f} %"
    })
    .set_caption("Bundesliga-Prognose 2026/27")
)

display(styled_tabelle)

# Europa League Wahrscheinlichkeit

plt.figure(figsize=(10, 8))

cl_plot = ergebnisse.sort_values("Europa League", ascending=True)

plt.barh(
    cl_plot["Verein"],
    cl_plot["Europa League"]
)

plt.title("Europa-League-Wahrscheinlichkeit 2026/27")
plt.xlabel("Wahrscheinlichkeit in %")
plt.ylabel("Verein")

plt.show()


# Conference League Wahrscheinlichkeit

plt.figure(figsize=(10, 8))

cl_plot = ergebnisse.sort_values("Conference League", ascending=True)

plt.barh(
    cl_plot["Verein"],
    cl_plot["Conference League"]
)

plt.title("Conference-League-Wahrscheinlichkeit 2026/27")
plt.xlabel("Wahrscheinlichkeit in %")
plt.ylabel("Verein")

plt.show()


# Übersicht

heatmap_daten = ergebnisse.set_index("Verein")[
    [
        "Meister",
        "Champions League",
        "Europa League",
        "Conference League",
        "Relegation",
        "Abstieg"
    ]
]

plt.figure(figsize=(12, 8))

sns.heatmap(
    heatmap_daten,
    annot=True,
    fmt=".1f",
    cmap="Blues"
)

plt.title("Wahrscheinlichkeiten 2026/27")
plt.xlabel("Kategorie")
plt.ylabel("Verein")

plt.show()


# Erwartete Punkte

plt.figure(figsize=(10, 8))

plt.barh(
    ergebnisse["Verein"],
    ergebnisse["Erwartete Punkte 26/27"]
)

plt.gca().invert_yaxis()

plt.title("Prognostizierte Punkte 2026/27")
plt.xlabel("Erwartete Punkte")
plt.ylabel("Verein")

plt.show()


# Meisterschaftswahrscheinlichkeit

plt.figure(figsize=(10, 8))

meister_plot = ergebnisse.sort_values("Meister", ascending=True)

plt.barh(
    meister_plot["Verein"],
    meister_plot["Meister"]
)

plt.title("Meisterwahrscheinlichkeit 2026/27")
plt.xlabel("Wahrscheinlichkeit in %")
plt.ylabel("Verein")

plt.show()


# Champions League Wahrscheinlichkeit

plt.figure(figsize=(10, 8))

cl_plot = ergebnisse.sort_values("Champions League", ascending=True)

plt.barh(
    cl_plot["Verein"],
    cl_plot["Champions League"]
)

plt.title("Champions-League-Wahrscheinlichkeit 2026/27")
plt.xlabel("Wahrscheinlichkeit in %")
plt.ylabel("Verein")

plt.show()


# Abstiegswahrscheinlichkeit

plt.figure(figsize=(10, 8))

abstieg_plot = ergebnisse.sort_values("Abstieg", ascending=True)

plt.barh(
    abstieg_plot["Verein"],
    abstieg_plot["Abstieg"]
)

plt.title("Abstiegswahrscheinlichkeit 2026/27")
plt.xlabel("Wahrscheinlichkeit in %")
plt.ylabel("Verein")

plt.show()


# Durchschnittlicher Platz
plt.figure(figsize=(10, 8))

platz_plot = ergebnisse.sort_values(
    "Durchschnittlicher Platz",
    ascending=False
)

plt.barh(
    platz_plot["Verein"],
    platz_plot["Durchschnittlicher Platz"]
)

plt.title("Durchschnittlicher Tabellenplatz 2026/27")
plt.xlabel("Durchschnittlicher Platz")
plt.ylabel("Verein")

plt.show()


# Übersicht mit Farben - Diagramm

import matplotlib.pyplot as plt

# Farben für die Tabelle
farben = []

for platz in ergebnisse["Prognose Platz"]:

    if platz == 1:
        farben.append("gold")

    elif platz <= 4:
        farben.append("forestgreen")

    elif platz == 5:
        farben.append("royalblue")

    elif platz == 6:
        farben.append("deepskyblue")

    elif platz == 16:
        farben.append("darkorange")

    elif platz >= 17:
        farben.append("firebrick")

    else:
        farben.append("lightgray")

# Grafik
plt.figure(figsize=(12,10))

plt.barh(
    ergebnisse["Verein"],
    ergebnisse["Erwartete Punkte 26/27"],
    color=farben,
    edgecolor="black"
)

plt.gca().invert_yaxis()

plt.title(
    "Bundesliga-Prognose 2026/27",
    fontsize=18,
    weight="bold"
)

plt.xlabel("Erwartete Punkte")
plt.ylabel("")

# Punktzahl an Balken schreiben
for i, wert in enumerate(ergebnisse["Erwartete Punkte 26/27"]):

    plt.text(
        wert + 0.3,
        i,
        f"{wert:.1f}",
        va="center",
        fontsize=10
    )

plt.grid(axis="x", alpha=0.3)

plt.show()
