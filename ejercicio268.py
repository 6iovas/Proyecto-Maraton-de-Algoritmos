// Proyecto de Informatica
// Ejercicio 268
Ejercicio 39  Longest Increasing Subsequence (LIS) O(n log n) con reconstrucción
Análisis
 Encontrar la LIS (por valor) en un arreglo a en O(n log n) usando patience sorting + track predecessors para reconstruir la subsecuencia.
Diseño
? Mantener vector d con la mínima cola terminadora para cada longitud.

? Mantener pos[len] índice en a del elemento que termina subseq de longitud len.

? parent[i] para reconstrucción.

? Finalmente reconstruir desde pos[len-1].

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    vector<long long> d;
    vector<int> pos; // pos[len-1] = index in a of tail
    vector<int> parent(n, -1);
    for(int i=0;i<n;++i){
        auto it = lower_bound(d.begin(), d.end(), a[i]);
        int len = int(it - d.begin());
        if(it == d.end()){
            d.push_back(a[i]);
            pos.push_back(i);
        } else {
            *it = a[i];
            pos[len] = i;
        }
        if(len>0) parent[i] = pos[len-1];
        pos[len] = i;
    }
    int lis_len = d.size();
    cout<<lis_len<<"\n";
    // reconstruct one LIS: find index of last element (pos[lis_len-1])
    int cur = pos[lis_len-1];
    vector<long long> lis;
    while(cur != -1){ lis.push_back(a[cur]); cur = parent[cur]; }
    reverse(lis.begin(), lis.end());
    for(auto x: lis) cout<<x<<" ";
    cout<<"\n";
    return 0;
}

Pruebas
? a=[3,1,5,2,6,4,9] ? LIS length 4, one LIS e.g., 1 2 4 9.