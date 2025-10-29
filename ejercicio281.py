// Proyecto de Informatica
// Ejercicio 281
Ejercicio 48  Tree centroid decomposition (for distance queries / dynamic problems)
Análisis
 Build centroid decomposition of a tree to support queries like "count nodes within distance ? D" with updates. Provide centroid tree construction.
Diseño
? Repeatedly find centroid of current subtree by sizes, mark centroid, recursively decompose subtrees, keep parent in centroid tree. Complexity O(n log n) build.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int n;
vector<vector<int>> g;
vector<int> sz, used, parentC;

int dfs_size(int u,int p){
    sz[u]=1;
    for(int v:g[u]) if(v!=p && !used[v]) sz[u]+=dfs_size(v,u);
    return sz[u];
}
int find_centroid(int u,int p,int total){
    for(int v: g[u]) if(v!=p && !used[v]){
        if(sz[v] > total/2) return find_centroid(v,u,total);
    }
    return u;
}
void decompose(int u,int p){
    int total = dfs_size(u,-1);
    int c = find_centroid(u,-1,total);
    used[c]=1;
    parentC[c] = p;
    for(int v: g[c]) if(!used[v]) decompose(v,c);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!(cin>>n)) return 0;
    g.assign(n, {});
    for(int i=0;i<n-1;++i){ int u,v; cin>>u>>v; g[u].push_back(v); g[v].push_back(u); }
    sz.assign(n,0); used.assign(n,0); parentC.assign(n,-1);
    decompose(0,-1);
    for(int i=0;i<n;++i) cout<<i<<" -> centroid parent: "<<parentC[i]<<"\n";
    return 0;
}

Pruebas
? Small trees show centroid parents forming centroid tree.