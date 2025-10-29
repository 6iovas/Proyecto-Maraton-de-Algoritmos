// Proyecto de Informatica
// Ejercicio 109
Ejercicio 107: Uso de std::binary_search
Análisis del Problema
 Determinar si un elemento existe en un vector ordenado.
Diseño de la Solución
 Aplicar std::sort y std::binary_search.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 3, 5, 7, 9};
    int x; cin >> x;
    if (binary_search(v.begin(), v.end(), x))
        cout << "Encontrado\n";
    else
        cout << "No encontrado\n";
}

Pruebas
? Entrada: 5 ? Encontrado

? Entrada: 4 ? No encontrado