# Designing and Implementing a Grid-World Environment for Sokoban Puzzle using Reinforcement Learning


## Environment Overview
The game takes place on a grid where each cell can either be a floor or a wall. Some floor cells contain boxes, while others are marked as storage locations. The objective is to guide a warehouse agent to push the boxes to their designated storage locations while adhering to the following rules:

- The agent can move horizontally or vertically onto empty squares but cannot move through walls or boxes.
- The agent can only push boxes, not pull them, by walking up to them and pushing them to the square directly beyond.
- Boxes cannot be pushed into walls or other boxes.
- The number of boxes equals the number of storage locations.
- The puzzle is solved once all boxes are placed at their respective storage locations.

## Environment Specifications

### Grid Dimensions
The environment consists of a 6 x 7 grid.

### State Space
Each grid cell represents a state. For example, if the agent is located in row 2, column 3, the state is represented as `(2, 3)`.

### Action Space
The agent can move in four possible directions: UP, DOWN, LEFT, RIGHT. It can only push boxes forward and cannot pull them. Some actions may lead to irreversible situations, such as pushing a box into a corner or against the edge of a wall.

### Reward Structure
- The agent receives a reward of -1 if a box is not placed at the storage location.
- A reward of 0 is given when the box reaches its goal location.

### Termination Conditions
- The episode terminates when all boxes are successfully placed in storage locations.
- The environment also terminates if a box gets stuck in an unrecoverable position (e.g., pushed into a corner or against a wall).

## Task
You need to solve this problem using the following two approaches:
1. **Dynamic Programming (DP)**: Implement either value iteration or policy iteration to solve the environment.
2. **Monte Carlo (MC)**: Solve the environment using the Monte Carlo method with exploring starts, and compare both the first-visit and every-visit approaches.


###  Run Code
```
python main.py

```


## Results:

| Metric                    | Dynamic Programming Agent | Monte Carlo Agent       |
|---------------------------|---------------------------|-------------------------|
| **Training Time**         | 19.71 seconds             | 5.14 seconds            |
| **Average Reward**        | -100.00                   | -92.59                  |
| **Average Steps**         | 100.00                    | 93.36                   |

### Comparison

- **Training Time**: The Monte Carlo Agent trained significantly faster than the Dynamic Programming Agent.
- **Average Reward**: Both agents received negative rewards, indicating room for improvement; however, the Monte Carlo Agent performed better.
- **Average Steps**: The Monte Carlo Agent used fewer steps on average to solve the puzzle compared to the Dynamic Programming Agent.
