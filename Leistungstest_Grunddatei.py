# import numpy as np
# import datetime as date

# first_experiment_id: int = 100
# versuchsleitung: str = "Doell"
# datum: str = "2025.03.11"
# anzahl_an_proben : int = 10
# anzahl_an_geraden_proben : int = 0

# erste_Experiment_Reihe : dict = {}

# id_nummer : np.array = np.arange(first_experiment_id, first_experiment_id + anzahl_an_proben)

# try:
#   for id in id_nummer:
#     erste_Experiment_Reihe.update({str(id) : {"Erstelldatum" : datum, "Versuchsleitung" : versuchsleitung, "Power" : np.random.standard_normal(720) * 25 + 250}})

#   id = first_experiment_id

#   for id in range(first_experiment_id, first_experiment_id + int(anzahl_an_proben/2)):
#     print(erste_Experiment_Reihe[str(id)])

#   for is_id_even_help in range(first_experiment_id, first_experiment_id + anzahl_an_proben):
#     if is_id_even_help % 2 == 0:
#       anzahl_an_geraden_proben += 1
#   print(anzahl_an_geraden_proben)
# except TypeError:
#   print("Mindestens ein Eingabewert hat nicht den richtigen Datentyp")
# finally:
#   pass
