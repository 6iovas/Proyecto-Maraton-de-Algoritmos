// Proyecto de Informatica
// Ejercicio 415
Título del Ejercicio: Buscar Número en Matriz con Punteros
Análisis del Problema
? Descripción del Problema: Buscar un número en matriz dinámica usando punteros.

? Entradas y Salidas:

? Entrada: Matriz m x n y número x.

? Salida: Posición o mensaje si no se encuentra.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer matriz usando aritmética de punteros.

2. Comparar cada elemento con x.

3. Mostrar posición o mensaje.

? Estructuras de Datos: Matriz dinámica y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int m=2,n=3;
    int mat[2][3]={{1,2,3},{4,5,6}};
    int x=5;
    bool encontrado=false;

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(*(*(mat+i)+j)==x){
                cout << "Elemento en fila " << i << ", col " << j << endl;
                encontrado=true;
            }
        }
    }
    if(!encontrado) cout << "Elemento no encontrado" << endl;
    return 0;
}

Pruebas
? Caso 1: x=5 ? fila 1, col 1

? Caso 2: x=7 ? no encontrado

? Caso 3: x=1 ? fila 0, col 0