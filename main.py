import numpy as np


N_VOTERS = 100
N_ALTERNATIVES = 4


def generate_initial_ballots():
    ballots = []
    for _ in range(N_VOTERS):
        ballots.append(np.random.permutation(N_ALTERNATIVES))

    return np.array(ballots)


def calculate_plurality_winner(ballots):
    first_only = ballots[:, 0]
    alternatives, votes = np.unique(first_only, return_counts=True)
    tally = dict(zip(alternatives, votes))
    return max(tally, key=tally.get)


def main():
    ballots = generate_initial_ballots()
    print(calculate_plurality_winner(ballots))


if __name__ == '__main__':
    main()