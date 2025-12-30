import pyxel

# magic numbers:
# in the draw_x_path() functions, pyxel.blt is called with
# w and h parameters = 16 since that's the size (in pixels) of each tile.

# x, y coordinates for the different path tiles:
# 0, 0 - horizontal
# 16, 0 - vertical
# 0, 16 - intersection
# 16, 16 - T-joint
# 32, 0 - bottom to right curve
# 48, 0 - left to bottom curve
# 48, 16 - top to left curve
# 32, 16 - right to top curve

tile_height, tile_width = (16, 16)
asset_map_coords: dict[str, tuple[int, int]] = {
    "horizontal" : (0, 0),
    "vertical" : (16, 0),
    "intersection" : (0, 16),
    "tjoint" : (16, 16),
    "btrcurve" : (32, 0),
    "ltbcurve" : (48, 0),
    "ttlcurve" : (48, 16),
    "rttcurve" : (32, 16),
    "empty" : (0, 32),
    "start" : (16, 32),
    "end" : (32, 32)
}

class Test:
    def __init__(self, length: int, height: int):
        pyxel.init(length, height)

    def load_tile_assets(self):
        pyxel.load("path.pyxres")

    def draw_path_end(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["end"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def draw_path_start(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["start"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def draw_path_horizontal(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["horizontal"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def draw_path_vertical(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["vertical"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def draw_path_tjoint(self, x: int, y: int, rot: int, scl: float):
        u, v = asset_map_coords["tjoint"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, rotate = rot, scale = scl)
    
    def draw_path_intersection(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["intersection"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)
    
    def draw_path_btr(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["btrcurve"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def draw_path_ltb(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["ltbcurve"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)
    
    def draw_path_ttl(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["ttlcurve"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)
    
    def draw_path_rtt(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["rttcurve"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def draw_empty_tile(self, x: int, y: int, scl: float):
        u, v = asset_map_coords["empty"]
        pyxel.blt(x, y, 0, u, v, tile_height, tile_width, scale = scl)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        tsl: int = 64
        scl = tsl / 16
        self.draw_path_horizontal(0, 0 + 100, scl)
        self.draw_path_horizontal(tsl, 0 + 100, scl)
        self.draw_path_horizontal(tsl*2, 0 + 100, scl)
        self.draw_path_horizontal(tsl*3, 0 + 100, scl)
        self.draw_path_ltb(tsl*4, 0 + 100, scl)
        self.draw_path_vertical(tsl*4, tsl + 100, scl)
        self.draw_path_vertical(tsl*4, tsl*2 + 100, scl)
        self.draw_path_vertical(tsl*4, tsl*3 + 100, scl)

    def run(self):
        self.load_tile_assets()
        pyxel.run(self.update, self.draw)
    
a = Test(500, 500)
a.run()