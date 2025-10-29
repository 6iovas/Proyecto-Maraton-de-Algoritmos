// Proyecto de Informatica
// Ejercicio 347
Título del Ejercicio: Contar Vocales en una Cadena
Análisis del Problema
? Descripción del Problema: Contar el número de vocales en una cadena de caracteres.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de vocales.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la cadena.

2. Incrementar contador si el carácter es vocal (a,e,i,o,u).

3. Mostrar resultado.

? Estructuras de Datos: Cadena y contador entero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string cadena = "Hola Mundo";
    int contador=0;

    for(char c : cadena) {
        c = tolower(c);
        if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u') contador++;
    }

    cout << "Numero de vocales: " << contador << endl; // 4
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? 4

? Caso 2: "C++ es divertido" ? 6

? Caso 3: "XYZ" ? 0