// Proyecto de Informatica
// Ejercicio 267
Ejercicio 38  Weighted Interval Scheduling (scheduling with binary search + DP)
Análisis
 Dado un conjunto de n intervalos [start_i, end_i) con valor w_i, seleccionar subconjunto disjunto de intervalos con máxima suma de pesos. Solución clásica O(n log n): ordenar por end, precomputar p(i) = último intervalo que termina ? start_i (binary search), DP dp[i] = max(dp[i-1], dp[p(i)] + w_i).
Diseño
? Ordenar por end.

? Construir array ends[] y para cada i buscar p(i) con upper_bound.

? DP iterativo O(n).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Interval { long long s,e,w; };
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<Interval> a(n);
    for(int i=0;i<n;++i) cin>>a[i].s>>a[i].e>>a[i].w;
    sort(a.begin(), a.end(), [](const Interval& A, const Interval& B){ return A.e < B.e; });
    vector<long long> ends(n);
    for(int i=0;i<n;++i) ends[i]=a[i].e;
    vector<long long> dp(n+1,0);
    vector<int> p(n, -1);
    for(int i=0;i<n;++i){
        int idx = int(upper_bound(ends.begin(), ends.end(), a[i].s) - ends.begin()) - 1;
        p[i] = idx;
    }
    for(int i=1;i<=n;++i){
        long long take = a[i-1].w + (p[i-1] >=0 ? dp[p[i-1]+1] : 0);
        dp[i] = max(dp[i-1], take);
    }
    cout<<dp[n]<<"\n";
    return 0;
}

Pruebas
? Intervals: [1,3,w=50],[2,5,w=20],[4,6,w=100] ? best pick [1,3] and [4,6] total 150.