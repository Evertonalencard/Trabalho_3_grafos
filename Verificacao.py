from Dados import adjacencia

def listaIndexada():
    for vertice in sorted(adjacencia, key=int):
        vizinhos = sorted(adjacencia[vertice], key=int)
        print(f"{vertice} -> {vizinhos}")

        
def eh_conexo(grafo):
    """Verifica se é possível alcançar todos os vértices."""
    if not grafo:
        return False

    inicio = next(iter(grafo))
    visitados = set()
    pilha = [inicio]

    while pilha:
        vertice = pilha.pop()

        if vertice in visitados:
            continue

        visitados.add(vertice)
        pilha.extend(grafo[vertice] - visitados)

    return len(visitados) == len(grafo)

        
def graus_vertices(grafo):
    """Retorna o grau de cada vértice."""
    return {
        vertice: len(vizinhos)
        for vertice, vizinhos in grafo.items()
    }
    
def classificar_euleriano(grafo):
    """Classifica o grafo pelos graus e pela conectividade."""
    if not eh_conexo(grafo):
        return "Não euleriano (grafo não conexo)"

    graus = graus_vertices(grafo)
    impares = [
        vertice
        for vertice, grau in graus.items()
        if grau % 2 != 0
    ]

    if len(impares) == 0:
        return "Euleriano"
    if len(impares) == 2:
        return "Semi-euleriano"

    return "Não euleriano"
    
def verificacao_concluida():
    if eh_conexo(adjacencia) and (classificar_euleriano(adjacencia) == "Euleriano" or classificar_euleriano(adjacencia) == "Semi-euleriano"):
        print("O grafo é conexo e possui um caminho ou circuito euleriano.")
        return True
    return False
