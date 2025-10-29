// Proyecto de Informatica
// Ejercicio 19
Ejercicio 18: Lower_bound / Upper_bound (primer/último índice de un elemento en array ordenado)
Análisis
 Encontrar primer índice (lower_bound) y último índice (upper_bound-1) de un valor.
Diseño
 Usar implementaciones estándar (std::lower_bound, std::upper_bound).
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int x; cin>>x;
    auto itl = lower_bound(a.begin(), a.end(), x);
    auto itu = upper_bound(a.begin(), a.end(), x);
    if (itl==a.end() || *itl != x) {
        cout << -1 << ' ' << -1 << '\n';
    } else {
        cout << int(itl - a.begin()) << ' ' << int(itu - a.begin() - 1) << '\n';
    }
    return 0;
}

Pruebas
? a=[1 2 2 2 3], x=2 ? 1 3

? x=4 ? -1 -1

? a=[5], x=5 ? 0 0