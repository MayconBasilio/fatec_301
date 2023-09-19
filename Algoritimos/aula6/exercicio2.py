valorCompra = float(input("Qual foi o valor da compra: "))

a = valorCompra - ((valorCompra*10)/100)
b = valorCompra - ((valorCompra*20)/100)
c = valorCompra - ((valorCompra*30)/100)

if valorCompra <= 1000.0:
    print(f'Você recebeu um desconto de 10%, sua compra ficou R${a}')
elif valorCompra <= 5000.0:
    print(f'Você recebeu um desconto de 20%, sua compra ficou R${b}')
else:
    print(f'Você recebeu um desconto de 30%, sua compra ficou R${c}')
