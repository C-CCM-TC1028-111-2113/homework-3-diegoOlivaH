def area(base,depth):
    base==base
    depth==depth
    AREA= base*depth
    return AREA

def volume(height):
    area(b,d)##b y d  no existen en el contexto de esta función, debiste pasarlos junto con h
    height==height
    vol = area(b,d)*height
    return float(vol)
def main():
    #escribe tu código abajo de esta línea
##Cuidado con la indentación
b= float(input("Input the base: "))
h= float(input("Input the height: "))
d= float(input("Input the depth: "))

print("The volume of your area is",volume(h))

if __name__=='__main__':
    main()
