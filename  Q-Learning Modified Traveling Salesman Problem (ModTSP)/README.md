# Modified Travelling Salesman Problem (TSP) using Q-Learning
**Objective**:

Model and solve a modified version of the Travelling Salesman Problem (TSP) using a Temporal Difference (TD)-based reinforcement learning algorithm. In this version of the TSP, each target has an associated profit that decays linearly with the distance travelled, described by the formula:

- `p_i = p_i - dist_so_far()`


Where:

- `p_i` is the profit of the target.
- `dist_so_far()` is the distance travelled so far.

The problem involves 10 fixed targets whose profit values are shuffled across the targets after every `k` episodes. The goal is to visit each target in a sequence that maximizes the total collected profit.

# Solution

### Requirements
~~~
pip install requirements.txt
~~~

###  Run Code
```
python q_learning.py

```
### Results

- 1) Below is the episode vs cumulative reward plot that illustrates the training convergence.

![Episode vs. Cumulative Reward](https://github.com/MOONLABIISERB/marl-ecs-course/blob/gavit_20114/MidSem/episode_rewards_plot.png) <!-- Ensure the link is accessible -->


| Metric                       | Value       |
|------------------------------|-------------|
| Total Episodes                | 10,000      |
| Average Reward                | 275.53       |
| Maximum Reward Achieved       | 515.05          |
| Final Epsilon (Exploration Rate) | 0.0100   |


- 2) Lets train and evaluate on different hyperparameters.



### Hyperparameter Comparison

- Run Code
```
python train_evaluate.py

```

The following hyperparameters were tested to evaluate performance:

| Learning Rate | Discount Factor | Epsilon Decay |
|---------------|-----------------|----------------|
| 0.01          | 0.85            | 0.9995         |
| 0.01          | 0.9             | 0.999          |
| 0.05          | 0.85            | 0.999          |
| 0.1           | 0.9             | 0.995          |


 convergence graph of all models test on vairous hyperparameters

 ![Episode vs. Cumulative Reward](https://github.com/gavit21/Multi-Agent-Reinforcement-Learning/blob/main/%20Q-Learning%20Modified%20Traveling%20Salesman%20Problem%20(ModTSP)/all_models_training_rewards.png)

 test reward comparision of all models

 ![Episode vs. Cumulative Reward](https://github.com/gavit21/Multi-Agent-Reinforcement-Learning/blob/main/%20Q-Learning%20Modified%20Traveling%20Salesman%20Problem%20(ModTSP)/test_reward_comparison.png)



### Conclusion

The Q-Learning agent effectively tackled the Modified Traveling Salesman Problem (ModTSP) by learning to navigate through targets efficiently over 10,000 training episodes. The agent exhibited significant performance improvements, as shown by the increasing average rewards and achieving a high maximum reward. The implementation of an epsilon-greedy policy facilitated a balanced exploration and exploitation strategy, enabling the discovery of optimal routes.

#### Key Observations:

1. **Performance Enhancement:** The consistent improvement in rewards indicates successful learning and policy optimization.
2. **Epsilon Decay Effectiveness:** The gradual reduction of the exploration rate allowed the agent to focus on exploiting learned strategies while maintaining minimal exploration.
3. **Scalability Considerations:** Although the agent performed well with 10 targets, scaling to larger problem sizes may necessitate advanced techniques such as state abstraction or deep reinforcement learning.

# Thank You !! 😊
