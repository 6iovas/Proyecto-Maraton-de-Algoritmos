// Proyecto de Informatica
// Ejercicio 253
Ejercicio 33  Graph Isomorphism (naive backtracking + pruning for small n)
Análisis
 Determinar si dos labelled graphs G1 and G2 (n ? 10-12) son isomorfos (exist permutation mapping adjacency). For small n backtracking with degree sequence pruning works.
Diseño
? Quick prune: degree sequences must match multiset.

? Backtracking: assign mapping node-by-node, check partial adjacency consistency. Use ordering by degrees to reduce branching.

Código (C++)
#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> A, B;
vector<int> perm;
vector<char> used;
vector<int> order;

bool checkPartial(int idx){
    int u = order[idx];
    for(int i=0;i<idx;++i){
        int ui = order[i];
        if(A[u][ui] != B[perm[u]][perm[ui]]) return false;
    }
    return true;
}

bool backtrack(int idx){
    if(idx==n) return true;
    int u = order[idx];
    for(int v=0; v<n; ++v) if(!used[v]){
        perm[u]=v; used[v]=1;
        bool ok=true;
        for(int i=0;i<idx;++i){
            int ui=order[i];
            if(A[u][ui] != B[perm[u]][perm[ui]]){ ok=false; break; }
        }
        if(ok && backtrack(idx+1)) return true;
        used[v]=0;
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!(cin>>n)) return 0;
    A.assign(n, vector<int>(n));
    B.assign(n, vector<int>(n));
    for(int i=0;i<n;++i) for(int j=0;j<n;++j) cin>>A[i][j];
    for(int i=0;i<n;++i) for(int j=0;j<n;++j) cin>>B[i][j];
    // degrees
    vector<int> da(n,0), db(n,0);
    for(int i=0;i<n;++i) for(int j=0;j<n;++j){ da[i]+=A[i][j]; db[i]+=B[i][j]; }
    auto sda = da; auto sdb = db;
    sort(sda.begin(), sda.end()); sort(sdb.begin(), sdb.end());
    if(sda != sdb){ cout<<"Not isomorphic\n"; return 0; }
    order.resize(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int x,int y){ if(da[x]!=da[y]) return da[x]>da[y]; return x<y; });
    perm.assign(n, -1); used.assign(n,0);
    bool iso = backtrack(0);
    cout << (iso ? "Isomorphic\n" : "Not isomorphic\n");
    return 0;
}

Prueba
? n small (?8): test isomorphic permutations and non-isomorphic graphs.