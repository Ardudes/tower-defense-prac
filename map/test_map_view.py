from map_view import MapView
from maps import read_map, Map, clean_map
import pyxel
from pathlib import Path

def test_map_view():
    mv = MapView('pathfind_test')
    m: Map = read_map('pathfind_test')
    # print(mv.display_map)
    w = mv.settings["SCREEN_WIDTH"]
    l = mv.settings["SCREEN_LENGTH"]
    pyxel.init(w, l)
    root_dir = Path(__file__).parent.parent
    path_to_assets = f"{root_dir}/assets/path.pyxres"
    pyxel.load(path_to_assets)
    pyxel.run(mv.update, mv.draw)


test_map_view()


# [['S', '#', '#', '#', '#', '#', '#', '#', '_', '_', '_', '_', '_', '_', '_'], 
#  ['_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_'], 
#  ['S', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '_', '_', '_'], 
#  ['_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_'], 
#  ['_', '_', '_', '_', '_', '_', '_', 'E', '#', '#', '#', '#', '_', '_', '_']]

# [['start', 'isolated', 'isolated', 'isolated', 'isolated', 'isolated', 'isolated', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], 
#  ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], 
#  ['start', 'empty', 'horizontal', 'horizontal', 'horizontal', 'horizontal', 'horizontal', 'intersection', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], 
#  ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'vertical', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'], 
#  ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'end', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']]