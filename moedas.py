# 100 moedas devem somar R$5.00
valores = [0.01, 0.05, 0.10, 0.50, 1.00]
from constraint import ExactSumConstraint, Problem

#Variáveis
moeda = ['1c', '5c', '10c', '50c', '1r']
#Domínio

soma= 5
moedas = Problem()
moedas.addVariable(moeda[0], range(0,101))
moedas.addVariable(moeda[1], range(0,101))
moedas.addVariable(moeda[2], range(0,51))
moedas.addVariable(moeda[3], range(0,11))
moedas.addVariable(moeda[4], range(0,6))
moedas.addConstraint(ExactSumConstraint(100))
moedas.addConstraint(ExactSumConstraint(soma, valores), moeda)

s= moedas.getSolution()
print(s)



#Restrições