"""
1- Crear una funcion que pase de entero >0 y <4000 a romano
2- Que cualquier otra entrada de error
3- limite 3999

Casos de prueba
a-1994 -> MCMXCIV
b-4000 ->RomanNumberError() el valor debe ser menor a 4000
c-"unacadena" -> RomanNumberError Debe ser un entero

M -> 1000
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I ->1
"""
dic_romano_a_entero = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

dic_entero_a_romano={
    1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
    10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',
    1000: "M", 2000: "MM", 3000: "MMM"
}

class RomanNumberError( Exception ):
    pass


def romano_a_entero(romano:str)->int:#'III'
    list_romano = list(romano)#['I','I','I']
    valor_entero=0
    for i in range(0,len(list_romano)):
        if i != 0:
            if dic_romano_a_entero.get(list_romano[i-1]) < dic_romano_a_entero.get(list_romano[i]):
                valor_entero -= dic_romano_a_entero.get(list_romano[i-1])
                valor_entero += dic_romano_a_entero.get(list_romano[i]) - dic_romano_a_entero.get(list_romano[i-1])
            else:
                valor_entero += dic_romano_a_entero.get(list_romano[i])
        else:
            valor_entero += dic_romano_a_entero.get(list_romano[i])

    return valor_entero

print(romano_a_entero("XXXIV"))

def entero_a_romano( numero:int )->str:
    numero = "{:0>4d}".format(numero)
    numero_list = list(numero)
    valor_romano=''
    cont = 0
    valor_num = 1000
    while cont < len(numero_list):
        numero_list[cont] = int(numero_list[cont])*valor_num
        valor_romano +=  dic_entero_a_romano.get(numero_list[cont],'')
        cont +=1
        valor_num /= 10
    
    return valor_romano