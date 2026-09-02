import csv

arquivo_entrada = "sorteios.csv"
arquivo_saida = "sorteios_validos.csv"

with open(arquivo_entrada, "r", newline="") as arquivo:
    leitor = csv.reader(arquivo)

    with open(arquivo_saida, "w", newline="") as arquivo_final:
        escritor = csv.writer(arquivo_final)

        for linha in leitor:

            # A primeira posição é o ID
            identificador = linha[0]

            # Tudo depois do ID são os números
            numeros = linha[1:]

            # Verifica se a quantidade de números está entre 6 e 15
            if 6 <= len(numeros) <= 15:
                escritor.writerow([identificador] + numeros)

print("Validação concluída!")
print("Arquivo criado:", arquivo_saida)