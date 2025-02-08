from pulp import LpProblem, LpVariable, LpMinimize, lpSum


prob = LpProblem("SchedulingProblem", LpMinimize) # Stawki godzinowe dla wybranych osób
stawka = {
    "Ania": 100,
    "Stefan": 50,
    "Hektor": 60,
    "Olaf": 40,
    "Lidia": 110,
    "Piotr": 70
}

days = ["pon", "wto", "sro", "czw", "pt"] # Dni pracujące
#Kiedy może pracować?
dayav = {
    "Ania": ["pon", "wto", "sro", "czw", "pt"],
    "Stefan": ["pon"],
    "Hektor": ["pon", "wto", "sro"],
    "Olaf": ["pon", "wto", "sro", "czw", "pt"],
    "Lidia": ["czw", "pt"],
    "Piotr": ["pon", "wto", "sro"]
}

#Ilu pracowników danego dnia
xpracow = {
    "pon": 2,
    "wto": 1,
    "sro": 1,
    "czw": 1,
    "pt": 3
}

#Zmienna decyzyjna: Czy dany pracownik pracuje danego dnia: 1 - tak, 0 - nie
work_vars = {
    (person, day): LpVariable(f"{person}_{day}", cat="Binary")
    for person in stawka for day in days
}

#Cel: minimalizacja kosztu zatrudnienia pracowników
prob += lpSum(work_vars[person, day] * stawka[person] for person in stawka for day in days)

#Ograniczenie1: pracownik może pracować maks 3 dni w tygodniu
for person in stawka:
    prob += lpSum(work_vars[person, day] for day in days) <= 3

#Ograniczenie2: wymagana liczba pracowników w każdy dzień
for day in days:
    prob += lpSum(work_vars[person, day] for person in stawka if day in dayav[person]) == xpracow[day]

prob.solve()
print("Optymalne rozwiązanie:")
for person in stawka:
    for day in days:
        if work_vars[person, day].value() == 1:
            print(f"{person} pracuje w {day}")
print(f"\nCałkowity koszt: {prob.objective.value()} zł")
