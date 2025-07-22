ventas = []
while True:
    print("Menu de opciones")
    print("1. Ingresar lista de ventas")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular venta más alta y baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuantos dias superaron los Q1000")
    print("6. Clasificar ventas")
    print("7. Salir")
    opcion= input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            dias = int(input("Ingrese los dias de ventas: "))
            for i in range(dias):
                while True:
                    venta = int(input("Ingrese las ventas de cada dia: "))
                    ventas.append(venta)
                    break
        case "2":
            print("Ventas ingresadas")
            ind=0
            for i in ventas:
                ind +=1
                print(f"{ind}. Q{i}")