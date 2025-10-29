// Proyecto de Informatica
// Ejercicio 447
Título del Ejercicio: Invertir Cadena
Análisis del Problema
? Descripción del Problema: Invertir una cadena de caracteres usando bucle.

? Entradas y Salidas:

? Entrada: Cadena s.

? Salida: Cadena invertida.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la cadena desde el final al inicio.

2. Concatenar cada carácter a la nueva cadena.

? Estructuras de Datos: Cadenas de caracteres.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s="Hola Mundo", invertida="";
    for(int i=s.length()-1;i>=0;i--) invertida+=s[i];
    cout << "Cadena invertida: " << invertida << endl; // odnuM aloH
    return 0;
}

Pruebas
? Caso 1: "Hola" ? "aloH"

? Caso 2: "C++" ? "++C"

? Caso 3: "" ? ""