# Solicita uma quantidade indefinida de números inteiros com pelo menos 4 valores
numeros = []

print("Digite pelo menos 4 números inteiros. Digite 'fim' para encerrar.")

while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    
    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números!")
            continue
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

# Exibindo as informações solicitadas usando fatiamento
print("\nLista original:           ", numeros)
print("3 primeiros elementos:     ", numeros[:3])
print("2 últimos elementos:       ", numeros[-2:])
print("Lista invertida:           ", numeros[::-1])
print("Elementos de índice par:   ", numeros[0::2])
print("Elementos de índice ímpar: ", numeros[1::2])
