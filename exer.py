# Definindo as listas para armazenar os números
numeros = []
pares = []
impares = []

# Lendo os 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

    # Verificando se o número é par ou ímpar e armazenando na lista apropriada
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Imprimindo os três vetores
print("Todos os números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
