import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import networkx as nx

from random import randint

# needed functions
def read_matrix(filepath):
    try:
        A = []
        with open(filepath, "r") as file:
            rows = file.readlines()
            values = None
            for row in rows:
                values = []
                for v in row.split(" "):
                    if v.isnumeric():
                        values.append(int(v))
                A.append(values)
        return A
    except Exception as e:
        print(f'Error in time of dropping {file_path}. Reason: {e}')


# checking of existence of directory "pictures"
if not os.path.exists("pictures"):
    os.mkdir("pictures")

# cleaning of directory "pictures"
folder_path = "pictures"
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)  # delete files
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  # delete directories
    except Exception as e:
        print(f'Error in time of dropping {file_path}. Reason: {e}')

# visualizing of graphs
reading_folder_path = "matrices"
writing_folder_path = folder_path
for filename in os.listdir(reading_folder_path):
    A = read_matrix( os.path.join(reading_folder_path, filename) )
    G = nx.from_numpy_array(np.array(A), create_using=nx.DiGraph)
    mapping = {i: i + 1 for i in G.nodes}
    G = nx.relabel_nodes(G, mapping)

    pos = nx.circular_layout(G)
    for k in pos:
        x, y = pos[k]
        pos[k] = (x, -y)

    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1000, arrows=True, arrowsize=33)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, label_pos=0.2)

    plt.savefig(f"{folder_path}/{filename.split(".")[0]}.png", dpi=300)
    plt.close()

print("All graphs visualized")
input()
