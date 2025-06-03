def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf_parcial, multiplicadores))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    # Remove pontos e hífen
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    
    # Verifica se o CPF tem 11 dígitos numéricos
    if not cpf_numeros.isdigit() or len(cpf_numeros) != 11:
        return False

    # Evita CPFs com todos os dígitos iguais, que são inválidos
    if cpf_numeros == cpf_numeros[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    primeiro_digito = calcular_digito(cpf_numeros[:9], range(10, 1, -1))

    # Calcula o segundo dígito verificador
    segundo_digito = calcular_digito(cpf_numeros[:9] + primeiro_digito, range(11, 1, -1))

    # Compara com os dígitos informados
    return cpf_numeros[-2:] == primeiro_digito + segundo_digito

# Solicita o CPF ao usuário
cpf_input = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# Valida e imprime o resultado
if validar_cpf(cpf_input):
    print("Válido")
else:
    print("Inválido")
