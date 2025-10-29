// Proyecto de Informatica
// Ejercicio 331
Título del Ejercicio: Suma de Diagonal de Matriz Cuadrada
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de la diagonal principal de una matriz cuadrada.

? Entradas y Salidas:

? Entrada: Matriz n x n.

? Salida: Suma de la diagonal principal.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la matriz.

2. Sumar los elementos donde fila == columna.

3. Mostrar resultado.

? Estructuras de Datos: Array bidimensional.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    int suma=0;

    for(int i=0;i<3;i++) suma += mat[i][i];

    cout << "Suma diagonal: " << suma << endl; // 1+5+9=15
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6],[7,8,9]] ? 15

? Caso 2: [[5]] ? 5

? Caso 3: [[1,0],[0,1]] ? 2