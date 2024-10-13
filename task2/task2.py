import csv
from collections import defaultdict


def main(var: str) -> str:
    reader = csv.reader(var.splitlines())
    edges = [(int(u), int(v)) for u, v in reader]
    tree = defaultdict(list)
    reverse_tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        reverse_tree[v].append(u)

    nodes = set(tree.keys()).union({v for _, v in edges})

    relationships = {i: [0, 0, 0, 0, 0] for i in nodes}
    
    def find_descendants(node, level=1):
        descendants = []
        for child in tree[node]:
            descendants.append((child, level))
            descendants.extend(find_descendants(child, level + 1))
        return descendants
    
    def find_ancestors(node, level=1):
        ancestors = []
        for parent in reverse_tree[node]:
            ancestors.append((parent, level))
            ancestors.extend(find_ancestors(parent, level + 1))
        return ancestors

    for node in nodes:
        # r1 and r2
        for child in tree[node]:
            relationships[node][0] += 1  
            relationships[child][1] += 1 

        # r3 and r4
        descendants = find_descendants(node)
        for descendant, level in descendants:
            if level > 1:
                relationships[node][2] += 1
                relationships[descendant][3] += 1

        # r5
        if reverse_tree[node]:
            parent = reverse_tree[node][0]
            siblings = [sibling for sibling in tree[parent] if sibling != node]
            relationships[node][4] += len(siblings)

    result_lines = ["\tA\tB\tC\tD\tE"]
    k = 0
    for node in sorted(nodes):
        k += 1
        result_lines.append(f"{k}\t" +"\t" .join(map(str, relationships[node])))

    return "\n".join(result_lines)

if __name__ == "__main__":
    
    csv_string = """1,2
                    1,3
                    3,4
                    3,5"""  
    output_fixed = main(csv_string)
    print(output_fixed)

