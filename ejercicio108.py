// Proyecto de Informatica
// Ejercicio 108
Ejercicio 106: Calcular todas las permutaciones lexicográficas posteriores
Análisis del Problema
 Encontrar la siguiente permutación lexicográfica posible.
Diseño de la Solución
 Usar std::next_permutation.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    if (next_permutation(a.begin(), a.end())) {
        for (int x : a) cout << x << ' ';
    } else {
        cout << "No existe siguiente permutación\n";
    }
}

Pruebas
? Entrada: 3 seguido de 1 2 3 ? 1 3 2

? Entrada: 3 2 1 ? No existe siguiente permutación