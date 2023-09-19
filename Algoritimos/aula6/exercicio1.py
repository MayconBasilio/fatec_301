a = float(input("Insira um número: "))
x = a / 5
y = a / 3
b = x % 5
c = y % 3
print(c)
print(b)

if  b == 0.0 and c == 0.0:
    print ("Resto 0")
else:
    print("Não divisivel")
