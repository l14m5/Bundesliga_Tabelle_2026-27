# Trainings- und Testdaten erstellen

# Trainingsdaten:
# Saison 16/17 bis 23/24
train = df_train[
    df_train["Saison"] != "Tabelle 24 25"
]

# Testdaten:
# Saison 24/25

test = df_train[
    df_train["Saison"] == "Tabelle 24 25"
]

X_train = train[features]
y_train = train["Zielpunkte"]

X_test = test[features]
y_test = test["Zielpunkte"]

print("Trainingsdaten:", X_train.shape)
print("Testdaten:", X_test.shape)


# Random Forest trainieren

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


# Modell bewerten

from sklearn.metrics import mean_absolute_error, r2_score

test_vorhersage = modell.predict(X_test)

mae = mean_absolute_error(y_test, test_vorhersage)
r2 = r2_score(y_test, test_vorhersage)

print(f"MAE: {mae:.2f} Punkte")
print(f"R²: {r2:.3f}")


# Feature Wichtigkeit

importance = pd.DataFrame({
    "Feature": features,
    "Wichtigkeit": modell.feature_importances_
})

importance = importance.sort_values(
    "Wichtigkeit",
    ascending=False
)

display(importance)

# Ausgeben, wie viele Teams im Datensatz fehlen
print(df_train["Saison"].value_counts().sort_index())

