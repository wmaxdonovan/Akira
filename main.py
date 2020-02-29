# !/usr/bin/env python3

import util
import file_shift


def main():

    base_dir = util.get_base_dir()
    download_dir = base_dir / 'Downloads'
    file_shift()


if __name__ == '__main__':
    main()
