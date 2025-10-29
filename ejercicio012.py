// Proyecto de Informatica
// Ejercicio 12
Ejercicio 12: Implementar Mergesort (recursivo)
Análisis del Problema
 Ordenar un arreglo de enteros aplicando Mergesort, un algoritmo de tipo divide y vencerás.
Diseño de la Solución
1. Dividir el arreglo en dos mitades.

2. Llamar recursivamente a Mergesort para cada mitad.

3. Combinar las dos mitades ordenadas.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

void merge_sort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int m = (l + r) / 2;
    merge_sort(a, l, m);
    merge_sort(a, m + 1, r);
    inplace_merge(a.begin() + l, a.begin() + m + 1, a.begin() + r + 1);
}

int main() {
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    merge_sort(a, 0, n - 1);
    for (int x : a) cout << x << " ";
}

Pruebas
? Entrada: 6 10 5 3 8 2 6
 Salida: 2 3 5 6 8 10