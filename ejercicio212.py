// Proyecto de Informatica
// Ejercicio 212
Ejercicio 7  Strongly Connected Components (Tarjan, O(n+m)) y compresión de componente
Análisis del problema
 Encontrar SCCs en grafo dirigido y construir grafo condensado (component graph) donde cada SCC es un nodo. Tarjan produce índices, lowlink, stack.
Diseño de la solución
? Implementar Tarjan: arrays disc, low, instack, stack.

? Asignar componente id a cada nodo.

? Construir grafo condensado eliminando aristas intra-componente; opcionalmente contar componentes sources/sinks.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int timerGlob = 0, compCnt = 0;
void tarjanDFS(int v, vector<vector<int>>& g, vector<int>& disc, vector<int>& low,
               vector<int>& st, vector<char>& inStack, vector<int>& comp) {
    disc[v] = low[v] = ++timerGlob;
    st.push_back(v); inStack[v]=1;
    for(int to: g[v]){
        if(disc[to]==0){
            tarjanDFS(to,g,disc,low,st,inStack,comp);
            low[v] = min(low[v], low[to]);
        } else if(inStack[to]){
            low[v] = min(low[v], disc[to]);
        }
    }
    if(low[v]==disc[v]){
        // root of SCC
        while(true){
            int u = st.back(); st.pop_back(); inStack[u]=0;
            comp[u] = compCnt;
            if(u==v) break;
        }
        ++compCnt;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<int>> g(n);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; g[u].push_back(v); }
    vector<int> disc(n,0), low(n,0), comp(n,-1), st; vector<char> inStack(n,0);
    for(int i=0;i<n;++i) if(disc[i]==0) tarjanDFS(i,g,disc,low,st,inStack,comp);
    cout<<"SCC count: "<<compCnt<<"\n";
    // Build condensed graph
    vector<unordered_set<int>> cond(compCnt);
    for(int u=0;u<n;++u){
        for(int v: g[u]){
            if(comp[u]!=comp[v]) cond[comp[u]].insert(comp[v]);
        }
    }
    cout<<"Condensed adjacency:\n";
    for(int i=0;i<compCnt;++i){
        cout<<i<<": ";
        for(int v: cond[i]) cout<<v<<" ";
        cout<<"\n";
    }
    return 0;
}

Pruebas
? Grafo con ciclos y componentes; comprobar SCC count y nodos por componente.