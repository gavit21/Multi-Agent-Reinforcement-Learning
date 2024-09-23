# mdp_solver.py

import numpy as np

# Define the MDP components: states, actions, rewards, and transition probabilities.

# States in the MDP
states = ['Dormitory', 'LectureHall', 'Cafeteria']

# Possible actions
actions = ['Study', 'Eat']

# Rewards associated with each state
state_rewards = {
    'Dormitory': -1,
    'LectureHall': 3,
    'Cafeteria': 1
}

# Transition probabilities P(s'|s,a)
transition_probs = {
    'Dormitory': {
        'Study': {'Dormitory': 0.5, 'LectureHall': 0.5},
        'Eat': {'Cafeteria': 1.0}
    },
    'LectureHall': {
        'Study': {'LectureHall': 0.7, 'Cafeteria': 0.3},
        'Eat': {'Cafeteria': 0.8, 'LectureHall': 0.2}
    },
    'Cafeteria': {
        'Study': {'LectureHall': 0.6, 'Dormitory': 0.3, 'Cafeteria': 0.1},
        'Eat': {'Cafeteria': 1.0}
    }
}

# Discount factor for future rewards
gamma = 0.9

def value_iteration(states, actions, rewards, transitions, gamma=0.9, epsilon=1e-6):
    """
    Perform value iteration to find the optimal value function and policy.

    Args:
        states (list): List of states in the MDP.
        actions (list): List of possible actions.
        rewards (dict): Rewards for each state.
        transitions (dict): Transition probabilities.
        gamma (float): Discount factor.
        epsilon (float): Threshold for convergence.

    Returns:
        V (dict): Optimal value function.
        policy (dict): Optimal policy mapping states to actions.
    """
    # Initialize the value function arbitrarily
    V = {state: 0 for state in states}

    while True:
        delta = 0
        # Iterate over all states
        for state in states:
            v = V[state]
            # Compute the value for each action
            action_values = []
            for action in actions:
                value = sum(
                    transitions[state][action][next_state] *
                    (rewards[next_state] + gamma * V[next_state])
                    for next_state in transitions[state][action]
                )
                action_values.append(value)
            # Update the value function with the maximum action value
            V[state] = max(action_values)
            # Update delta
            delta = max(delta, abs(v - V[state]))
        # Check for convergence
        if delta < epsilon:
            break

    # Derive the optimal policy
    policy = {}
    for state in states:
        # Choose the action that maximizes the expected value
        best_action = None
        best_value = float('-inf')
        for action in actions:
            value = sum(
                transitions[state][action][next_state] *
                (rewards[next_state] + gamma * V[next_state])
                for next_state in transitions[state][action]
            )
            if value > best_value:
                best_value = value
                best_action = action
        policy[state] = best_action

    return V, policy

def policy_evaluation(policy, states, rewards, transitions, gamma=0.9, epsilon=1e-6):
    """
    Evaluate a policy to find its value function.

    Args:
        policy (dict): Current policy mapping states to actions.
        states (list): List of states in the MDP.
        rewards (dict): Rewards for each state.
        transitions (dict): Transition probabilities.
        gamma (float): Discount factor.
        epsilon (float): Threshold for convergence.

    Returns:
        V (dict): Value function for the given policy.
    """
    V = {state: 0 for state in states}

    while True:
        delta = 0
        for state in states:
            v = V[state]
            action = policy[state]
            V[state] = sum(
                transitions[state][action][next_state] *
                (rewards[next_state] + gamma * V[next_state])
                for next_state in transitions[state][action]
            )
            delta = max(delta, abs(v - V[state]))
        if delta < epsilon:
            break

    return V

def policy_iteration(states, actions, rewards, transitions, gamma=0.9):
    """
    Perform policy iteration to find the optimal policy and value function.

    Args:
        states (list): List of states in the MDP.
        actions (list): List of possible actions.
        rewards (dict): Rewards for each state.
        transitions (dict): Transition probabilities.
        gamma (float): Discount factor.

    Returns:
        V (dict): Optimal value function.
        policy (dict): Optimal policy mapping states to actions.
    """
    # Initialize a random policy
    policy = {state: np.random.choice(actions) for state in states}

    while True:
        # Policy Evaluation
        V = policy_evaluation(policy, states, rewards, transitions, gamma)

        policy_stable = True

        # Policy Improvement
        for state in states:
            old_action = policy[state]
            best_action = None
            best_value = float('-inf')
            for action in actions:
                value = sum(
                    transitions[state][action][next_state] *
                    (rewards[next_state] + gamma * V[next_state])
                    for next_state in transitions[state][action]
                )
                if value > best_value:
                    best_value = value
                    best_action = action
            policy[state] = best_action
            if old_action != best_action:
                policy_stable = False
        # If the policy is stable, we have found the optimal policy
        if policy_stable:
            break

    return V, policy

def display_results(V, policy, method_name):
    """
    Display the optimal value function and policy.

    Args:
        V (dict): Value function.
        policy (dict): Policy mapping states to actions.
        method_name (str): Name of the method used.
    """
    print(f"\nOptimal Value Function from {method_name}:")
    for state in V:
        print(f"V({state}) = {V[state]:.2f}")

    print(f"\nOptimal Policy from {method_name}:")
    for state in policy:
        print(f"π({state}) = {policy[state]}")

def main():
    # Discount factor
    gamma = 0.9

    # Run Value Iteration
    V_vi, policy_vi = value_iteration(
        states, actions, state_rewards, transition_probs, gamma
    )
    display_results(V_vi, policy_vi, "Value Iteration")

    # Run Policy Iteration
    V_pi, policy_pi = policy_iteration(
        states, actions, state_rewards, transition_probs, gamma
    )
    display_results(V_pi, policy_pi, "Policy Iteration")

if __name__ == "__main__":
    main()
