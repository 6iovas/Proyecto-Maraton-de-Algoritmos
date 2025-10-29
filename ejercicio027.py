// Proyecto de Informatica
// Ejercicio 27
Ejercicio 25: Counting Sort (enteros pequeños, no negativos)
Análisis
 Orden estable para rango 0..K.
Diseño
 Contar frecuencias y reconstruir array.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    int mx = 0;
    for(int i=0;i<n;++i){ cin>>a[i]; mx = max(mx, a[i]); }
    vector<int> cnt(mx+1, 0);
    for(int x:a) ++cnt[x];
    for(int i=0;i<=mx;++i){
        while(cnt[i]--) cout<<i<<' ';
    }
    cout<<'\n';
    return 0;
}

Pruebas
? a=[4 2 2 1 3] ? 1 2 2 3 4.