a = list()
b = list()
for i in range(6):
    valor = int(input())
    if (valor < 0): b.append(valor)
    else:a.append(valor)
print("Valores Positivos: ",a )
print("Valores Negativos: ",b)
