name=input("Krishnendhu: ")
USN=input("1AY24BT023: ")
import time
grid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
]
def print_grid(g):
    for row in g:
        print("".join("█" if cell else "." for cell in row))
    print()
def next_gen(g):
    new = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            count = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    ni, nj = i + x, j + y
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        count += g[ni][nj]
            if g[i][j] == 1 and count in [2, 3]:
                new[i][j] = 1
            if g[i][j] == 0 and count == 3:
                new[i][j] = 1
    return new
for _ in range(6):  # Run 6 steps
    print_grid(grid)
    grid = next_gen(grid)
    time.sleep(0.5)
