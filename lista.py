lista_compras = []

while True:
    print("Escolha uma opção:")
    print("1 - Inserir um item na lista")
    print("2 - Apagar um item da lista")
    print("3 - Listar os itens na lista")
    print("4 - Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        item = input("Digite o nome do item: ")
        lista_compras.append(item)
        print(f"O item {item} foi adicionado à lista.")

    elif opcao == 2:
        item = input("Digite o nome do item que deseja apagar: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"O item {item} foi removido da lista.")
        else:
            print(f"O item {item} não está na lista.")

    elif opcao == 3:
        print("Lista de compras:")
        for item in lista_compras:
            print(item)

    elif opcao == 4:
        break

    else:
        print("Opção inválida. Tente novamente.")