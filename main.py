#!/usr/bin/env python
from __future__ import print_function
import argparse


def subset_sum(numbers, target, k_num, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target and len(partial) == k_num:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, k_num, partial + [n])


def read_file(fname):
    with open(fname, 'r') as fi:
        k_num = int(fi.readline().rstrip())
        t_sum = int(fi.readline().rstrip())
        ary = []
        line = fi.readline()
        while line:
            ary.append(int(line.rstrip()))
            line = fi.readline()
        return k_num, t_sum, ary


def main(args):
    k_num, t_sum, ary = read_file(args.fname)
    print("K=%d, Tsum=%d, ary=%r" % (k_num, t_sum, ary))
    subset_sum(ary, t_sum, k_num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='targeted_sum')
    parser.add_argument('-f', dest='fname', help='input file name',
                        required=True)
    main(parser.parse_args())
