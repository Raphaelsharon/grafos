from class_testes import Grafos

print("\nMatriz de adjacencia\n")
        
grafo = Grafos.ler_grafo_ad()
Grafos.imprimir_matriz_ad(grafo)

print("\nMatriz de encidencia\n")

grafo = Grafos.ler_grafo_en()
Grafos.imprimir_matriz_en(grafo)