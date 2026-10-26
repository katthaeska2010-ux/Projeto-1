from validacoes import  ler_texto, ler_quantidade, ler_preco

def exibir_produto(codigo, produto):
# Mostra um produto numa linha. Se a quantidade é 0, avisa.
 aviso="" 
 if produto["quantidade"] == 0:
    aviso=" **SEM ESTOQUE**"  
    print(f"[{codigo}] {produto['nome']} | {produto['categoria']} |"
          f"R$ {produto['preco']:.2f} | Qtd: {produto['quantidade']}{aviso}")

def cadastrar_produto(estoque):
    codigo = ler_texto("Código: ")
    if codigo in estoque:
        print("Já existe um produto com esse código. Tente novamente.")
        return
    nome = ler_texto("Nome:") 
    categoria = ler_texto("Categoria:")
    preco = ler_preco()
    quantidade= ler_quantidade()
    estoque[codigo] = {
            "nome":nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade,
        }
    print("Produto cadastrado com sucesso!")

def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    for codigo, produto in estoque.items():
        exibir_produto(codigo, produto)

def pesquisar_produto(estoque):
    print("Pesquisar por: 1 - Código | 2 - Nome | 3- Categoria")
    opcao= input("Escolha uma opção: ").strip()

    if opcao == "1":
        codigo = input("Código: ").strip()
        if codigo in estoque:
            exibir_produto(codigo, estoque[codigo])
        else:
            print("Produto não encontrado.")
    elif opcao == "2" or opcao =="3":
        campo = "nome" if opcao == "2" else "categoria"
        termo = input("Digite o termo:").strip().lower()
        encontrou = False
        for codigo, produto in estoque.items():
            if termo in produto[campo].lower():
                exibir_produto(codigo, produto)
                encontrou = True
        if not encontrou:
            print("Nenhum produto encontrado.")
        
    else:
        print("Opção inválida. Tente novamente.")

def atualizar_produto(estoque):
    codigo = input("Digite o código do produto que deseja atualizar: ").strip()
    if codigo not in estoque:
        print("Produto não encontrado.")
        return
    produto = estoque[codigo]
    produto["nome"] = ler_texto("Novo nome:")
    produto["categoria"] = ler_texto("Nova categoria:")
    produto["preco"] = ler_preco("Novo preço:")
    produto["quantidade"] = ler_quantidade("Nova quantidade:")
    print("Produto atualizado com sucesso!")

def remover_produto(estoque):
    codigo = input("Digite o código do produto que deseja remover: ").strip()
    if codigo not in estoque:
        print("Produto não encontrado.")
        return
    confirmar = input(f"Tem certeza que deseja remover o produto {estoque[codigo]['nome']}? (s/n): ").strip().lower()
    if confirmar == "s":
        del estoque[codigo]
        print("Produto removido com sucesso!")
    else:
        print("Remoção cancelada.")
   