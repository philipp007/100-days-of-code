from image_processing import get_gray_scale
from vizdoom import *
import random
import time
import matplotlib
from matplotlib import pyplot as plt


def draw_image(buffer, map):
    if map is None:
        map = plt.imshow(buffer)
    else:
        map.set_data(buffer)

    plt.pause(0.000005)
    return map



game = DoomGame()
game.load_config("scenarios/basic.cfg")
number_actions = 3
game.init()

shoot = [0, 0, 1]
left = [1, 0, 0]
right = [0, 1, 0]
actions = [shoot, left, right]

plt.ion()

map = None

episodes = 10
for i in range(episodes):
    game.new_episode()
    while not game.is_episode_finished():
        state = game.get_state()
        img = state.screen_buffer
        img_gray = get_gray_scale(img)
        map = draw_image(img_gray, map)
        misc = state.game_variables
        reward = game.make_action(random.choice(actions))
        print("\treward:", reward)
        time.sleep(0.02)
    print("Result:", game.get_total_reward())
    time.sleep(2)