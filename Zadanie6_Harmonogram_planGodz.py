from pulp import LpProblem, LpVariable, LpMinimize, lpSum

# Problem minimalizacji kosztów
prob = LpProblem("SchedulingProblem", LpMinimize)

# Stawki godzinowe pracowników
stawka = {
    "Ania": 35,
    "Barbara": 100,
    "Krzys": 35,
    "Franek": 50,
}

# Maksymalna liczba godzin, jaką każdy pracownik może przepracować w tygodniu
max_godz = {
    "Ania": 30,
    "Barbara": None,  # Barbara nie ma ograniczonych liczby godzin
    "Krzys": 20,
    "Franek": 50,
}

# Funkcja sprawdzająca czy dany pracownik pracuje, czy nie
assign_vars = {person: LpVariable(f"{person}_assigned", cat="Binary") for person in stawka}

# Funkcja sprawdzająca ile godzin pracuje każdy pracownik
work_vars = {
    person: LpVariable(f"{person}_hours", lowBound=0, cat="Continuous")
    for person in stawka
}

# Ograniczenie dotyczące przepracowanych godzin
for person in stawka:
    if max_godz[person] is not None:  # Jeśli istnieje maksymalna liczba godzin
        prob += work_vars[person] <= max_godz[person] * assign_vars[person]
    else:
        # Dla Barbary, nie ma ograniczonych liczby godzin. 
        prob += work_vars[person] >= 0 

# Funkcja dotycząca minimalizacji kosztów
prob += lpSum(stawka[person] * work_vars[person] for person in stawka), "TotalCost"

# Ograniczenie dotyczące przepracowanych godzin 
prob += lpSum(work_vars[person] for person in stawka) == 120.5, "TotalHours"

# Funkcja rozwiązania problemu
prob.solve()

# Wyświetlanie zadania
print("Status:", prob.status)
for person in stawka:
    print(f"{person}: {work_vars[person].varValue} godzin ")
print("Koszt:", sum(stawka[person] * work_vars[person].varValue for person in stawka))
