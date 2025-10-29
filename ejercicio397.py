// Proyecto de Informatica
// Ejercicio 397
Título del Ejercicio: Concatenar Dos Cadenas
Análisis del Problema
? Descripción del Problema: Concatenar dos cadenas de texto y mostrar resultado.

? Entradas y Salidas:

? Entrada: Dos cadenas a y b.

? Salida: Cadena concatenada.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar operador + para concatenar.

2. Mostrar cadena resultante.

? Estructuras de Datos: Cadenas (string).

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a="Hola ", b="Mundo";
    string c = a + b;
    cout << "Concatenacion: " << c << endl; // "Hola Mundo"
    return 0;
}

Pruebas
? Caso 1: "Hola ", "Mundo" ? "Hola Mundo"

? Caso 2: "", "Test" ? "Test"

? Caso 3: "C++", "" ? "C++"