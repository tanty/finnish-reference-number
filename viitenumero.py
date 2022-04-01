#!/usr/bin/env python
# -*- coding: utf-8 -*-
# viitenumero.py

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice (including the
# next paragraph) shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Authors:
#    Chiman, ossimantylahti

# Code re-licensed as MIT from the public domain publishing at:
#
# https://www.ohjelmointiputka.net/koodivinkit/26782-python-viitenumerolaskuri


def reference_number_check_digit(reference_number_raw):
    """return checksum number of non-checksum referencen number 
    palauta annetun tarkisteettoman viitenumeron perään kuuluva tarkistenumero"""
    multiplication_feed = (7, 3, 1)
    reference_number_raw = reference_number_raw.replace(' ', '')
    numbers_reverse = map(int, reference_number_raw[::-1])
    sum_of_multiplication = sum(multiplication_feed[i % 3] * x for i, x in enumerate(numbers_reverse))
    return (10 - (sum_of_multiplication % 10)) % 10

def reference_number_ok(viitenumero):
    """check if checksum is valid 
    tarkista vastaako lopun tarkistenumero viitenumeron alkuosaa"""
    return reference_number_check_digit(viitenumero[:-1]) == int(viitenumero[-1])

def divide_in_groups_from_right(s, n):
    """divide a string separated by space in grops of n 

    Start grouping from the right end.
    Example s='1234567890', n=4 returns '12 3456 7890'


    palauta merkkijono s eroteltuna n merkin ryhmiin, välilyönti erottaa

    Ryhmittely aloitetaan oikeasta reunasta.
    Esimerkki: s='1234567890', n=4 palauttaa '12 3456 7890'

    """
    reversed_number = s[::-1]
    part_of_number = [(' ' if i and i % n == 0 else '') + c for i, c in enumerate(reversed_number)]
    return ''.join(part_of_number)[::-1]

def tests():
    assert reference_number_check_digit('1662') == 5
    assert reference_number_ok('16625')
    assert divide_in_groups_from_right('966846848', 5) == '9668 46848'
    print('Testing ok')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        # oleta argumentiksi viitenumero ilman tarkistetta, tulosta tarkisteen kanssa
        # Expect the argument to be a reference number without checksum. Output with checksum
        reference_number_raw = argv[-1]
        checksum_number = reference_number_check_digit(reference_number_raw)
        reference_number_calculated = reference_number_raw + str(checksum_number)
        print(divide_in_groups_from_right(reference_number_calculated, 5))
    else:
        tests()
        print('Please input reference number without checksum')
