// Proyecto de Informatica
// Ejercicio 107
Ejercicio 105: Generar todas las particiones de un número entero
Análisis del Problema
 Dividir un número n en sumas de enteros positivos (orden no importa).
Diseño de la Solución
 Usar backtracking recursivo para generar todas las combinaciones no decrecientes.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

void partition(int n, int max_val, vector<int>& cur) {
    if (n == 0) {
        for (int x : cur) cout << x << ' ';
        cout << '\n';
        return;
    }
    for (int i = min(n, max_val); i >= 1; --i) {
        cur.push_back(i);
        partition(n - i, i, cur);
        cur.pop_back();
    }
}

int main() {
    int n; cin >> n;
    vector<int> cur;
    partition(n, n, cur);
}

Pruebas
? Entrada: 4

Salida esperada:

 4
3 1
2 2
2 1 1
1 1 1 1
?