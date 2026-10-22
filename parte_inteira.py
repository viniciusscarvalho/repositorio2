# Programa que mostre a parte inteira de um valor decimal
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, math.trunc(num)))
