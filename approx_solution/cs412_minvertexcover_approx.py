"""
name: Mason Cox & Chingiz Rajabli
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.
"""

def main():
    edge_count = int(input())

    graph = {}

    for _ in range(edge_count):
        v,u = input().split()
        graph.setdefault(v, set()).add(u)
        graph.setdefault(u, set()).add(v)

    vertex_cover(graph)


def vertex_cover(graph):
    min_cover = []

    sort_graph = sorted(graph, key=lambda key: len(graph[key]), reverse=True)

    for v in sort_graph:
        if v not in graph:
            continue
        for u in graph[v]:
            graph[u].remove(v)
            if not graph[u]:
                graph.pop(u)
        graph.pop(v)
        min_cover.append(v)
        if not graph:
            break
        
        
    print(" ".join(min_cover))

if __name__ == "__main__":
    main()