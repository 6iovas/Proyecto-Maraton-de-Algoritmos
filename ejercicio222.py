// Proyecto de Informatica
// Ejercicio 222
Ejercicio 17  Segment Tree (range sum) con point updates y soporte para índices grandes (coordinate compression)
Análisis del problema
 Implementar segment tree clásico para sumas en rango con updates puntuales. Además, si los índices son dispersos y grandes, usar compressión de coordenadas.
? Operaciones: update(pos, val) y query(l,r) inclusive.

? Complejidad: O(log n) por operación.

Diseño de la solución
? Si las posiciones son arbitrarias (<=1e9), primero compress: copiar y ordenar posiciones relevantes.

? Implementar segtree iterativo o recursivo. Aquí iterativo bottom-up (tamaño N = next power of two).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct SegTree {
    int n; vector<long long> t;
    SegTree(int _n=0){ init(_n); }
    void init(int _n){ n=1; while(n<_n) n<<=1; t.assign(2*n,0); }
    void setVal(int pos, long long val){ int p = pos + n; t[p] = val; for(p>>=1; p; p>>=1) t[p] = t[p<<1] + t[p<<1|1]; }
    long long query(int l,int r){ long long res=0; for(l+=n, r+=n; l<=r; l>>=1, r>>=1){
        if(l&1) res += t[l++];
        if(!(r&1)) res += t[r--];
    } return res;}
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q; if(!(cin>>q)) return 0;
    // queries: type 1 pos val (set pos to val), type 2 l r (sum)
    vector<tuple<int,long long,long long>> queries;
    vector<long long> coords;
    for(int i=0;i<q;++i){
        int t; cin>>t;
        if(t==1){ long long pos,val; cin>>pos>>val; queries.emplace_back(t,pos,val); coords.push_back(pos); }
        else { long long l,r; cin>>l>>r; queries.emplace_back(t,l,r); coords.push_back(l); coords.push_back(r); }
    }
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    auto getIdx = [&](long long x){ return int(lower_bound(coords.begin(), coords.end(), x) - coords.begin()); };
    SegTree st(coords.size());
    for(auto &qq: queries){
        int t; long long a,b; tie(t,a,b) = qq;
        if(t==1){
            int pos = getIdx(a);
            st.setVal(pos, b);
        } else {
            int l = getIdx(a), r = getIdx(b);
            cout << st.query(l,r) << "\n";
        }
    }
    return 0;
}

Prueba
? q=4: set (100->5), set (200->10), query(50,150) => 5, query(150,250) => 10.