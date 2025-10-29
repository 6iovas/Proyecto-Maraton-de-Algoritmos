// Proyecto de Informatica
// Ejercicio 214
Ejercicio 9  Fenwick Tree (BIT) con support para range update & point query (difference trick)
Análisis del problema
 Implementar Fenwick Tree (BIT) para soporte de range add y point query (frecuente en tareas con actualizaciones por rango y consulta de un índice). Operaciones en O(log n).
Diseño de la solución
? Usar BIT sobre diferencia d[i] tal que a[i] = sum_{j<=i} d[j].

? Range add [l,r] con add(l, val); add(r+1, -val).

? Point query prefix_sum(i).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct Fenwick {
    int n; vector<long long> bit;
    Fenwick(int n): n(n), bit(n+1,0) {}
    void add(int idx, long long val){ for(++idx; idx<=n; idx+=idx&-idx) bit[idx]+=val; }
    long long sumPrefix(int idx){ long long r=0; for(++idx; idx>0; idx-=idx&-idx) r+=bit[idx]; return r; }
    // range add [l,r] by val:
    void rangeAdd(int l,int r,long long val){ add(l,val); if(r+1<n) add(r+1,-val); }
    long long pointQuery(int idx){ return sumPrefix(idx); }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    Fenwick fw(n);
    int q; cin>>q;
    while(q--){
        int type; cin>>type;
        if(type==1){ int l,r; long long v; cin>>l>>r>>v; fw.rangeAdd(l,r,v); }
        else { int idx; cin>>idx; cout<<fw.pointQuery(idx)<<"\n"; }
    }
    return 0;
}

Pruebas
? Inicial n=5; update range (1,3) +10; query point 2 -> 10; query point 4 -> 0.