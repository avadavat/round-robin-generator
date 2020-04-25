def apply_offset(p, n, o):
    if p == 1:
        return 1
    # Take the list of players 1 2 3 4 5 6, with offset 2, ignore the 1
    # Start with 2 3 4 5 6, we want 4 5 6 2 3
    # Shift down to 0 1 2 3 4 (p - 2)
    # Apply the offset -2 -1 0 1 2 (p - o)
    # Scale up 2 3 4 5 6 (p + (n-1))
    # Mod by (p-1) 2 3 4 0 1
    # Shift back up: 4 5 6 2 3

    s = n - 1
    return ((p - 2 - o + s) % s) + 2

# Generates the matchups for n players playing the r-th round of the tournament
def generate_matchups(n, r):
    if n <= 0:
        raise Exception('Number of players must be positive')
    if r <= 0 or r >= n:
        raise Exception('Round number must be within [1,n-1]')

    # Circle method, bottom array will have more than the bottom
    top = [(x+1) for x in range(n // 2)]
    bottom = [(x+1) for x in range(n // 2, n)]

    # Reverse bottom
    bottom.reverse()

    # Change offsets based on round
    offset = r - 1

    def rotate(arr):
        new_arr = []
        for a in arr:
            new_arr.append(apply_offset(a, n, offset))
        return new_arr

    top = rotate(top)
    bottom = rotate(bottom)

    # Match players
    matchups = []
    for i in range(len(top)):
        matchups.append((top[i], bottom[i]))

    return matchups


players = 6
for r in range(1, players):
    print('Round ' + str(r))
    print(generate_matchups(players, r))
