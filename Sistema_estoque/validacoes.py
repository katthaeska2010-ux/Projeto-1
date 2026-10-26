"""
Primeiro começar por aqui :construir de baixo pra cima:
primeiro as peças pequenas 
que não dependem de ninguém, depois as que usam essas peças.
"""

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto

        print("Este campo não pode estar vazio.")


def ler_quantidade(mensagem="Digite a quantidade: "):
    while True:
        try:
            quantidade = int(input(mensagem))

            if quantidade >= 0:
                return quantidade

            print("A quantidade não pode ser negativa. Por favor, insira um valor válido para a quantidade.")

        except ValueError:
            print("Digite um número inteiro.")


def ler_preco(mensagem="Digite o preço: "):
    while True:
        try:
            preco = float(input(mensagem).replace(",", "."))

            if preco > 0:
                return preco

            print("O preço deve ser maior que zero. Por favor, insira um valor válido para o preço.")

        except ValueError:
            print("Digite um número válido para o preço.")


        

