distancia = int (input("Digite a distancia em km "))
peso = float (input ("Digite o peso do pacote em"))
if distancia <= 100:
    frete = 1
elif distancia >= 101 and distancia <= 300:
    frete = 1.5   
else:
    frete = 2

if peso > 10:
    print(f"O valor do frete será {(peso*frete)+10} reais")
else:
    print(f"O valor do frete será {peso8frete} reais")    