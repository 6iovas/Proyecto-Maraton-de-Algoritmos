// Proyecto de Informatica
// Ejercicio 32
Ejercicio 30: Kadane  Subarray con suma máxima
Análisis
 Encontrar suma máxima de subarray contiguo (algoritmo de Kadane O(n)).
Diseño
 Mantener current y best.
Código
#include <bits/stdc++.h>
using namespace std;

long long kadane(const vector<long long>& a){
    long long best = LLONG_MIN, cur = 0;
    for(long long x: a){
        cur = max(x, cur + x);
        best = max(best, cur);
    }
    return best;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    cout<<kadane(a)<<"\n";
    return 0;
}

Pruebas
? [-2 1 -3 4 -1 2 1 -5 4] ? 6 (subarray 4 -1 2 1)