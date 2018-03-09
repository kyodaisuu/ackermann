#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Show process of Ackermann function calculation
# written by Fish
# MIT License
# Language: Python 3


def main():
    """Show process of Ackermann function calculation"""
    # Set reduction value. Ack(red,n) is directly computed.
    red = 0
    # Test some values
    assert ack('A(0,2)', 0) == '3'
    assert ack('A(1,1)', 0) == 'A(0,A(1,0))'
    assert ack('A(2,2)', 0) == 'A(1,A(2,1))'
    assert ack('A(3,3)', 0) == 'A(2,A(3,2))'
    assert ack('A(1,3)', 1) == '5'
    assert ack('A(2,3)', 2) == '9'
    assert ack('A(3,3)', 3) == '61'
    assert ack('A(3,13)', 3) == '65533'
    # Get parameters
    m = int(input('Calculate Ack(m, n)\nm = '))
    assert m >= 0, "m should be larger than or equal to 0"
    n = int(input('n = '))
    assert n >= 0, "n should be larger than or equal to 0"
    # Start calculation
    eq = 'A('+str(m)+','+str(n)+')'
    print("{0} ".format(eq), end='')
    i = 0
    while eq.find('A') == 0:
        eq = ack(eq, red)
        i += 1
        print("= {0}".format(eq))
    print("Repetition: {0}".format(i))
    return


def ack(eq, red):
    """One step calculation of Ackermann function"""
    assert red <= 3
    start = eq[:eq.rfind('(')-1]
    calc = eq[eq.rfind('(')+1:eq.find(')')].split(',')
    end = eq[eq.find(')')+1:len(eq)]
    m = int(calc[0])
    n = int(calc[1])
    if m <= red:
        result = str([n+1, n+2, 2*n + 3, 2**(n+3)-3][m])
    else:
        if n == 0:
            result = 'A('+str(m-1)+',1)'
        else:
            result = 'A('+str(m-1)+',A('+str(m)+','+str(n-1)+'))'
    return start + result + end


if __name__ == '__main__':
    main()
