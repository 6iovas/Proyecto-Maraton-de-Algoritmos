// Proyecto de Informatica
// Ejercicio 273
Ejercicio 42  Range minimum query (RMQ) with sparse table  O(1) queries, O(n log n) build
Análisis
 Construir estructura para consultas de mínimo en rango (static array, no updates). Preprocesamiento O(n log n), consultas O(1) con sparse table using overlapping intervals.
Diseño
? st[k][i] = min on range [i, i+2^k-1].

? Query [l,r]: k = floor(log2(r-l+1)) ? min(st[k][l], st[k][r-2^k+1]).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct RMQ {
    int n;
    vector<vector<long long>> st;
    vector<int> lg;
    RMQ(const vector<long long>& a){
        n = a.size();
        lg.assign(n+1,0);
        for(int i=2;i<=n;++i) lg[i]=lg[i>>1]+1;
        int K = lg[n];
        st.assign(K+1, vector<long long>(n));
        st[0] = a;
        for(int k=1;k<=K;++k){
            for(int i=0;i + (1<<k) <= n; ++i)
                st[k][i] = min(st[k-1][i], st[k-1][i + (1<<(k-1))]);
        }
    }
    long long query(int l,int r){
        int k = lg[r-l+1];
        return min(st[k][l], st[k][r - (1<<k) + 1]);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    RMQ rmq(a);
    int q; cin>>q;
    while(q--){
        int l,r; cin>>l>>r;
        cout<<rmq.query(l,r)<<"\n";
    }
    return 0;
}

Pruebas
? Array [1,3,-1,7,0]. Query [1,3] ? -1, query [0,4] ? -1.