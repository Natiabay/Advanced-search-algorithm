# Question 1: BFS and DFS
# Breadth-First Search and Depth-First Search implementations

from collections import deque
from graph_data import FIGURE_1_GRAPH


class BFS:
    """Breadth-First Search using a queue."""
    
    def __init__(self, graph, initial_state):
        """Initialize with graph and starting state."""
        self.graph = graph
        self.initial_state = initial_state
    
    def search(self, goal_state):
        """BFS to find path from initial to goal state."""
        queue = deque([(self.initial_state, [self.initial_state])])
        visited = set()
        nodes_explored = 0
        
        while queue:
            current, path = queue.popleft()
            nodes_explored += 1
            
            if current == goal_state:
                return path, nodes_explored
            
            if current not in visited:
                visited.add(current)
                
                # Add neighbors to queue
                for neighbor in self.graph.get(current, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return None, nodes_explored
    
    def get_solution(self, goal_state):
        """Format the solution output."""
        path, nodes_explored = self.search(goal_state)
        
        if path is None:
            return f"No path found from {self.initial_state} to {goal_state}.\nNodes explored: {nodes_explored}"
        
        result = f"Breadth-First Search (BFS)\n"
        result += f"Initial State: {self.initial_state}\n"
        result += f"Goal State: {goal_state}\n"
        result += f"Path Length: {len(path) - 1} steps\n"
        result += f"Nodes Explored: {nodes_explored}\n"
        result += f"Path: {' -> '.join(path)}\n"
        
        return result


class DFS:
    """Depth-First Search using a stack."""
    
    def __init__(self, graph, initial_state):
        """Initialize with graph and starting state."""
        self.graph = graph
        self.initial_state = initial_state
    
    def search(self, goal_state):
        """DFS to find path from initial to goal state."""
        stack = [(self.initial_state, [self.initial_state])]
        visited = set()
        nodes_explored = 0
        
        while stack:
            current, path = stack.pop()
            nodes_explored += 1
            
            if current == goal_state:
                return path, nodes_explored
            
            if current not in visited:
                visited.add(current)
                
                # Add neighbors to stack (reverse order to explore left-to-right)
                neighbors = self.graph.get(current, [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        
        return None, nodes_explored
    
    def get_solution(self, goal_state):
        """Format the solution output."""
        path, nodes_explored = self.search(goal_state)
        
        if path is None:
            return f"No path found from {self.initial_state} to {goal_state}.\nNodes explored: {nodes_explored}"
        
        result = f"Depth-First Search (DFS)\n"
        result += f"Initial State: {self.initial_state}\n"
        result += f"Goal State: {goal_state}\n"
        result += f"Path Length: {len(path) - 1} steps\n"
        result += f"Nodes Explored: {nodes_explored}\n"
        result += f"Path: {' -> '.join(path)}\n"
        
        return result


def main():
    """Run the BFS and DFS examples."""
    print("=" * 70)
    print("Question 1: Breadth-First Search and Depth-First Search")
    print("=" * 70)
    
    # Example: Find path from Addis Ababa to Lalibela
    initial = 'Addis Ababa'
    goal = 'Lalibela'
    
    print(f"\nFinding path from {initial} to {goal}")
    print("-" * 70)
    
    # BFS
    print("\nBFS Results:")
    print("-" * 70)
    bfs = BFS(FIGURE_1_GRAPH, initial)
    print(bfs.get_solution(goal))
    
    # DFS
    print("\nDFS Results:")
    print("-" * 70)
    dfs = DFS(FIGURE_1_GRAPH, initial)
    print(dfs.get_solution(goal))
    
    # Another example
    print("\n" + "=" * 70)
    print("Another example: Addis Ababa to Moyale")
    print("=" * 70)
    
    goal2 = 'Moyale'
    print(f"\nFinding path from {initial} to {goal2}")
    print("-" * 70)
    
    print("\nBFS Results:")
    print("-" * 70)
    bfs2 = BFS(FIGURE_1_GRAPH, initial)
    print(bfs2.get_solution(goal2))
    
    print("\nDFS Results:")
    print("-" * 70)
    dfs2 = DFS(FIGURE_1_GRAPH, initial)
    print(dfs2.get_solution(goal2))


if __name__ == "__main__":
    main()

