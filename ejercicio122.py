// Proyecto de Informatica
// Ejercicio 122
Ejercicio 120: Encadenar algoritmos STL (transform + sort + unique)
Análisis del Problema
 Dado vector de strings, normalizar (lowercase), ordenar, quitar duplicados, y mostrar.
Diseño de la Solución
 transform para lowercase, sort, unique, erase.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<string> v(n);
    for(int i=0;i<n;++i) cin>>v[i];
    for(auto &s: v) transform(s.begin(), s.end(), s.begin(), ::tolower);
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for(auto &s: v) cout << s << '\n';
    return 0;
}

Pruebas
? n=5 strings: A a B b A -> output: a b.