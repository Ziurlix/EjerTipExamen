import random
import math

vendedores = [
    "Camila Soto", "Esteban Ruiz", "Daniela Pérez", "Jorge Vargas",
    "Soledad Acuña", "Felipe Campos","Laura Silva", "Marcelo Torres"
]
ventas = {}

def gen_ventas():
    global ventas
    ventas = {v: random.randint(20000, 2000000) for v in vendedores}
    print("Ventas generadas con éxito.")

def clasifica():
    if not ventas:
        print("Ventas aun no generadas")
        return
    
    print("Ventas menores a $500.000:")
    for v, m in ventas.items():
        if m < 500000:
            print(f" - {v}: ${m}")

    print("Ventas entre $500.000 y $1.200.000:")
    for v, m in ventas.items():
        if 500000 <= m <= 1200000:
            print(f" - {v}: ${m}")

    print("\nVentas mayores a $1.200.000:")
    for v, m in ventas.items():
        if m > 1200000:
            print(f" - {v}: ${m}")
    print()

def stats():
    if not ventas:
        print("No hay ventas generadas")
        return
    
    valores=list(ventas.values())
    print(f"Venta máxima: ${max(valores)}")
    print(f"Venta mínima: ${min(valores)}")
    print(f"Promedio de ventas: ${sum(valores) / len(valores):.2f}")
    print(f"Media geométrica: ${math.prod(valores) ** (1/len(valores)):.2f}\n")

def reporte():
    if not ventas:
        print("Primero debe generar las ventas.\n")
        return

    print(f"{'Vendedor':<20} {'Venta':>10} {'Comisión (10%)':>15} {'Impuesto (8%)':>15} {'Venta Neta':>15}")
    for v, m in ventas.items():
        comision = m * 0.10
        impuesto = m * 0.08
        neto = m - impuesto
        print(f"{v:<20} ${m:>10} ${comision:>14.2f} ${impuesto:>14.2f} ${neto:>14.2f}")
    print()

def menu():
    while True:
        print("=== Menú - Control de Ventas de Librería ===")
        print("1. Generar Ventas Aleatorias")
        print("2. Clasificar Ventas")
        print("3. Estadísticas Generales")
        print("4. Reporte Completo de Comisiones")
        print("5. Finalizar Programa")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            gen_ventas()
        elif opcion == "2":
            clasifica()
        elif opcion == "3":
            stats()
        elif opcion == "4":
            reporte()
        elif opcion == "5":
            print("\nPrograma finalizado.")
            print("Nombre: Tu Nombre")
            print("RUT: 12345678-9")
            print("Carrera: Ingeniería en Computación\n")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()

    


    
