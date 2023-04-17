from romanos_class import NumeroRomano

def test_suma_romanos():
    nr1 = NumeroRomano("XX")
    nr2 = NumeroRomano(30)

    nr3 = nr1 + nr2

    assert isinstance(nr3,NumeroRomano) == True
    assert nr3.valor == 50
    assert nr3.representacion_romano == 'L'

def test_resta_romanos():
    nra = NumeroRomano("XXX")
    nrb = NumeroRomano(5)

    nrc = nra - nrb

    assert isinstance(nrc,NumeroRomano) == True
    assert nrc.valor == 25
    assert nrc.representacion_romano == 'XXV'