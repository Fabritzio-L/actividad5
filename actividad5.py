ventas = []
while True:
    print("Menu de opciones")
    print("1. Ingresar lista de ventas")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular venta más alta y baja")
    print("4. Calcular promedio de ventas")
    print("5. Ventas que superan los Q1000")
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
            if ventas:
                print("Ventas ingresadas")
                dia=0
                for i in ventas:
                        dia +=1
                        print(f"Dia {dia}. Q{i}")
            else:
                print("No hay ventas registradas")
        case "3":
            if ventas:
                venta_mayor= ventas[0]
                venta_menor = ventas[0]
                for i in ventas:
                    if i > venta_mayor:
                        venta_mayor = i
                    if i < venta_menor:
                        venta_menor = i
                print(f"La venta mayor es: {venta_mayor}")
                print(f"La venta menor es: {venta_menor}")
            else: print("No hay ventas registradas")
        case "4":
            if ventas:
                total_de_ventas =0
                for i in ventas:
                    total_de_ventas += i
                promedio_ventas = total_de_ventas/len(ventas)
                print(f"El promedio de las ventas es de Q{promedio_ventas:.2f}")
            else:
                print("No hay ventas registradas")
        case "5":
            if ventas:
                contador =0
                for i in ventas:
                    if i > 1000:
                        contador +=1
                print(f"Los días en que las ventas superan los Q10OO: {contador}")
            else:
                print("No hay ventas registradas")
        case "6":
            if ventas:
                enumerar_dias =1
                for i in ventas:
                    if i > 1000:
                        clasificacion_venta= "venta alta"
                    elif 500 <= i <= 1000:
                        clasificacion_venta = "venta media"
                    else:
                        clasificacion_venta= "venta baja"
                    print(f"Dia {enumerar_dias}. Q{i} es una {clasificacion_venta}")
                    enumerar_dias +=1
            else:
                print("No hay ventas registradas")