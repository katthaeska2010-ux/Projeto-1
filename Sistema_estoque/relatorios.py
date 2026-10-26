from validacoes import ler_quantidade
from produtos import exibir_produto


def valor_total_estoque(estoque):
    total = 0
    for produto in estoque.values():
        total += produto["preco"] * produto["quantidade"]
    return total


def total_unidades(estoque):
    total = 0
    for produto in estoque.values():
        total += produto["quantidade"]
    return total


def relatorio_geral(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    print(f"Valor total do estoque: R$ {valor_total_estoque(estoque):.2f}")
    print(f"Total de unidades: {total_unidades(estoque)}")


def produtos_abaixo_minimo(estoque):
    limite = ler_quantidade("Digite o limite mínimo: ")
    encontrou = False
    for codigo, produto in estoque.items():
        if produto["quantidade"] < limite:
            exibir_produto(codigo, produto)
            encontrou = True
    if not encontrou:
        print("Nenhum produto abaixo do limite mínimo.")


def produtos_zerados(estoque):
    encontrou = False
    for codigo, produto in estoque.items():
        if produto["quantidade"] == 0:
            exibir_produto(codigo, produto)
            encontrou = True
    if not encontrou:
        print("Nenhum produto com estoque zerado.")


def ordenar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    print("Ordenar por: 1 - Nome | 2 - Preço | 3 - Quantidade")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        ordenados = sorted(estoque.items(), key=lambda item: item[1]["nome"].lower())
    elif opcao == "2":
        ordenados = sorted(estoque.items(), key=lambda item: item[1]["preco"])
    elif opcao == "3":
        ordenados = sorted(estoque.items(), key=lambda item: item[1]["quantidade"])
    else:
        print("Opção inválida.")
        return

    for codigo, produto in ordenados:
        exibir_produto(codigo, produto)


def listar_por_categoria(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    categorias = set()                         # set não repete elementos
    for produto in estoque.values():
        categorias.add(produto["categoria"])

    for categoria in sorted(categorias):
        print(f"\n--- {categoria} ---")
        for codigo, produto in estoque.items():
            if produto["categoria"] == categoria:
                exibir_produto(codigo, produto)