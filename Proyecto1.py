def funcion_polaca(expresion):
    jerarquia_operaciones = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}  # Prioridad de operadores
    operadores = []
    salida = []
    pasos = []
    simbolos = expresion.split()  # Dividimos la expresión en símbolos

    for s in simbolos:
        # Verificamos si es un número (o sea que soporta enteros y flotantes)
        try:
            float(s)
            salida.append(s)
            pasos.append(f"Agregar número {s} al segmento salida: {salida}")
        except ValueError:
            if s in jerarquia_operaciones:  # Si es un operador
                while (operadores and operadores[-1] != '(' and
                       jerarquia_operaciones[operadores[-1]] >= jerarquia_operaciones[s]):
                    operador = operadores.pop()
                    salida.append(operador)
                    pasos.append(f"Agregar {operador} del segmento operadores al segmento salida: {salida}")
                operadores.append(s)
                pasos.append(f"Agregar operador {s} al segmento operadores: {operadores}")
            elif s == '(':  # Si es un paréntesis abierto
                operadores.append(s)
                pasos.append(f"Agregar paréntesis {s} al segmento operadores: {operadores}")
            elif s == ')':  # Si es un paréntesis cerrado
                while operadores and operadores[-1] != '(':
                    operador = operadores.pop()
                    salida.append(operador)
                    pasos.append(f"Agregar {operador} del segmento operadores al segmento salida: {salida}")
                if operadores:
                    operadores.pop()  # Quita el paréntesis de apertura
                    pasos.append(f"Quitar paréntesis de apertura del segmento operadores: {operadores}")
                else:
                    raise ValueError("Expresión mal formada: falta paréntesis de apertura")

    # Vaciar los operadores restantes
    while operadores:
        operador = operadores.pop()
        salida.append(operador)
        pasos.append(f"Agregar {operador} al final del segmento salida: {salida}")

    return salida, pasos


# Función para generar el reporte en un archivo .txt
def generar_reporte_rpn(pasos, nombre_archivo="generar_reporte_rpn.txt"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Reporte de Conversión a Notación Polaca Inversa (RPN)\n")
        archivo.write("--------------------------------------------------\n")
        for paso in pasos:
            archivo.write(paso + "\n")
    print(f"Reporte generado exitosamente: {nombre_archivo}")


# Código principal
if __name__ == "__main__":
    expresion = input("Agregar expresión: ")  # Solicitar expresión
    try:
        salida, pasos = funcion_polaca(expresion)

        # Mostrar la expresión en notación polaca inversa
        print(f"Expresión en notación polaca inversa: {' '.join(salida)}")

        # Generar el reporte en el archivo .txt
        generar_reporte_rpn(pasos)
    except ValueError as e:
        print(f"Error: {e}")