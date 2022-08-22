import os

import argeasy
import tabulate

from .__init__ import __version__
from .counter import count_directory
from .counter import count_file


def main() -> int:
    parser = argeasy.ArgEasy(
        name='pylcount',
        description='Python file line counter',
        version=__version__
    )

    parser.add_argument(
        'count',
        ('Count lines of file/directory. '
         'The next argument must be the file path.')
    )

    parser.add_flag('--ext', 'Count lines with specific extensions', action='append')
    parser.add_flag('--ignore', 'Skip such files', action='append')

    args = parser.parse()

    if args.count:
        filepath = args.count
        ignore_list = args.ignore or []
        ext_list = args.ext or []

        if os.path.isdir(filepath):
            result = count_directory(filepath, ignore=ignore_list, ext=ext_list)
        elif os.path.isfile(filepath):
            result = count_file(filepath)

        print(tabulate.tabulate(result, headers=['File', 'Lines'], tablefmt='pretty'))
