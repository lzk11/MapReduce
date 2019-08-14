#!env/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split(' ')
    for word in line:
        print '\t'.join([word, '1'])
