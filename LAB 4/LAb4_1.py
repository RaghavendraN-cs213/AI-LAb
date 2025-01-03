import heapq
import numpy as np

goal = [[2,8,1], [0,4,3], [7,6,5]]
vis = set()
q = []
parent_map = {}
move_map = {}

def manhattan(curr):
    ans = 0
    pos = {goal[i][j]: (i, j) for i in range(3) for j in range(3)}
    for i in range(3):
        for j in range(3):
            x, y = pos[curr[i][j]]
            ans += abs(i - x) + abs(j - y)
    return ans

def moves(curr,g):
    x, y = [(i, j) for i in range(3) for j in range(3) if curr[i][j] == 0][0]
    poss = [[0, -1, 'left'], [-1, 0, 'up'], [1, 0, 'down'], [0, 1, 'right']]
    for dx, dy, direction in poss:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            curr1 = [row[:] for row in curr]
            curr1[x][y], curr1[nx][ny] = curr1[nx][ny], curr1[x][y]
            tuple_curr1 = tuple(map(tuple, curr1))
            if tuple_curr1 not in vis:
                f=g+1+manhattan(curr1)
                heapq.heappush(q, (f, curr1,g+1))
                vis.add(tuple_curr1)
                parent_map[tuple(map(tuple, curr1))] = curr
                move_map[tuple(map(tuple, curr1))] = direction

def a_star(curr,g):
    vis.add(tuple(map(tuple, curr)))
    if curr == goal:
        return True
    moves(curr,g)
    if q:
        curr = heapq.heappop(q)
        if a_star(curr[1],curr[2]):
            return True
    return False

def display_board(board):
    print("+---+---+---+")
    for row in board:
        print("| " + " | ".join(str(x) if x != 0 else ' ' for x in row) + " |")
        print("+---+---+---+")

c =[[] for i in range(3)]
for i in range(3):
  print(f"Enter elements of row {i+1}")
  c[i]=list(map(int,input().split()))
a_star(c,0)

result_path = []
directions = []
state = goal
while state:
    result_path.append(state)
    directions.append(move_map.get(tuple(map(tuple, state)), None))
    state = parent_map.get(tuple(map(tuple, state)))

for ind, (state, direction) in enumerate(reversed(list(zip(result_path, directions)))):
    print(f"Step {ind}:")
    display_board(state)
    if ind==0:
      print("Initial state")
    if direction:
        print(f" Move empty space {direction}")
    print()

print(f"Steps taken: {len(result_path) - 1}")
