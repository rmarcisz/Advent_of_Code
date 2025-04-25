from collections import defaultdict

def is_binary_tree(edges):
    child_count = defaultdict(int)
    parent_map = defaultdict(list)
    nodes = set()

    # Step 1: Process edges and count children
    for parent, child in edges:
        parent_map[parent].append(child)
        child_count[child] += 1
        nodes.add(parent)
        nodes.add(child)

        # Check if any node has more than one parent
        if child_count[child] > 1:
            return False  # A node has multiple parents, not a tree
    # Step 2: Find the root (should be exactly one)
    root_candidates = nodes - set(child_count.keys())  # Nodes that are never children
    if len(root_candidates) != 1:
        return False  # Either no root or multiple roots
    root = root_candidates.pop()
    # Step 3: Check for cycles and connectivity using DFS
    visited = set()
    def dfs(node):
        if node in visited:
            return False  # Cycle detected
        visited.add(node)
        for child in parent_map[node]:
            if not dfs(child):
                return False
        return True

    if not dfs(root):
        return False  # Cycle detected

    # Step 4: Ensure all nodes are connected
    return len(visited) == len(nodes)  # All nodes must be reachable from root

# Example usage:
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
print(is_binary_tree(edges))  # True

edges_with_cycle = [(1, 2), (2, 3), (3, 1)]
print(is_binary_tree(edges_with_cycle))  # False (Cycle)

edges_multiple_parents = [(1, 2), (2, 3), (4, 3)]
print(is_binary_tree(edges_multiple_parents))  # False (Node 3 has two parents)