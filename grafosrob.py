#pede ao usuario uma quantidade de linhas
# que o grafo possui, as colunas serao
# adicionadas por linha
quantidade_listas = int(input("Digite a quantidade de vertices que o grafo possui: "))

listas = []

for i in range(quantidade_listas):
  # f é usado para que apaareca o resultado do parametro e nao o parametro
    nome_lista = {i + 1}
    colunas = input(f"Digite as arcos da linha {nome_lista}° separados por vírgulas: ")
    nova_lista = [int(i) for i in colunas.split(',')]  # Converte os elementos para inteiros
    listas.append((nome_lista, nova_lista))

for nome, lista in listas: # imprimir a matriz
    print(f" {lista}")

for nome, lista in listas: # imprimir os graus
    soma = sum(lista) # soma os valores 
    print(f"grau '{nome}': {soma}")