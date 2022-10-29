from constraint import Problem, AllDifferentConstraint

australia = Problem()
#Adicionar as variáveis
australia.addVariables(['wa', 'nt', 'sa', 'q', 'nsw', 'v', 't'], ['vermelho', 'verde', 'azul'])
#Restrições
#australia.addConstraint(lambda x, y: x != y,['wa', 'nt'])
australia.addConstraint(AllDifferentConstraint(),['sa', 'wa'])
australia.addConstraint(AllDifferentConstraint(),['sa', 'nt'])
australia.addConstraint(AllDifferentConstraint(),['sa', 'q'])
australia.addConstraint(AllDifferentConstraint(),['sa', 'nsw'])
australia.addConstraint(AllDifferentConstraint(),['sa', 'v'])
australia.addConstraint(AllDifferentConstraint(),['nt', 'wa'])
australia.addConstraint(AllDifferentConstraint(),['nt', 'q'])
australia.addConstraint(AllDifferentConstraint(),['q', 'nsw'])
australia.addConstraint(AllDifferentConstraint(),['nsw', 'v'])
s = australia.getSolutions()
print(len(s))
print(s)

s = australia.getSolution()
print(s)