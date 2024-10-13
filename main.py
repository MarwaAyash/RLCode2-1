
import gym
import numpy as np
import matplotlib.pyplot as plt
from QLearning import QLAgent
from helpers import discretize

######## CONSTANTS ########
EPISODES = 2000

# due to discretization of continuous state
N_STATES = 20 * 20

# push-left, no-push and push-right
N_ACTIONS = 3

# evaluation trials
TRIALS = 10
######## CONSTANTS ########

env = gym.make('MountainCar-v0', render_mode=None)
agent = QLAgent(env=env,
                n_states=N_STATES,
                n_actions=N_ACTIONS,
                lr=0.5,
                discount=0.95)

# Train agent
agent.learn(episodes=EPISODES)

# Evaluate
successes = []
timesteps_per_trial = []
for tr in range(TRIALS):
    state, _ = env.reset()
    env_render = gym.make('MountainCar-v0', render_mode='human')
    state_render, _ = env_render.reset()
    t = 0
    while True:
        env_render.render()
        action = agent.act(discretize(state_render))
        state_render, reward, done, _, info = env_render.step(action)
        t += 1
        if done:
            print(f"Trial {tr} finished after {t} timesteps")
            timesteps_per_trial.append(t)
            if t < 200:
                successes.append(1)
            else:
                successes.append(0)
            break
    env_render.close()

print(f"Success: {sum(successes)}/{TRIALS}")

env.close()

# Créer la figure et les sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Graphique des succès/échecs
ax1.plot(range(1, len(successes)+1), successes, 'bo-')
ax1.set_xlabel('Numéro d\'essai')
ax1.set_ylabel('Succès (1) / Échec (0)')
ax1.set_title('Résultats des essais')
ax1.set_ylim(-0.1, 1.1)
ax1.grid(True)

# Graphique des pas de temps par essai
ax2.plot(range(1, len(timesteps_per_trial)+1), timesteps_per_trial, 'ro-')
ax2.set_xlabel('Numéro d\'essai')
ax2.set_ylabel('Nombre de pas de temps')
ax2.set_title('Pas de temps par essai')
ax2.grid(True)

# Ajouter des statistiques textuelles
stats_text = f"Taux de succès : {sum(successes)/len(successes):.2%}\n"
stats_text += f"Moyenne des pas de temps : {np.mean(timesteps_per_trial):.2f}\n"
stats_text += f"Médiane des pas de temps : {np.median(timesteps_per_trial):.2f}"
fig.text(0.1, 0.01, stats_text, fontsize=12, verticalalignment='bottom')

# Ajuster la mise en page et afficher
plt.tight_layout()
plt.show()




"""
import gym
import numpy as np
from QLearning import QLAgent
from helpers import discretize

######## CONSTANTS ########
EPISODES = 2000

# due to discretization of continuous state
N_STATES = 20 * 20

# push-left, no-push and push-right
N_ACTIONS = 3

# evaluation trials
TRIALS = 10
######## CONSTANTS ########

env = gym.make('MountainCar-v0', render_mode=None)
agent = QLAgent(env=env,
                n_states=N_STATES,
                n_actions=N_ACTIONS,
                lr=0.5,
                discount=0.95)

# Train agent
agent.learn(episodes=EPISODES)

# Evaluate
success = 0
for tr in range(TRIALS):
    state, _ = env.reset()
    env_render = gym.make('MountainCar-v0', render_mode='human')
    state_render, _ = env_render.reset()
    t = 0
    while True:
        env_render.render()
        action = agent.act(discretize(state_render))
        state_render, reward, done, _, info = env_render.step(action)
        t += 1
        if done:
            print(f"Trial {tr} finished after {t} timesteps")
            if t < 200:
                success += 1
            break
    env_render.close()

print(f"Success: {success}/{TRIALS}")

env.close()


"""


