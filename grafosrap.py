import numpy as np

# definir o tamanho da matriz
x = int(input("Informe a quantidade de vertices: "))
y = x + 1  # variavel de controle

def grafo():
    
    matriz = np.zeros((x, y), dtype=int)  # matriz de adjacencia
    x1 = 0
    for l in range(x):
        x1 += 1
        for c in range(x):
            matriz[l][c] = int(input(f"\nSe os verteces tem arcos digite (1), caso contrario digite (0), {x1}: "))

    # somar os itens de cada linha
    for l in range(x):
        sum = 0
        for c in range(y - 1):
            sum += matriz[l][c]
        matriz[l][x] = sum

    print("\nTabela\n")
    # imprimir a matriz adjacente
    for l in range(x):
        for c in range(y):
            print(matriz[l][c], end=" ")
        print("\n")

    g = int(input("Digite a quantidade de arcos: "))
    matriz_2 = np.zeros((x, g + 1), dtype=int)  # matriz de encidencia

    # coletar os dados de cada vertece se ele tem arco com tal arco
    x1 = 0
    for l in range(x):
        x1 += 1
        for c in range(g):
            matriz_2[l][c] = int(input(f"Digite (1) caso tenham arco ou (0) caso nao tenha arco (arcos entre um vertice e outro) {x1}: "))

    # somar os itens de cada linha
    for l in range(x):
        som2 = 0
        for c in range(g):
            som2 += matriz_2[l][c]
        matriz_2[l][g] = som2

    print("\nTabela\n")
    # imprimir a matriz de encidencia
    for l in range(x):
        for c in range(g + 1):
            print(matriz_2[l][c], end=" ")
        print("\n")
    print("\nA utima coluna é o grau")
    print("Fim!")

grafo()