// Proyecto de Informatica
// Ejercicio 303
Título del Ejercicio: Contar Consonantes en una Cadena (Recursivo)
Análisis del Problema
? Descripción del Problema: Contar cuántas consonantes hay en una cadena usando recursión.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de consonantes.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir cadena al usuario.

2. Crear función recursiva que revise si el carácter es consonante y sume 1.

3. Llamar recursivamente con el resto de la cadena.

4. Mostrar el total.

? Estructuras de Datos: Cadena de caracteres y contador entero.

? Funciones Principales: main() y contarConsonantes().

Código Fuente (C++)
#include <iostream>
#include <cstring>

bool esConsonante(char c) {
    c = tolower(c);
    return (c >= 'a' && c <= 'z') && !(c=='a'||c=='e'||c=='i'||c=='o'||c=='u');
}

int contarConsonantes(char* str) {
    if(*str == '\0') return 0;
    return (esConsonante(*str) ? 1 : 0) + contarConsonantes(str+1);
}

int main() {
    char cadena[100];
    std::cout << "Ingresa una cadena: ";
    std::cin.getline(cadena, 100);

    std::cout << "Numero de consonantes: " << contarConsonantes(cadena) << std::endl;
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? Salida: 5

? Caso 2: "C++ es divertido" ? Salida: 7

? Caso 3: "AEIOU" ? Salida: 0