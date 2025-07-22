ventas = []
while True:
    print("Menu de opciones")
    print("1. Ingresar lista de ventas")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular venta más alta y baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuantos dias superaron los Q1000")
    print("6. Buscar una venta")
    print("7. Clasificar ventas")
    print("8. Salir")
    opcion= input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            dias = int(input("Ingrese cuantos dias por venta quiere ingresar: "))
            for i in range(dias+1):
                venta = int(input("Ingrese las ventas de cada dia: "))
                for j in range(venta+1):
                    ventas.append((venta))