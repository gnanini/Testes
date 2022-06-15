def main():
    texto = input('Digite o texto: ')
    invertido = ''

    for i in range(len(texto), 0, -1):
        invertido += texto[i - 1]

    print(invertido)
# nessa versão parece mais óbvio apenas imprimir a
# string, por ser apenas um programa simples!!!
#    return invertido
    return


main()
