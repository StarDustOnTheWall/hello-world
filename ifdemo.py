

import pulp as pp

prob = pp.LpProblem('test', pp.LpMaximize)
x = pp.LpVariable('x', lowBound=0, cat=pp.LpInteger)
y = pp.LpVariable('y', lowBound=0, cat=pp.LpInteger)
z = pp.LpVariable('z', lowBound=0, cat=pp.LpInteger)
objective = 1000*x+2000*y+3000*z
constraints = [x+2*y+3*z <= 10, y+2*z <= 5]
prob += objective
for cons in constraints:
    prob += cons
status = prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)



