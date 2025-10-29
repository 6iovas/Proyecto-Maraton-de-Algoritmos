// Proyecto de Informatica
// Ejercicio 75
Título del Ejercicio: Orden Descendente de Enteros usando std::sort
Análisis del Problema
? Descripción del Problema: Ordenar un vector de enteros de mayor a menor usando std::sort y lambda.

? Entradas y Salidas:

? Entrada: Vector de enteros.

? Salida: Vector ordenado de mayor a menor.

Diseño de la Solución
? Algoritmo Propuesto:

1. Leer tamaño y elementos del vector.

2. Usar std::sort con lambda (a,b) => a>b.

3. Mostrar vector ordenado.

? Estructuras de Datos: std::vector.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cout << "Ingrese tamaño del vector: ";
    cin >> n;
    vector<int> v(n);
    cout << "Ingrese elementos:\n";
    for(int i=0;i<n;i++) cin >> v[i];

    sort(v.begin(), v.end(), [](int a,int b){ return a>b; });

    cout << "Vector ordenado descendente: ";
    for(int x:v) cout << x << " ";
    cout << endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada 5 1 3 2 ? Salida: 5 3 2 1
74. Buscar Primer Número Mayor que X usando Búsqueda Binaria Modificada