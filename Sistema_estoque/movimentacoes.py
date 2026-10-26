from datetime import datetime
from validacoes import ler_quantidade


def registrar_historico(historico, tipo, codigo, quantidade):
    historico.append({
        "tipo": tipo,
        "codigo": codigo,
        "quantidade": quantidade,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
    })


def entrada_produto(estoque, historico):
    codigo = input("Código do produto: ").strip()
    if codigo not in estoque:
        print("Produto não encontrado.")
        return
    quantidade = ler_quantidade("Quantidade de entrada: ")
    if quantidade == 0:
        print("A quantidade deve ser maior que zero.")
        return
    estoque[codigo]["quantidade"] += quantidade
    registrar_historico(historico, "ENTRADA", codigo, quantidade)
    print(f"Entrada registrada. Estoque atual: {estoque[codigo]['quantidade']}")


def saida_produto(estoque, historico):
    codigo = input("Código do produto: ").strip()
    if codigo not in estoque:
        print("Produto não encontrado.")
        return
    produto = estoque[codigo]
    if produto["quantidade"] == 0:
        print("Este produto está com o estoque zerado.")
        return
    quantidade = ler_quantidade("Quantidade de saída: ")
    if quantidade == 0:
        print("A quantidade deve ser maior que zero.")
        return
    if quantidade > produto["quantidade"]:     # impede saída maior que o estoque
        print(f"Estoque insuficiente. Disponível: {produto['quantidade']}")
        return
    produto["quantidade"] -= quantidade
    registrar_historico(historico, "SAÍDA", codigo, quantidade)
    print(f"Saída registrada. Estoque atual: {produto['quantidade']}")


def exibir_historico(historico):
    if not historico:
        print("Nenhuma movimentação registrada.")
        return
    for mov in historico:
        print(f"{mov['data']} | {mov['tipo']} | código {mov['codigo']} | {mov['quantidade']} un.")