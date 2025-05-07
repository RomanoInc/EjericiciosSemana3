def mayor_edad():
    edad = int(input("Ingrese edad: "))
    if edad > 18:
        print("Eres mayor de edad ")
    else:
        print("Eres menor de edad ")
        
def convert_grados():
    convert_grados = float(input("Ingrese grados celsius: "))
    temperatura = float(input("Ingrese grados farenheit: "))
    print(convert_grados - temperatura / 1.8)


def area_tri():
    base = float(input("Ingrese base"))
    altura = float(input("Ingrese altura"))
    print(base * altura)

def mayor_list():
    list = [444,25,33,12,114]
    numero_mayor= max(list)
    print(numero_mayor)
    mayor_list()

def count():
    palabra=input("Ingrese palabra: ")
    cantidad= len(palabra)
    print(cantidad)

def filtrar_pares():
    list4 = [4,5,8,9]
    for numero in list4:
        if numero % 2 == 0:
            print(numero)
    

            


        

        


