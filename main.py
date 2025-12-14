from functions import adicionar_produto, listar_produtos, atualizar_produtos, remover_produtos
from persistencia import carregar_produtos, calcular_proximo_id

produtos = carregar_produtos()
id_atual = calcular_proximo_id(produtos)

while True:
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Sair")
    
    # Validação para opção
    try:
        opcao = input("Selecione uma opção: ").strip()
        opcao = int(opcao)
        if opcao > 5 or opcao < 1:
            print("Selecione um número válido!")
    except:
        print("Opção inválida! Digite apenas números.")
        continue
    
    if opcao == 1:
        adicionar_produto(produtos, id_atual)
        id_atual += 1

    elif opcao == 2:
        listar_produtos(produtos)

    elif opcao == 3:
        atualizar_produtos(produtos)

    elif opcao == 4:
        remover_produtos(produtos)
    
    elif opcao == 5:
        print("Você saiu do sistema!")
        break