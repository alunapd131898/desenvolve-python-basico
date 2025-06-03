# Lista com os nomes dos meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita a data de nascimento
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separa os valores em dia, mês e ano
dia, mes, ano = data.split('/')

# Converte o mês para inteiro e busca o nome correspondente
mes_extenso = meses[int(mes) - 1]

# Exibe o resultado
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
