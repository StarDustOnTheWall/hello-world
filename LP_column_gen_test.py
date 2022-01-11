import random
import pulp as pp
import pandas as pd


class MasterProblem:
    def __init__(self, object_vector, constrain_matrix, constrain_parameter, non_to_basic_matrix,
                 non_to_basic_parameter, problem_name='prob'):
        self.object_vector = object_vector
        self.constrain_matrix = constrain_matrix
        self.prob = None
        self.problem_name = problem_name
        self.constrain_parameter = constrain_parameter
        self.patterns = []
        self.non_to_basic_constrain = non_to_basic_matrix
        self.non_to_basic_parameter = non_to_basic_parameter
        self.reduced_cost = []
        self.result = None

    def parameter_check(self):
        parameter_check = True
        if len(self.constrain_matrix) != len(self.constrain_parameter) or \
                len(self.constrain_parameter) != len(self.non_to_basic_constrain):
            print('parameter not right')
            parameter_check = False
        for row in range(len(self.constrain_matrix)):
            if len(self.constrain_matrix[row]) != len(self.object_vector):
                print('parameter not right')
                parameter_check = False
        return parameter_check

    def set_initial(self):
        for i in range(len(self.constrain_parameter)):
            temp = [0.0 for j in range(i)]
            temp.append(1.0)
            temp += [0.0 for k in range(len(self.object_vector) - i - 1)]
            self.patterns.append(temp)

    def solve_mp(self):
        x = [pp.LpVariable('x_' + str(k), lowBound=0, cat=pp.LpInteger) for k in range(len(self.object_vector))]
        objective = sum(x[p] * self.object_vector[p] for p in range(len(x)))
        self.prob = pp.LpProblem(self.problem_name, pp.LpMaximize)
        self.prob += objective
        for i in range(len(self.constrain_parameter)):
            self.prob += sum(self.constrain_matrix[i][j] * x[j] for j in range(len(x))) <= self.constrain_parameter[i]
        solver = pp.PULP_CBC_CMD()
        solver.msg = False
        status = self.prob.solve(solver)
        return [self.prob.constraints[i].pi for i in self.prob.constraints]

    def solve_dual_problem(self, dual, object_parameter):
        dual_prob = pp.LpProblem('dual_prob', pp.LpMinimize)
        a = [pp.LpVariable('a_' + str(k), lowBound=0, cat=pp.LpInteger) for k in range(len(dual))]
        dual_obj = object_parameter - sum(a[p] * dual[p] for p in range(len(dual)))
        dual_prob += dual_obj
        dual_prob += sum(self.non_to_basic_constrain[j] * a[q] for q in range(len(a))) <= self.non_to_basic_parameter
        solver = pp.PULP_CBC_CMD()
        solver.msg = False
        status = dual_prob.solve(solver)
        return dual_prob.objective.value(), dual_prob

    def run(self):
        if not self.parameter_check():
            print('parameter not right')
            return None
        self.set_initial()
        while True:
            dual = self.solve_mp()
            self.reduced_cost = []
            for obj in self.object_vector:
                reduced_cost_value, dual_result = self.solve_dual_problem(dual, obj)
                if not pd.isnull(reduced_cost_value):
                    self.reduced_cost.append((self.solve_dual_problem(dual, obj)))
            if len(self.reduced_cost) > 0:
                self.reduced_cost.sort(key=lambda x: x[0])
                if self.reduced_cost[0][0] < 0:
                    choose_dual = self.reduced_cost[0][1]
                    for m in range(len(self.constrain_parameter)):
                        self.constrain_matrix[m].append(choose_dual.variables()[m].varValue)
                    self.object_vector.append(1)
                else:
                    self.result = self.prob
                    break
            else:
                self.result = self.prob
                break


if __name__ == '__main__':
    row = 3
    column = 10
    object_test = []
    constrain_mat = []
    constrain = []
    non_to_basic = []
    non_to_basic_con = random.randint(10000, 100000)
    for i in range(row):
        object_test.append(random.randint(1, 10))
    for j in range(column):
        constrain.append(random.randint(10000, 100000))
        non_to_basic.append(random.randint(1, 10))
        one_constrain = []
        for i in range(row):
            one_constrain.append(random.randint(1, 10))
        constrain_mat.append(one_constrain)
    test = MasterProblem(object_test, constrain_mat, constrain, non_to_basic, non_to_basic_con)
    result = test.run()