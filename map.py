from enum import Enum, auto
from pathlib import Path
from collections import deque

class Tile(Enum):
    TILE_PATH = '#'
    TILE_VOID = ' '
    TILE_TOWER_SPOT = '_'
    TILE_PATH_START = 'S'
    TILE_PATH_END = 'E'
    TILE_MINE = 'M'

class Tower(Enum):
    TOWER_ARROW = '1' # Generic single-target tower
    TOWER_ICE = '2' # Slow/freeze tower
    TOWER_FIREBALL = '3' # AoE tower
    TOWER_MINE = '4' # Income tower
    TOWER_BALLISTA = '5' # High-damage, low fire-rate tower

type Map = list[list[str]]

def read_map(filename: str):
    # searches for a specific directory
    current_dir = Path(__file__).parent
    path = Path(f"{current_dir}/levels/{filename}.lvl")
    print(path)
    Map = []
    with open(path, 'r') as f:
        for r in f:
            map_row = []    
            for ch in r:
                if ch != "\n":
                    map_row.append(ch)
            Map.append(map_row)
            map_row = []

    # print(Map)
    return Map


def save_map(filename: str, m: Map):
    path = f"levels/{filename}.lvl"
    with open(path, 'w') as f:
        for row in m:
            assert(isinstance(row, str))
            f.write(f"{''.join(row)}\n")


def print_map(m: Map):
    for row in m:
        print(row)

def pathfind(m: Map):
    # uses BFS to check if a valid path from S to E exists.
    # If one exists, return the path as a list of coordinate pairs.
    r = len(m)
    c = len(m[0])
    memo = [[0] * c for _ in range(r)]
    Path_Tiles = {'S', '#', 'E'}

    def find_end():
        for i in range(r):
            for j in range(c):
                if m[i][j] == 'E':
                    memo[i][j] = 1
                    return (i, j)

    def in_bounds(i, j):
        return 0 <= i < r and 0 <= j < c

    def neighbors(i, j):
        assert(m[i][j] in Path_Tiles)
        vecs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ret = []
        for vec in vecs:
            di, dj = vec
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj) and m[ni][nj] in {'#', 'S'}:
                ret.append((ni, nj))
        return ret

    def BFS(si, sj):

        starts = set()
        prevs = {}
        paths = []
        kyu = deque([])
        kyu.append((si, sj))
        prevs[(si, sj)] = None
        memo[si][sj] = 1

        while kyu:
            ci, cj = kyu.popleft()
            if m[ci][cj] == 'S':
                starts.add((ci, cj))
                continue

            else:
                for ni, nj in neighbors(ci, cj):
                    if memo[ni][nj] == 0:
                        kyu.append((ni, nj))
                        prevs[(ni, nj)] = (ci, cj)
                        memo[ni][nj] = 1

        for start in starts:
            curr_path = []
            curr_loc = start
            while curr_loc != None:
                curr_path.append(curr_loc)
                curr_loc = prevs[(curr_loc)]
            paths.append(curr_path)

    si, sj = find_end()
    BFS(si, sj)











