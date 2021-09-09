def número_de_pliegos(pliegos,plumones):  ##def
    pliegos*=12
    plumones*=35
    if (plumones<=pliegos):
        return plumones
    if(plumones>=pliegos):
        return pliegos
def main():
    #escribe tu código abajo de esta línea
##Indentacion
pli= int(input("Input the number of sheets of albanene paper: "))
plu= int(input("Input the number of markers: "))

print("The maximum number of cards that can be done are:",número_de_pliegos(pli,plu))



if __name__=='__main__':
    main()
