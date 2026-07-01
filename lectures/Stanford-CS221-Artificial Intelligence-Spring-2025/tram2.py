import os

############################################################
# Modeling

class TransportationMDP(object):
    walkCost = 1
    tramCost = 1
    failProb = 0.5

    def __init__(self, N):
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def actions(self, state):
        results = []
        if state + 1 <= self.N:
            results.append('walk')
        if 2 * state <= self.N:
            results.append('tram')
        return results

    def succProbReward(self, state, action):
        # Return a list of (newState, prob, reward) triples, where:
        # - newState: s' (where I might end up)
        # - prob: T(s, a, s')
        # - reward: Reward(s, a, s')
        results = []
        if action == 'walk':
            results.append((state + 1, 1, -self.walkCost))
        elif action == 'tram':
            results.append((state, self.failProb, -self.tramCost))
            results.append((2 * state, 1 - self.failProb, -self.tramCost))
        return results

    def discount(self):
        return 1.0

    def states(self):
        return list(range(1, self.N + 1))

############################################################
# Inference algorithms

def valueIteration(mdp):
    V = {}  # state -> estimate of V_opt(state)
    pi = {}  # state -> estimate of pi_opt(state)

    # Based on current estimate of V
    def Q(state, action):
        return sum(
            prob * (reward + mdp.discount() * V[newState])
            for newState, prob, reward in mdp.succProbReward(state, action)
        )

    # Initialize
    for state in mdp.states():
        V[state] = 0

    while True:
        newV = {}  # new values at iteration t based on t - 1 (V)

        # Compute new values
        os.system('clear')
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state], pi[state] = 0, None
            else:
                newV[state], pi[state] = max((Q(state, action), action) for action in mdp.actions(state))
            print(('{}: {} {}'.format(state, newV[state], pi[state])))
        #raw_input()

        # Test for convergence
        if max(abs(V[state] - newV[state]) for state in mdp.states()) < 1e-10:
            break

        V = newV


############################################################
# Main

mdp = TransportationMDP(N=27)
#print mdp.actions(10)
#print mdp.succProbReward(3, 'tram')
valueIteration(mdp)
