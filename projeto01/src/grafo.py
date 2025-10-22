from collections import defaultdict, deque
import heapq

class Grafo:
    """
    Grafo representado por lista de adjacência
    Complexidade:
        BFS/DFS: O(V + E)
        Dijkstra: O(E log V)
    """
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, u, v, peso=1):
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))  # grafo não direcionado

    def mostrar_grafo(self):
        for node, adj in self.grafo.items():
            print(f"{node}: {[v for v, _ in adj]}")

    def busca_largura(self, inicio, alvo):
        visitado = set()
        fila = deque([inicio])
        while fila:
            vertice = fila.popleft()
            if vertice == alvo:
                print(f"Caminho encontrado até {alvo}")
                return True
            if vertice not in visitado:
                visitado.add(vertice)
                fila.extend([v for v, _ in self.grafo[vertice] if v not in visitado])
        print(f"Caminho não encontrado até {alvo}")
        return False

    def busca_profundidade(self, inicio, alvo):
        visitado = set()
        stack = [inicio]
        while stack:
            vertice = stack.pop()
            if vertice == alvo:
                print(f"Caminho encontrado até {alvo}")
                return True
            if vertice not in visitado:
                visitado.add(vertice)
                stack.extend([v for v, _ in self.grafo[vertice] if v not in visitado])
        print(f"Caminho não encontrado até {alvo}")
        return False

    def dijkstra(self, inicio):
        dist = {v: float('inf') for v in self.grafo}
        dist[inicio] = 0
        heap = [(0, inicio)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, peso in self.grafo[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    heapq.heappush(heap, (dist[v], v))
        return dist
