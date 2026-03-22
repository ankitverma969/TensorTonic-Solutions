import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)

    for episode in episodes:
        G = 0
        T = len(episode)

        states = [s for s, _ in episode]

        # Compute returns backward
        returns = np.zeros(T)
        for t in reversed(range(T)):
            _, reward = episode[t]
            G = reward + gamma * G
            returns[t] = G

        visited = set()

        # Now iterate forward for FIRST visit
        for t in range(T):
            state = states[t]

            if state not in visited:
                visited.add(state)
                returns_sum[state] += returns[t]
                returns_count[state] += 1

    V = np.zeros(n_states)
    mask = returns_count > 0
    V[mask] = returns_sum[mask] / returns_count[mask]

    return V