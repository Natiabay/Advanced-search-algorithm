# Question 3: A* Search
# Uses heuristics and backward costs

import heapq
from graph_data import FIGURE_3_GRAPH, FIGURE_3_HEURISTICS


class AStarSearch:
    """A* search with heuristics."""
    
    def __init__(self, graph, heuristics, initial_state):
        """Initialize A* with graph, heuristics, and starting state."""
        self.graph = graph
        self.heuristics = heuristics
        self.initial_state = initial_state
    
    def search(self, goal_state):
        """A* search to find optimal path. f(n) = g(n) + h(n)."""
        g_score = {self.initial_state: 0}
        f_score = {self.initial_state: self.heuristics.get(self.initial_state, 0)}
        
        priority_queue = [
            (f_score[self.initial_state], 0, self.initial_state, [self.initial_state])
        ]
        visited = set()
        nodes_explored = 0
        
        while priority_queue:
            current_f, current_g, current, path = heapq.heappop(priority_queue)
            nodes_explored += 1
            
            if current == goal_state:
                return path, current_g, nodes_explored
            
            if current in visited:
                continue
            
            visited.add(current)
            
            # Explore neighbors
            for neighbor, edge_cost in self.graph.get(current, {}).items():
                if neighbor in visited:
                    continue
                
                tentative_g = current_g + edge_cost
                
                # If this path to neighbor is better, update
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    h_value = self.heuristics.get(neighbor, 0)
                    f_value = tentative_g + h_value
                    f_score[neighbor] = f_value
                    
                    heapq.heappush(
                        priority_queue,
                        (f_value, tentative_g, neighbor, path + [neighbor])
                    )
        
        return None, float('inf'), nodes_explored
    
    def get_solution(self, goal_state):
        """Format the solution output."""
        path, cost, nodes_explored = self.search(goal_state)
        
        if path is None:
            return f"No path found from {self.initial_state} to {goal_state}.\nNodes explored: {nodes_explored}"
        
        result = f"A* Search Algorithm\n"
        result += f"Initial State: {self.initial_state}\n"
        result += f"Goal State: {goal_state}\n"
        result += f"Total Cost (g): {cost}\n"
        result += f"Heuristic at Start (h): {self.heuristics.get(self.initial_state, 0)}\n"
        result += f"Path Length: {len(path) - 1} steps\n"
        result += f"Nodes Explored: {nodes_explored}\n"
        result += f"Path: {' -> '.join(path)}\n"
        
        # Show cost breakdown
        result += "\nCost Breakdown:\n"
        for i in range(len(path) - 1):
            from_city = path[i]
            to_city = path[i + 1]
            edge_cost = self.graph.get(from_city, {}).get(to_city, 0)
            result += f"  {from_city} -> {to_city}: {edge_cost}\n"
        
        return result


def main():
    """Run the A* example."""
    print("=" * 70)
    print("Question 3: A* Search Algorithm")
    print("=" * 70)
    
    # A* from Addis Ababa to Moyale
    print("\nA* Search from Addis Ababa to Moyale")
    print("-" * 70)
    astar = AStarSearch(FIGURE_3_GRAPH, FIGURE_3_HEURISTICS, 'Addis Ababa')
    print(astar.get_solution('Moyale'))


if __name__ == "__main__":
    main()



