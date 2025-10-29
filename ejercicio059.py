// Proyecto de Informatica
// Ejercicio 59
Ejercicio 57: Bellman-Ford (pesos negativos permitidos)
Análisis
 Distancias mínimas y detección de ciclo negativo.
Diseño
 Relajación n-1 veces y verificación de relax adicional.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL<<60);
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    struct Edge{int u,v; ll w;};
    vector<Edge> edges(m);
    for(int i=0;i<m;++i) cin>>edges[i].u>>edges[i].v>>edges[i].w;
    int s; cin>>s;
    vector<ll> dist(n, INF); dist[s]=0;
    for(int it=0; it<n-1; ++it){
        for(auto &e: edges) if(dist[e.u]!=INF && dist[e.v] > dist[e.u]+e.w) dist[e.v] = dist[e.u]+e.w;
    }
    bool negCycle=false;
    for(auto &e: edges) if(dist[e.u]!=INF && dist[e.v] > dist[e.u]+e.w) negCycle=true;
    if(negCycle) cout<<"NEGATIVE CYCLE\n";
    else for(int i=0;i<n;++i) cout<<(dist[i]==INF?-1:dist[i])<<(i+1==n?'\n':' ');
    return 0;
}

Pruebas
? Caso con ciclo negativo para detectar.