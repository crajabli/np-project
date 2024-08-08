# generate test data for the vector cover problem

import random
import sys

def main():
    v_count = int(sys.argv[1])
    e_chance = int(sys.argv[2]) / 100
    file_num = int(sys.argv[3])
    vertices = []

    for v in range(v_count):
        vertices.append(chr(97 + v))
    
    generate_graph(vertices, e_chance, file_num)

def generate_graph(vertices, edge_chance, file_num):
    # Graph object
    graph = {v:[] for v in vertices}
    edge_count = 0

    for u in graph:
        for v in graph:
            if u == v or u in graph[v]:
                continue
            percent = random.random()
            if edge_chance >= percent:
                graph[u].append(v)
                graph[v].append(u)
                edge_count += 1

    # File to be created with graph edges as input
    file_name = f"test_cases\\input{file_num}.txt"

    # Open file to write to
    open(file_name, "w").close()
    f = open(file_name, "a")

    # Write edge count to file
    f.write(f"{edge_count}\n")

    # Write all edges to the file
    for u in graph:
        for v in graph[u]:
            f.write(f"{u} {v}\n")
            graph[v].remove(u)

    f.close()
  

if __name__ == '__main__':  
    main()