// Proyecto de Informatica
// Ejercicio 76
Título del Ejercicio: Primer Número Mayor que X
Análisis del Problema
? Descripción del Problema: Dado un array ordenado, encontrar el primer número mayor que X.

? Entradas y Salidas:

? Entrada: Array ordenado, valor X.

? Salida: Primer número mayor que X o mensaje de no encontrado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Leer array ordenado y X.

2. Aplicar búsqueda binaria modificada para encontrar primer número mayor.

3. Mostrar resultado.

? Estructuras de Datos: Array.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
using namespace std;

int primerMayor(int arr[], int n, int X) {
    int res=-1, inicio=0, fin=n-1;
    while(inicio<=fin) {
        int mid = inicio + (fin-inicio)/2;
        if(arr[mid]>X) {
            res=arr[mid];
            fin=mid-1;
        } else inicio=mid+1;
    }
    return res;
}

int main() {
    int n,X;
    cout << "Ingrese tamaño del array: ";
    cin >> n;
    int arr[n];
    cout << "Ingrese elementos ordenados:\n";
    for(int i=0;i<n;i++) cin >> arr[i];
    cout << "Ingrese X: ";
    cin >> X;

    int res=primerMayor(arr,n,X);
    if(res!=-1) cout << "Primer número mayor que " << X << ": " << res << endl;
    else cout << "No hay número mayor que " << X << endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [1 3 5 7], X=4 ? Salida: 5

? Caso 2: Entrada [2 4 6 8], X=8 ? Salida: No hay número mayor que 8
75. HeapSort