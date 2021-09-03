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
#    Chiman

# Code re-licensed as MIT from the public domain publishing at:
#
# https://www.ohjelmointiputka.net/koodivinkit/26782-python-viitenumerolaskuri


def viitenumeron_tarkiste(viitenumero_raaka):
    """palauta annetun tarkisteettoman viitenumeron perään kuuluva tarkistenumero"""
    kertoimet = (7, 3, 1)
    viitenumero_raaka = viitenumero_raaka.replace(' ', '')
    nrot_kaanteinen = map(int, viitenumero_raaka[::-1])
    tulosumma = sum(kertoimet[i % 3] * x for i, x in enumerate(nrot_kaanteinen))
    return (10 - (tulosumma % 10)) % 10

def viitenumero_ok(viitenumero):
    """tarkista vastaako lopun tarkistenumero viitenumeron alkuosaa"""
    return viitenumeron_tarkiste(viitenumero[:-1]) == int(viitenumero[-1])

def jaa_ryhmiin_oikealta(s, n):
    """palauta merkkijono s eroteltuna n merkin ryhmiin, välilyönti erottaa

    Ryhmittely aloitetaan oikeasta reunasta.
    Esimerkki: s='1234567890', n=4 palauttaa '12 3456 7890'

    """
    kaannetty = s[::-1]
    osat = [(' ' if i and i % n == 0 else '') + c for i, c in enumerate(kaannetty)]
    return ''.join(osat)[::-1]

def testit():
    assert viitenumeron_tarkiste('1662') == 5
    assert viitenumero_ok('16625')
    assert jaa_ryhmiin_oikealta('966846848', 5) == '9668 46848'
    print('testit ok')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        # oleta argumentiksi viitenumero ilman tarkistetta, tulosta tarkisteen kanssa
        viite_raaka = argv[-1]
        tarkiste = viitenumeron_tarkiste(viite_raaka)
        viite = viite_raaka + str(tarkiste)
        print(jaa_ryhmiin_oikealta(viite, 5))
    else:
        testit()
        print('Anna argumenttina viitenumero ilman tarkistetta')
