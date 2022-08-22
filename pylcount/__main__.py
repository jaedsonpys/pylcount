import argeasy

from .__init__ import __version__


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
