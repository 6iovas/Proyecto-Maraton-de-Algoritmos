// Proyecto de Informatica
// Ejercicio 329
Título del Ejercicio: Matriz Transpuesta
Análisis del Problema
? Descripción del Problema: Crear un programa que calcule la transpuesta de una matriz de enteros.

? Entradas y Salidas:

? Entrada: Matriz de tamaño m x n.

? Salida: Matriz transpuesta n x m.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la matriz original.

2. Asignar transpuesta[j][i] = original[i][j].

3. Mostrar matriz transpuesta.

? Estructuras de Datos: Array bidimensional.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3] = {{1,2,3},{4,5,6}};
    int trans[3][2];

    for(int i=0;i<2;i++)
        for(int j=0;j<3;j++)
            trans[j][i] = mat[i][j];

    cout << "Matriz transpuesta:\n";
    for(int i=0;i<3;i++) {
        for(int j=0;j<2;j++)
            cout << trans[i][j] << " ";
        cout << endl;
    }
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? [[1,4],[2,5],[3,6]]

? Caso 2: [[1]] ? [[1]]

? Caso 3: [[1,2],[3,4]] ? [[1,3],[2,4]]