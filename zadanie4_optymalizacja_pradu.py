from pulp import LpMaximize, LpProblem, LpVariable, lpSum
# Wartości rezystancji
R1 = 8
R2 = 6 
R3 = 4
R4 = 10
R5 = 8

# Maksymalny prąd jaki może płynąć dla poszczególnych rezystorów
I1_max = 2
I2_max = 3
I3_max = 4
I4_max = 2
I5_max = 2

#Zmienne decyzyjne dla prądów płynących przez rezystory
prob = LpProblem("Maximize_Current", LpMaximize)

I1 = LpVariable("I1", 0, upBound=I1_max)
I2 = LpVariable("I2", 0, upBound=I2_max) 
I3 = LpVariable("I3", 0, upBound=I3_max)
I4 = LpVariable("I4", 0, upBound=I4_max)
I5 = LpVariable("I5", 0, upBound=I5_max)

prob += I3

#Ograniczenie: Wynikające z praw Kirchhoffa, I3 to suma prądów I1 i I2
prob += I1 + I2 == I3

#Ograniczenie: I3 rozdziela się na I4 i I5
prob += I3 == I4 + I5

#Ograniczenie: Wynikające z praw Kirchhoffa, czyli spadek napięcia na R1 jest równy spadkowi napięcia na R2
prob += R1 * I1 == R2 * I2

#Ograniczenie: Wynikające z praw Kirchhoffa, czyli spadek napięcia na R4 jest równy spadkowi napięcia na R5
prob += R4 * I4 == R5 * I5

# Rozwiązanie problemu
prob.solve()

#Wyświetlanie rozwiązania 
results = {
    "I1": I1.value(),
    "I2": I2.value(), 
    "I3": I3.value(),
    "I4": I4.value(),
    "I5": I5.value()
}
print(results)