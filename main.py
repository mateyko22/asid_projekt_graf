from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List
from typing import Callable
from lista import Queue
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    def __init__(self, data: Any):
        self.data = data
        self.index: int

    def __str__(self):
        return self.data


class Edge:
    def __init__(self, src: Vertex, dst: Vertex, wgt: Optional[float]):
        self.source = src
        self.destination = dst
        self.weight = wgt


class Graph:
    def __init__(self):
        self.adjacencies = {}

    def __str__(self):
        j = 0
        lise = {}

        for i in self.adjacencies:
            lis = []
            for x in range(len(self.adjacencies[i])):
                lis.append(self.adjacencies[i][x].destination.data)
            lise[i.data] = lis

        for i in lise:
            print(j, ':', list(lise)[j], '---->', lise[i])
            j += 1
        return ''

    def create_vertex(self, data: Any) -> Vertex:
        new_v = Vertex(data)
        self.adjacencies.update({new_v: []})
        return new_v

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_e = Edge(source, destination, weight)
        self.adjacencies[source].append(new_e)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        if edge == 2:
            self.add_undirected_edge(destination, source, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        visited = []
        q1 = Queue()
        visited.append(list(self.adjacencies.keys())[0])
        q1.enqueue(list(self.adjacencies.keys())[0])
        while len(q1) > 0:
            if q1.head is None:
                return
            v = q1.head.data
            visit(v)
            for i in self.adjacencies[v]:
                d = i.destination
                if d not in visited:
                    visited.append(d)
                    q1.enqueue(d)
            q1.dequeue()

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        vb = (list(self.adjacencies.keys())[0])
        vis = []

        def dfs(v: Vertex, visited, visit: Callable[[Any], None]):
            visit(v)
            visited.append(v)
            for nb in self.adjacencies[v]:
                x = nb.destination
                if x not in visited:
                    dfs(nb.destination, visited, visit)

        dfs(vb, vis, visit)

    def show(self):
        def nodes(g: Graph) -> List:
            lis = []
            for i in g.adjacencies:
                lis.append(i.data)
            return lis

        def edges(g: Graph) -> List:
            lisq = []
            for i in g.adjacencies:
                lisy = []
                for x in range(len(g.adjacencies[i])):
                    lis5 = []
                    lis5.append(g.adjacencies[i][x].source.data)
                    lis5.append(g.adjacencies[i][x].destination.data)
                    lis5.append(g.adjacencies[i][x].weight)
                    lisy.append(lis5)
                lisq.extend(lisy)
            return lisq

        def weights(g: Graph) -> Dict:
            wg = {}
            for i in g.adjacencies:
                lisy = []
                for x in range(len(g.adjacencies[i])):
                    lis5 = []
                    lis5.append(g.adjacencies[i][x].source.data)
                    lis5.append(g.adjacencies[i][x].destination.data)
                    lisy.append(lis5)
                    wg.update({tuple(lis5): g.adjacencies[i][x].weight})
            return wg

        gn = nx.DiGraph()
        gn.add_nodes_from(nodes(self))
        gn.add_weighted_edges_from(edges(self))
        pos = nx.planar_layout(gn)
        plt.figure()
        nx.draw(gn, pos, edge_color='black', node_color='blue', labels={node: node for node in gn.nodes()})
        nx.draw_networkx_edge_labels(gn, pos, edge_labels=weights(self), font_color='red')
        plt.show()


def visit(self) -> None:
    print(self.data)


def get_edge(g: Graph, src: Vertex, dest: Vertex) -> Edge:
    for edge in g.adjacencies[src]:
        if edge.destination == dest:
            return edge


def get_path(g: Graph, src: Vertex, parents) -> List:
    path = []
    edg = get_edge(g, parents[src], src)
    path.append(edg)
    if edg.source not in parents:
        return path

    while True:
        src2 = edg.source
        edg = get_edge(g, parents[src2], src2)
        path.append(edg)
        if edg.source not in parents:
            break
    path.reverse()
    return path


def cheapest(tab, visited: List) -> Vertex:
    lc = float("Inf")
    cheap = 0
    for v in tab:
        if tab[v] < lc and v not in visited:
            lc = tab[v]
            cheap = v
    return cheap


def all_weighted_shortest_paths(g: Graph, start: Any) -> Dict[Any, List[Edge]]:
    cost = {i: float("Inf") for i in g.adjacencies}
    parents = {}
    cost[start] = 0
    visited = []

    for i in range(len(g.adjacencies)):
        v = cheapest(cost, visited)
        ads = g.adjacencies[v]
        visited.append(v)
        for edge in ads:
            nc = edge.weight + cost[v]
            if cost[edge.destination] > nc:
                cost[edge.destination] = nc
                parents[edge.destination] = v

    paths = {}
    for i in g.adjacencies:
        if i != start:
            paths[i.data] = get_path(g, i, parents)
    return paths


g1 = Graph()
v0 = g1.create_vertex('v0')
v1 = g1.create_vertex('v1')
v2 = g1.create_vertex('v2')
v3 = g1.create_vertex('v3')
v4 = g1.create_vertex('v4')
v5 = g1.create_vertex('v5')
g1.add(2, v0, v5, 7)
g1.add(2, v0, v1, 90)

g1.add(2, v2, v1, 1)
g1.add(2, v2, v3, 1)
g1.add(2, v3, v4, 10)
g1.add(2, v4, v1, 4)
g1.add(2, v4, v5, 30)
g1.add(2, v5, v1, 20)
g1.add(2, v5, v2, 3)


g2 = Graph()
vA = g2.create_vertex('A')
vB = g2.create_vertex('B')
vC = g2.create_vertex('C')
vD = g2.create_vertex('D')
g2.add(2, vA, vB, 30)
g2.add(2, vA, vC, 10)
g2.add(2, vB, vD, 2)
g2.add(2, vC, vD, 9)
g2.add(2, vC, vB, 5)


g3 = Graph()
qA = g3.create_vertex('qA')
qB = g3.create_vertex('qB')
qC = g3.create_vertex('qC')
qD = g3.create_vertex('qD')
qE = g3.create_vertex('qE')
qF = g3.create_vertex('qF')
qG = g3.create_vertex('qG')
g3.add(2, qA, qB, 7)
g3.add(2, qB, qC, 4)
g3.add(2, qC, qD, 5)
g3.add(2, qD, qB, 1)
g3.add(2, qA, qE, 2)
g3.add(2, qE, qC, 10)
g3.add(2, qE, qD, 1)
g3.add(2, qC, qF, 9)
g3.add(2, qF, qG, 8)
g3.add(2, qA, qG, 21)
g3.add(2, qB, qF, 6)
