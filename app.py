numero = int(input("pasame un numero:  "))


cont = 1
for i in range(1, numero+1):
    if numero % i == 0:
        cont +=1

if cont == 2:
    print("el numero", numero, " es primo")
else:
    print("el numero NO es primo")