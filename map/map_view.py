import pyxel
from pathlib import Path
from maps import Map, pathfind, read_map
import json

type DisplayMap = list[list[str]]

tile_height, tile_width = (16, 16)
asset_map_coords: dict[str, tuple[int, int]] = {
    "horizontal" : (0, 0),
    "vertical" : (16, 0),
    "intersection" : (0, 16),
    "tjointdown" : (16, 16),
    "btrcurve" : (32, 0),
    "ltbcurve" : (48, 0),
    "ttlcurve" : (48, 16),
    "rttcurve" : (32, 16),
    "empty" : (0, 32),
    "start" : (16, 32),
    "end" : (32, 32),
    "isolated" : (48, 32),
    "tjointup" : (0, 48),
    "tjointleft" : (16, 48),
    "tjointright" : (32, 48)
}

class MapView:
    def __init__(self, map_filename: str):
        self.settings = self.get_video_settings()
        self.m = read_map(map_filename)
        self.display_map: DisplayMap = self.make_displaymap(self.m)
        self.camera_x = -100
        self.camera_y = -100

    def get_video_settings(self) -> dict[str, int]:
        curr_dir = Path(__file__).parent.parent
        p = Path(f"{curr_dir}/vidsettings.json")
        with open(p, 'r') as f:
            settings = json.load(f)
    
        return settings

    def show_map(self, scl: float, tile_size: int):
        curr_x, curr_y = (0, 0)
        m = self.display_map
        for i in range(len(m)):
            curr_y = tile_size * i * scl
            for j in range(len(m[0])):
                curr_x = tile_size * j * scl
                tile_type: str = m[i][j]
                u, v = asset_map_coords[tile_type]
                pyxel.blt(curr_x, curr_y, 0, u, v, tile_size, tile_size, scale = scl)
                # print((curr_x, curr_y))

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.camera_y -= 1
        if pyxel.btn(pyxel.KEY_A):
            self.camera_x -= 1
        if pyxel.btn(pyxel.KEY_S):
            self.camera_y += 1
        if pyxel.btn(pyxel.KEY_D):
            self.camera_x += 1
        pass

    def draw(self):
        pyxel.camera(self.camera_x, self.camera_y)
        pyxel.cls(0)
        self.show_map(self.settings["SCALE"], self.settings["TILE_SIZE"])

    def in_bounds(self, i: int, j: int, r: int, c: int) -> bool:
        return 0 <= i < r and 0 <= j < c

    def is_path(self, i: int, j: int, r: int, c: int) -> bool:
        path_tiles: set[str] = {'S', '#', 'E'}
        return self.in_bounds(i, j, r, c) and self.m[i][j] in path_tiles

    def check_surroundings(self, i: int, j: int, r: int, c: int) -> list[bool]:
        vecs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
        ret: list[bool] = []
        for di, dj in vecs:
            ni, nj = i + di, j + dj
            ret.append(self.is_path(ni, nj, r, c)) # type: ignore

        # print(f'{ret}, {(i, j)}, tile: {m[i][j]}')
        assert(len(ret) == 4)
        return ret

    def make_displaymap(self, m: Map) -> DisplayMap:
        ret: DisplayMap = []
        for row in m:
            curr_row = []
            for tile in row:
                match tile:
                    case 'S':
                        curr_row.append('start') # type: ignore
                    case 'E':
                        curr_row.append('end') # type: ignore
                    case _:
                        curr_row.append('empty') # type: ignore

            ret.append(curr_row) # type: ignore

        paths = pathfind(m)
        
        r: int = len(m)
        c: int = len(m[0])
        done: set[tuple[int, int]] = set()
        for path in paths:
            for idx in range(1, len(path) - 1):
                i, j = path[idx]
                if (i, j) not in done:
                    done.add((i, j))
                    up, right, down, left = self.check_surroundings(i, j, r, c)
                    if all([up, right, down, left]):
                        ret[i][j] = 'intersection'
                    elif all([not up, right, not down, left]):
                        ret[i][j] = 'horizontal'
                    elif all([up, down, not left, not right]):
                        ret[i][j] = 'vertical'
                    elif all([not up, not down, not left, not right]):
                        ret[i][j] = 'isolated'
                    elif all([not up, down, left, right]):
                        ret[i][j] = 'tjointdown'
                    elif all([up, not down, left, right]):
                        ret[i][j] = 'tjointup'
                    elif all([up, down, not left, right]):
                        ret[i][j] = 'tjointright'
                    elif all([up, down, left, not right]):
                        ret[i][j] = 'tjointleft'
                    elif all([not up, down, not left, right]):
                        ret[i][j] = 'btrcurve'
                    elif all([up, right, not down, not left]):
                        ret[i][j] = 'rttcurve'
                    elif all([up, left, not right, not down]):
                        ret[i][j] = 'ttlcurve'
                    elif all([left, not up, not right, down]):
                        ret[i][j] = 'ltbcurve'
                    else:
                        pass

        return ret
