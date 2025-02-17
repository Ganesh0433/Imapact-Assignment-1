
# Clone Graph
def cloneGraph(node):
    if not node:
        return None
    clones = {}
    def dfs(node):
        if node in clones:
            return clones[node]
        copy = Node(node.val, [])
        clones[node] = copy
        copy.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
        return copy
    return dfs(node)
