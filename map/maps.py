from enum import Enum
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
    TOWER_ICE = '2' # Slow/freeze tower, reduces enemies' speed stat
    TOWER_FIREBALL = '3' # AoE tower
    TOWER_MINE = '4' # Income tower
    TOWER_BALLISTA = '5' # High-damage, low fire-rate tower

type Map = list[list[str]]
type pair = tuple[int, int]

def read_map(filename: str) -> Map:
    # searches the levels directory given a filename
    current_dir = Path(__file__).parent
    main_dir = current_dir.parent
    path = Path(f"{main_dir}/levels/{filename}.lvl")
    ret: Map = []
    with open(path, 'r') as f:
        for r in f:
            map_row: list[str] = []    
            for ch in r:
                if ch != "\n":
                    map_row.append(ch)
            ret.append(map_row)
            map_row = []

    return ret

def save_map(filename: str, m: Map):
    current_dir = Path(__file__).parent
    main_dir = current_dir.parent
    path = f"{main_dir}/levels/{filename}.lvl"
    print(path)
    with open(path, 'w') as f:
        for row in m:
            f.write(f"{''.join(row)}\n")

def clean_map(m: Map):
    paths = pathfind(m)
    r = len(m)
    c = len(m[0])
    ret: Map = [['_'] * c for _ in range(r)]
    for path in paths:
        si, sj = path[0]
        m[si][sj] = 'S'
        for i in range(1, len(path) - 1):
            ci, cj = path[i]
            m[ci][cj] = '#'
        ei, ej = path[-1]
        m[ei][ej] = 'E'

    return ret

def print_map(m: Map):
    for row in m:
        print(row)

def pathfind(m: Map) -> list[list[pair]]:
    # uses BFS starting from E to check for paths from E to S.
    r: int = len(m)
    c: int = len(m[0])
    memo: list[list[int]] = [[0] * c for _ in range(r)]
    Path_Tiles = {'S', '#', 'E'}

    def find_end() -> pair | None:
        for i in range(r):
            for j in range(c):
                if m[i][j] == 'E':
                    memo[i][j] = 1
                    return (i, j)

    def in_bounds(i: int, j: int) -> bool:
        return 0 <= i < r and 0 <= j < c

    def neighbors(i: int, j: int) -> list[pair]:
        assert(m[i][j] in Path_Tiles)
        vecs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ret: list[tuple[int, int]] = []
        for vec in vecs:
            di, dj = vec
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj) and m[ni][nj] in {'#', 'S'}:
                ret.append((ni, nj))
        return ret

    def BFS(si: int, sj: int):

        starts: list[pair] = []
        prevs = {}
        paths: list[list[pair]] = []
        kyu: deque[pair] = deque([])
        kyu.append((si, sj))
        prevs[(si, sj)] = None
        memo[si][sj] = 1

        while kyu:
            curr: pair = kyu.popleft()
            ci: int = curr[0]
            cj: int = curr[1]
            if m[ci][cj] == 'S':
                starts.append((ci, cj))
                continue

            else:
                for ni, nj in neighbors(ci, cj):
                    if memo[ni][nj] == 0:
                        kyu.append((ni, nj))
                        prevs[(ni, nj)] = (ci, cj)
                        memo[ni][nj] = 1

        for i in range(len(starts)):
            curr_path: list[pair] = []
            curr_loc: pair = starts[i]
            while curr_loc != None:
                curr_path.append(curr_loc) # type: ignore
                curr_loc: pair = prevs[(curr_loc)] # type: ignore
            paths.append(curr_path)
            curr_path = []

        return paths

    p: pair | None = find_end()
    if p == None:
        raise ValueError("The map is invalid and lacks a path end tile.")
    else:
        si: int = p[0]
        sj: int = p[1]
        
    ret: list[list[pair]] = BFS(si, sj)
    return ret
