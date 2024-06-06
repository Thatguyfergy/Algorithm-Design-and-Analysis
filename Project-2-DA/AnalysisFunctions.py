import Dijkstra_Algo
import Graph

def minE(V):
    return V-1

def maxE(V):
    return V*(V-1)/2

def ArrayMatrixRep(V, E, W, Rep):
    AM_avg_comp = 0
    AM_avg_tt = 0
    for i in range(Rep):
        graph = Graph.ConnectedGraph(V, E, W)
        graph.generateGraph()
        AM_tt, AM_comp, AM_pre = Dijkstra_Algo.DijkstraAlgo.MatrixArray(graph, 0)
        AM_avg_comp += AM_comp
        AM_avg_tt += AM_tt
    AM_avg_tt /= Rep
    AM_avg_comp /= Rep
    return AM_avg_tt, AM_avg_comp
def HeapListRep(V, E, W, Rep):
    HL_avg_comp = 0
    HL_avg_tt = 0
    for i in range(Rep):
        graph = Graph.ConnectedGraph(V, E, W)
        graph.generateGraph()
        HL_tt, HL_comp, HL_pre = Dijkstra_Algo.DijkstraAlgo.ListMinHeap(graph, 0)
        HL_avg_comp += HL_comp
        HL_avg_tt += HL_tt
    HL_avg_tt /= Rep
    HL_avg_comp /= Rep
    return HL_avg_tt, HL_avg_comp
def CompareBetweenRep(V, E, W, Rep):
    AM_avg_tt = 0
    AM_avg_comp = 0
    HL_avg_tt = 0
    HL_avg_comp = 0
    for i in range(Rep):
        graph = Graph.ConnectedGraph(V, E, W)
        graph.generateGraph()
        AM_tt, AM_comp, AM_pre = Dijkstra_Algo.DijkstraAlgo.MatrixArray(graph, 0)
        HL_tt, HL_comp, HL_pre = Dijkstra_Algo.DijkstraAlgo.ListMinHeap(graph, 0)
        AM_avg_comp += AM_comp
        AM_avg_tt += AM_tt
        HL_avg_comp += HL_comp
        HL_avg_tt += HL_tt
    AM_avg_tt /= Rep
    AM_avg_comp /= Rep
    HL_avg_tt /= Rep
    HL_avg_comp /= Rep
    return AM_avg_tt, AM_avg_comp, HL_avg_tt, HL_avg_comp
def WorstCaseArrayMatrixRep(V, E, W, Rep):
    AM_avg_comp = 0
    AM_avg_tt = 0
    for i in range(Rep):
        graph = Graph.ConnectedGraph(V, E, W)
        graph.generateWorstCaseGraph()
        AM_tt, AM_comp, AM_pre = Dijkstra_Algo.DijkstraAlgo.MatrixArray(graph, 0)
        AM_avg_comp += AM_comp
        AM_avg_tt += AM_tt
    AM_avg_tt /= Rep
    AM_avg_comp /= Rep
    return AM_avg_tt, AM_avg_comp
def WorstCaseHeapListRep(V, E, W, Rep):
    HL_avg_comp = 0
    HL_avg_tt = 0
    for i in range(Rep):
        graph = Graph.ConnectedGraph(V, E, W)
        graph.generateWorstCaseGraph()
        HL_tt, HL_comp, HL_pre = Dijkstra_Algo.DijkstraAlgo.ListMinHeap(graph, 0)
        HL_avg_comp += HL_comp
        HL_avg_tt += HL_tt
    HL_avg_tt /= Rep
    HL_avg_comp /= Rep
    return HL_avg_tt, HL_avg_comp
def WorstCaseCompareBetweenRep(V, E, W, Rep):
    AM_avg_tt = 0
    AM_avg_comp = 0
    HL_avg_tt = 0
    HL_avg_comp = 0
    for i in range(Rep):
        graph = Graph.ConnectedGraph(V, E, W)
        graph.generateWorstCaseGraph()
        AM_tt, AM_comp, AM_pre = Dijkstra_Algo.DijkstraAlgo.MatrixArray(graph, 0)
        HL_tt, HL_comp, HL_pre = Dijkstra_Algo.DijkstraAlgo.ListMinHeap(graph, 0)
        AM_avg_comp += AM_comp
        AM_avg_tt += AM_tt
        HL_avg_comp += HL_comp
        HL_avg_tt += HL_tt
    AM_avg_tt /= Rep
    AM_avg_comp /= Rep
    HL_avg_tt /= Rep
    HL_avg_comp /= Rep
    return AM_avg_tt, AM_avg_comp, HL_avg_tt, HL_avg_comp