print('Hello!')
def equation_2_D(a,b,c):
    import math

    #a = float(input("donner a :"))
    #b = float(input("donner b :"))
    #c = float(input("donner c :"))
    print("a = " + str(a)  + "    b = "+ str(b)+ "    c = "+str(c))
    print("L'equation est de la forme :" , "E =" + str(a) + "XX  + "+str(b)+ "X  + " + str(c))
    if (a == 0):
        x = -c/a
        print("la soulution vaut :\n", "x = " + str(x))
    else:
        deltat = b*b - 4*a*c
        print("Le descreminent vaut : " + str(deltat))
        if deltat > 0:
            x1 = (-b + math.sqrt(deltat))/(2*a)
            x2 = (-b - math.sqrt(deltat))/(2*a)
            print("L'equation  E a deux solutions distincts X1 et X2 :\n", "X1 = " + str(x1) +" et " + "X2 = "+str(x2))
        elif deltat ==0:
            x= b/(2*a)
            print("L'equation  E a une soltion double X :\n ", "X = " + str(x))
        else:
            print("L'equation  E n'a pas de solutions dans R") 
#equation_2_D(0,4,1)
equation_2_D(7,1,8)
