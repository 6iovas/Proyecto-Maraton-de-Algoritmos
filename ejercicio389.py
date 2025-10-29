// Proyecto de Informatica
// Ejercicio 389
Título del Ejercicio: Contar Dígitos de un Número
Análisis del Problema
? Descripción del Problema: Contar cuántos dígitos tiene un número entero positivo.

? Entradas y Salidas:

? Entrada: Número entero n.

? Salida: Cantidad de dígitos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Mientras n>0, dividir entre 10 y contar iteraciones.

2. Mostrar contador.

? Estructuras de Datos: Variable entera.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int n=12345, contador=0;
    int temp=n;
    while(temp>0){
        temp/=10;
        contador++;
    }
    cout << "Numero de digitos en " << n << " = " << contador << endl; // 5
    return 0;
}

Pruebas
? Caso 1: 12345 ? 5

? Caso 2: 0 ? 1

? Caso 3: 987654 ? 6