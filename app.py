numero = int(input("pasame un numero:  "))


cont = 1
for i in range(numero):
    if numero % i == 0:
        cont +=1

if cont == 2:
    print("el numero", numero, " es primo")