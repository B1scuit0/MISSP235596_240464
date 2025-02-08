from pulp import *

def blending(ingredients, costs, macros, constraints):
    probvar = LpProblem("Blending", LpMinimize)
    # var dicitionary 
    ingredient_var = {ingredient: LpVariable(f"{ingredient}_Percentage", lowBound=0) for ingredient in ingredients}
    # cost constraint (zmienna decyzyjna)
    probvar += lpSum(costs[i] * ingredient_var[ingredient] for i, ingredient in enumerate(ingredients))
    # sum constraint (x1+xn==100%) 
    probvar += lpSum(ingredient_var[ingredient] for ingredient in ingredients) == 100
    # macro constraint loop 
    for macro, macro_val in macros.items():
            macro_sum = lpSum(macro_val[i] * ingredient_var[ingredient] for i, ingredient in enumerate(ingredients))
            if "min" in constraints[macro]:
                probvar += macro_sum >= constraints[macro]
            if "max" in constraints[macro]:
                probvar += macro_sum <= constraints[macro]
    # solve 
    probvar.solve()
    # priny solution 
    print("Status:", LpStatus[probvar.status]) #“Not Solved”, “Infeasible”, “Unbounded”, “Undefined” or “Optimal”.
    for v in probvar.variables():
        print(f"{v.name}: {v.varValue}%") 
    print(f"cost/can: {value(probvar.objective)}$")


#####:            
ingredients = ["Chicken", "Beef", "Mutton", "Rice", "Wheat", "Gel", "Sardines"] 
costs =       [0.013, 0.008, 0.010, 0.003, 0.005, 0.002, 0.002]
# macro_val table
macros = {       
    "witB": [0.3, 0.6, 1.6, 1.2, 1.0, 0.0, 2.9],
    "salt": [0.4, 0.11, 1.0, 0.1, 1.0, 3.0, 0.1]
}                                                       # n*macros -> n*constrains
# manual macro constraints ("min"/"max")
constraints = {
    "witB":    {"min": 5},
    "salt":    {"max": 4}
}

# main fnction call
blending(ingredients, costs, macros, constraints)