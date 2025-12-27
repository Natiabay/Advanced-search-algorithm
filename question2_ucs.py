"""
Question 2: Uniform Cost Search
Implements UCS for single goal and multiple goals (customized)
"""

import heapq
from graph_data import FIGURE_2_GRAPH


class UniformCostSearch:
    """
    Uniform Cost Search implementation for traveling Ethiopia problem.
    """
    
    def __init__(self, graph, initial_state):
        """
        Initialize UCS with graph and initial state.
        
        Args:
            graph: Dictionary with costs {node: {neighbor: cost}}
            initial_state: Starting state
        """
        self.graph = graph
        self.initial_state = initial_state
    
    def search(self, goal_state):
        """
        Uniform Cost Search to find optimal path to single goal.
        
        Args:
            goal_state: Target state
            
        Returns:
            tuple: (path, total_cost, nodes_explored)
        """
        # Priority queue: (total_cost, current_node, path)
        priority_queue = [(0, self.initial_state, [self.initial_state])]
        visited = set()
        nodes_explored = 0
        
        while priority_queue:
            cost, current, path = heapq.heappop(priority_queue)
            nodes_explored += 1
            
            if current == goal_state:
                return path, cost, nodes_explored
            
            if current not in visited:
                visited.add(current)
                
                # Explore neighbors
                for neighbor, edge_cost in self.graph.get(current, {}).items():
                    if neighbor not in visited:
                        new_cost = cost + edge_cost
                        heapq.heappush(
                            priority_queue,
                            (new_cost, neighbor, path + [neighbor])
                        )
        
        return None, float('inf'), nodes_explored
    
    def search_multiple_goals(self, goal_states):
        """
        Customized UCS to visit all goal states preserving local optimum.
        Uses greedy approach: always go to nearest unvisited goal.
        
        Args:
            goal_states: List of goal states to visit
            
        Returns:
            tuple: (complete_path, total_cost, nodes_explored)
        """
        unvisited_goals = set(goal_states)
        current_state = self.initial_state
        complete_path = [current_state]
        total_cost = 0
        total_nodes_explored = 0
        
        while unvisited_goals:
            # Find nearest unvisited goal
            best_path = None
            best_cost = float('inf')
            best_goal = None
            nodes_for_this_goal = 0
            
            for goal in unvisited_goals:
                # Use UCS to find path to this goal
                path, cost, nodes = self._search_from_state(current_state, goal)
                if path and cost < best_cost:
                    best_path = path
                    best_cost = cost
                    best_goal = goal
                    nodes_for_this_goal = nodes
            
            if best_path is None:
                break
            
            # Add path to complete path (skip first node as it's already in path)
            complete_path.extend(best_path[1:])
            total_cost += best_cost
            total_nodes_explored += nodes_for_this_goal
            current_state = best_goal
            unvisited_goals.remove(best_goal)
        
        return complete_path, total_cost, total_nodes_explored
    
    def _search_from_state(self, start_state, goal_state):
        """
        Helper method to perform UCS from any start state.
        
        Args:
            start_state: Starting state
            goal_state: Target state
            
        Returns:
            tuple: (path, total_cost, nodes_explored)
        """
        priority_queue = [(0, start_state, [start_state])]
        visited = set()
        nodes_explored = 0
        
        while priority_queue:
            cost, current, path = heapq.heappop(priority_queue)
            nodes_explored += 1
            
            if current == goal_state:
                return path, cost, nodes_explored
            
            if current not in visited:
                visited.add(current)
                
                for neighbor, edge_cost in self.graph.get(current, {}).items():
                    if neighbor not in visited:
                        new_cost = cost + edge_cost
                        heapq.heappush(
                            priority_queue,
                            (new_cost, neighbor, path + [neighbor])
                        )
        
        return None, float('inf'), nodes_explored
    
    def get_solution(self, goal_state):
        """
        Get formatted solution for single goal.
        
        Args:
            goal_state: Target state
            
        Returns:
            str: Formatted solution
        """
        path, cost, nodes_explored = self.search(goal_state)
        
        if path is None:
            return f"No path found from {self.initial_state} to {goal_state}.\nNodes explored: {nodes_explored}"
        
        result = f"Uniform Cost Search\n"
        result += f"Initial State: {self.initial_state}\n"
        result += f"Goal State: {goal_state}\n"
        result += f"Total Cost: {cost}\n"
        result += f"Path Length: {len(path) - 1} steps\n"
        result += f"Nodes Explored: {nodes_explored}\n"
        result += f"Path: {' -> '.join(path)}\n"
        
        return result
    
    def get_multiple_goals_solution(self, goal_states):
        """
        Get formatted solution for multiple goals.
        
        Args:
            goal_states: List of goal states
            
        Returns:
            str: Formatted solution
        """
        path, total_cost, nodes_explored = self.search_multiple_goals(goal_states)
        
        result = f"Customized Uniform Cost Search (Multiple Goals)\n"
        result += f"Initial State: {self.initial_state}\n"
        result += f"Goal States: {', '.join(goal_states)}\n"
        result += f"Total Cost: {total_cost}\n"
        result += f"Total Path Length: {len(path) - 1} steps\n"
        result += f"Total Nodes Explored: {nodes_explored}\n"
        result += f"Complete Path: {' -> '.join(path)}\n"
        
        return result


def main():
    """Demonstrate UCS implementations."""
    print("=" * 70)
    print("Question 2: Uniform Cost Search")
    print("=" * 70)
    
    # Question 2.2: UCS from Addis Ababa to Lalibela
    print("\nQuestion 2.2: UCS from Addis Ababa to Lalibela")
    print("-" * 70)
    ucs = UniformCostSearch(FIGURE_2_GRAPH, 'Addis Ababa')
    print(ucs.get_solution('Lalibela'))
    
    # Question 2.3: Customized UCS for multiple goals
    print("\nQuestion 2.3: Customized UCS - Visit All Goal States")
    print("-" * 70)
    goal_states = ['Axum', 'Gondar', 'Lalibela', 'Babile', 'Jimma', 
                   'Bale', 'Sof Oumer', 'Arba Minch']
    print(ucs.get_multiple_goals_solution(goal_states))


if __name__ == "__main__":
    main()



