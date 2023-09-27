class Grafos(): #  classe dos grafos
    
    def ler_grafo_ad(): #  ler a matriz de adjacencia do grafo
        
        grafo = {}
        
        stop = "Digite (0) para finalizar\n" 
        
        while True:
    
            vert = str(input("Digite o nome do vertice: "))
    
            if (vert == '0'):
        
                break
    
            arco = str(input("Digite os vertices no qual ele tem uma ligação (use (,) para separar): "))
    
            if  (arco == '0'):
        
                break
    
            arco = [str(i) for i in arco.split(',')] #  separar criando antes a depois da virgula 
            arco_r = list(arco) #  criar uma lista
    
            if  (arco == '0'):
        
                break
    
            grafo[vert] = arco_r #  adicionar os elemendos ao dicionario
            
        return grafo 
        
    def ler_grafo_en(): #ler a matriz de encidencia
         
        grafo = {}

        stop = "Digite (0) para finalizar\n"

        while True:
    
            vert = str(input("Digite o nome do arco: "))
    
            if (vert == '0'):
        
                break
    
            arco = str(input("Digite os vertices no qual ele tem uma ligação (use (,) para separar): "))
    
            if  (arco == '0'):
        
                break
    
            arco = [str(i) for i in arco.split(',')] #  separar criando antes a depois da virgula
            arco_r = list(arco) #  criar uma lista
    
            if  (arco == '0'):
        
                break
    
            grafo[vert] = arco_r #  adicionar ao dicionario
            
        return grafo 
    
    def imprimir_matriz_ad(grafo):
    
        print('\nTabela\n')

        for vertices, arcos in grafo.items(): # mostrar as chaves e os elementos contidos nelas
    
            print(f"\033[0mVertice {vertices} : Arco {arcos}", end= " ===> ")
    
            dic = dict(grafo) #  retornar a dicionario
            grau = len(grafo[vertices]) # exibir a quantidade de elemendotos contidos da chave
    
            print(f"\033[1;34mGrau : {grau}\n")

        print("\033[0m") #  voltar a cor original do terminal
    
    def imprimir_matriz_en(grafo): #exibir grafo
    
        print('\nTabela\n')

        for vertices, arcos in grafo.items(): # mostrar as chaves e os elementos contidos nelas
    
            print(f"\033[0mArco {arcos} : Vertice {vertices}", end= " ===> ")
    
            dic = dict(grafo) #  retornar a dicionario
            grau = len(grafo[vertices]) # exibir a quantidade de elemendotos contidos da chave
    
            print(f"\033[1;34mGrau : {grau}\n")

        print("\033[0m") #  voltar a cor original do terminal
          
