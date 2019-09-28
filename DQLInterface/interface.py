from dql_grasping import policies
from dql_grasping import grasping_env
from dql_grasping import run_env
import pygame
from pygame.locals import QUIT, KEYDOWN
from pynput.keyboard import Key, Listener
import numpy as np

env = None
obs = None
import time
done, env_step, episode_reward, episode_data = (False, 0, 0.0, [])


char_to_action = {
    'w': np.array([0, -1, 0, 0, 0]),
    'a': np.array([1, 0, 0, 0, 0]),
    's': np.array([0, 1, 0, 0, 0]),
    'd': np.array([-1, 0, 0, 0, 0]),
    'q': np.array([1, -1, 0, 0, 0]),
    'e': np.array([-1, -1, 0, 0, 0]),
    'z': np.array([1, 1, 0, 0, 0]),
    'c': np.array([-1, 1, 0, 0, 0]),
    'k': np.array([0, 0, 1, 0, 0]),
    'j': np.array([0, 0, -1, 0, 0]),
    'h': np.array([0, 0, 0, 1, 0]),
    'l': np.array([0, 0, 0, -1, 0]),
    'v': np.array([0, 0, 0, 0, 0.1]), 
    'r': 'reset'
}


def startEnv():
    global obs, env, screen
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    resetEnvironment()
    #wait(screen, 5)
    while True:
        action = [0, 0, 0, 0, 0]
        done = False
        for event in pygame.event.get():
            event_happened = True
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                char = event.dict['key']
                new_action = char_to_action.get(chr(char), None)
                if str(new_action) == 'reset':
                    done = True
                elif new_action is not None:
                    action = new_action
                break
        
        stepEnvironment(2 * action)
        #action = [0, 0, 0, 0]
        if done:
            obs = env.reset()
            #wait(screen, 5)
           
def wait(screen, t):
    screen.fill([255, 0, 0])
    pygame.display.update()
    time.sleep(t)
    screen.fill([0, 255, 0])
    pygame.display.update() 

def resetEnvironment():
    global obs, env
    env = grasping_env.KukaGraspingProceduralEnv(
        downsample_width=48, downsample_height=48,
        continuous=True, remove_height_hack=True, render_mode='GUI')
    print(env.action_space)
    obs = env.reset()
    done, env_step, episode_reward, episode_data = (False, 0, 0.0, [])

def stepEnvironment(action):
    global obs, env
    action[4] = 1
    done, env_step, episode_reward, episode_data = (False, 0, 0.0, [])
    new_obs, rew, done, env_debug = env.step(action)

def main():
    startEnv() 
    

if __name__ == '__main__':
    main()
