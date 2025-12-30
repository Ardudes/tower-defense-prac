import os
from pathlib import Path
from maps import save_map, read_map, pathfind, Map

def test_save_read():
    new_map: Map = [
        ['_', '_', '_'],
        ['_', 'S', '#'],
        ['_', 'E', '#'],
    ]
    save_map("sample_save", new_map)
    m: Map = read_map("sample_save")
    assert(len(m) == len(new_map))
    for i in range(len(m)):
        assert(m[i] == new_map[i])

    main_dir = Path(__file__).parent.parent
    p = Path(f"{main_dir}/levels/sample_save.lvl")
    os.remove(p)

def test_pathfind():
    m = read_map("pathfind_test")
    print(pathfind(m))
