// Proyecto de Informatica
// Ejercicio 471
Título del Ejercicio: Contar Dígitos en Número
Análisis del Problema
? Descripción del Problema: Contar la cantidad de dígitos de un número entero positivo.

? Entradas y Salidas:

? Entrada: Número entero.

? Salida: Cantidad de dígitos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Mientras n>0, dividir entre 10 y aumentar contador.

? Estructuras de Datos: Entero y contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int n=12345, contador=0;
    int temp=n;
    while(temp>0){contador++; temp/=10;}
    cout << "Cantidad de digitos: " << contador << endl; // 5
    return 0;
}

Pruebas
? Caso 1: 12345 ? 5

? Caso 2: 7 ? 1

? Caso 3: 0 ? 1 (considerando 0 como un dígito)