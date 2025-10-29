// Proyecto de Informatica
// Ejercicio 393
Título del Ejercicio: Contar Apariciones de un Elemento en Array
Análisis del Problema
? Descripción del Problema: Contar cuántas veces aparece un número en un array.

? Entradas y Salidas:

? Entrada: Array y número x.

? Salida: Cantidad de apariciones.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador.

2. Recorrer array y comparar con x.

3. Incrementar contador si coincide.

? Estructuras de Datos: Array y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,2,4,2}, n=6, x=2, contador=0;
    for(int i=0;i<n;i++)
        if(arr[i]==x) contador++;

    cout << "El numero " << x << " aparece " << contador << " veces" << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,2,4,2], x=2 ? 3

? Caso 2: [1,1,1], x=1 ? 3

? Caso 3: [5,6,7], x=4 ? 0