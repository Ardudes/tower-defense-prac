from map import save_map, read_map, pathfind
import os
from pathlib import Path

def test_save_read():
    new_map = [
        ['_', '_', '_'],
        ['_', 'S', '#'],
        ['_', 'E', '#'],
    ]
    save_map("sample_save", new_map)
    m = read_map("sample_save")
    assert(len(m) == len(new_map))
    for i in range(len(m)):
        assert(m[i] == new_map[i])

    current_dir = Path("__file__").parent
    p = Path(f"{current_dir}/levels/sample_save.lvl")
    os.remove(p)

def test_pathfind():
    m = read_map("pathfind_test")
    pathfind(m)

test_pathfind()