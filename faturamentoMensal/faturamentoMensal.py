import json
arquivo = "dados.json"


def main():
    global arquivo
    faturas = abrirDados(arquivo)

    for i in faturas:
        print(f"{i} {porcentagem(i, faturas):.1f}%")
    return


def abrirDados(arquivo):
    text = open(arquivo, 'r')
    return json.load(text)


def valorTotal(dic):
    x = 0
    for i in dic:
        x += dic[i]
    return x


def porcentagem(estado, arquivo):
    total = valorTotal(arquivo)
    return arquivo[estado] / total * 100


main()
