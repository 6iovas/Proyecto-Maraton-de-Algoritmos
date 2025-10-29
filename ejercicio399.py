// Proyecto de Informatica
// Ejercicio 399
Título del Ejercicio: Reemplazar Caracter en Cadena
Análisis del Problema
? Descripción del Problema: Reemplazar todas las apariciones de un carácter en una cadena por otro.

? Entradas y Salidas:

? Entrada: Cadena, carácter a reemplazar, carácter nuevo.

? Salida: Cadena modificada.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la cadena.

2. Si carácter coincide con el original, reemplazar.

? Estructuras de Datos: Cadena (string).

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto="banana";
    char orig='a', nuevo='o';

    for(int i=0;i<texto.length();i++)
        if(texto[i]==orig) texto[i]=nuevo;

    cout << "Cadena modificada: " << texto << endl; // "bonono"
    return 0;
}

Pruebas
? Caso 1: "banana", a?o ? "bonono"

? Caso 2: "abc", b?x ? "axc"

? Caso 3: "aaa", a?a ? "aaa"