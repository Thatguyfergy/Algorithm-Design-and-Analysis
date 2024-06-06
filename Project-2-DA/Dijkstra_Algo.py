import time
from Graph import Graph, ConnectedGraph
from PriorityQueues import UnorderedArrayPriorityQueue, HeapPQ
       
class DijkstraAlgo:
    @classmethod
    def MatrixArray(self, graph, start):
        start_time = time.time()
        comparisons = 0
        predecessor = [-1 for i in range(graph.NumVertices)]
        visited = [False for i in range(graph.NumVertices)]
        distance = [-1 for i in range(graph.NumVertices)]
        predecessor[start] = start
        visited[start] = True
        distance[start] = 0
        priorityQ = UnorderedArrayPriorityQueue(graph.NumVertices)
        priorityQ.enqueue((start,0))
        cur = start
        while (priorityQ.size > 0):
            cur, comp = priorityQ.dequeue()
            comparisons += comp
            visited[cur] = True
            for adj_node in range(graph.NumVertices):
                comparisons += 1
                if ((graph.AdjMatrix[cur][adj_node] != Graph.NO_EDGE) and (visited[adj_node] != True)):
                    if (distance[cur] + graph.AdjMatrix[cur][adj_node] < distance[adj_node]):
                        distance[adj_node] = distance[cur] + graph.AdjMatrix[cur][adj_node]
                        predecessor[adj_node] = cur
                        priorityQ.update((adj_node, distance[adj_node]))
                        comparisons += 1
                    if (distance[adj_node] == -1):
                        distance[adj_node] = distance[cur] + graph.AdjMatrix[cur][adj_node]
                        predecessor[adj_node] = cur
                        priorityQ.enqueue((adj_node, distance[adj_node]))
                        comparisons += 1
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"MatrixArray Time taken: {time_taken}s")
        print(f"MatrixArray Comparisons: {comparisons}")
        return time_taken, comparisons, predecessor
        
    @classmethod                
    def ListMinHeap(self, graph, start):
        start_time = time.time()
        comparisons = 0
        predecessor = [-1 for i in range(graph.NumVertices)]
        visited = [False for i in range(graph.NumVertices)]
        distance = [-1 for i in range(graph.NumVertices)]
        predecessor[start] = start
        visited[start] = True
        distance[start] = 0
        priorityQ = HeapPQ(graph.NumVertices)
        priorityQ.enqueue((start,0))
        cur = start
        while (priorityQ.size > 0):
            cur, comp = priorityQ.dequeue()
            comparisons += comp
            visited[cur] = True
            for adj_node, weight in graph.AdjList[cur]:
                comparisons += 1
                if ((visited[adj_node] != True)):
                    if (distance[cur] + weight < distance[adj_node]):
                        distance[adj_node] = distance[cur] + weight
                        predecessor[adj_node] = cur
                        comparisons += priorityQ.updateNodeWeightTuple((adj_node, distance[adj_node]))
                    if (distance[adj_node] == -1):
                        distance[adj_node] = distance[cur] + weight
                        predecessor[adj_node] = cur
                        comparisons += priorityQ.enqueue((adj_node, distance[adj_node]))
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"ListMinHeap Time taken: {time_taken}s")
        print(f"ListMinHeap Comparisons: {comparisons}")
        return time_taken, comparisons, predecessor