// Proyecto de Informatica
// Ejercicio 124
Ejercicio 122: Fenwick Tree (BIT)  construcción y range sum
Análisis del Problema
 Soportar add at pos and prefix sum queries; show range sum.
Diseño de la Solución
 Implementación clásica 1-based internal.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
struct Fenwick {
    int n; vector<long long> bit;
    Fenwick(int _n): n(_n), bit(n+1,0) {}
    void add(int idx, long long val){ for(; idx<=n; idx+=idx&-idx) bit[idx]+=val; }
    long long sum(int idx){ long long r=0; for(; idx>0; idx-=idx&-idx) r+=bit[idx]; return r; }
    long long range(int l,int r){ return sum(r) - sum(l-1); }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    Fenwick fw(n);
    for(int i=1;i<=n;++i){ long long x; cin>>x; fw.add(i,x); }
    int q; cin>>q;
    while(q--){
        int t; cin>>t;
        if(t==1){ int pos; long long val; cin>>pos>>val; fw.add(pos,val); }
        else { int l,r; cin>>l>>r; cout<<fw.range(l,r)<<"\n"; }
    }
    return 0;
}

Pruebas
? Initialize 1..5 with 1..5, range(1,5)=15; add at pos3 +10, range(1,5)=25.