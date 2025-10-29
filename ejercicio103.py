// Proyecto de Informatica
// Ejercicio 103
Ejercicio 101: Generar todas las permutaciones de un vector
Análisis del Problema
 Se requiere generar e imprimir todas las permutaciones posibles de un conjunto de números distintos.
Diseño de la Solución
? Ordenar inicialmente el vector.

? Usar std::next_permutation hasta agotar todas las permutaciones posibles.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; 
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());
    do {
        for (int x : a) cout << x << ' ';
        cout << '\n';
    } while (next_permutation(a.begin(), a.end()));

    return 0;
}

Pruebas
? Entrada: 3 seguido de 1 2 3

Salida esperada:

 1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
?