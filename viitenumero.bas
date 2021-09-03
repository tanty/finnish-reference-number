REM  *****  BASIC  *****

REM Copyright © 2002 Kaj Bredenberg <kaj.bredenberg@kb-consulting.fi>
REM
REM Permission is hereby granted, free of charge, to any person
REM obtaining a copy of this software and associated documentation files
REM (the "Software"), to deal in the Software without restriction,
REM including without limitation the rights to use, copy, modify, merge,
REM publish, distribute, sublicense, and/or sell copies of the Software,
REM and to permit persons to whom the Software is furnished to do so,
REM subject to the following conditions:
REM
REM The above copyright notice and this permission notice (including the
REM next paragraph) shall be included in all copies or substantial
REM portions of the Software.
REM
REM THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
REM EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
REM MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
REM NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
REM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
REM ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
REM CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
REM SOFTWARE.
REM
REM Authors:
REM    Kaj Bredenberg <kaj.bredenberg@kb-consulting.fi>

REM Code re-licensed as MIT from the public domain publishing at:
REM
REM https://groups.google.com/g/sfnet.atk.ohjelmointi/c/ffP0Zvl580c


Function LaskeViite(ByVal numerosarja As String) As String
    'Muuttujien esittely
    Dim origSarja As String    ' alkuperäinen numerosarja
    Dim Laskuri As Byte        ' laskuri
    Dim sarjanPituus As Byte   ' numerosarjan pituus
    Dim tarkisteNumero As Byte ' tarkistenumero
    Dim sarjanSumma As String  ' numerosarjan summa
    Dim kertoimet(2) As Byte   ' kertoimet
    Dim i As Integer
    Dim j As Integer
    Dim refnumber As String    ' Viitenumero ilman jarjestelyä
    Dim outstr As String
    Dim UusiViite As String    ' Viitenumero 5 mrk. ryhmissä

    'muuttujien alustus
    origSarja = numerosarja
    sarjanPituus = Len(numerosarja)
    Laskuri = 0
    sarjanSumma = 0
    tarkisteNumero = 0
    kertoimet(0) = 7: kertoimet(1) = 3: kertoimet(2) = 1

    'tarkistetaan annetun numerosarjan pituus ja sisältö
    If (sarjanPituus < 1 Or sarjanPituus > 19) Or Not IsNumeric(numerosarja) Then GoTo Viite_Error

    'käydään numerosarja lävitse
    Do While Laskuri < sarjanPituus
        sarjanSumma = sarjanSumma + (Mid(numerosarja, sarjanPituus - Laskuri, 1) * kertoimet(Laskuri Mod 3))
        Laskuri = Laskuri + 1 'laskurin inkrementointi
    Loop

    'lasketaan tarkistenumero (sarjan summasta seuraava täysi kymmen - sarjan summa)
    tarkisteNumero = (10 - (sarjanSumma Mod 10)) Mod 10

    'palautetaan kutsuvaan aliohjelmaan alkuperäinen numerosarja ja tarkisteNumero
    LaskeViite = origSarja & tarkisteNumero

    refnumber = origSarja & tarkisteNumero
    strlen = Len(origSarja & tarkisteNumero)
    ' / Järjestetään 5 merkin ryhmiin

    If strlen > 5 Then
        j = 0
        For i = strlen To 1 Step -1
            j = j + 1
            If j = 6 Then
                outstr = outstr & " "
                j = 1
            End If
            outstr = outstr & Mid(refnumber, i, 1)
        Next
        UusiViite = ""
        For i = Len(outstr) To 1 Step -1
            UusiViite = UusiViite & Mid(outstr, i, 1)
        Next i

        LaskeViite = UusiViite

    End If

    Exit Function

Viite_Error:

    On Error GoTo 0
    Err.Raise vbObjectError + 1001, , "Viitenumeroksi laskettava numerosarja virheellinen"
    LaskeViite = ""
    Exit Function

End Function