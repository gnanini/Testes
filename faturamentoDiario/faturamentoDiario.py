import json
arquivo = "dados.json"


# O programa apenas retorna os valores, como solicitado, não imprime.
def main():
    global arquivo
    fatMen = getDados(arquivo)
    print(menorValor(fatMen), maiorValor(fatMen), acimaDaMedia(fatMen))
    return


# pega os dados do .json.
def getDados(arquivo):
    lista = open(arquivo, "r")
    return json.load(lista)


# retorna o menor valor entre os valores do .json.
# esse valor é zero porque o programa não especifica que não se
# deve considerar os zeros ao contrário da instrução dada para
# o algorítimo de média
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
    n = 0
    for k in range(len(tabela)):
        soma += tabela[k]['valor']
        if tabela[k]['valor'] != 0:
            n += 1
    media = soma / n
    resultado = 0
    for k in range(len(tabela)):
        if tabela[k]['valor'] > media:
            resultado += 1
    return resultado


main()
