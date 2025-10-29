// Proyecto de Informatica
// Ejercicio 126
Ejercicio 124: Implementar Union-Find (disjoint set) con path compression & union by rank
Análisis del Problema
 Estructura para mantener particiones dinámicas.
Diseño de la Solución
 find con path compression, union by rank/size.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, r;
    DSU(int n): p(n), r(n,0){ iota(p.begin(), p.end(), 0); }
    int find(int x){ return p[x]==x ? x : p[x]=find(p[x]); }
    bool unite(int a,int b){
        a=find(a); b=find(b);
        if(a==b) return false;
        if(r[a]<r[b]) swap(a,b);
        p[b]=a;
        if(r[a]==r[b]) ++r[a];
        return true;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    DSU dsu(n);
    for(int i=0;i<m;++i){
        int u,v; cin>>u>>v; dsu.unite(u,v);
    }
    int q; cin>>q;
    while(q--){
        int a,b; cin>>a>>b;
        cout << (dsu.find(a)==dsu.find(b) ? "SAME\n" : "DIFFERENT\n");
    }
    return 0;
}

Pruebas
? Crear edges, preguntar conectividad.