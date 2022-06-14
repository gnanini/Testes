def main():
    x = int(input("Qual é o número que deseja testar? "))
    return fibonacci(x)


def fibonacci(x):
    lista = [0, 1]
    k = 1
    while lista[k] <= x:
        if lista[k] == x:
            return "Seu número faz parte da sequência de Fibonacci!"
        else:
            lista.append(lista[k-1] + lista[k])
            k += 1
    return "Seu número não faz parte da sequência da Fibonacci!"


main()
