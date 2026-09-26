from Dados import adjacencia
from Verificacao import graus_vertices, classificar_euleriano, eh_conexo, listaIndexada
from Inicio import escolher_inicio
from Fleury import caminho_fleury




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
