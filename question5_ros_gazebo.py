"""
Question 5: ROS and Gazebo Implementation
ROS-based pathfinding for three-wheel robot in Gazebo world
"""

from graph_data import FIGURE_5_GRAPH
import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import math


class TravelingEthiopiaRobot:
    """
    ROS-based robot controller using uninformed search (BFS) for pathfinding.
    """
    
    def __init__(self):
        """Initialize ROS node and robot components."""
        rospy.init_node('traveling_ethiopia_robot', anonymous=True)
        
        # Publishers and Subscribers
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        
        # Robot state
        self.current_position = None
        self.current_orientation = None
        self.laser_data = None
        
        # Graph for pathfinding
        self.graph = FIGURE_5_GRAPH
        
        # City coordinates (Cartesian system for Gazebo world)
        # These would be defined in the .world file
        self.city_coordinates = self._initialize_city_coordinates()
        
        rospy.loginfo("Traveling Ethiopia Robot initialized")
    
    def _initialize_city_coordinates(self):
        """
        Initialize Cartesian coordinates for cities in Gazebo world.
        These coordinates should match the .world file.
        """
        # Example coordinates - should match .world file
        coordinates = {
            'Addis Ababa': (0.0, 0.0, 0.0),
            'Adama': (2.0, 0.0, 0.0),
            'Ambo': (-2.0, 0.0, 0.0),
            'Wolkite': (0.0, 2.0, 0.0),
            'Jimma': (2.0, 2.0, 0.0),
            'Worabe': (0.0, 4.0, 0.0),
            'Hossana': (2.0, 4.0, 0.0),
            'Shashemene': (4.0, 4.0, 0.0),
            'Hawassa': (6.0, 4.0, 0.0),
            'Dilla': (8.0, 4.0, 0.0),
            # Add more cities as needed
        }
        return coordinates
    
    def odom_callback(self, msg):
        """Callback for odometry data."""
        self.current_position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation
        # Convert quaternion to euler angles if needed
        self.current_orientation = orientation
    
    def laser_callback(self, msg):
        """Callback for laser scan data."""
        self.laser_data = msg
    
    def bfs_search(self, initial_state, goal_state):
        """
        Breadth-First Search for pathfinding.
        
        Args:
            initial_state: Starting city
            goal_state: Target city
            
        Returns:
            list: Path from initial to goal
        """
        from collections import deque
        
        queue = deque([(initial_state, [initial_state])])
        visited = set()
        
        while queue:
            current, path = queue.popleft()
            
            if current == goal_state:
                return path
            
            if current not in visited:
                visited.add(current)
                
                for neighbor in self.graph.get(current, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def navigate_to_city(self, target_city):
        """
        Navigate robot to target city using pathfinding.
        
        Args:
            target_city: Target city name
        """
        if target_city not in self.city_coordinates:
            rospy.logwarn(f"City {target_city} not found in coordinates")
            return
        
        target_pos = self.city_coordinates[target_city]
        self.move_to_position(target_pos)
    
    def move_to_position(self, target_pos):
        """
        Move robot to target position using simple control.
        
        Args:
            target_pos: Target position (x, y, z)
        """
        rate = rospy.Rate(10)  # 10 Hz
        tolerance = 0.1
        
        while not rospy.is_shutdown():
            if self.current_position is None:
                rate.sleep()
                continue
            
            # Calculate distance and angle to target
            dx = target_pos[0] - self.current_position.x
            dy = target_pos[1] - self.current_position.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < tolerance:
                # Stop
                twist = Twist()
                self.cmd_vel_pub.publish(twist)
                rospy.loginfo("Reached target position")
                break
            
            # Simple proportional control
            angle = math.atan2(dy, dx)
            linear_speed = min(0.5, distance * 0.5)
            angular_speed = angle * 0.5
            
            twist = Twist()
            twist.linear.x = linear_speed
            twist.angular.z = angular_speed
            self.cmd_vel_pub.publish(twist)
            
            rate.sleep()
    
    def execute_path(self, initial_state, goal_state):
        """
        Execute complete path from initial to goal state.
        
        Args:
            initial_state: Starting city
            goal_state: Target city
        """
        rospy.loginfo(f"Finding path from {initial_state} to {goal_state}")
        path = self.bfs_search(initial_state, goal_state)
        
        if path is None:
            rospy.logerr("No path found")
            return
        
        rospy.loginfo(f"Path found: {' -> '.join(path)}")
        
        # Navigate through each city in path
        for city in path:
            rospy.loginfo(f"Navigating to {city}")
            self.navigate_to_city(city)
            rospy.sleep(1)  # Brief pause between cities
        
        rospy.loginfo("Path execution complete")


def main():
    """Main function for ROS node."""
    try:
        robot = TravelingEthiopiaRobot()
        
        # Example: Navigate from Addis Ababa to Jimma
        initial = 'Addis Ababa'
        goal = 'Jimma'
        
        robot.execute_path(initial, goal)
        
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


if __name__ == "__main__":
    main()



