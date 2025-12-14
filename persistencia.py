import os, json

def carregar_produtos():
    if os.path.exists("produtos.json"):
        with open("produtos.json", "r") as arquivo:
            try:
                dados = json.load(arquivo)
                return dados  # pode ser lista com itens ou lista vazia
            except json.JSONDecodeError:
                # Arquivo vazio ou corrompido
                return []
    else:
        return []

def salvar_produtos(lista):
    with open("produtos.json", "w") as arquivo:
        json.dump(lista, arquivo)


def calcular_proximo_id(lista):
    maior_id = 0
    if not lista:
        return 1
    else:
        for p in lista:
            if p["id"] > maior_id:
                maior_id = p["id"]
        return maior_id + 1