from dql_grasping import policies
from dql_grasping import grasping_env
from dql_grasping import run_env
import pygame
from pygame.locals import QUIT, KEYDOWN
from pynput.keyboard import Key, Listener
#pip install pygame
env = None
obs = None
done, env_step, episode_reward, episode_data = (False, 0, 0.0, [])

char_to_action = {
    'w': [0, -1, 0, 0],
    'a': [1, 0, 0, 0],
    's': [0, 1, 0, 0],
    'd': [-1, 0, 0, 0],
    'q': [1, -1, 0, 0],
    'e': [-1, -1, 0, 0],
    'z': [1, 1, 0, 0],
    'c': [-1, 1, 0, 0],
    'k': [0, 0, 1, 0],
    'j': [0, 0, -1, 0],
    'h': 'close',
    'l': 'open',
    'x': 'toggle',
    'r': 'reset',
    'p': 'put obj in hand',
}


def startEnv():
    global obs, env
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    resetEnvironment()
    while True:
        action = [0, 0, 0, 0]
        done = False
        for event in pygame.event.get():
            event_happened = True
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                char = event.dict['key']
                new_action = char_to_action.get(chr(char), None)
                if new_action == 'toggle':
                    print('toggle')
                elif new_action == 'reset':
                    done = True
                elif new_action == 'close':
                    action[3] = 1
                elif new_action == 'open':
                    action[3] = -1
                elif new_action == 'put obj in hand':
                    print("putting obj in hand")
                    action[3] = 1
                elif new_action is not None:
                    action[:3] = new_action[:3]
 
        stepEnvironment(action)
        if done:
            obs = env.reset()

def resetEnvironment():
    global obs, env
    env = grasping_env.KukaGraspingProceduralEnv(
        downsample_width=48, downsample_height=48,
        continuous=True, remove_height_hack=True, render_mode='GUI')
    obs = env.reset()
    done, env_step, episode_reward, episode_data = (False, 0, 0.0, [])

def stepEnvironment(action):
    global obs, env
    done, env_step, episode_reward, episode_data = (False, 0, 0.0, [])
    new_obs, rew, done, env_debug = env.step(action)

def main():
    startEnv() 
    
    print("Wow this actually worked???!!??!!??!?!?!")
    print("The mighty snek has looked favorably down upon us")

if __name__ == '__main__':
    main()
