from dql_grasping import policies

class UserInputPolicy(policies.Policy):
  """ Policy with keyboard user input for continuous action space without height hack"""

  def __init__(self):
    self._height_hack_prob = height_hack_prob
    self._action_space = spaces.Box(low=-1, high=1, shape=(4,))

  def reset(self):
    pass

  def restore(self, checkpoint):
    pass

  def sample_action(self, obs, explore_prob):
    del explore_prob
    dx, dy, dz, da = self._action_space.sample()
    if np.random.random() < self._height_hack_prob:
      dz = -1
    return [dx, dy, dz, da], None


def main():
    print("Wow this actually worked???!!??!!??!?!?!")

if __name__ == '__main__':
    main()
