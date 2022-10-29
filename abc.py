# Qual o menor valor para:
#
#        ABC
#      -------
#       A+B+C
# 
#Ex.: A= 2, B =5 , c = 3
#       253/(2+5+3)
from constraint import Problem

abc = Problem()
abc.addVariables(['a','b','c'], range(10) )
solucao = {}
menor_valor = 9999
contador = 0
abc.addConstraint(lambda x,y,z: x != 0)
for s in abc.getSolutions():
    a = s['a']
    b = s['b']
    c = s['c']
    conta = (a * 100 + b * 10 + c) / (a+b+c)
    if conta < menor_valor:
        menor_valor = conta
        solucao = s

print(menor_valor)
print(solucao)