import csv
import os


# ========== FUNÇÕES DE ARQUIVO ==========
def carregar_usuarios():
    usuarios = []
    caminho = os.path.join(os.path.dirname(__file__), "usuarios.csv")
    try:
        with open(caminho, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                usuarios.append(linha)
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    return usuarios

def salvar_usuarios(usuarios):
    caminho = os.path.join(os.path.dirname(__file__), "usuarios.csv")

    with open(caminho, "w", newline='', encoding='utf-8') as f:
        campos = ["id", "nome", "senha", "nivel"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for u in usuarios:
            escritor.writerow(u)

def carregar_produtos():
    produtos = []
    caminho = os.path.join(os.path.dirname(__file__), "produtos.csv")
    try:
        
        with open(caminho, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                linha["preco"] = float(linha["preco"])
                produtos.append(linha)
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
    return produtos

def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline='', encoding='utf-8') as f:
        campos = ["id", "nome", "preco", "quantidade"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for p in produtos:
            escritor.writerow(p)

# ========== AUTENTICAÇÃO ==========
def login(usuarios):
    nome = input("Usuário: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print(f"Bem-vindo, {nome}!")
            return u
    print("Usuário ou senha inválidos.")
    return None

# ========== MENU PRINCIPAL ==========
def menu_gerente():
    print("\n--- MENU GERENTE ---")
    print("1. CRUD Usuários")
    print("2. CRUD Produtos")
    print("0. Sair")

def menu_funcionario():
    print("\n--- MENU FUNCIONÁRIO ---")
    print("1. Consultar Produtos")
    print("2. Atualizar Produto")
    print("0. Sair")

def menu_cliente():
    print("\n--- MENU CLIENTE ---")
    print("1. Ver Produtos")
    print("0. Sair")

# ========== CRUD USUÁRIOS ==========
def crud_usuarios(usuarios):
    while True:
        print("\nCRUD Usuários")
        print("1. Adicionar usuário (Create)")
        print("2. Listar usuários (Read)")
        print("3. Editar usuário (Update)")
        print("4. Remover usuário (Delete)")
        print("0. Voltar")
        op = input("Opção: ")

        if op == "1":
            novo = {
                "id": input("ID: "),
                "nome": input("Nome: "),
                "senha": input("Senha: "),
                "nivel": input("Nível (gerente/funcionario/cliente): ")
            }
            usuarios.append(novo)
            salvar_usuarios(usuarios)
            print("Usuário adicionado.")

        elif op == "2":
            for u in usuarios:
                print(u)

        elif op == "3":
            id_edit = input("ID do usuário a editar: ")
            for u in usuarios:
                if u["id"] == id_edit:
                    u["nome"] = input("Novo nome: ")
                    u["nivel"] = input("Novo nível: ")
                    salvar_usuarios(usuarios)
                    print("Usuário atualizado.")
                    break

        elif op == "4":
            id_del = input("ID do usuário a remover: ")
            usuarios = [u for u in usuarios if u["id"] != id_del]
            salvar_usuarios(usuarios)
            print("Usuário removido.")

        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== CRUD PRODUTOS ==========
def crud_produtos(produtos):
    while True:
        print("\nCRUD Produtos")
        print("1. Adicionar produto (Create)")
        print("2. Listar produtos (Read)")
        print("3. Editar produto (Update)")
        print("4. Remover produto (Delete)")
        print("5. Buscar por nome")
        print("6. Ordenar por nome")
        print("7. Ordenar por preço")
        print("0. Voltar")
        op = input("Opção: ")

        if op == "1":
            novo = {
                "id": input("ID: "),
                "nome": input("Nome: "),
                "preco": float(input("Preço: ")),
                "quantidade": input("Quantidade: ")
            }
            produtos.append(novo)
            salvar_produtos(produtos)
            print("Produto adicionado.")

        elif op == "2":
            for p in produtos:
                print(p)

        elif op == "3":
            id_edit = input("ID do produto a editar: ")
            for p in produtos:
                if p["id"] == id_edit:
                    p["nome"] = input("Novo nome: ")
                    p["preco"] = float(input("Novo preço: "))
                    p["quantidade"] = input("Nova quantidade: ")
                    salvar_produtos(produtos)
                    print("Produto atualizado.")
                    break

        elif op == "4":
            id_del = input("ID do produto a remover: ")
            produtos = [p for p in produtos if p["id"] != id_del]
            salvar_produtos(produtos)
            print("Produto removido.")

        elif op == "5":
            termo = input("Buscar por nome: ").lower()
            encontrados = [p for p in produtos if termo in p["nome"].lower()]
            for p in encontrados:
                print(p)

        elif op == "6":
            ordenados = sorted(produtos, key=lambda x: x["nome"].lower())
            for p in ordenados:
                print(p)

        elif op == "7":
            ordenados = sorted(produtos, key=lambda x: x["preco"])
            for p in ordenados:
                print(p)

        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== SISTEMA ==========
def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()
    usuario = login(usuarios)
    if not usuario:
        return

    while True:
        if usuario["nivel"] == "gerente":
            menu_gerente()
            escolha = input("Escolha: ")
            if escolha == "1":
                crud_usuarios(usuarios)
            elif escolha == "2":
                crud_produtos(produtos)
            elif escolha == "0":
                break

        elif usuario["nivel"] == "funcionario":
            menu_funcionario()
            escolha = input("Escolha: ")
            if escolha == "1":
                for p in produtos:
                    print(p)
            elif escolha == "2":
                crud_produtos(produtos)
            elif escolha == "0":
                break

        elif usuario["nivel"] == "cliente":
            menu_cliente()
            escolha = input("Escolha: ")
            if escolha == "1":
                for p in produtos:
                    print(p)
            elif escolha == "0":
                break

        else:
            print("Nível de acesso inválido.")
            break

if __name__ == "__main__":
    main()


 
       