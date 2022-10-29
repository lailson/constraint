#Resolver o problema de agendamento de horario das aulas dos professores

#Problema de satisfaçÃo de restrição 
#Variaveis
#domínio
#restrições


#Problema1
#a e b [1,2,3]
from constraint import Problem
problema1 = Problem()
problema1.addVariable('a', [1,2,3,4,5,6])
problema1.addVariable('b', [1,2,3,4,5,6])
problema1.addConstraint(lambda a,b: a!=b )
s = problema1.getSolutions()
print(len(s))
print(s)


