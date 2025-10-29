// Proyecto de Informatica
// Ejercicio 229
Ejercicio 23  Edmonds algorithm (Directed Minimum Spanning Arborescence / ChuLiu)  skeleton
Análisis
 Encontrar un minimum spanning arborescence (directed MST) rooted at r (min total incoming cost to reach all nodes) usando Edmonds/ChuLiu. Es útil cuando aristas son dirigidas y queremos árbol arborescente (cada nodo excepto root tiene exactamente un in-edge). Implementación completa es larga; proponemos plantilla funcional adecuada para n?~2000.
Diseño
? Algoritmo por pasos: elegir mínimo in-edge para each node; detectar ciclos; contractar ciclos; adjust costs; iterate until no cycles.

? Complejidad: O(E * V).

Código (C++) (implementación funcional, adapted from classic templates)
#include <bits/stdc++.h>
using namespace std;
const long long INF = (1LL<<60);
// returns total cost or -1 if not possible
long long directed_mst(int n, int root, vector<tuple<int,int,long long>>& edges){
    long long res = 0;
    while(true){
        vector<long long> in(n, INF);
        vector<int> pre(n, -1);
        for(auto &e: edges){
            int u,v; long long w; tie(u,v,w)=e;
            if(w < in[v] && u!=v){ in[v]=w; pre[v]=u; }
        }
        in[root]=0; // root has no incoming
        for(int i=0;i<n;++i) if(in[i]==INF) return -1; // no arborescence
        // detect cycles
        int cnt=0;
        vector<int> id(n, -1), vis(n, -1);
        for(int i=0;i<n;++i) res += in[i];
        for(int i=0;i<n;++i){
            int v=i;
            while(vis[v]!=i && id[v]==-1 && v!=root){ vis[v]=i; v=pre[v]; }
            if(v!=root && id[v]==-1){
                for(int u = pre[v]; u!=v; u=pre[u]) id[u]=cnt;
                id[v]=cnt++;
            }
        }
        if(cnt==0) break; // no cycles
        for(int i=0;i<n;++i) if(id[i]==-1) id[i]=cnt++;
        // contract
        vector<tuple<int,int,long long>> newEdges;
        for(auto &e: edges){
            int u,v; long long w; tie(u,v,w)=e;
            int uu=id[u], vv=id[v];
            if(uu!=vv) newEdges.emplace_back(uu, vv, w - in[v]);
        }
        n = cnt; root = id[root];
        edges.swap(newEdges);
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<tuple<int,int,long long>> edges;
    for(int i=0;i<m;++i){
        int u,v; long long w; cin>>u>>v>>w;
        edges.emplace_back(u,v,w);
    }
    int root; cin>>root;
    long long ans = directed_mst(n, root, edges);
    if(ans<0) cout<<"No arborescence\n"; else cout<<"Min arborescence cost: "<<ans<<"\n";
    return 0;
}

Pruebas
? Small directed graph example from standard references; check result.