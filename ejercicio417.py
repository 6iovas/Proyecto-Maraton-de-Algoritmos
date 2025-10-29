// Proyecto de Informatica
// Ejercicio 417
Título del Ejercicio: Contar Vocales en Cadena
Análisis del Problema
? Descripción del Problema: Contar la cantidad de vocales en una cadena de texto.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de vocales.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la cadena.

2. Incrementar contador si es vocal (a,e,i,o,u).

? Estructuras de Datos: Cadena de caracteres y contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto="Hola Mundo";
    int contador=0;
    for(char c:texto)
        if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
            contador++;

    cout << "Cantidad de vocales: " << contador << endl; // 4
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? 4

? Caso 2: "ABCDE" ? 2

? Caso 3: "xyz" ? 0