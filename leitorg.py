grafo = {}

stop = "Digite (0) para finalizar\n"

while True:
    
    vert = str(input("Digite o nome do vertice: "))
    
    if (vert == '0'):
        
        break
    
    arco = str(input("Digite os vertices no qual ele tem uma ligação (use (,) para separar): "))
    
    arco = [str(i) for i in arco.split(',')]
    
    arco = list(arco)
    
    if  (arco == '0'):
        
        break
    
    grafo[vert] = arco

for i in grafo:
    
    print(len(grafo[i]))
    
print(grafo)