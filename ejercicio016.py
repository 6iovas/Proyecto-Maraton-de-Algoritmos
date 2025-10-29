// Proyecto de Informatica
// Ejercicio 16
Ejercicio 16: Búsqueda Binaria (Iterativa)
Análisis del Problema
 Buscar un valor en un array ordenado; devolver índice (0-based) o -1 si no existe.
Diseño de la Solución
 Búsqueda binaria clásica: mantener l, r, calcular m = l + (r-l)/2.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int binary_search_iter(const vector<int>& a, int target) {
    int l = 0, r = (int)a.size() - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] == target) return m;
        else if (a[m] < target) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int x; cin>>x;
    cout << binary_search_iter(a,x) << '\n';
    return 0;
}

Pruebas
? n=6, a=[1 2 4 5 7 9], x=5 ? 3

? x=3 ? -1

? n=1, a=[10], x=10 ? 0