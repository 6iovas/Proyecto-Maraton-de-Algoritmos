// Proyecto de Informatica
// Ejercicio 13
Ejercicio 13: Búsqueda Binaria (Iterativa)
Análisis del Problema
 Dado un arreglo ordenado, buscar un elemento usando búsqueda binaria.
Diseño de la Solución
1. Definir límites l y r.

2. Mientras l ? r, calcular el punto medio m.

3. Ajustar los límites según el valor del objetivo.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int binary_search_iter(const vector<int>& a, int target) {
    int l = 0, r = a.size() - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] == target) return m;
        else if (a[m] < target) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

int main() {
    int n, x;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> x;
    cout << binary_search_iter(a, x);
}

Pruebas
? Entrada: 6 1 2 4 5 7 9 5
 Salida: 3