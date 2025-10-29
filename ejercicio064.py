// Proyecto de Informatica
// Ejercicio 64
Ejercicio 62: Componentes fuertemente conexas (Kosaraju)
Análisis
 Dividir grafo dirigido en SCCs.
Diseño
 Kosaraju: orden por finish times, transpose, DFS.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
void dfs1(int u, vector<vector<int>>& g, vector<int>& vis, vector<int>& order){
    vis[u]=1;
    for(int v:g[u]) if(!vis[v]) dfs1(v,g,vis,order);
    order.push_back(u);
}
void dfs2(int u, vector<vector<int>>& gt, vector<int>& comp){
    comp.push_back(u);
    for(int v: gt[u]) if(find(comp.begin(), comp.end(), v)==comp.end()) dfs2(v,gt,comp);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<int>> g(n), gt(n);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; g[u].push_back(v); gt[v].push_back(u); }
    vector<int> vis(n,0), order;
    for(int i=0;i<n;++i) if(!vis[i]) dfs1(i,g,vis,order);
    reverse(order.begin(), order.end());
    vector<int> compvis(n,0);
    for(int u: order){
        if(compvis[u]) continue;
        vector<int> comp;
        // stack DFS to avoid find() inside recursion --> use normal DFS marking
        stack<int> st; st.push(u); compvis[u]=1;
        while(!st.empty()){
            int x = st.top(); st.pop(); comp.push_back(x);
            for(int v: gt[x]) if(!compvis[v]){ compvis[v]=1; st.push(v); }
        }
        for(int x: comp) cout<<x<<' ';
        cout<<"\n";
    }
    return 0;
}

Pruebas
? Pequeño grafo con SCCs  imprime componentes por línea.