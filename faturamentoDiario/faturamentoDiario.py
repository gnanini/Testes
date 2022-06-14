import json
arquivo = "dados.json"


# O programa apenas retorna os valores, como solicitado, não imprime.
def main():
    global arquivo
    fatMen = getDados(arquivo)
    return (menorValor(fatMen), maiorValor(fatMen), acimaDaMedia(fatMen))


# pega os dados do .json.
def getDados(arquivo):
    lista = open(arquivo, "r")
    return json.load(lista)


# retorna o menor valor entre os valores do .json.
def menorValor(tabela):
    minimo = tabela[0]['valor']
    for k in range(len(tabela) - 1):
        if tabela[k + 1]['valor'] < minimo:
            minimo = tabela[k + 1]['valor']
    return minimo


# retorna o maior valor entre os valores do .json.
def maiorValor(tabela):
    maximo = tabela[0]['valor']
    for k in range(len(tabela) - 1):
        if tabela[k + 1]['valor'] > maximo:
            maximo = tabela[k + 1]['valor']
    return maximo


# retorna  o número de dias em que o rendimento foi acima da média.
def acimaDaMedia(tabela):
    soma = 0
    for k in range(len(tabela)):
        soma += tabela[k]['valor']
    media = soma / len(tabela)
    n = 0
    for k in range(len(tabela)):
        if tabela[k]['valor'] > media:
            n += 1
    return n


main()
