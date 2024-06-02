#Entrada:
#Digite o nome do produto 1: calça
#Digite o preço unitário do produto 1: 199.90
#Digite a quantidade do produto 1: 3
#Digite o nome do produto 2: camisa
#Digite o preço unitário do produto 2: 49.95
#Digite a quantidade do produto 2: 10
#Digite o nome do produto 3: cinto
#Digite o preço unitário do produto 3: 25
#Digite a quantidade do produto 3: 3
#Saída:
#Total: R$1,174.20

produto1= input("Digite o nome do produto 1:")
preço1=float(input("Digite o preço unitário do produto 1:"))
quantidade1=int(input("Digite a quantidade do produto 1:"))

produto2= input("Digite o nome do produto 2:")
preço2=float(input("Digite o preço unitário do produto 2:"))
quantidade2=int(input("Digite a quantidade do produto 2:"))

produto3= input("Digite o nome do produto3:")
preço3=float(input("Digite o preço unitário do produto 3:"))
quantidade3=int(input("Digite a quantidade do produto 3:"))

total = (preço1*quantidade1)+(preço2*quantidade2)+(preço3*quantidade3)
print(f'total:R${total:,.2f}')