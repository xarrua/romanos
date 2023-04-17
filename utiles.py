diccionario={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

dic_entero_a_romanos={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',

    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',

    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM',

    1000:'M',2000:'MM',3000:'MMM'
}

dic_romano_a_entero={
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
}

restas = { 'I':('V','X'), 'X':('L','C'),'C':('D','M') }