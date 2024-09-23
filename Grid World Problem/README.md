    # Question 2: Optimal Values and Policies

# Grid World MDP Solver

This project implements Value Iteration and Policy Iteration algorithms to solve a grid-based Markov Decision Process (MDP). The environment is a grid world with obstacles, a start position, a goal, and a tunnel (wormhole) that connects two points.

### Optimal Values

| Rows | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     |
|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 0    | 0.914 | 0.923 | 0.932 | 0.923 | 0.914 | 0.904 | 0.895 | 0.886 | 0.878 |
| 1    | 0.923 | 0.932 | 0.941 | 0.000 | 0.904 | 0.895 | 0.886 | 0.878 | 0.869 |
| 2    | 0.932 | 0.941 | 0.951 | 0.000 | 0.895 | 0.886 | 0.878 | 0.869 | 0.860 |
| 3    | 0.923 | 0.000 | 0.000 | 0.000 | 0.886 | 0.878 | 0.869 | 0.860 | 0.851 |
| 4    | 0.914 | 0.904 | 0.895 | 0.886 | 0.878 | 0.869 | 0.860 | 0.851 | 0.843 |
| 5    | 0.904 | 0.895 | 0.886 | 0.877 | 0.869 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6    | 0.895 | 0.886 | 0.878 | 0.869 | 0.860 | 0.000 | 0.961 | 0.970 | 0.980 |
| 7    | 0.886 | 0.878 | 0.869 | 0.860 | 0.851 | 0.000 | 0.970 | 0.980 | 0.990 |
| 8    | 0.878 | 0.869 | 0.860 | 0.851 | 0.843 | 0.000 | 0.980 | 0.990 | 1.000 |

### Optimal Policies

| Rows | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
|------|------|------|------|------|------|------|------|------|------|
| 0    | up   | up   | up   | left | left | left | left | left | left |
| 1    | up   | up   | up   | up   | down | down | down | down | down |
| 2    | right| right| down | up   | down | down | down | down | down |
| 3    | down | up   | up   | up   | down | down | down | down | down |
| 4    | down | left | left | left | down | down | down | down | down |
| 5    | down | down | down | down | down | up   | up   | up   | up   |
| 6    | down | down | down | down | down | up   | up   | up   | up   |
| 7    | down | down | down | down | down | up   | up   | up   | up   |
| 8    | down | down | down | down | down | up   | right| right| up   |

### Quiver Plot
![alt text](https://github.com/MOONLABIISERB/marl-ecs-course/blob/gavit_20114/Assignment-1/value_iteration.png)


## b) Policy Iteration

### Optimal Values

| Rows | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     |
|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 0    | 0.914 | 0.923 | 0.932 | 0.923 | 0.914 | 0.904 | 0.895 | 0.886 | 0.878 |
| 1    | 0.923 | 0.932 | 0.941 | 0.000 | 0.904 | 0.895 | 0.886 | 0.878 | 0.869 |
| 2    | 0.932 | 0.941 | 0.951 | 0.000 | 0.895 | 0.886 | 0.878 | 0.869 | 0.860 |
| 3    | 0.923 | 0.000 | 0.000 | 0.000 | 0.886 | 0.878 | 0.869 | 0.860 | 0.851 |
| 4    | 0.914 | 0.904 | 0.895 | 0.886 | 0.878 | 0.869 | 0.860 | 0.851 | 0.843 |
| 5    | 0.904 | 0.895 | 0.886 | 0.877 | 0.869 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6    | 0.895 | 0.886 | 0.878 | 0.869 | 0.860 | 0.000 | 0.961 | 0.970 | 0.980 |
| 7    | 0.886 | 0.878 | 0.869 | 0.860 | 0.851 | 0.000 | 0.970 | 0.980 | 0.990 |
| 8    | 0.878 | 0.869 | 0.860 | 0.851 | 0.843 | 0.000 | 0.980 | 0.990 | 1.000 |

### Optimal Policies

| Rows | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
|------|------|------|------|------|------|------|------|------|------|
| 0    | up   | up   | up   | left | left | left | left | left | left |
| 1    | up   | up   | up   | up   | down | down | down | down | down |
| 2    | right| right| down | up   | down | down | down | down | down |
| 3    | down | up   | up   | up   | down | down | down | down | down |
| 4    | down | left | left | left | down | down | down | down | down |
| 5    | down | down | down | down | down | up   | up   | up   | up   |
| 6    | down | down | down | down | down | up   | up   | up   | up   |
| 7    | down | down | down | down | down | up   | up   | up   | up   |
| 8    | down | down | down | down | down | up   | right| right| up   |

### Quiver Plot
![alt text](https://github.com/MOONLABIISERB/marl-ecs-course/blob/gavit_20114/Assignment-1/policy_iteratioin.png)

