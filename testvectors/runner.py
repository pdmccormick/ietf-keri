#!/usr/bin/env python3

import os
from pathlib import Path

from vectors import TESTVECTORS
from keriutils import json_dumps_compact, json_dumps_pretty

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / 'output'

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for tv in TESTVECTORS:
        obj = tv()
        event = obj.generate()
        out = json_dumps_compact(event)

        if out != (expect := obj.EXPECT):
            print(f'{obj.NAME}: expected:')
            print()
            print(f'\t\t\t{expect}')
            print()
            print(f'\t... but got:')
            print()
            print(f'\t\t\t{out}')
            continue

        filename = OUTPUT_DIR / f'{obj.NAME}.json'
        with open(filename, 'w') as fobj:
            fobj.write(out)

        print(f'{obj.NAME}: wrote {filename.relative_to(BASE_DIR)}')

        filename = OUTPUT_DIR / f'{obj.NAME}.pretty.json'
        out_pretty = json_dumps_pretty(event)
        with open(filename, 'w') as fobj:
            fobj.write(out_pretty)
