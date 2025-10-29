// Proyecto de Informatica
// Ejercicio 495
Título del Ejercicio: Transponer Matriz
Análisis del Problema
? Descripción del Problema: Calcular la transpuesta de una matriz m x n.

? Entradas y Salidas:

? Entrada: Matriz m x n.

? Salida: Matriz transpuesta n x m.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer matriz original.

2. Asignar elemento [i][j] a [j][i] de la transpuesta.

? Estructuras de Datos: Matrices 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3]={{1,2,3},{4,5,6}}, trans[3][2];

    for(int i=0;i<2;i++)
        for(int j=0;j<3;j++)
            trans[j][i]=mat[i][j];

    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++) cout << trans[i][j] << " ";
        cout << endl;
    }
    // 1 4
    // 2 5
    // 3 6
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? [[1,4],[2,5],[3,6]]

? Caso 2: [[1]] ? [[1]]

? Caso 3: [[1,2],[3,4]] ? [[1,3],[2,4]]