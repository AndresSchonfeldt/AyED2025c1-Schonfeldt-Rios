import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, start, end, weight):
        if start not in self.adj_list:
            self.adj_list[start] = []
        if end not in self.adj_list:
            self.adj_list[end] = []
        self.adj_list[start].append((end, weight))
        self.adj_list[end].append((start, weight))

    def get_nodes(self):
        return sorted(self.adj_list.keys())

    def find_min_spanning_tree(self, start):
        """Algoritmo de Prim para encontrar el árbol de expansión mínima."""
        mst = {}
        visited = set()
        min_heap = [(0, start, None)]
        total_distance = 0

        while min_heap:
            weight, current, parent = heapq.heappop(min_heap)
            if current in visited:
                continue
            
            visited.add(current)
            total_distance += weight
            if parent:
                mst[current] = parent
            
            for neighbor, edge_weight in self.adj_list.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current))

        return mst, total_distance
