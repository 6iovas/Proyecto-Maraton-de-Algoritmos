// Proyecto de Informatica
// Ejercicio 123
Ejercicio 121: Implementar Segment Tree (range sum) iterativo (bottom-up)
Análisis del Problema
 Range sum queries + point updates, implementación iterativa (n power of two).
Diseño de la Solución
 Árbol en array de tamaño 2*n, where leaves stored at n..2n-1.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
struct SegTree {
    int n; vector<long long> t;
    SegTree(int _n): n(_n), t(2*_n,0) {}
    void build(const vector<long long>& a){
        for(int i=0;i<n;++i) t[n+i]=a[i];
        for(int i=n-1;i>0;--i) t[i]=t[i<<1]+t[i<<1|1];
    }
    void update(int pos, long long val){
        pos += n; t[pos]=val;
        for(pos >>=1; pos; pos>>=1) t[pos]=t[pos<<1]+t[pos<<1|1];
    }
    long long query(int l, int r){ // [l,r)
        long long res=0;
        for(l+=n, r+=n; l<r; l>>=1, r>>=1){
            if(l&1) res += t[l++];
            if(r&1) res += t[--r];
        }
        return res;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    SegTree st(n);
    st.build(a);
    int q; cin>>q;
    while(q--){
        int type; cin>>type;
        if(type==1){ int pos; long long val; cin>>pos>>val; st.update(pos,val); }
        else { int l,r; cin>>l>>r; cout<<st.query(l,r)<<"\n"; }
    }
    return 0;
}

Pruebas
? Build with [1,2,3,4,5], query(0,5)=15; update pos2 to 10, query(0,5)=22.