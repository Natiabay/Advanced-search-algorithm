# Test script to run all questions

import sys

def run_question(question_num, module_name):
    """Run a question module."""
    print(f"\n{'='*70}")
    print(f"Running Question {question_num}")
    print(f"{'='*70}")
    try:
        __import__(module_name)
    except Exception as e:
        print(f"Error running {module_name}: {e}")
        return False
    return True

def main():
    """Run all the questions."""
    questions = [
        (1, 'question1_bfs_dfs'),
        (2, 'question2_ucs'),
        (3, 'question3_astar'),
        (4, 'question4_minimax'),
    ]
    
    print("="*70)
    print("Traveling Ethiopia Search Problem - All Questions")
    print("="*70)
    
    results = []
    for q_num, module in questions:
        success = run_question(q_num, module)
        results.append((q_num, success))
    
    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    for q_num, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"Question {q_num}: {status}")
    
    print("\nNote: Question 5 requires ROS and Gazebo to be running.")
    print("Please run it separately in a ROS environment.")

if __name__ == "__main__":
    main()



