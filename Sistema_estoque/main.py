from produtos import (cadastrar_produto, listar_produtos,pesquisar_produto,
                      atualizar_produto, remover_produto)
from movimentacoes import entrada_produto, saida_produto, exibir_historico
from relatorios import (relatorio_geral, produtos_abaixo_minimo,produtos_zerados,
                        ordenar_produtos, listar_por_categoria)

estoque = {}
historico=[]

def mostrar_menu():
    print("\n==== SISTEMA DE ESTOQUE ====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Pesquisar produto")
    print("4 - Atualizar produto")
    print("5 - Remover produto")
    print("6 - Entrada de produtos")
    print("7 - Saída de produtos")
    print("8 - Histórico de movimentações")
    print("9 - Relatório geral")
    print("10 - Produtos abaixo do mínimo")
    print("11 - Produtos com estoque zerado")
    print("12 - Ordenar produtos")
    print("13 - Listar por categoria")
    print("0 - Sair ")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção:").strip()

        if opcao == "1":
           cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            pesquisar_produto(estoque)
        elif opcao =="4":
            atualizar_produto(estoque)
        elif opcao =="5":
            remover_produto(estoque)
        elif opcao =="6":
            entrada_produto(estoque, historico)
        elif opcao == "7":
            saida_produto(estoque, historico)
        elif opcao == "8":
            exibir_historico(historico)
        elif opcao == "9":
            relatorio_geral(estoque)
        elif opcao == "10":
            produtos_abaixo_minimo(estoque)
        elif opcao =="11":
            produtos_zerados(estoque)
        elif opcao =="12":
            ordenar_produtos(estoque)
        elif opcao == "13":
            listar_por_categoria(estoque)
        elif opcao == "0":
            print("Encerrando o sistema.Até logo!")
            break
        else:
            print("Opção inálida, tente novamente.")

if __name__ == "__main__":
    main()
   