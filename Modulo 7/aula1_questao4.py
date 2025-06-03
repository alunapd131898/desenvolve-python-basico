# Solicita o número do usuário
numero = input("Digite o número: ")

# Verifica o comprimento e ajusta conforme necessário
if len(numero) == 8:
    numero = '9' + numero
elif len(numero) == 9:
    if numero[0] != '9':
        print("Número inválido: um número de 9 dígitos deve começar com 9.")
    # Neste caso, não precisamos alterar nada
else:
    print("Número inválido: deve ter 8 ou 9 dígitos.")
    exit()

# Adiciona o separador "-" no formato XXXXX-XXXX
numero_formatado = numero[:5] + '-' + numero[5:]

# Imprime o número completo
print("Número completo:", numero_formatado)
