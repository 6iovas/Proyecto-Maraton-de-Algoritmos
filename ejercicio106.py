// Proyecto de Informatica
// Ejercicio 106
Ejercicio 104: Generar permutaciones únicas con elementos repetidos
Análisis del Problema
 Generar permutaciones sin duplicados, aunque existan elementos iguales.
Diseño de la Solución
 Usar std::next_permutation tras ordenar el vector.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a.begin(), a.end());
    do {
        for (int x : a) cout << x << ' ';
        cout << '\n';
    } while (next_permutation(a.begin(), a.end()));
}

Pruebas
? Entrada: 3 seguido de 1 1 2

Salida esperada:

 1 1 2
1 2 1
2 1 1
?