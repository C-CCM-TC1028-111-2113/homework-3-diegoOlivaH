def año_bisiesto(año):
    año==año
    if (año%4==0 and año%100==0 and año%400==0):
        print("True,",año,"is a leap-year")
    elif (año%4==0 and año%100==0):
        print("False,",año,"isn't a leap-year")
    elif (año%4==0):
        print("True,",año,"is a leap year")
    else:
        print("False,",año,"isn't a leap year")
def main():
    #escribe tu código abajo de esta línea
y= int(input("Input the year"))

año_bisiesto(y)


if __name__=='__main__':
    main()
