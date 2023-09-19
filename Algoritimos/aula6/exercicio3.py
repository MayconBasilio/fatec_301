larguraQuarto = float(input("Insira a Largura do quarto: "))
comprimentoQuarto = float(input("Insira a Comprimento do quarto: "))
ladoA = (larguraQuarto * 2.80)*2
ladoB = (comprimentoQuarto * 2.80)*2
totalQuarto = (ladoA + ladoB) - (0.80*2.10)
print(f'O tamanho do quarto é {totalQuarto}')

recepienteTinta = int(input(f'Insira o tipo da tinta 1 (Litro), 2 (Galão), 3 (Lata): '))
lata = 18
galão = 3.6
litro = 1
litroMetro = litro * 3
galãoMetro = galão * 10.8
lataMetro = lata * 54

if recepienteTinta == 1:
    Z = litroMetro
elif recepienteTinta == 2:
    Z = galãoMetro
elif recepienteTinta == 3:
    Z = lataMetro
else:
    print("Valor Invalido")


quantidadeTinta = Z / totalQuarto
print(f'Ira de precisar de {quantidadeTinta} unidades ')