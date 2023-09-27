from class_testes import Dgrafo

#  matriz de adjacência
dgrafo_entrada = Dgrafo.ler_dgrafo_entrada_ad()
dgrafo_saida = Dgrafo.ler_dgrafo_saida_ad()
Dgrafo.imprimir_matriz_ad(dgrafo_entrada, dgrafo_saida)

#  matriz de encidência
dgrafo_entrada_en = Dgrafo.ler_dgrafo_entrada_en()
dgrafo_saida_en = Dgrafo.ler_dgrafo_saida_en()
Dgrafo.imprimir_matriz_en(dgrafo_entrada_en, dgrafo_saida_en)