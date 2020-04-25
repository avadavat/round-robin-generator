
# Generates the matchups for n players playing the r-th round of the tournament


def generate_matchups(n, r):
    if n <= 0:
        raise Exception('Number of players must be positive')
    if r <= 0 or r >= n:
        raise Exception('Round number must be within [1,n-1]')

    # Circle method, bottom array will have more than the bottom
    top = [x for x in range(n // 2)]
    bottom = [x for x in range(n // 2, n)]

    # Reverse bottom
    bottom.reverse()

    # Change offsets based on round

    print(top, bottom)

    # delta = n // 2
    # offset = r - 1

    # matchups = []

    # for i in range(n-1):
    #     home = (i + offset) % n
    #     away = (home + delta) % n
    #     matchups.append((home, away))

    # return matchups


players = 6
for i in range(1, players):
    print('Round ' + str(i))
    print(generate_matchups(players, i))

# print(generate_matchups(6, 1))
