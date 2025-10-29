// Proyecto de Informatica
// Ejercicio 177
Ejercicio 173: Implementar Segment Tree con Lazy Propagation (range add, range sum)
Análisis
 Range add and range sum queries.
Diseño
 Classic segment tree with lazy array.
Código
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Seg {
    int n; vector<ll> t, lazy;
    Seg(int n):n(n),t(4*n),lazy(4*n,0){}
    void apply(int p,int l,int r,ll val){ t[p]+=val*(r-l+1); lazy[p]+=val; }
    void push(int p,int l,int r){
        if(lazy[p]){
            int m=(l+r)/2;
            apply(p*2,l,m,lazy[p]); apply(p*2+1,m+1,r,lazy[p]); lazy[p]=0;
        }
    }
    void update(int p,int l,int r,int ql,int qr,ll v){
        if(ql>r||qr<l) return;
        if(ql<=l&&r<=qr){ apply(p,l,r,v); return; }
        push(p,l,r); int m=(l+r)/2;
        update(p*2,l,m,ql,qr,v); update(p*2+1,m+1,r,ql,qr,v);
        t[p]=t[p*2]+t[p*2+1];
    }
    ll query(int p,int l,int r,int ql,int qr){
        if(ql>r||qr<l) return 0;
        if(ql<=l&&r<=qr) return t[p];
        push(p,l,r); int m=(l+r)/2;
        return query(p*2,l,m,ql,qr)+query(p*2+1,m+1,r,ql,qr);
    }
};
int main(){
    int n; if(!(cin>>n)) return 0;
    Seg st(n);
    int q; cin>>q;
    while(q--){
        int t; cin>>t;
        if(t==1){ int l,r; long long v; cin>>l>>r>>v; st.update(1,0,n-1,l,r,v); }
        else { int l,r; cin>>l>>r; cout<<st.query(1,0,n-1,l,r)<<"\n"; }
    }
}

Prueba
? n=5, update(0,4,1), query(0,4)=5