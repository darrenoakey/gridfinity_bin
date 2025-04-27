#!/usr/bin/env python3
# bin.py – Generate custom Gridfinity bins based on given shape

import argparse
from gfthings.Bin import FunkyBin  # gfthings master branch
from build123d import export_stl  # build123d 0.9 helper


def parse_shape(shape_args):
    # If user passed two integers, it's a simple rect shape
    if len(shape_args) == 2 and all(s.isdigit() for s in shape_args):
        x, y = map(int, shape_args)
        shape = [[1]*x for _ in range(y)]
        name = f"gridfinity_{x}x{y}"
        return shape, name
    else:
        # Otherwise, treat each arg as a binary string
        shape = []
        for row_str in shape_args:
            row = [1 if ch == '1' else 0 for ch in row_str.strip()]
            shape.append(row)
        height = len(shape)
        width = max(len(row) for row in shape)
        name = f"gridfinity_{width}x{height}"
        return shape, name


def main():
    parser = argparse.ArgumentParser(description="Generate Gridfinity bin STL with specified shape.")
    parser.add_argument('shape', nargs='+', help='Either two integers (columns rows) or a binary matrix as row strings.')
    parser.add_argument('--height', type=int, default=3, help='Number of height units (default: 3)')
    args = parser.parse_args()

    shape, basename = parse_shape(args.shape)
    stl_name = f"{basename}x{args.height}.stl"

    export_stl(FunkyBin(shape, height_units=args.height), stl_name)
    print(f"Exported: {stl_name}")


if __name__ == "__main__":
    main()