class Dgrafo(): #  classe dos dgrafos
    
    def ler_dgrafo_entrada_ad(): #  ler as informações de entrada dos dgrafo
        
        dgrafo_entrada = {} 
        
        print("\n\033[1;35mDgrafo entrada\nMATRIZ DE ADJACÊNCIA\033[0m\n")
        
        stop = print("Digite (0) para finalizar\n")
        obs = print("Caso nao tenha digite (-1)\n")
        
        while True:
            
            
            vert = str(input("\033[1;38mDigite o nome do vertece: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (vert == '0'):
                break
            
            arco_entrada = str(input("\033[1;38mDigite de onde vem o arco dirigido: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (arco_entrada == '0'):
                break
            
            if(arco_entrada != '-1'):
            
                arco_entrada = [str(i) for i in arco_entrada.split(',')] #  separar criando antes a depois da virgula
                arco_entrada_list = list(arco_entrada) #  criar uma lista
                dgrafo_entrada[vert] = arco_entrada_list #  adicionar ao dicionario
        
        return dgrafo_entrada

    def ler_dgrafo_saida_ad(): #  ler as informações de saida do dgrafo
        
        dgrafo_saida = {}
        
        print("\n\033[1;35mDgrafo saida\nMATRIZ DE ADJACÊNCIA\033[0m\n")
        
        stop = print("Digite (0) para finalizar\n")
        obs = print("Caso nao tenha digite (-1)\n")
        
        while True:
            
            vert = str(input("\033[1;38mDigite o nome do vertece: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (vert == '0'):
                break
            
            arco_saida = str(input("\033[1;38mDigite para onde vai o arco dirigido: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (arco_saida == '0'):
                break
            
            if(arco_saida != '-1'):
                
                arco_saida = [str(i) for i in arco_saida.split(',')] #  separar criando antes a depois da virgula
                arco_saida_list = list(arco_saida) #  criar uma lista
                dgrafo_saida[vert] = arco_saida_list #  adicionar ao dicionario
        
        return dgrafo_saida
      
    def imprimir_matriz_ad(dgrafo_entrada, dgrafo_saida ): #  exibir dgrafo  
    
        print('\n\033[1;33mTabela dgrafos entrada\nMATRIZ DE ADJACÊNCIA\033[0m\n')

        for vertices, arcos in dgrafo_entrada.items(): #  mostrar as chaves e os elementos contidos nelas
    
            print(f"\033[0mVertice {vertices} : Arco {arcos}", end= " ===> ")
    
            dic = dict(dgrafo_entrada) #  retornar a dicionario
            grau = len(dgrafo_entrada[vertices]) #  exibir a quantidade de elemendotos contidos da chave
    
            print(f"\033[1;34mGrau : {grau}\n")

        print("\033[0m") #  voltar a cor original do terminal 
        
        print('\n\033[1;33mTabela dgrafos saída\nMATRIZ DE ADJACÊNCIA\033[0m\n')
        
        for vertices, arcos in dgrafo_saida.items(): #  mostrar as chaves e os elementos contidos nelas
    
            print(f"\033[0mVertice {vertices} : Arco {arcos}", end= " ===> ")
    
            dic = dict(dgrafo_saida) #  retornar a dicionario
            
            grau = len(dgrafo_saida[vertices]) #  exibir a quantidade de elemendotos contidos da chave
    
            print(f"\033[1;34mGrau : {grau}\n")
        
        print("\033[0m") #  voltar a cor original do terminal
        
    def ler_dgrafo_entrada_en(): #  ler as informações de entrada dos dgrafo
        
        dgrafo_entrada = {} 
        
        print("\n\033[1;35mDgrafo entrada\nMATRIZ DE ENCIDÊNCIA\033[0m\n")
        
        stop = print("Digite (0) para finalizar\n")
        obs = print("Caso nao tenha digite (-1)\n")
        
        while True:
            
            
            vert = str(input("\033[1;38mDigite o nome do arco: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (vert == '0'):
                break
            
            arco_entrada = str(input("\033[1;38mDigite para qual vertece o arco vai: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (arco_entrada == '0'):
                break
            
            if(arco_entrada != '-1'):
            
                arco_entrada = [str(i) for i in arco_entrada.split(',')] #  separar criando antes a depois da virgula
                arco_entrada_list = list(arco_entrada) #  criar uma lista
                dgrafo_entrada[vert] = arco_entrada_list #  adicionar ao dicionario
        
        return dgrafo_entrada 
    
    def ler_dgrafo_saida_en(): #  ler as informações de saida do dgrafo
        
        dgrafo_saida = {}
        
        print("\n\033[1;35mDgrafo saida\nMATRIZ DE ENCIDÊNCIA\033[0m\n")
        
        stop = print("Digite (0) para finalizar\n")
        obs = print("Caso nao tenha digite (-1)\n")
        
        while True:
            
            vert = str(input("\033[1;38mDigite o nome do arco: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (vert == '0'):
                break
            
            arco_saida = str(input("\033[1;38mDigite de onde vem o arco: "))
            
            print("\033[0m") #  voltar a cor original do terminal
            
            if (arco_saida == '0'):
                break
            
            if(arco_saida != '-1'):
                
                arco_saida = [str(i) for i in arco_saida.split(',')] #  separar criando antes a depois da virgula
                arco_saida_list = list(arco_saida) #  criar uma lista
                dgrafo_saida[vert] = arco_saida_list #  adicionar ao dicionario
                
        return dgrafo_saida
                
    def imprimir_matriz_en(dgrafo_entrada_en,dgrafo_saida_en ): #  exibir dgrafo  
    
        print('\n\033[1;33mTabela dgrafos entrada\nMATRIZ DE ENCIDÊNCIA\033[0m\n')

        for vertices, arcos in dgrafo_entrada_en.items(): #  mostrar as chaves e os elementos contidos nelas
    
            print(f"\033[0mVertice {vertices} : Arco {arcos}", end= " ===> ")
    
            dic = dict(dgrafo_entrada_en) #  retornar a dicionario
            grau = len(dgrafo_entrada_en[vertices]) #  exibir a quantidade de elemendotos contidos da chave
    
            print(f"\033[1;34mGrau : {grau}\n")

        print("\033[0m") #  voltar a cor original do terminal 
        
        print('\n\033[1;33mTabela dgrafos saída\nMATRIZ DE ENCIDÊNCIA\033[0m\n')
        
        for vertices, arcos in dgrafo_saida_en.items(): #  mostrar as chaves e os elementos contidos nelas
    
            print(f"\033[0mVertice {vertices} : Arco {arcos}", end= " ===> ")
    
            dic = dict(dgrafo_saida_en) #  retornar a dicionario
            
            grau = len(dgrafo_saida_en[vertices]) #  exibir a quantidade de elemendotos contidos da chave
    
            print(f"\033[1;34mGrau : {grau}\n")
        
        print("\033[0m") #  voltar a cor original do terminal