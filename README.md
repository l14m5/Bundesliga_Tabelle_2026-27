# Bundesliga_Tabelle_2026-27
Dieses Projekt erstellt eine Prognose für die Bundesliga-Saison 2026/27 mithilfe eines Machine Learning Modells.

Auf Basis historischer Bundesliga-Tabellen, Vereinsdaten und Leistungskennzahlen aus den letzten 10 Jahren wird ein Random-Forest-Modell trainiert. Anschließend werden erwartete Punkte, Tabellenplätze und Wahrscheinlichkeiten für Meisterschaft, Champions League, Europa League, Conference League, Relegation und Abstieg berechnet.

## Projektziel
Ziel des Projekts ist es, eine datenbasierte Bundesliga-Prognose zu erstellen, um die Bundesliga Saison 2026/27 vorherzusagen. Dafür werden vergangene Saisons analysiert und ein Machine-Learning-Modell trainiert.

## Funktionen
- Einlesen von 10 Bundesliga-Saisons aus einer Excel-Datei
- Zusammenführen der Daten zu einem Gesamtdatensatz
- Berechnung von zusätzlichen Features wie Bundesliga-Erfahrung und Ligafaktor
- Training eines Random-Forest-Regressionsmodells
- Bewertung des Modells mit MAE und R²
- Prognose der erwarteten Punkte für die Saison 2026/27
- Monte-Carlo-Simulation mit 1000 Durchläufen
- Berechnung von Wahrscheinlichkeiten für: Meisterschaft, Champions League, Europa League, Conference League, Relegation und Abstieg
- Visualisierung der Ergebnisse mit Diagrammen

## Verwendete Technologien
- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- openpyxl

## Nutzung
Die Excel-Datei muss im Ordner data/ liegen. Anschließend kann das Skript ausgeführt werden

Sollte Google Colab verwendet werden, dann muss zuerst der Ordner data angelegt werden und das Dokument dort hochgeladen werden. Siehe Schritt 00_nur_fuer_google_colab.

## Datengrundlage
Die Daten stammen aus einer Excel-Datei mit mehreren Tabellenblättern. Jedes Tabellenblatt enthält Daten zu einer Bundesliga-Saison, mit Angaben zu Platzierung, Punkte, Tore, Gegentore, Marktwert, Kadergröße, Transfers, Trainerwechsel und Aufsteiger.

## Modell
Für die Vorhersage wird ein RandomForestRegressor verwendet. 
Das Modell lernt aus vergangenen Saisons und sagt die Zielpunkte der folgenden Saison vorher. Die Modellqualität wird mit folgenden Kennzahlen bewertet:
- MAE: durchschnittliche Abweichung in Punkten
- R²: Anteil der erklärten Varianz durch das Modell

## Ergebnis
Das Projekt gibt eine prognostizierte Bundesliga-Tabelle für die Saison 2026/27 aus. Zusätzlich werden Wahrscheinlichkeiten für verschiedene Saisonziele berechnet.

## Hinweis
Dieses Projekt dient zu Lern- und Analysezwecken. Die Ergebnisse sind statistische Prognosen und keine sicheren Vorhersagen.
