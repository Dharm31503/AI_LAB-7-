import numpy as np

def epsilon_greedy(num_trials, epsilon):
    # Initialize variables
    counts = [0, 0]  # Action counts for bandit A and B
    rewards_sum = [0, 0]  # Cumulative rewards for both actions
    
    # Loop over the number of trials
    for t in range(num_trials):
        # Epsilon-greedy action selection
        if np.random.rand() < epsilon:
            action = np.random.randint(2)  # Randomly select action 0 (A) or 1 (B)
        else:
            # Exploit the best known action
            avg_rewards = [rewards_sum[i] / max(1, counts[i]) for i in range(2)]  # Prevent division by zero
            action = np.argmax(avg_rewards)
        
        # Call the appropriate bandit function based on action
        if action == 0:
            reward = binaryBanditA()  # Call binary bandit A function
        else:
            reward = binaryBanditB()  # Call binary bandit B function
        
        # Update counts and rewards
        counts[action] += 1
        rewards_sum[action] += reward
        
        # Optionally, display progress
        print(f'Trial {t+1}: Action {action+1}, Reward {reward}')
    
    # Display final results
    avg_rewards = [rewards_sum[i] / max(1, counts[i]) for i in range(2)]
    print(f'Final average reward for Action 1: {avg_rewards[0]:.2f}')
    print(f'Final average reward for Action 2: {avg_rewards[1]:.2f}')

# Example binary bandit functions (replace these with your actual implementations)
def binaryBanditA():
    return np.random.choice([0, 1], p=[0.7, 0.3])  # Example: 30% success

def binaryBanditB():
    return np.random.choice([0, 1], p=[0.4, 0.6])  # Example: 60% success