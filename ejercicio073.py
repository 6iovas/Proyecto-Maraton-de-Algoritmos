// Proyecto de Informatica
// Ejercicio 73
Título del Ejercicio: Ordenamiento de un Array usando Mergesort
Análisis del Problema
? Descripción del Problema: Dado un array de números enteros, ordenar sus elementos de menor a mayor usando el algoritmo Mergesort.

? Entradas y Salidas:

? Entrada: Array de tamaño n con números enteros.

? Salida: Array ordenado de menor a mayor.

Diseño de la Solución
? Algoritmo Propuesto:

1. Leer tamaño del array y elementos.

2. Aplicar Mergesort: dividir array en dos mitades, ordenar cada mitad recursivamente, fusionarlas.

3. Mostrar array ordenado.

? Estructuras de Datos: Array simple.

? Funciones Principales: main, mergeSort, merge.

Código Fuente (C++):
#include <iostream>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    for(int i = 0; i < n1; i++) L[i] = arr[l+i];
    for(int j = 0; j < n2; j++) R[j] = arr[m+1+j];

    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while(i<n1) arr[k++] = L[i++];
    while(j<n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if(l<r) {
        int m = l + (r-l)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}

int main() {
    int n;
    cout << "Ingrese tamaño del array: ";
    cin >> n;
    int arr[n];
    cout << "Ingrese elementos del array:\n";
    for(int i=0;i<n;i++) cin >> arr[i];

    mergeSort(arr,0,n-1);

    cout << "Array ordenado: ";
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada 5 2 4 1 3 ? Salida: 1 2 3 4 5

? Caso 2: Entrada 10 7 8 9 ? Salida: 7 8 9 10
72. Ordenar un Array de Estructuras usando std::sort