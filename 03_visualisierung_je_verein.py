# Vereinsfarben

vereinsfarben = {

    # Rot
    "1.FC Union Berlin": "red",
    "FC Bayern Muenchen": "red",
    "FC Augsburg": "red",
    "Eintracht Frankfurt": "red",
    "1.FC Koeln": "red",
    "RB Leipzig": "red",
    "Bayer 04 Leverkusen": "red",
    "1.FSV Mainz 05": "red",
    "VfB Stuttgart": "red",

    # Grün
    "Borussia Moenchengladbach": "forestgreen",
    "SV Werder Bremen": "forestgreen",

    # Gelb
    "Borussia Dortmund": "gold",

    # Blau
    "FC Schalke 04": "royalblue",
    "Hamburger SV": "royalblue",
    "TSG Hoffenheim": "royalblue",
    "SC Paderborn 07": "royalblue",

    # Schwarz
    "SV Elversberg": "black",
    "Sport-Club Freiburg": "black"
}


# Platzverteilung je Verein

import matplotlib.pyplot as plt

# Verein auswählen - Borussia Moenchengladbach
verein = "Borussia Moenchengladbach"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()


# Verein auswählen - 1.FC Union Berlin
verein = "1.FC Union Berlin"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()


# Verein auswählen - FC Schalke 04
verein = "FC Schalke 04"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()


# Verein auswählen - SC Freiburg
verein = "Sport-Club Freiburg"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()


# Verein auswählen - SV Werder Bremen
verein = "SV Werder Bremen"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()


# Verein auswählen - VfB Stuttgart
verein = "VfB Stuttgart"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()


# Verein auswählen - SV Elversberg
verein = "SV Elversberg"

# Farbe
farbe = vereinsfarben.get(verein, "gray")

# Daten auswählen
team = alle_simulationen[
    alle_simulationen["Verein"] == verein
]

platz = (
    team["Simulierter Platz"]
        .value_counts()
        .sort_index()
        / anzahl_simulationen
        * 100
)

platz = platz.reindex(range(1,19), fill_value=0)

# Grafik
plt.figure(figsize=(12,5))

plt.bar(
    platz.index,
    platz.values,
    color=farbe,
    edgecolor="black"
)

plt.xticks(range(1,19))

plt.xlabel("Tabellenplatz")
plt.ylabel("Wahrscheinlichkeit (%)")

plt.title(
    f"Platzwahrscheinlichkeiten {verein}"
)

plt.grid(axis="y", alpha=0.3)

plt.show()
