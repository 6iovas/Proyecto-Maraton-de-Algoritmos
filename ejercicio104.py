// Proyecto de Informatica
// Ejercicio 104
Ejercicio 102: Generar combinaciones de tamaño k
Análisis del Problema
 Se pide imprimir todas las combinaciones posibles de tamaño k de un conjunto de n elementos.
Diseño de la Solución
 Usar una máscara binaria de n bits con k unos. Luego aplicar std::prev_permutation.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> mask(n, 0);
    fill(mask.begin(), mask.begin() + k, 1);
    do {
        for (int i = 0; i < n; ++i)
            if (mask[i]) cout << i + 1 << ' ';
        cout << '\n';
    } while (prev_permutation(mask.begin(), mask.end()));
}

Pruebas
? Entrada: n=4 k=2

Salida esperada:

 1 2
1 3
1 4
2 3
2 4
3 4
?