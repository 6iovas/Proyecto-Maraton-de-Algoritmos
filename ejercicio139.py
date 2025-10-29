// Proyecto de Informatica
// Ejercicio 139
Ejercicio 137: Kruskal  Árbol de Expansión Mínima (MST)
Análisis del Problema
 Encontrar el costo mínimo de conectar todos los nodos con aristas ponderadas.
Diseño de la Solución
 Ordenar aristas por peso y usar Union-Find para evitar ciclos.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Edge{int u,v,w;};
struct DSU{
    vector<int> p;
    DSU(int n){p.resize(n);iota(p.begin(),p.end(),0);}
    int find(int x){return p[x]==x?x:p[x]=find(p[x]);}
    bool unite(int a,int b){a=find(a);b=find(b);if(a==b)return false;p[b]=a;return true;}
};

int main(){
    int n,m;cin>>n>>m;
    vector<Edge> e(m);
    for(auto &x:e)cin>>x.u>>x.v>>x.w;
    sort(e.begin(),e.end(),[](auto&a,auto&b){return a.w<b.w;});
    DSU d(n);
    int total=0;
    for(auto &x:e)if(d.unite(x.u,x.v)) total+=x.w;
    cout<<"Costo MST: "<<total<<"\n";
}

Pruebas
? Pequeño grafo ? imprime costo total.