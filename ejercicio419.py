// Proyecto de Informatica
// Ejercicio 419
Título del Ejercicio: Convertir Número a Binario
Análisis del Problema
? Descripción del Problema: Convertir un número entero a su representación binaria.

? Entradas y Salidas:

? Entrada: Número entero positivo.

? Salida: Representación binaria como cadena.

Diseño de la Solución
? Algoritmo Propuesto:

1. Mientras n>0, obtener n%2 y agregar al resultado.

2. Invertir la cadena final.

? Estructuras de Datos: Entero y cadena.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n=13;
    string bin="";
    int temp=n;
    while(temp>0){
        bin=to_string(temp%2)+bin;
        temp/=2;
    }
    cout << "Binario de " << n << " = " << bin << endl; // 1101
    return 0;
}

Pruebas
? Caso 1: 13 ? 1101

? Caso 2: 5 ? 101

? Caso 3: 0 ? ""