class grafos:
    
    grafo = {}

    stop = "Digite (0) para finalizar\n"

    while True:
    
        vert = str(input("Digite o nome do vertice: "))
    
        if (vert == '0'):
        
            break
    
        arco = str(input("Digite os vertices no qual ele tem uma ligação (use (,) para separar): "))
    
        if  (arco == '0'):
        
            break
    
        arco = [str(i) for i in arco.split(',')]
        arco_r = list(arco)
    
        if  (arco == '0'):
        
            break
    
        grafo[vert] = arco_r
    
    print('\nTabela\n')

    for vertices, arcos in grafo.items():
    
        print(f"\033[0mVertice {vertices} : Arco {arcos}", end= " ===> ")
    
        dic = dict(grafo)
        grau = len(grafo[vertices])
    
        print(f"\033[1;34mGrau : {grau}\n")

    print("\033[0m")