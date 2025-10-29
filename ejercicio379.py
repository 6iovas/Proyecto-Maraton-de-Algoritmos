// Proyecto de Informatica
// Ejercicio 379
Título del Ejercicio: Buscar Elemento en Matriz
Análisis del Problema
? Descripción del Problema: Buscar un número en una matriz y devolver su posición (fila,columna).

? Entradas y Salidas:

? Entrada: Matriz y número a buscar.

? Salida: Posición o mensaje si no se encuentra.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer matriz con bucles anidados.

2. Comparar cada elemento con el valor buscado.

3. Mostrar fila y columna si se encuentra.

? Estructuras de Datos: Matriz bidimensional.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3]={{1,2,3},{4,5,6}};
    int buscar=5;
    bool encontrado=false;

    for(int i=0;i<2;i++){
        for(int j=0;j<3;j++){
            if(mat[i][j]==buscar){
                cout << "Elemento encontrado en fila " << i << ", columna " << j << endl;
                encontrado=true;
            }
        }
    }

    if(!encontrado) cout << "Elemento no encontrado" << endl;
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6]], buscar 5 ? fila 1, columna 1

? Caso 2: buscar 7 ? Elemento no encontrado

? Caso 3: buscar 1 ? fila 0, columna 0