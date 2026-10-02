#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Qual é o salário do funcionário? R$ '))
novo = salário + (salário * 0.15)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salário,novo))