# Modeling and Solving the Travelling Salesman Problem (TSP) using Reinforcement Learning:

**Objective**:  In the TSP, an agent starts at a designated point and must visit a set of 50 targets, with the goal of minimizing the total travel cost.

**Instructions**: The provided TSP code is available in the marl-ecs-course repository under the Assignment 2 folder. You are expected to solve the problem using the following two approaches:

- Dynamic Programming (DP): Implement either the value iteration or policy iteration method to find the optimal solution.

- Monte Carlo (MC): Solve the TSP using the Monte Carlo method with exploring starts, and compare both the first-visit and every-visit approaches.


###  Run Code
```
python main.py

```

# Results

### Performance Comparison

| Solver                          | Average Return  |
|---------------------------------|-----------------|
| Dynamic Programming              | -59.1517        |
| Monte Carlo                     | -61.8428        |
| Monte Carlo Epsilon-Greedy      | -64.5150        |

## Conclusion

The results indicate the performance of each solver:

- **Dynamic Programming** achieved the best average return, indicating the shortest path on average.
- **Monte Carlo Methods** performed slightly worse but provided reasonable solutions.
- **Epsilon-Greedy Exploration** resulted in a higher average total reward compared to the other methods, suggesting that the added exploration did not significantly improve the solution quality in this case.


