#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from app import app

def main():
    if len(sys.argv) > 1:
        port = int(sys.argv[2])
    else:
        port = 3000

    app.run(port = port, debug = True)

if __name__ == '__main__':
    main()
