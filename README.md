# Traveling Ethiopia AI Search Problem

**Project Name:** `traveling-ethiopia-ai-search`

This project implements various search algorithms for solving the Traveling Ethiopia search problem, as part of the Artificial Intelligence: Principles and Techniques course at Addis Ababa University Institute of Technology, School of Information Science and Engineering.

## Project Structure

```
.
├── graph_data.py              # Data structures for all graph figures (1-5)
├── question1_bfs_dfs.py       # Question 1: BFS and DFS implementation
├── question2_ucs.py           # Question 2: Uniform Cost Search
├── question3_astar.py         # Question 3: A* Search Algorithm
├── question4_minimax.py       # Question 4: MiniMax for adversarial search
├── question5_ros_gazebo.py    # Question 5: ROS and Gazebo implementation
├── gazebo_world.world         # Gazebo world file with city coordinates
├── robot_model.urdf           # Three-wheel robot URDF model
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Requirements

- Python 3.7+
- ROS (for Question 5)
- Gazebo (for Question 5)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. For Question 5 (ROS/Gazebo):
   - Ensure ROS is installed and sourced
   - Ensure Gazebo is installed
   - Source your ROS workspace

## Usage

### Question 1: Breadth-First Search and Depth-First Search

```bash
python question1_bfs_dfs.py
```

This implements:
- Conversion of state space graph (Figure 1) into adjacency list data structure
- BFS and DFS search algorithms
- Path finding from initial state to goal state

### Question 2: Uniform Cost Search

```bash
python question2_ucs.py
```

This implements:
- UCS from Addis Ababa to Lalibela
- Customized UCS to visit multiple goal states (Axum, Gondar, Lalibela, Babile, Jimma, Bale, Sof Oumer, Arba Minch)

### Question 3: A* Search Algorithm

```bash
python question3_astar.py
```

This implements:
- A* search from Addis Ababa to Moyale
- Uses heuristic values and backward costs from Figure 3

### Question 4: MiniMax Algorithm

```bash
python question4_minimax.py
```

This implements:
- MiniMax algorithm for adversarial search
- Finds best path considering adversary's moves
- Maximizes utility to reach state with good quality coffee

### Question 5: ROS and Gazebo

1. Launch Gazebo with the world file:
```bash
gazebo gazebo_world.world
```

2. Spawn the robot:
```bash
rosrun gazebo_ros spawn_model -file robot_model.urdf -urdf -model three_wheel_robot -x 0 -y 0 -z 0.1
```

3. Run the ROS node:
```bash
python question5_ros_gazebo.py
```

## Algorithm Implementations

### Breadth-First Search (BFS)
- Uses queue data structure
- Explores all nodes at current depth before moving to next level
- Guarantees shortest path (in terms of number of steps)

### Depth-First Search (DFS)
- Uses stack data structure
- Explores as far as possible along each branch
- May not find shortest path but uses less memory

### Uniform Cost Search (UCS)
- Uses priority queue (min-heap)
- Considers path costs
- Guarantees optimal path (minimum cost)

### A* Search
- Combines UCS with heuristic function
- Uses f(n) = g(n) + h(n) where:
  - g(n) = cost from start to node n
  - h(n) = heuristic estimate from n to goal
- More efficient than UCS when heuristic is admissible

### MiniMax Algorithm
- Used for adversarial search
- Agent maximizes utility, adversary minimizes
- Finds best achievable outcome considering opponent's optimal play

## Graph Data Structures

All graphs are stored as Python dictionaries:
- **Figure 1**: Simple adjacency list (no costs)
- **Figure 2**: Weighted graph with backward costs
- **Figure 3**: Weighted graph with heuristics and costs
- **Figure 4**: Adversarial search graph with utilities
- **Figure 5**: Relaxed graph for ROS/Gazebo

## Robot Specifications (Question 5)

- **Type**: Three-wheel robot
- **Sensors**:
  - Proximity sensor (LaserScan)
  - Gyroscope (IMU)
  - RGB Camera
- **Physics**: Full physics engine enabled
- **Control**: ROS-based velocity control

## World File

The Gazebo world file (`gazebo_world.world`) contains:
- All cities from Figure 5 as waypoints
- Cartesian coordinate system
- Ground plane and lighting
- Physics engine configuration

## Results

Each algorithm outputs:
- Path from initial to goal state
- Total cost (where applicable)
- Number of nodes explored
- Step-by-step path breakdown

## Author

Prepared by Natnael Abayneh

## License

This project is for educational purposes as part of the AI Principles and Techniques course.

