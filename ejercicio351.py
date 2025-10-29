// Proyecto de Informatica
// Ejercicio 351
Título del Ejercicio: Sumar Dos Arrays Elemento a Elemento
Análisis del Problema
? Descripción del Problema: Crear un array resultado donde cada elemento sea la suma de los elementos correspondientes de dos arrays.

? Entradas y Salidas:

? Entrada: Dos arrays del mismo tamaño.

? Salida: Array con la suma.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer arrays con un bucle.

2. Sumar elementos y almacenar en nuevo array.

3. Mostrar resultado.

? Estructuras de Datos: Tres arrays de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int a[] = {1,2,3};
    int b[] = {4,5,6};
    int n=3, c[3];

    for(int i=0;i<n;i++) c[i] = a[i] + b[i];

    cout << "Array suma: ";
    for(int i=0;i<n;i++) cout << c[i] << " ";
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3] + [4,5,6] ? [5,7,9]

? Caso 2: [0,0,0] + [1,2,3] ? [1,2,3]

? Caso 3: [10,20] + [5,5] ? [15,25]