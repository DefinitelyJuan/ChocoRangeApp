from rangeKata.kataRange import rango
import os  
if(__name__=="__main__"):

    strRange = input("Introduzca el rango: ")
    mainRange = rango(strRange)
    while(True):
        print("""MENU
1.Equals
2.Get All Points
3.Endpoints
4.Contains Range
====================""")
        op = input("Introduzca su opción:")
        match(op):
            case "1":
                strCompRange = input("Introducza el rango a comparar:")
                compRange = kataRange.rango(strCompRange)
                equalBool = mainRange.equals(compRange)
                print(equalBool)
            case "2":
                allPoints = []
                allPoints = mainRange.getAllPoints()
                for i in allPoints:
                    print(i)           
            case "3":
                endpoint = ()
                endpoint = mainRange.endpoints()
                print(endpoint)
           
            case "4":
                strCompRange = input("Introducza el rango a comparar:")
                compRange = kataRange.rango(strCompRange)
                contains = mainRange.containsRange(compRange)
                print(contains)
            case _:
                print("Seleccione una opción valida...")
                

        ans = input("Desea salir? (Y/N): ")
        if (ans.upper() == "Y"):
            break
        os.system("cls")

