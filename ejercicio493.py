// Proyecto de Informatica
// Ejercicio 493
Título del Ejercicio: Multiplicar Matrices
Análisis del Problema
? Descripción del Problema: Multiplicar dos matrices m x n y n x p.

? Entradas y Salidas:

? Entrada: Dos matrices de dimensiones compatibles.

? Salida: Matriz resultante m x p.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar matriz resultado con ceros.

2. Recorrer filas y columnas multiplicando y sumando los productos correspondientes.

? Estructuras de Datos: Matrices 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int A[2][3]={{1,2,3},{4,5,6}};
    int B[3][2]={{7,8},{9,10},{11,12}};
    int C[2][2]={0};

    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            for(int k=0;k<3;k++)
                C[i][j]+=A[i][k]*B[k][j];

    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++) cout << C[i][j] << " ";
        cout << endl;
    }
    // 58 64
    // 139 154
    return 0;
}

Pruebas
? Caso 1: A=[[1,2],[3,4]], B=[[5,6],[7,8]] ? [[19,22],[43,50]]

? Caso 2: A=[[1]], B=[[2]] ? [[2]]

? Caso 3: A=[[0]], B=[[0]] ? [[0]]