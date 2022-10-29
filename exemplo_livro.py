from constraint import Problem
questao = Problem()
questao.addVariables(['Joe', 'Mary', 'Sue'], [0,15,16])
questao.addConstraint(lambda x, y, z : (x == z or y== z) and x!=y)
s = questao.getSolution()
print(s)

