// Proyecto de Informatica
// Ejercicio 355
Título del Ejercicio: Multiplicar Dos Matrices
Análisis del Problema
? Descripción del Problema: Multiplicar dos matrices compatibles y mostrar el resultado.

? Entradas y Salidas:

? Entrada: Dos matrices m x n y n x p.

? Salida: Matriz resultante m x p.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar matriz resultado en 0.

2. Multiplicar filas de A por columnas de B.

3. Mostrar resultado.

? Estructuras de Datos: Arrays bidimensionales.

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

    cout << "Matriz resultante:\n";
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++) cout << C[i