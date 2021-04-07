import random
import pulp as pp


class MasterProblem:
    def __init__(self, object_vector, constrain_matrix, constrain_parameter, problem_name='prob'):
        self.object_vector = object_vector
        self.constrain_matrix = constrain_matrix
        self.prob = pp.LpProblem(problem_name, pp.LpMaximize)
        self.constrain_parameter = constrain_parameter
        self.patterns = []

    def parameter_check(self):
        parameter_check = True
        if len(self.constrain_matrix) != len(self.constrain_parameter):
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
        self.prob += objective
        for i in range(len(self.constrain_parameter)):
            self.prob += sum(self.constrain_matrix[i][j] * x[j] for j in range(len(x))) <= self.constrain_parameter[i]
        solver = pp.PULP_CBC_CMD()
        solver.msg = False
        status = self.prob.solve(solver)
        return [self.prob.constraints[i].pi for i in self.prob.constraints]

    def run(self):
        if not self.parameter_check():
            print('parameter not right')
            return None
        self.set_initial()
        dual = self.solve_mp()
        for v in self.prob.variables():
            print(v.name, "=", v.varValue)
        print([self.prob.constraints[i].pi for i in self.prob.constraints])


if __name__ == '__main__':
    row = 20
    column = 10
    object_test = []
    constrain_mat = []
    constrain = []
    for i in range(row):
        object_test.append(random.randint(1, 10))
    for j in range(column):
        constrain.append(random.randint(10000, 100000))
        one_constrain = []
        for i in range(row):
            one_constrain.append(random.randint(1, 10))
        constrain_mat.append(one_constrain)
    test = MasterProblem(object_test, constrain_mat, constrain)
    result = test.run()