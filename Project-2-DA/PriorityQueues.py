class UnorderedArrayPriorityQueue:
    def __init__(self, array_size):
        self.size = 0
        self.pq = [-1 for i in range(array_size)]
        self.NodeInQ = [-1 for i in range(array_size)]
    def enqueue(self, node_weight_tuple):
        self.update(node_weight_tuple)
        self.NodeInQ[self.size] = node_weight_tuple[0]
        self.size += 1
    def update(self, node_weight_tuple):
        self.pq[node_weight_tuple[0]] = node_weight_tuple[1]
    def dequeue(self):
        comparisons = 0
        lowest_weight_node = self.NodeInQ[0]
        lowest_weight_node_index = 0
        for index_in_nodeinq in range(1, self.size):
            comparisons += 1
            if ((self.pq[lowest_weight_node]) > (self.pq[self.NodeInQ[index_in_nodeinq]])):
                lowest_weight_node_index = index_in_nodeinq
                lowest_weight_node = self.NodeInQ[lowest_weight_node_index]
        self.size -= 1
        for i in range(lowest_weight_node_index, self.size):
            self.NodeInQ[i] = self.NodeInQ[i+1]
        return lowest_weight_node, comparisons
        
class HeapPQ:
    def __init__(self, array_size):
        self.comparisons = 0
        self.size = 0
        self.pq = [(-1, -1) for i in range(array_size)]
        self.nodeIndex = [-1 for i in range(array_size)]
    def updateNodeIndex(self, new_index):
        self.nodeIndex[self.pq[new_index][0]] = new_index
    def swapNodeTuplesIndex(self, index_1, index_2):
        temp = self.pq[index_1]
        self.pq[index_1] = self.pq[index_2]
        self.pq[index_2] = temp
        self.updateNodeIndex(index_1)
        self.updateNodeIndex(index_2)
    def dequeue(self):
        comparisons = 0
        self.size -= 1
        to_return = self.pq[0][0]
        self.pq[0] = self.pq[self.size]
        self.updateNodeIndex(0)
        cur_index = 0
        LC_index = ((cur_index*2)+1)
        RC_index = ((cur_index*2)+2)
        while (LC_index < self.size):
            comparisons += 1
            if ((self.pq[LC_index][1] < self.pq[RC_index][1]) or (RC_index >= self.size)):
                smaller_child_index = LC_index
            else:
                smaller_child_index = RC_index
            comparisons += 1
            if (self.pq[cur_index][1] > self.pq[smaller_child_index][1]):
                self.swapNodeTuplesIndex(cur_index, smaller_child_index)
                cur_index = smaller_child_index
                LC_index = ((cur_index*2)+1)
                RC_index = ((cur_index*2)+2)
            else:
                break            
        return to_return, comparisons   
    def enqueue(self, node_weight_tuple):
        comparisons = 0
        self.pq[self.size] = node_weight_tuple
        cur_index = self.size
        self.updateNodeIndex(cur_index)
        self.size += 1
        parent_index = ((cur_index-1)//2)
        while(parent_index >= 0):
            comparisons += 1
            if (self.pq[cur_index][1] < self.pq[parent_index][1]):
                self.swapNodeTuplesIndex(cur_index, parent_index)
                cur_index = parent_index
                parent_index = ((cur_index-1)//2)
            else:
                break
        return comparisons        
    def updateNodeWeightTuple(self, node_weight_tuple):
        comparisons = 0
        cur_index = self.nodeIndex[node_weight_tuple[0]]
        self.pq[cur_index] = node_weight_tuple
        parent_index = ((cur_index-1)//2)
        while(parent_index >= 0):
            comparisons += 1
            if (self.pq[cur_index][1] < self.pq[parent_index][1]):
                self.swapNodeTuplesIndex(cur_index, parent_index)
                cur_index = parent_index
                parent_index = ((cur_index-1)//2)
            else:
                break
        return comparisons      