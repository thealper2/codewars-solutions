from collections import defaultdict


def center(graph_edges):
    graph = defaultdict(int)
    for item in graph_edges:
        graph[item[0]] += 1
        graph[item[1]] += 1
        
    max_val = float('-inf')
    max_key = None
    for k, v in graph.items():
        if v > max_val:
            max_val = v
            max_key = k
            
    return max_key
