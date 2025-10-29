// Proyecto de Informatica
// Ejercicio 11
Ejercicio 11: Implementar Quicksort (versión Lomuto)
Análisis del Problema
 El objetivo es ordenar un arreglo de enteros usando el algoritmo Quicksort, aplicando la partición Lomuto, que selecciona el último elemento como pivote.
Diseño de la Solución
1. Definir una función partition_lomuto() que coloque el pivote en su posición correcta.

2. Implementar quicksort() de forma recursiva.

3. En main(), leer el arreglo y aplicar el algoritmo.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int partition_lomuto(vector<int>& a, int l, int r) {
    int pivot = a[r];
    int i = l;
    for (int j = l; j < r; ++j)
        if (a[j] < pivot) swap(a[i++], a[j]);
    swap(a[i], a[r]);
    return i;
}

void quicksort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int p = partition_lomuto(a, l, r);
    quicksort(a, l, p - 1);
    quicksort(a, p + 1, r);
}

int main() {
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    quicksort(a, 0, n - 1);
    for (int x : a) cout << x << " ";
}

Pruebas
? Entrada: 7 3 6 8 10 1 2 1
 Salida esperada: 1 1 2 3 6 8 10

? Entrada: 5 5 4 3 2 1
 Salida esperada: 1 2 3 4 5