# Escreva um programa que leia um valor em metros e o exiba convertido em dm e cm.
medida = float(input('Uma distância em metros: '))
dm = medida * 10
cm = medida * 100
print('A medida de {}m corresponde a {:.0f}dm e {:.0f}mm'.format(medida, dm, cm))