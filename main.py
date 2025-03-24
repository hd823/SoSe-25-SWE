from datetime import datetime
from my_functions import estimate_max_hr, build_person, build_experiment


if __name__ == "__main__":
    try:
        experiment_name = input("Bitte geben Sie den Namen des Experiments ein: ")
        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        supervisor = input("Bitte geben Sie den Namen des Betreuers ein: ")
        first_name = input("Bitte geben Sie den Vornamen des Probanden ein: ")
        last_name = input("Bitte geben Sie den Nachnamen des Probanden ein: ")
        sex = input("Bitte geben Sie das Geschlecht des Probanden ein: ")
        age = int(input("Bitte geben Sie das Alter des Probanden ein: "))
        experiment = build_experiment(experiment_name, date, supervisor, build_person(first_name, last_name, sex, age))
        print(experiment)
    except ValueError:
        print("Fehler mit der Eingabe.")
