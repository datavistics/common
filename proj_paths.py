import re
from pathlib import Path

proj_dir = Path(__file__).parents[1]


def tree(directory):
    """
    Gets all sub_directories under *directory* and puts them in a flat dictionary

    nested subdirs use a . instead of / for the dict key

    :param directory:
    :return:
    """
    d = {}

    # the list comprehension recursively looks for dirs that dont have double underscores or periods
    for path in [f for f in sorted(directory.rglob('*')) if not re.search(r'__|\.', str(f)) and f.is_dir()]:
        path_name = str(path.relative_to(directory)).replace('/', '.')
        d[path_name] = path
    d['proj'] = directory
    return d


print(proj_dir)
dirs = tree(proj_dir)
