import csv
import random
import string
import sys

# Verifica se a quantidade de linhas foi informada
if len(sys.argv) != 2:
    print("Uso: python sorteios.py <quantidade_de_linhas>")
    sys.exit(1)

# Converte o argumento para inteiro
quantidade = int(sys.argv[1])

# Caracteres usados no identificador
caracteres = string.ascii_uppercase + string.digits

# Cria o arquivo CSV
with open("sorteios.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    # Gera a quantidade exata de linhas informada
    for i in range(quantidade):
        # Sorteia 6 números entre 1 e 60, sem repetição
        numeros = random.sample(range(1, 61), 6)

        # Cria um código com 6 caracteres
        codigo = ''.join(random.choices(caracteres, k=6))

        # Cria o identificador
        identificador = "AP-" + codigo

        # Grava a linha no CSV
        escritor.writerow([identificador] + numeros)

print(f"{quantidade} linhas geradas com sucesso!")