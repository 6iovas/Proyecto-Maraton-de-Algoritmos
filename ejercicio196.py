// Proyecto de Informatica
// Ejercicio 196
Ejercicio 192: Buscar primer y último índice de un elemento (binary search bounds)
Análisis
 Encontrar primer y último índice de x en array ordenado.
Diseño
 lower_bound y upper_bound-1.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n); for(int i=0;i<n;++i) cin>>a[i];
    int x; cin>>x;
    auto itl = lower_bound(a.begin(), a.end(), x);
    auto itu = upper_bound(a.begin(), a.end(), x);
    if(itl==a.end() || *itl!=x) cout<<"-1 -1\n";
    else cout<<int(itl - a.begin())<<" "<<int(itu - a.begin() - 1)<<"\n";
}

Prueba
? a=[1,2,2,2,3], x=2 ? 1 3