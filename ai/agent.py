import random
import pickle
import os

class DinoAgent:
    def __init__(self, save_path="q_table.pkl"):
        self.q_table = {}
        self.last_state = None
        self.last_action = None
        self.save_path = save_path
        self.load_q_table()

    def choose_action(self, state):
        state = self.discretize(state)
        if state not in self.q_table:
            self.q_table[state] = [0, 0]
        action = random.choice([0, 1]) if random.random() < 0.1 else self.argmax(self.q_table[state])
        self.last_state = state
        self.last_action = action
        return action

    def learn(self, reward, new_state):
        if self.last_state is None or self.last_action is None:
            return
        state = self.last_state
        action = self.last_action
        new_state = self.discretize(new_state)
        if new_state not in self.q_table:
            self.q_table[new_state] = [0, 0]
        current_q = self.q_table[state][action]
        max_future_q = max(self.q_table[new_state])
        self.q_table[state][action] = current_q + 0.9 * (reward + 0.9 * max_future_q - current_q)
        self.save_q_table()

    def discretize(self, state):
        dist1, h1, dist2, h2, y = state
        return (dist1 // 20, h1 // 10, dist2 // 20, h2 // 10, y // 10)

    def argmax(self, values):
        return values.index(max(values))

    def save_q_table(self):
        with open(self.save_path, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self):
        if os.path.exists(self.save_path):
            with open(self.save_path, 'rb') as f:
                self.q_table = pickle.load(f)

    def reset_q_table(self):
        self.q_table = {}
        if os.path.exists(self.save_path):
            os.remove(self.save_path)
