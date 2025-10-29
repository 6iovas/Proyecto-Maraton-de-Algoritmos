// Proyecto de Informatica
// Ejercicio 146
Ejercicio 144: Búsqueda binaria en un vector de pares (clave, valor)
Análisis del Problema
 Dado un vector de pares (clave, valor) ordenado por la clave, se desea buscar una clave específica y devolver su valor asociado.
Diseño de la Solución
 Usar std::binary_search y std::lower_bound para encontrar el índice exacto del par que contiene la clave buscada.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    vector<pair<int, string>> data(n);
    for (int i = 0; i < n; ++i)
        cin >> data[i].first >> data[i].second;
    sort(data.begin(), data.end());
    int key; cin >> key;

    auto it = lower_bound(data.begin(), data.end(), make_pair(key, string("")));
    if (it != data.end() && it->first == key)
        cout << "Valor encontrado: " << it->second << '\n';
    else
        cout << "Clave no encontrada\n";
}

Pruebas
Entrada:

 3
10 perro
20 gato
30 pez
20
? 
? Salida: Valor encontrado: gato