// Proyecto de Informatica
// Ejercicio 112
Ejercicio 110: Calcular mediana usando dos priority_queue
Análisis del Problema
 Calcular la mediana de un flujo continuo de números.
Diseño de la Solución
 Mantener dos heaps: uno max-heap (menores) y otro min-heap (mayores).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    priority_queue<int> left;
    priority_queue<int, vector<int>, greater<int>> right;
    int x;
    while (cin >> x) {
        if (left.empty() || x <= left.top()) left.push(x);
        else right.push(x);

        if (left.size() > right.size() + 1) {
            right.push(left.top()); left.pop();
        } else if (right.size() > left.size()) {
            left.push(right.top()); right.pop();
        }

        double median;
        if (left.size() == right.size()) median = (left.top() + right.top()) / 2.0;
        else median = left.top();
        cout << "Mediana actual: " << median << "\n";
    }
}

Pruebas
? Entrada: 5 2 1 4 3

? Salidas intermedias: 5, 3.5, 2, 3, 3