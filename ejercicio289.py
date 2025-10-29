// Proyecto de Informatica
// Ejercicio 289
Título del Ejercicio: Contar Vocales en una Cadena (Recursivo)
Análisis del Problema
? Descripción del Problema: Contar cuántas vocales hay en una cadena usando recursión.

? Entradas y Salidas:

? Entrada: Una cadena de caracteres.

? Salida: Número de vocales en la cadena.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir al usuario que ingrese una cadena.

2. Crear función recursiva que revise el primer carácter y sume 1 si es vocal.

3. Llamar a la función para el resto de la cadena.

4. Mostrar el total de vocales.

? Estructuras de Datos: Cadena de caracteres y contador entero.

? Funciones Principales: main() y contarVocales(char* str).

Código Fuente (C++)
#include <iostream>
#include <cstring>

int contarVocales(char* str) {
    if (*str == '\0') return 0;

    char c = tolower(*str);
    int suma = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ? 1 : 0;
    return suma + contarVocales(str + 1);
}

int main() {
    char cadena[100];
    std::cout << "Ingresa una cadena: ";
    std::cin.getline(cadena, 100);

    std::cout << "Numero de vocales: " << contarVocales(cadena) << std::endl;
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? Salida: 4

? Caso 2: "C++ es divertido" ? Salida: 6

? Caso 3: "XYZ" ? Salida: 0