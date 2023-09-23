from class_testes import Grafos

print("\nMatriz de adjacencia\n")
        
grafo = Grafos.ler_grafo_ad()
Grafos.exibir_grafo(grafo)

print("\nMatriz de encidencia\n")

grafo = Grafos.ler_grafo_en()
Grafos.exibir_grafo(grafo)