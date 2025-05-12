import networkx as nx
n = 25
p = 0.9
a = 0
G = nx.erdos_renyi_graph(n, p)
for n in G.nodes():
    a=a+G.degree(n)
degree_lec = (float(a)/len(G.nodes()))
degree_theor = p * (n - 1)
print(f"Средняя степень вершины: {degree_theor:.2f}")
print(f"Средняя степень вершины по формуле: {degree_lec:.2f}")
print(f"Разница: {abs(degree_lec - degree_theor):.2f}")
