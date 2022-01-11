

import pulp as pp

prob = pp.LpProblem('test', pp.LpMaximize)
x_1 = pp.LpVariable('x', lowBound=0, cat=pp.LpInteger)
x_2 = pp.LpVariable('y', lowBound=0, cat=pp.LpInteger)
x_3 = pp.LpVariable('z', lowBound=0, cat=pp.LpInteger)
objective = x_1 + x_2 + x_3
constraints = [5*x_1 >= 25, 2*x_2 >= 20, 2*x_3>=18]
prob += objective
for cons in constraints:
    prob += cons
solver = pp.PULP_CBC_CMD()
solver.msg = False
status = prob.solve(solver)
# for v in prob.variables():
#     print(v.name, "=", v.varValue)
# for c in prob.constraints:
#     print(prob.constraints[c].pi)
print(prob.objective.value())




