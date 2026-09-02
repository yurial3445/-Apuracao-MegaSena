import csv
import random
import string

caracteres = string.ascii_uppercase + string.digits

with open("sorteios.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for i in range(10):
        numeros = random.sample(range(1, 61), 6)

        codigo = ''.join(random.choices(caracteres, k=6))

        identificador = "AP-" + codigo

        escritor.writerow([identificador] + numeros)