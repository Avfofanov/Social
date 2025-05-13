import networkx as nx
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (0, 3)])
G.add_edges_from([(1, 4), (2, 5), (3, 6)])
centrality = nx.eigenvector_centrality(G)
for n in centrality:
    print(f"Узел {n}: {centrality[n]:.4f}")
