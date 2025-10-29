// Proyecto de Informatica
// Ejercicio 283
Ejercicio 50  Graph coloring heuristic (greedy Welsh-Powell) + exact check small graphs (backtracking)
Análisis
 Color the vertices of a graph with minimum colors (chromatic number). Exact is NP-hard; implement heuristic WelshPowell (order vertices by descending degree, greedily color each with smallest possible color). Also provide exact backtracking for n ? 20.
Diseño
? Heuristic: sort vertices by degree, assign smallest available color using boolean used array.

? Exact: backtracking try assign colors up to current best and prune by conflicts.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int n;
vector<vector<int>> adj;
vector<int> order;

int greedy_coloring(){
    vector<int> deg(n);
    for(int i=0;i<n;++i) deg[i]=adj[i].size();
    order.resize(n); iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a,int b){ return deg[a]>deg[b]; });
    vector<int> color(n, -1);
    int maxc = 0;
    for(int u: order){
        vector<char> used(n+1,false);
        for(int v: adj[u]) if(color[v]!=-1) used[color[v]] = true;
        int c=1; while(used[c]) ++c;
        color[u]=c; maxc = max(maxc, c);
    }
    return maxc;
}

// exact (backtracking) for small n
int best = INT_MAX;
void exact_bt(vector<int>& color, int idx, int usedColors){
    if(usedColors >= best) return;
    if(idx==n){ best = min(best, usedColors); return; }
    int u = idx;
    vector<char> used(usedColors+2,false);
    for(int v: adj[u]) if(color[v]>0 && color[v] <= usedColors) used[color[v]]=true;
    for(int c=1;c<=usedColors;++c){
        if(!used[c]){ color[u]=c; exact_bt(color, idx+1, usedColors); color[u]=0; }
    }
    // try new color
    color[u] = usedColors+1;
    exact_bt(color, idx+1, usedColors+1);
    color[u]=0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!(cin>>n)) return 0;
    adj.assign(n, {});
    int m; cin>>m;
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; adj[u].push_back(v); adj[v].push_back(u); }
    int g = greedy_coloring();
    cout<<"Greedy colors: "<<g<<"\n";
    if(n<=20){
        vector<int> color(n,0);
        best = g;
        exact_bt(color, 0, 0);
        cout<<"Exact chromatic (n<=20): "<<best<<"\n";
    } else cout<<"Exact coloring skipped (n>20)\n";
    return 0;
}

Pruebas
? Small graphs: triangle -> greedy 3, exact 3; bipartite -> greedy 2, exact 2.