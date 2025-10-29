// Proyecto de Informatica
// Ejercicio 125
Ejercicio 123: Sparse Table  RMQ (idempotent, O(1) queries)
Análisis del Problema
 Preprocesar para consultas de mínimo en rango (sin updates).
Diseño de la Solución
 st[k][i] min of length 2^k starting at i; query uses log.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct SparseTable {
    vector<vector<long long>> st;
    vector<int> lg;
    SparseTable(const vector<long long>& a){
        int n=a.size(), K=__lg(n)+1;
        st.assign(K, vector<long long>(n));
        lg.assign(n+1,0);
        for(int i=2;i<=n;++i) lg[i]=lg[i/2]+1;
        st[0]=a;
        for(int k=1;k<K;++k){
            for(int i=0;i + (1<<k) <= n; ++i)
                st[k][i] = min(st[k-1][i], st[k-1][i + (1<<(k-1))]);
        }
    }
    long long query(int l,int r){
        int k = lg[r - l + 1];
        return min(st[k][l], st[k][r - (1<<k) + 1]);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    SparseTable st(a);
    int q; cin>>q;
    while(q--){
        int l,r; cin>>l>>r;
        cout<<st.query(l,r)<<"\n";
    }
    return 0;
}

Pruebas
? a=[1,3,2,7,9,11,3], query(1,4)=min(3,2,7,9)=2.