// Proyecto de Informatica
// Ejercicio 77
Título del Ejercicio: Ordenamiento usando HeapSort
Análisis del Problema
? Descripción del Problema: Ordenar un array de enteros usando HeapSort.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Array ordenado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Construir heap máximo.

2. Intercambiar raíz con último elemento.

3. Reducir tamaño del heap y heapify.

4. Mostrar array ordenado.

? Estructuras de Datos: Array.

? Funciones Principales: main, heapify.

Código Fuente (C++):
#include <iostream>
using namespace std;

void heapify(int arr[], int n, int i) {
    int largest=i,l=2*i+1,r=2*i+2;
    if(l<n && arr[l]>arr[largest]) largest=l;
    if(r<n && arr[r]>arr[largest]) largest=r;
    if(largest!=i){
        swap(arr[i],arr[largest]);
        heapify(arr,n,largest);
    }
}

void heapSort(int arr[], int n) {
    for(int i=n/2-1;i>=0;i--) heapify(arr,n,i);
    for(int i=n-1;i>=0;i--){
        swap(arr[0],arr[i]);
        heapify(arr,i,0);
    }
}

int main(){
    int n;
    cout<<"Ingrese tamaño del array: ";
    cin>>n;
    int arr[n];
    cout<<"Ingrese elementos: \n";
    for(int i=0;i<n;i++) cin>>arr[i];

    heapSort(arr,n);

    cout<<"Array ordenado: ";
    for(int i=0;i<n;i++) cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: [4 10 3 5] ? Salida: 3 4 5 10
76. Ordenar Array de Cadenas usando std::sort