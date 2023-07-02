#!/usr/bin/python3
import sys


def factorization():

    try:
        files = sys.argv[1]
        with open(files) as f:
            for numbs in f:
                numbs = int(numbs)
                if numbs % 2 == 0:
                    print("{}={}*{}".format(numbs, numbs // 2, 2))
                    continue
                run = 3
                while run < numbs // 2:
                    if numbs % run == 0:
                        print("{}={}*{}".format(numbs, numbs // run, run))
                        break
                    run = run + 2
                if run == (numbs // 2) + 1:
                    print("{}={}*{}".format(numbs, numbs, 1))
    except (IndexError):
        pass


factorization()
