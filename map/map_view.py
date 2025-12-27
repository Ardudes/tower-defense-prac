import pyxel
from pathlib import Path
from maps import read_map, Map
import json

class MapTest:
    def __init__(self):
        self.settings = self.get_video_settings()

    def get_video_settings(self) -> dict[str, int]:
        curr_dir = Path(__file__).parent.parent
        p = Path(f"{curr_dir}/vidsettings.json")
        with open(p, 'r') as f:
            settings = json.load(f)
    
        return settings

    def display_map(self, m: Map):
        pass

    def update(self):
        pass

    def draw_map(m: Map):
        

    def draw(self):
        pyxel.cls(0)

    def start_graphics(self, filename: str): # placeholder name
        settings: dict[str, int] = self.get_video_settings()
        m: Map = read_map(filename)
        root_dir = Path(__file__).parent.parent
        path_to_assets = Path(f"{root_dir}/assets")
        pyxel.load(f"{path_to_assets}/path.pyxres")


