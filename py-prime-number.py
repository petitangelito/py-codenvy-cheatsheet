#!/usr/bin/env python
#
# Copyright 2014 Arn-O. See the LICENSE file at the top-level directory of this
# distribution and at
# https://github.com/Arn-O/py-codenvy-cheatsheet/blob/master/LICENSE.

'''
A simple program that displays a list of divisors. This is code is a part of the Codenvy cheatsheet project.
'''

import timeit

def get_divisors(number):
    '''Compute the divisors and the duration time.'''
    start_time = timeit.default_timer()
    divisors = []
    for i in range(1, int(number/2) ):
        if not number%i:
            divisors.append(i)
    end_time = timeit.default_timer() 
    duration = end_time - start_time
    return divisors, duration

def main():
    '''Very simple user interface'''
    user_number = int(raw_input("Enter a number: "))
    divisors, duration = get_divisors(user_number)
    print divisors
    print 'Total computation time: %f' % duration

if __name__ == '__main__':
    main()
