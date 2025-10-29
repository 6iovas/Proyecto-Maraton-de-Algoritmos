// Proyecto de Informatica
// Ejercicio 375
Título del Ejercicio: Eliminar Duplicados en un Array
Análisis del Problema
? Descripción del Problema: Crear un nuevo array que contenga los elementos únicos de un array dado.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño.

? Salida: Array sin duplicados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer array original.

2. Verificar si el elemento ya está en el nuevo array.

3. Agregar solo si no está presente.

? Estructuras de Datos: Dos arrays y un contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,2,3,3,3,4};
    int n=7, unicos[7], k=0;

    for(int i=0;i<n;i++){
        bool encontrado=false;
        for(int j=0;j<k;j++)
            if(unicos[j]==arr[i]) encontrado=true;
        if(!encontrado) unicos[k++]=arr[i];
    }

    cout << "Array sin duplicados: ";
    for(int i=0;i<k;i++) cout << unicos[i] << " ";
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,2,3,3,3,4] ? [1,2,3,4]

? Caso 2: [1,1,1] ? [1]

? Caso 3: [1,2,3] ? [1,2,3]