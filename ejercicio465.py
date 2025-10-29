// Proyecto de Informatica
// Ejercicio 465
Título del Ejercicio: Contar Letras en Cadena
Análisis del Problema
? Descripción del Problema: Contar la cantidad de letras (a-z, A-Z) en una cadena.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de letras.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer cada carácter y verificar si es letra con isalpha().

2. Incrementar contador si es letra.

? Estructuras de Datos: Cadena y contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string texto="Hola 123 Mundo!";
    int contador=0;
    for(char c:texto)
        if(isalpha(c)) contador++;
    cout << "Cantidad de letras: " << contador << endl; // 9
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? 9

? Caso 2: "12345" ? 0

? Caso 3: "a1b2c3" ? 3