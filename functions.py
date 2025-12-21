from persistencia import registrar_evento

# ===============================
# Funções auxiliares reutilizáveis
# ===============================

def input_int(msg):
    """Lê um inteiro com validação."""
    while True:
        valor = input(msg).strip()
        try:
            return int(valor)
        except:
            print("Digite um número inteiro válido!")


def input_float(msg):
    """Lê um float com validação."""
    while True:
        valor = input(msg).strip()
        try:
            return float(valor)
        except:
            print("Digite um valor numérico válido!")


def input_texto(msg):
    """Lê texto não vazio."""
    while True:
        texto = input(msg).strip().title()
        if texto:
            return texto
        print("Este campo não pode ser vazio!")


def encontrar_produto(lista, id_digitado):
    """Retorna o produto com aquele ID ou None."""
    for p in lista:
        if p["id"] == id_digitado:
            return p
    return None


# ===============================
# CRUD
# ===============================

def adicionar_produto(lista, id_atual):
    nome = input_texto("Nome do produto: ")

    # preço
    while True:
        preco = input_float("Preço do produto: ")
        if preco < 0:
            print("O preço deve ser maior que 0!")
        else:
            break

    # estoque
    while True:
        estoque = input_int("Quantidade do estoque: ")
        if estoque < 0:
            print("O estoque deve ser maior que 0!")
        else:
            break

    produto = {
        "id": id_atual,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    lista.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")
    registrar_evento(produto, "ADD")

def listar_produtos(lista):
    if not lista:
        print("Nenhum produto foi cadastrado!")
        return

    print("\n=== Lista de Produtos ===")
    for p in lista:
        print(f"ID: {p['id']}")
        print(f"Nome: {p['nome']}")
        print(f"Preço: R${p['preco']}")
        print(f"Estoque: {p['estoque']}")
        print("-" * 30)
    print()


def atualizar_produtos(lista):
    id_digitado = input_int("Digite o ID do produto que você deseja atualizar: ")

    produto = encontrar_produto(lista, id_digitado)

    if not produto:
        print("Produto não encontrado!")
        return 

    print("\nPRODUTO ENCONTRADO!")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R${produto['preco']}")
    print(f"Estoque: {produto['estoque']}\n")

    while True:
        print("O que deseja atualizar?")
        print("1. Nome")
        print("2. Preço")
        print("3. Estoque")
        print("4. Voltar")

        opcao = input_int("Opção: ")

        if opcao == 4:
            print("Voltando ao menu...")
            break

        elif opcao == 1:  # nome
            novo_nome = input_texto("Novo nome: ")
            if novo_nome == produto["nome"]:
                print("O nome não pode ser igual ao anterior!")
            else:
                produto["nome"] = novo_nome
                print("Nome atualizado!")

        elif opcao == 2:  # preço
            while True:
                novo_preco = input_float("Novo preço: ")
                if novo_preco < 0:
                    print("Valor deve ser maior que 0!")
                elif novo_preco == produto["preco"]:
                    print("O preço não pode ser igual!")
                else:
                    produto["preco"] = novo_preco
                    print("Preço atualizado!")
                    break

        elif opcao == 3:  # estoque
            while True:
                novo_estoque = input_int("Novo estoque: ")
                if novo_estoque < 0:
                    print("O estoque deve ser maior que 0!")
                elif novo_estoque == produto["estoque"]:
                    print("O estoque não pode ser igual!")
                else:
                    produto["estoque"] = novo_estoque
                    print("Estoque atualizado!")
                    break

        else:
            print("Opção inválida!")


def remover_produtos(lista):
    if not lista:
        print("Nenhum produto foi cadastrado!")
        return 

    id_digitado = input_int("Digite o ID do produto que você deseja remover: ")

    produto = encontrar_produto(lista, id_digitado)

    if not produto:
        print("Produto não encontrado!")
        return 

    print("\nPRODUTO ENCONTRADO!")
    print(f"Nome : {produto['nome']}")
    print(f"Preço : R${produto['preco']}")
    print(f"Estoque : {produto['estoque']}\n")

    while True:
        escolha = input("Tem certeza que deseja apagar? [S/N] ").strip().upper()

        if escolha == "N":
            print("O produto não foi apagado.")
            return False
        elif escolha == "S":
            lista.remove(produto)
            print("Produto removido com sucesso!")
            return
        else:
            print("Opção inválida! Digite apenas S ou N.")

