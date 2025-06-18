import random
import math

Huertos = ["Huerto Norte", "Huerto Sur", "Huerto Este", "Huerto Oeste", "Huerto Central", "Huerto 1", "Huerto 2", "Huerto 3", "Huerto 4", "Huerto 5"]	
Producciones = []

def Prod():
    global Producciones
    Producciones = [random.randit(5000, 50000) for _ in range(len(Huertos))]
    print ("Produccion de los huertos: ", Producciones)

def ClassProd():
    global Prod
    if not Prod:
        print ("Sin producciones generadas")
        return
    Min_10k = []
    Mid_10k_30k = []
    Max_30k = []
    for Prod in Prod:
        if Prod < 10000:
            Min_10k.append(Prod)
        elif 10000 <= Prod < 30000:
            Mid_10k_30k.append(Prod)
        else:
            Max_30k.append(Prod)
    print(f"Producciones menores a 10,000: {Min_10k}")
    print(f"Producciones entre 10,000 y 30,000: {Mid_10k_30k}")
    print(f"Producciones mayores a 30,000: {Max_30k}")

def VerEsta():
    if not Prod:
        print ("Genera la produccion")
        return
    
    MaxProd = max(Prod)
    MinProd = min(Prod)
    PromPro = sum(Prod) / len (Prod)
    MedGeomet = math.prod(Prod)**(1/len(Prod))

    print (f"""
    ------- Estadisticas de produccion -------
    Produccion maxima: {MaxProd}kg
    Produccion minima: {MinProd}kg
    Promedio de produccion: {PromPro:2f}kg
    Media geometrica: {MedGeomet:2f}kg
    ------------------------------------------
           """)

def ReportDet():
    if not Prod:
        print ("Genera la produccion")
        return
    
    print ("""
    ------------------------------------------- Reporte detallado -------------------------------------------
    Huerto\t\tProduccion Total (kg)\tDescuento Transporte (5%)\tDescuento Embalaje (3%)\tProduccion neta (kg)
    ---------------------------------------------------------------------------------------------------------
           """)
    for i in range(len(Huertos)):
        ProdTot = Producciones[i]
        DescTran = ProdTot * 0.05
        DescEmba = ProdTot * 0.03
        ProdNeta = ProdTot - DescTran - DescEmba
        print (f"{Huertos[i]:<15}\t{ProdTot:<20.2f}\t{DescTran:<25.2f}\t{DescEmba:25.2f}\t{ProdNeta:<20.2f}")

def Salir():
    print ("Saliendo del programa")


while True:
    print ("""
    ------- Analisis de produccion agricola -------
    1. Generar Produccion aleatoria
    2. Clasificar Produccion
    3. Ver Estadiscticas
    4. Reporte detallado
    5. Salir
    ------------------------------------------------
           """)
    
    Opc = int (input ("Opcion: "))

    if Opc == 1:
        Prod()
    elif Opc == 2:
        ClassProd()
    elif Opc == 3:
        VerEsta()
    elif Opc == 4: 
        ReportDet()
    elif == 5:
        Salir()
        break
    else:
        print ("Opcion no valida")
    