#Faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f}m².'.format(largura,altura, área))
tinta = área / 2
print('Para pintar a parede, você precisará de {:.2f}litros de tinta.'.format(tinta))