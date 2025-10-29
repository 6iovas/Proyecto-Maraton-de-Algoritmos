// Proyecto de Informatica
// Ejercicio 14
Ejercicio 14: Encontrar el k-ésimo elemento más grande (Heap)
Análisis del Problema
 Encontrar el k-ésimo elemento más grande de un arreglo usando una cola de prioridad (min-heap).
Diseño de la Solución
1. Insertar los elementos en un min-heap.

2. Mantener el tamaño del heap ? k.

3. El tope del heap será el k-ésimo elemento.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int kth_largest(vector<int>& a, int k) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int x : a) {
        pq.push(x);
        if (pq.size() > k) pq.pop();
    }
    return pq.top();
}

int main() {
    int n, k;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> k;
    cout << kth_largest(a, k);
}

Pruebas
? Entrada: 6 7 10 4 3 20 15 3
 Salida: 7