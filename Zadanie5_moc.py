import pulp

# Define the prob
prob = pulp.LpProblem("Minimize_Power_Dissipation", pulp.LpMinimize)

I_zn = [4, 2, 2, 2, 4]


I1 = pulp.LpVariable("I1", 3, upBound=5)
I2 = pulp.LpVariable("I2", 1, upBound=3)
I3 = pulp.LpVariable("I3", 1, upBound=3)
I4 = pulp.LpVariable("I4", 1, upBound=3)
I5 = pulp.LpVariable("I5", 3, upBound=5)

U = [6, 10, 4, 7, 3]
delta_I = 1

prob += U[0] * I1 + U[1] * I2 + U[2] * I3 + U[3] * I4 + U[4] * I5, "Moc rozpr"

prob += I1 >= I_zn[0] - delta_I
prob += I1 <= I_zn[0] + delta_I
prob += I2 >= I_zn[1] - delta_I
prob += I2 <= I_zn[1] + delta_I
prob += I3 >= I_zn[2] - delta_I
prob += I3 <= I_zn[2] + delta_I
prob += I4 >= I_zn[3] - delta_I
prob += I4 <= I_zn[3] + delta_I
prob += I5 >= I_zn[4] - delta_I
prob += I5 <= I_zn[4] + delta_I

prob.solve()

print("Minimalna moc rozproszona:", pulp.value(prob.objective), "mW")
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue} mA")
