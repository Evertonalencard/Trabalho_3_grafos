from Dados import adjacencia
from Verificacao import graus_vertices, classificar_euleriano, eh_conexo, listaIndexada
from Inicio import escolher_inicio
from Fleury import caminho_fleury
from front import desenhar_grafo, desenhar_tour, animar_tour, mostrar


if __name__ == "__main__":
    print("Passo 1")
    listaIndexada()
    print("--------------------------------")
    print("\nÉ conexo?", eh_conexo(adjacencia))
    graus = graus_vertices(adjacencia)
    print("--------------------------------")
    for vertice in sorted(graus, key=int):
        grau = graus[vertice]
        paridade = "par" if grau % 2 == 0 else "ímpar"
        print(f"Grau do vértice {vertice}: {grau} ({paridade})")
    print("--------------------------------")
    print("Classificação:", classificar_euleriano(adjacencia))
    print("Passo 2")
    inicio = escolher_inicio(adjacencia)
    print(f"Vértice inicial escolhido: {inicio}")
    print("Passo 3")
    caminho = caminho_fleury(adjacencia, inicio)
    print("Caminho euleriano:", " -> ".join(caminho))
    if caminho[0] == caminho[-1]:
        print("Começa e termina no mesmo vértice: é um CIRCUITO (Tour de Euler).")
    print("--------------------------------")
    print("Passo 4 - Visualização")
    desenhar_grafo(adjacencia)
    desenhar_tour(adjacencia, caminho)
    animar_tour(adjacencia, caminho)
    mostrar()