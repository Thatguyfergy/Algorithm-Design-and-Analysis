import networkx as nx

def drawGraph(graph):
    G = nx.Graph()

    # Add nodes to the graph
    G.add_nodes_from([i for i in range(graph.NumVertices)])

    # Add edges to the graph
    for edge, weight in graph.Edges.items():
        G.add_edge(edge[0], edge[1], weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=300,
        node_color="skyblue",
        font_size=10,
        font_color="black",
        font_weight="bold",
    )
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2.0, edge_color="red")

    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    ##plt.show()       