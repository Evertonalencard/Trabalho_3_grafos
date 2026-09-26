from Dados import adjacencia
from Verificacao import graus_vertices, classificar_euleriano


def escolher_inicio(grafo):
    classificacao = classificar_euleriano(grafo)

    if classificacao.startswith("Não euleriano"):
        raise ValueError("O grafo não possui caminho euleriano.")

    graus = graus_vertices(grafo)

    while True:
        entrada = input("Escolha o vértice inicial: ").strip()

        if entrada not in grafo:
            print("Vértice inexistente. Tente novamente.")
            continue

        if graus[entrada] == 0:
            print("Esse vértice não possui arestas. Escolha outro.")
            continue

        if classificacao == "Semi-euleriano" and graus[entrada] % 2 == 0:
            impares = [v for v, grau in graus.items() if grau % 2 != 0]
            print(f"Escolha um dos vértices de grau ímpar: {impares}")
            continue

        return entrada

