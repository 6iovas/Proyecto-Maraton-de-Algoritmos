// Proyecto de Informatica
// Ejercicio 223
Ejercicio 18  Heavy-Light Decomposition (HLD)  path sum queries on tree, basic version
Análisis del problema
 Implementar HLD para manejar consultas sobre caminos en un árbol (por ejemplo, sumar valores a lo largo del camino uv) con updates puntuales.
? Requisitos: tree with n nodes, initial node values, operations: update(u,val) (set/assign) and query(u,v) (sum along path).

? Complejidad: O(log² n) per query using segment tree over base array.

Código (C++) (esqueleto funcional con operaciones set and sum)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Seg {
    int n; vector<ll> t;
    Seg(int n=0){ init(n); }
    void init(int _n){ n=1; while(n<_n) n<<=1; t.assign(2*n,0); }
    void setVal(int pos, ll val){ int p=pos+n; t[p]=val; for(p>>=1;p;p>>=1) t[p]=t[p<<1]+t[p<<1|1]; }
    ll query(int l,int r){ ll res=0; for(l+=n,r+=n;l<=r;l>>=1,r>>=1){ if(l&1) res+=t[l++]; if(!(r&1)) res+=t[r--]; } return res; }
};

int n;
vector<vector<int>> g;
vector<int> parent_, depth_, heavy, head, pos;
vector<int> sz;
int curPos;
vector<ll> value; // initial values
Seg seg;

int dfs1(int v,int p){
    parent_[v]=p; sz[v]=1; int maxsz=0;
    for(int to: g[v]) if(to!=p){
        depth_[to]=depth_[v]+1;
        int s = dfs1(to,v);
        sz[v]+=s;
        if(s>maxsz){ maxsz=s; heavy[v]=to; }
    }
    return sz[v];
}
void dfs2(int v,int h){
    head[v]=h; pos[v]=curPos++;
    seg.setVal(pos[v], value[v]);
    if(heavy[v]!=-1) dfs2(heavy[v], h);
    for(int to: g[v]) if(to!=parent_[v] && to!=heavy[v]) dfs2(to, to);
}
ll queryPath(int a,int b){
    ll res=0;
    while(head[a]!=head[b]){
        if(depth_[head[a]] < depth_[head[b]]) swap(a,b);
        int h = head[a];
        res += seg.query(pos[h], pos[a]);
        a = parent_[h];
    }
    if(depth_[a] > depth_[b]) swap(a,b);
    res += seg.query(pos[a], pos[b]);
    return res;
}
void updateNode(int v, ll val){
    seg.setVal(pos[v], val);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if(!(cin>>n>>q)) return 0;
    g.assign(n, {});
    for(int i=0;i<n-1;++i){ int u,v; cin>>u>>v; g[u].push_back(v); g[v].push_back(u); }
    value.assign(n,0);
    for(int i=0;i<n;++i) cin>>value[i];
    parent_.assign(n,-1); depth_.assign(n,0); heavy.assign(n,-1);
    head.assign(n,0); pos.assign(n,0); sz.assign(n,0);
    seg.init(n);
    curPos=0;
    dfs1(0,-1);
    dfs2(0,0);
    while(q--){
        int type; cin>>type;
        if(type==1){ int v; ll val; cin>>v>>val; updateNode(v,val); }
        else { int u,v; cin>>u>>v; cout<<queryPath(u,v)<<"\n"; }
    }
    return 0;
}

Prueba
? Árbol simple con valores en nodos; consulta path sum returns sum of node values along uv.