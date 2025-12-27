# Advanced Search Algorithms

This repository contains my implementations of various search algorithms for the Traveling Ethiopia problem. It was done as part of my AI Principles and Techniques coursework.

## What's Inside

I've implemented five different search algorithms:

- **Question 1**: Breadth-First Search (BFS) and Depth-First Search (DFS)
- **Question 2**: Uniform Cost Search (UCS)
- **Question 3**: A* Search Algorithm
- **Question 4**: MiniMax Algorithm for adversarial search
- **Question 5**: ROS and Gazebo simulation

The graph data for all the problems is in `graph_data.py`. Each question has its own Python file that you can run independently.

## Files Overview

- `question1_bfs_dfs.py` - BFS and DFS implementations
- `question2_ucs.py` - Uniform Cost Search
- `question3_astar.py` - A* search
- `question4_minimax.py` - MiniMax algorithm
- `question5_ros_gazebo.py` - ROS/Gazebo integration
- `graph_data.py` - All the graph data structures
- `gazebo_world.world` - World file for Gazebo
- `robot_model.urdf` - Robot model definition
- `requirements.txt` - Python packages needed

## Getting Started

First, clone this repo and install the dependencies:

```bash
git clone https://github.com/Natiabay/Advanced-search-algorithm.git
cd Advanced-search-algorithm
pip install -r requirements.txt
```

For questions 1-4, you just need Python 3.7 or higher. For question 5, you'll need ROS and Gazebo installed and set up.

## Running the Code

### Question 1: BFS and DFS
```bash
python question1_bfs_dfs.py
```
This converts the state space graph into an adjacency list and runs both BFS and DFS to find paths.

### Question 2: Uniform Cost Search
```bash
python question2_ucs.py
```
Finds the optimal path from Addis Ababa to Lalibela, and also handles visiting multiple cities.

### Question 3: A* Search
```bash
python question3_astar.py
```
Uses A* to find the best path from Addis Ababa to Moyale using the heuristic values.

### Question 4: MiniMax
```bash
python question4_minimax.py
```
Implements MiniMax for the adversarial search problem where we're trying to maximize utility while an adversary tries to minimize it.

### Question 5: ROS/Gazebo
If you have ROS and Gazebo installed:

1. Start Gazebo:
```bash
gazebo gazebo_world.world
```

2. Spawn the robot:
```bash
rosrun gazebo_ros spawn_model -file robot_model.urdf -urdf -model three_wheel_robot -x 0 -y 0 -z 0.1
```

3. Run the script:
```bash
python question5_ros_gazebo.py
```

## Notes on the Algorithms

**BFS** uses a queue and finds the shortest path in terms of steps. **DFS** uses a stack and goes deep first, which can be more memory efficient but might not give you the shortest path.

**UCS** is like BFS but considers the actual costs of edges, so it finds the cheapest path overall.

**A*** combines UCS with a heuristic function. It's usually faster than UCS because it uses the heuristic to guide the search toward the goal.

**MiniMax** is for when you have an opponent. It assumes the opponent will play optimally and finds the best move you can make given that.

## About the Graphs

All the graph data is stored as Python dictionaries in `graph_data.py`. Figure 1 is just a simple adjacency list, Figure 2 has costs, Figure 3 has both costs and heuristics, Figure 4 is for the adversarial problem, and Figure 5 is used for the Gazebo simulation.

## Robot Setup (Question 5)

The robot is a three-wheel design with a proximity sensor, gyroscope, and camera. The world file has all the Ethiopian cities positioned as waypoints.

---

Prepared by Natnael Abayneh
