# Experience Replay

# Importing the libraries
import numpy as np
from collections import namedtuple, deque
from scipy.misc import imresize

# Defining one Step
Step = namedtuple('Step', ['state', 'action', 'reward', 'done'])

left = [1, 0, 0, 0, 0, 0, 0]
right = [0, 1, 0, 0, 0, 0, 0]
shoot = [0, 0, 1, 0, 0, 0, 0]
forward = [0, 0, 0, 1, 0, 0, 0]
backward = [0, 0, 0, 0, 1, 0, 0]
turn_left = [0, 0, 0, 0, 0, 1, 0]
turn_right = [0, 0, 0, 0, 0, 0, 1]


actions = [left, right, shoot, forward, backward, turn_left, turn_right]

def get_gray_scale(state):
    state = (state[0] + state[1] + state[2]) / 3
    state = imresize(state, (48,64))
    return state


# Making the AI progress on several (n_step) steps
class NStepProgress:
    def __init__(self, env, ai, n_step):
        self.ai = ai
        self.rewards = []
        self.env = env
        self.n_step = n_step
    
    def __iter__(self):
        state = get_gray_scale(self.env.get_state().screen_buffer)
        history = deque()
        reward = 0.0
        while True:
            action = self.ai(np.array([state]))[0][0]
            r = self.env.make_action(actions[action])
            reward += r
            is_done = self.env.is_episode_finished()
            history.append(Step(state=state, action=actions[action], reward=r, done=is_done))
            while len(history) > self.n_step + 1:
                history.popleft()
            if len(history) == self.n_step + 1:
                yield tuple(history)

            if not is_done:
                state = get_gray_scale(self.env.get_state().screen_buffer)
            if is_done:
                if len(history) > self.n_step + 1:
                    history.popleft()
                while len(history) >= 1:
                    yield tuple(history)
                    history.popleft()

                self.rewards.append(reward)
                reward = 0.0
                history.clear()
                self.env.new_episode()
                state = get_gray_scale(self.env.get_state().screen_buffer)

    def rewards_steps(self):
        rewards_steps = self.rewards
        self.rewards = []
        return rewards_steps


# Implementing Experience Replay
class ReplayMemory:
    def __init__(self, n_steps, capacity = 10000):
        self.capacity = capacity
        self.n_steps = n_steps
        self.n_steps_iter = iter(n_steps)
        self.buffer = deque()

    def sample_batch(self, batch_size): # creates an iterator that returns random batches
        ofs = 0
        vals = list(self.buffer)
        np.random.shuffle(vals)
        while (ofs+1)*batch_size <= len(self.buffer):
            yield vals[ofs*batch_size:(ofs+1)*batch_size]
            ofs += 1

    def run_steps(self, samples):
        while samples > 0:
            entry = next(self.n_steps_iter) # 10 consecutive steps
            self.buffer.append(entry) # we put 200 for the current episode
            samples -= 1
        while len(self.buffer) > self.capacity: # we accumulate no more than the capacity (10000)
            self.buffer.popleft()
