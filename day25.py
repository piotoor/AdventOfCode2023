import networkx as nx


def parse_day25_a():
    with open("day25.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        k, v_str = row.split(": ")
        v = v_str.split(" ")
        for x in v:
            parsed.append((k, x))

    # for x in parsed:
    #     print(x)

    return parsed


def multiple_size_of_groups(data):
    graph = nx.Graph()
    graph.add_edges_from(data)
    # print(G.number_of_nodes())
    # print(G.number_of_edges())
    # print("nodes = ", G.nodes)
    # print("edges = ", G.edges)

    edges_to_remove = nx.minimum_edge_cut(graph)

    graph.remove_edges_from(edges_to_remove)
    ans = 1
    for g in nx.connected_components(graph):
        ans *= len(g)

    # for i, node in enumerate(G.nodes):
    #     G.nodes[node]['color'] = colors[parts[i]]
    #
    # nx.nx_pydot.write_dot(G, 'example.dot')
    return ans


def day25_a():
    data = parse_day25_a()
    print("day25_a = {}".format(multiple_size_of_groups(data)))
