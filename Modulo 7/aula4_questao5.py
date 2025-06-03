# Abrir (ou criar) o arquivo CSV para escrita
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escrevendo o cabeçalho da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrevendo os dados dos livros
    arquivo.write("1984,George Orwell,1949,328\n")
    arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
    arquivo.write("O Senhor dos Anéis,J.R.R. Tolkien,1954,1178\n")
    arquivo.write("Cem Anos de Solidão,Gabriel García Márquez,1967,417\n")
    arquivo.write("A Revolução dos Bichos,George Orwell,1945,112\n")
    arquivo.write("Ensaio sobre a Cegueira,José Saramago,1995,312\n")
    arquivo.write("O Nome do Vento,Patrick Rothfuss,2007,662\n")
    arquivo.write("Grande Sertão: Veredas,João Guimarães Rosa,1956,624\n")
    arquivo.write("Orgulho e Preconceito,Jane Austen,1813,279\n")
    arquivo.write("O Apanhador no Campo de Centeio,J.D. Salinger,1951,277\n")

print("Arquivo CSV 'meus_livros.csv' criado com sucesso.")
