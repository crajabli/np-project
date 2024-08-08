"""
name: Mason Cox & Chingiz Rajabli
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.

This is where we found how to use setDefault
https://www.w3schools.com/python/ref_dictionary_setdefault.asp
"""
import itertools


def main():
    edge_count = int(input())

    graph = {}

    for _ in range(edge_count):
        v,u = input().split()
        graph.setdefault(v, set()).add(u)
        graph.setdefault(u, set()).add(v)

    vertex_cover(graph)

def vertex_cover(graph):
    min_cover = None

    def check_cover(i):
        for combo in itertools.combinations(graph, i):
            g_clone = {u:set([v for v in graph[u]]) for u in graph}
  
            for v in combo:
                if v not in g_clone:
                    continue
                for u in g_clone[v]:
                    g_clone[u].remove(v)
                    if not g_clone[u]:
                        g_clone.pop(u)
                g_clone.pop(v)
            if not g_clone:
                return combo
            
        return None

    # for i in range((len(graph) // 2) + 1):
    for i in range((len(graph) + 1)):
        min_cover = check_cover(i)
        if min_cover != None:
            break

        # min_cover = check_cover(len(graph) - i)
        # if min_cover != None and len(min_cover) <= len(graph) // 2:
        #     break

    print(" ".join(min_cover))


if __name__ == "__main__":
    main()