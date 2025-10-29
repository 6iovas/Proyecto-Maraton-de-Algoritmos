// Proyecto de Informatica
// Ejercicio 71
Ejercicio 69: Eulerian Path / Circuit (Hierholzer)
Análisis
 Determinar y encontrar Eulerian path/circuit en grafo dirigido o no dirigido.
Diseño
 Check degree conditions, run Hierholzer.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<pair<int,int>>> g(n);
    vector<int> deg(n,0);
    vector<pair<int,int>> edges(m);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; edges[i]={u,v}; g[u].push_back({v,i}); g[v].push_back({u,i}); deg[u]++; deg[v]++; }
    // Check Eulerian for undirected: all vertices with deg>0 must be connected & 0 or 2 odd degrees
    int odd=0, start=0;
    for(int i=0;i<n;++i){ if(deg[i]%2) odd++; if(deg[i]>0) start=i; }
    if(start==0 && deg[0]==0 && m==0){ cout<<"EMPTY\n"; return 0; }
    if(!(odd==0 || odd==2)){ cout<<"NO EULER\n"; return 0; }
    vector<char> used(m,0);
    vector<int> st, path;
    st.push_back(start);
    vector<int> idx(n,0);
    while(!st.empty()){
        int v=st.back();
        while(idx[v] < (int)g[v].size() && used[g[v][idx[v]].second]) idx[v]++;
        if(idx[v]==(int)g[v].size()){ path.push_back(v); st.pop_back(); }
        else { auto [to,id]=g[v][idx[v]++]; used[id]=1; st.push_back(to); }
    }
    if((int)path.size() != m+1){ cout<<"NO EULER\n"; return 0; }
    reverse(path.begin(), path.end());
    for(int x: path) cout<<x<<" ";
    cout<<"\n";
    return 0;
}

Pruebas
? Small Eulerian graphs tested.