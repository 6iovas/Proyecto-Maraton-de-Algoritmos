// Proyecto de Informatica
// Ejercicio 111
Ejercicio 109: Ordenar palabras alfabéticamente ignorando mayúsculas
Análisis del Problema
 Ordenar texto sin diferenciar entre mayúsculas y minúsculas.
Diseño de la Solución
 Usar std::sort con comparador que convierte temporalmente a minúsculas.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

bool cmp(string a, string b) {
    transform(a.begin(), a.end(), a.begin(), ::tolower);
    transform(b.begin(), b.end(), b.begin(), ::tolower);
    return a < b;
}

int main() {
    int n; cin >> n;
    vector<string> v(n);
    for (auto &s : v) cin >> s;
    sort(v.begin(), v.end(), cmp);
    for (auto &s : v) cout << s << '\n';
}

Pruebas
? Entrada: 3 ? Hola hola mundo

Salida:

 hola
Hola
? mundo