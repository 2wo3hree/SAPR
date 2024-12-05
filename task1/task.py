import json
import numpy as np

def main(graph):
    data = json.loads(graph)
    nodes = list(data["nodes"].keys())

    matrix = np.zeros((len(nodes), len(nodes),))

    for node, neighbors in data["nodes"].items():
        for neighbor in neighbors:
            matrix[nodes.index(node)][nodes.index(neighbor)] = 1
            matrix[nodes.index(neighbor)][nodes.index(node)] = 1

    return matrix


if __name__ == "__main__":

    graph = """

    {
        "nodes":{
            "1": ["2"],
            "2": ["3", "4"],
            "3": ["5"],
            "4": [],
            "5": []
        }
    }
    """

    matrix = main(graph)
    print(matrix)
