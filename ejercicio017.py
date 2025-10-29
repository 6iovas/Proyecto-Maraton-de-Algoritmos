// Proyecto de Informatica
// Ejercicio 17
Ejercicio 17: Búsqueda Binaria (Recursiva)
Análisis
 Misma funcionalidad que la iterativa pero con recursión.
Diseño
 Función recursiva binsearch(a, l, r, target).
Código
#include <bits/stdc++.h>
using namespace std;

int binsearch_rec(const vector<int>& a, int l, int r, int target) {
    if (l > r) return -1;
    int m = l + (r - l) / 2;
    if (a[m] == target) return m;
    if (a[m] < target) return binsearch_rec(a, m+1, r, target);
    return binsearch_rec(a, l, m-1, target);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int x; cin>>x;
    cout << binsearch_rec(a, 0, n-1, x) << '\n';
    return 0;
}

Pruebas