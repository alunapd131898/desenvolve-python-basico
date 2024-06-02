# Dados
compr = int(input("Digite o comprimento:"))
largura =int(input("Digite a largura:"))
preço_m2 = float(input("Valor do m2: "))

area = compr * largura #m
preco_total = area * preço_m2

print(f' O terreno POSSUI{area}m2 e custa R${preco_total:,.2}')