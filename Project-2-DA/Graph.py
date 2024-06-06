import random

class DisconnectedGraphException(Exception):
    pass

class OverCompleteGraphException(Exception):
    pass

class Graph:
    MAX_WEIGHT = 999999
    NO_EDGE = 1000000
    def __init__(self, V, E, W):
        if (E > (V-1)*V/2):
            raise OverCompleteGraphException("E > (V-1)*V/2")
        self.NumVertices = V
        self.NumEdges = E
        self.AdjList = {vertex :[] for vertex in range(self.NumVertices)}
        self.AdjMatrix = [[Graph.NO_EDGE for j in range(self.NumVertices)] for i in range(self.NumVertices)]
        self.Edges = {}
        if (W > Graph.MAX_WEIGHT):
            self.MaxWeight = Graph.MAX_WEIGHT
            print("MaxWeight set to MAX_WEIGHT of 999999 since W > MAX_WEIGHT")
        else:
            self.MaxWeight = W
    def generateGraph(self, subclass=False, edges_done=0):
        remaining_edges = self.NumEdges
        if (subclass == True):
            remaining_edges -= edges_done
        while (remaining_edges > 0):
            u, v = random.sample(range(self.NumVertices), 2)
            if (u != v and self.AdjMatrix[u][v] == Graph.NO_EDGE):
                weight = random.randint(1, self.MaxWeight)
                self.AdjList[u].append((v, weight))
                self.AdjList[v].append((u, weight))
                self.AdjMatrix[u][v] = self.AdjMatrix[v][u] = weight
                self.Edges[(u,v)] = weight
                remaining_edges -= 1
    def printAdjList(self):
        for node, adj_node in self.AdjList.items():
            print(f"{node}: {adj_node}")
    def printAdjMatrix(self):
        for i in self.AdjMatrix:
            for j in i:
                print(f"{j:7}", end=" ")
            print()
            
class ConnectedGraph(Graph):
    def __init__(self, V, E, W):
        if (E < V-1):
            raise DisconnectedGraphException("E < V-1")
        super().__init__(V, E, W)
    def generateGraph(self):
        for i in range(self.NumVertices - 1):
            weight = random.randint(1, self.MaxWeight)
            self.AdjList[i].append((i+1, weight))
            self.AdjList[i+1].append((i, weight))
            self.AdjMatrix[i][i+1] = self.AdjMatrix[i+1][i] = weight
            self.Edges[(i,i+1)] = weight
        super().generateGraph(True, self.NumVertices-1)
    def generateWorstCaseGraph(self):
        max_edges = int(self.NumVertices*((self.NumVertices-1)/2))
        min_edges = (self.NumVertices-1)
        max_neccessary_edge_weight = max_edges-min_edges +1
        edge_weight = max_neccessary_edge_weight
        for node in range(self.NumVertices-2):
            for connected_node in range((self.NumVertices-1), (node+1), -1):
                self.AdjList[node].append((connected_node, edge_weight))
                self.AdjList[connected_node].append((node, edge_weight))
                self.AdjMatrix[node][connected_node] = self.AdjMatrix[connected_node][node] = edge_weight
                self.Edges[(node, connected_node)] = edge_weight
                edge_weight -= 1
        ideal_path_weight = 1
        for node in range(self.NumVertices - 1):
            self.AdjList[node].append((node+1, ideal_path_weight))
            self.AdjList[node+1].append((node, ideal_path_weight))
            self.AdjMatrix[node][node+1] = self.AdjMatrix[node+1][node] = ideal_path_weight
            self.Edges[(node,node+1)] = ideal_path_weight
    def generateBestCaseGraph(self):
        ideal_path_weight = 1
        for node in range(1,self.NumVertices):
            self.AdjList[0].append((node, ideal_path_weight))
            self.AdjList[node].append((0, ideal_path_weight))
            self.AdjMatrix[0][node] = self.AdjMatrix[node][0] = ideal_path_weight
            self.Edges[(0,node)] = ideal_path_weight
        super().generateGraph(True, self.NumVertices-1)