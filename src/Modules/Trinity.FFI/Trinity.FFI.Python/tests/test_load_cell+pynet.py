from initialize import *
import timeit
from pprint import pprint
import sys

file_name, cell_type = sys.argv[:2]


@test_fn
def test():
    number = int(3e6)
    cells = [new_cell_pynet(cell_type) for i in range(number)]

    for i in range(number):
        save_cell_pynet(i, cells[i])

    time = timeit.timeit(f"load_cell_pynet(i); i+=1;",
                         number=number,
                         globals={'load_cell_pynet': load_cell_pynet},
                         setup='global i; i=0;')

    title = file_name.replace('+pynet', '').replace('+swig', '').replace('.py', '')
    backend = 'pynet' if 'pynet' in file_name else 'swig'

    stats_info = dict(backend=backend,
                      cell_type=cell_type,
                      time_per_10000=time * 10000 / number,
                      data_size=None)

    res = {title: stats_info}

    return pprint(res) or res
