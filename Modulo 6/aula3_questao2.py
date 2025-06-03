# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Usando fatiamento para extrair o nome principal dos domínios
dominios = [url[4:-4] for url in urls]

# Resultado
print(dominios)
