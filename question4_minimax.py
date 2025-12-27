"""
Question 4: MiniMax Algorithm for Adversarial Search
Implements MiniMax to find best path considering adversary
"""

from graph_data import FIGURE_4_GRAPH, FIGURE_4_UTILITIES


class MiniMaxSearch:
    """
    MiniMax algorithm implementation for adversarial search problem.
    The agent tries to maximize utility while adversary tries to minimize it.
    """
    
    def __init__(self, graph, utilities, initial_state):
        """
        Initialize MiniMax search.
        
        Args:
            graph: Dictionary representing state space graph
            utilities: Dictionary with utility values for terminal nodes
            initial_state: Starting state
        """
        self.graph = graph
        self.utilities = utilities
        self.initial_state = initial_state
        self.nodes_evaluated = 0
    
    def is_terminal(self, state):
        """Check if state is a terminal node."""
        return state in self.utilities
    
    def get_utility(self, state):
        """Get utility value for terminal state."""
        return self.utilities.get(state, 0)
    
    def get_successors(self, state):
        """Get all possible successor states."""
        return self.graph.get(state, [])
    
    def minimax(self, state, is_maximizing, depth=0, max_depth=100):
        """
        MiniMax algorithm with depth limiting.
        
        Args:
            state: Current state
            is_maximizing: True if agent's turn (maximize), False if adversary (minimize)
            depth: Current depth in search tree
            max_depth: Maximum depth to search
            
        Returns:
            tuple: (best_value, best_path)
        """
        self.nodes_evaluated += 1
        
        # Terminal state: return utility
        if self.is_terminal(state):
            return self.get_utility(state), [state]
        
        # Depth limit reached: return heuristic (0 for non-terminal)
        if depth >= max_depth:
            return 0, [state]
        
        successors = self.get_successors(state)
        
        # No successors: return utility if terminal, else 0
        if not successors:
            if self.is_terminal(state):
                return self.get_utility(state), [state]
            return 0, [state]
        
        if is_maximizing:
            # Agent's turn: maximize
            best_value = float('-inf')
            best_path = [state]
            
            for successor in successors:
                value, path = self.minimax(successor, False, depth + 1, max_depth)
                if value > best_value:
                    best_value = value
                    best_path = [state] + path
            
            return best_value, best_path
        else:
            # Adversary's turn: minimize
            best_value = float('inf')
            best_path = [state]
            
            for successor in successors:
                value, path = self.minimax(successor, True, depth + 1, max_depth)
                if value < best_value:
                    best_value = value
                    best_path = [state] + path
            
            return best_value, best_path
    
    def get_best_path(self):
        """
        Find best path from initial state using MiniMax.
        Assumes agent starts (maximizing player).
        
        Returns:
            tuple: (best_utility, best_path, nodes_evaluated)
        """
        self.nodes_evaluated = 0
        utility, path = self.minimax(self.initial_state, is_maximizing=True)
        return utility, path, self.nodes_evaluated
    
    def get_solution(self):
        """
        Get formatted solution.
        
        Returns:
            str: Formatted solution
        """
        utility, path, nodes_evaluated = self.get_best_path()
        
        result = f"MiniMax Search Algorithm\n"
        result += f"Initial State: {self.initial_state}\n"
        result += f"Best Achievable Utility: {utility}\n"
        result += f"Terminal State Reached: {path[-1]}\n"
        result += f"Nodes Evaluated: {nodes_evaluated}\n"
        result += f"Path Length: {len(path) - 1} steps\n"
        result += f"Optimal Path: {' -> '.join(path)}\n"
        
        # Show decision points
        result += "\nDecision Points:\n"
        for i, state in enumerate(path):
            if i < len(path) - 1:
                next_state = path[i + 1]
                if i % 2 == 0:
                    player = "Agent (Maximize)"
                else:
                    player = "Adversary (Minimize)"
                result += f"  Step {i}: {state} [{player}] -> {next_state}\n"
        
        result += f"\nFinal Utility at {path[-1]}: {utility}\n"
        
        return result


def main():
    """Demonstrate MiniMax search."""
    print("=" * 70)
    print("Question 4: MiniMax Algorithm for Adversarial Search")
    print("=" * 70)
    
    # MiniMax from Addis Ababa
    print("\nMiniMax Search from Addis Ababa")
    print("(Agent wants to reach state with good quality coffee)")
    print("-" * 70)
    
    minimax = MiniMaxSearch(FIGURE_4_GRAPH, FIGURE_4_UTILITIES, 'Addis Ababa')
    print(minimax.get_solution())
    
    # Show all terminal utilities
    print("\nTerminal States and Utilities:")
    print("-" * 70)
    for state, utility in sorted(FIGURE_4_UTILITIES.items(), key=lambda x: x[1], reverse=True):
        print(f"  {state}: {utility}")


if __name__ == "__main__":
    main()



