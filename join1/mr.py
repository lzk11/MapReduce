#! /usr/bin/env python
# coding:utf-8
import os
import sys


def read_input(file, sepr=' '):
    for line in file:
        line = line.split(sepr)
        yield line


def mapper():
    filepath = os.environ['map_input_file']
    filename = os.path.split(filepath)[1]
    lines = read_input(sys.stdin)
    for data in lines:
        if data[0].strip() == "":
            continue

        if "student.txt" == filename:
            if len(data) != 2:
                continue
            else:
                print "%s\t%s\t%s" % (data[0], "0", data[1].strip())
        else:
            if len(data) != 3:
                continue
            else:
                print "%s\t%s\t%s\t%s" % (data[0], "1", data[1].strip(), data[2].strip())


def reducer():

    sno = None
    sname = None

    line = read_input(sys.stdin, '\t')
    for data in line:
        if (len(data) != 3 and len(data) != 4) or data[0].split() == "":
            continue
        if data[0] != sno:
            sno = data[0]
            if data[1] == "0":
                sname = data[2].strip('\n')
        else:
            cname = data[2]
            cnum = data[3].strip('\n')
            print "%s\t%s\t%s\t%s" % (sno, sname, cname, cnum)

if __name__ == "__main__":
    d = {"mapper": mapper, "reducer": reducer}
    if sys.argv[1] in d:
        d[sys.argv[1]]()
