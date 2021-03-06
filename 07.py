#!/bin/python

import math

def is_prime(num):
    limit = int(math.sqrt(num) + 1)
    for i in range(2, limit):
        if not num % i:
            return False
    return True


def find_target_prime(prime):
    counter = 0
    num = 0
    while counter <= prime:
        num += 1
        if is_prime(num):
            counter += 1

    return num

if __name__ == '__main__':
    print "Answer Found: ", find_target_prime(10001)
