def alcancavel(grafo, origem, destino):
    """Verifica se destino ainda é alcançável a partir de origem."""
    visitados = set()
    pilha = [origem]

    while pilha:
        vertice = pilha.pop()

        if vertice == destino:
            return True

        if vertice in visitados:
            continue

        visitados.add(vertice)
        pilha.extend(grafo[vertice] - visitados)

    return False


def eh_ponte(grafo, origem, destino):
    """Testa se remover a aresta desconecta seus extremos."""
    grafo[origem].remove(destino)
    grafo[destino].remove(origem)

    ponte = not alcancavel(grafo, origem, destino)

    grafo[origem].add(destino)
    grafo[destino].add(origem)

    return ponte


def caminho_fleury(grafo, inicio):
    """Encontra um caminho ou circuito euleriano pelo algoritmo de Fleury."""
    restante = {
        vertice: set(vizinhos)
        for vertice, vizinhos in grafo.items()
    }

    total_arestas = sum(len(vizinhos) for vizinhos in restante.values()) // 2
    caminho = [inicio]
    atual = inicio

    while restante[atual]:
        vizinhos = sorted(restante[atual], key=int)

        # Uma ponte só pode ser escolhida se não houver alternativa.
        proximo = next(
            (v for v in vizinhos if not eh_ponte(restante, atual, v)),
            vizinhos[0]
        )

        print(f"Percorrendo: {atual} -> {proximo}")

        restante[atual].remove(proximo)
        restante[proximo].remove(atual)

        atual = proximo
        caminho.append(atual)

    if len(caminho) != total_arestas + 1:
        raise ValueError("Não foi possível percorrer todas as arestas.")

    return caminho
