"""Parte visual: desenha o grafo no estilo do PDF e o Tour de Euler encontrado."""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation, PillowWriter

# Posições copiadas do desenho do PDF (x, y)
POSICOES = {
    "0": (0.0, 2.0), "1": (3.0, 2.0),
    "5": (1.5, 1.0), "4": (4.5, 1.0),
    "3": (0.0, 0.0), "2": (3.0, 0.0),
}

COR_FUNDO = "#d9d9d9"     # fundo cinza
COR_ARESTA = "#e3a92b"    # amarelo-ouro das arestas
COR_BORDA = "#c47a3d"     # contorno laranja dos vértices
COR_NO = "#dedede"        # preenchimento dos vértices
COR_TEXTO = "#35507a"     # números azulados
COR_TOUR = "#c0392b"      # destaque do percurso
RAIO = 0.35


def lista_arestas(grafo):
    """Converte a lista de adjacência em arestas únicas (u, v)."""
    arestas = set()
    for u, vizinhos in grafo.items():
        for v in vizinhos:
            arestas.add(tuple(sorted((u, v), key=int)))
    return sorted(arestas, key=lambda a: (int(a[0]), int(a[1])))


def _encurtar(p1, p2, r=RAIO):
    """Recorta o segmento para não invadir os círculos dos vértices."""
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    d = (dx ** 2 + dy ** 2) ** 0.5
    ux, uy = dx / d, dy / d
    return (x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)


def _preparar_eixo(ax, titulo):
    ax.set_facecolor(COR_FUNDO)
    ax.set_xlim(-0.7, 5.2)
    ax.set_ylim(-0.7, 2.7)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for lado in ax.spines.values():
        lado.set_visible(False)
    ax.set_title(titulo, fontsize=14, fontweight="bold", pad=12)


def _desenhar_arestas(ax, grafo, cor=COR_ARESTA, largura=3):
    for u, v in lista_arestas(grafo):
        (x1, y1), (x2, y2) = _encurtar(POSICOES[u], POSICOES[v])
        ax.plot([x1, x2], [y1, y2], color=cor, linewidth=largura, zorder=1)


def _desenhar_vertices(ax, grafo, atual=None):
    for v in grafo:
        x, y = POSICOES[v]
        cor_borda = COR_TOUR if v == atual else COR_BORDA
        ax.add_patch(Circle((x, y), RAIO, facecolor=COR_NO,
                            edgecolor=cor_borda, linewidth=2.5, zorder=3))
        ax.text(x, y, v, ha="center", va="center", fontsize=16,
                fontweight="bold", color=COR_TEXTO, zorder=4)


def _desenhar_passo(ax, ordem, u, v):
    """Seta de u para v com o número do passo no meio."""
    inicio, fim = _encurtar(POSICOES[u], POSICOES[v])
    ax.annotate("", xy=fim, xytext=inicio, zorder=2,
                arrowprops=dict(arrowstyle="-|>", color=COR_TOUR,
                                lw=2.5, mutation_scale=20))
    mx, my = (inicio[0] + fim[0]) / 2, (inicio[1] + fim[1]) / 2
    ax.text(mx, my, str(ordem), ha="center", va="center", fontsize=11,
            fontweight="bold", color="white", zorder=5,
            bbox=dict(boxstyle="circle,pad=0.25", facecolor=COR_TOUR,
                      edgecolor="none"))


def desenhar_grafo(grafo, arquivo="grafo.png"):
    """Imagem do grafo original, parecida com a do PDF."""
    fig, ax = plt.subplots(figsize=(8, 5))
    _preparar_eixo(ax, "Grafo do Trabalho 03")
    _desenhar_arestas(ax, grafo)
    _desenhar_vertices(ax, grafo)
    fig.savefig(arquivo, dpi=150, bbox_inches="tight")
    print(f"Imagem salva: {arquivo}")
    return fig


def desenhar_tour(grafo, caminho, arquivo="tour_euler.png"):
    """Lado a lado: grafo original e Tour de Euler numerado."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5.5))

    _preparar_eixo(ax1, "Grafo original")
    _desenhar_arestas(ax1, grafo)
    _desenhar_vertices(ax1, grafo)

    _preparar_eixo(ax2, "Tour de Euler (Fleury)")
    _desenhar_arestas(ax2, grafo, cor="#bdbdbd", largura=2)
    for i in range(len(caminho) - 1):
        _desenhar_passo(ax2, i + 1, caminho[i], caminho[i + 1])
    _desenhar_vertices(ax2, grafo, atual=caminho[0])

    fig.text(0.5, 0.1, "Caminho: " + " → ".join(caminho),
             ha="center", fontsize=13, fontweight="bold")
    fig.savefig(arquivo, dpi=150, bbox_inches="tight")
    print(f"Imagem salva: {arquivo}")
    return fig


def animar_tour(grafo, caminho, arquivo="tour_euler.gif", intervalo=900):
    """GIF mostrando o algoritmo percorrendo uma aresta por vez."""
    fig, ax = plt.subplots(figsize=(8, 5.5))
    total = len(caminho) - 1

    def quadro(k):
        ax.clear()
        _preparar_eixo(ax, f"Fleury — passo {k} de {total}")
        _desenhar_arestas(ax, grafo)
        for i in range(k):
            _desenhar_passo(ax, i + 1, caminho[i], caminho[i + 1])
        _desenhar_vertices(ax, grafo, atual=caminho[k])
        ax.text(2.25, -0.6, " → ".join(caminho[:k + 1]),
                ha="center", fontsize=12, fontweight="bold")

    anim = FuncAnimation(fig, quadro, frames=total + 1, interval=intervalo)
    anim.save(arquivo, writer=PillowWriter(fps=1000 / intervalo))
    plt.close(fig)
    print(f"Animação salva: {arquivo}")


def mostrar():
    """Abre as janelas (só se houver interface gráfica)."""
    if matplotlib.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    # Teste isolado: python front.py
    from Dados import adjacencia
    desenhar_grafo(adjacencia)
    mostrar()