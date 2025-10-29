// Proyecto de Informatica
// Ejercicio 278
Ejercicio 45  Persistent Segment Tree (point update, range sum queries on any version)
Análisis
 Implementar persistent segtree supporting update(version, pos, val) returning new version and query(version, l, r). Useful for persistent arrays, offline queries, kth order statistics, etc.
Diseño
? Node stores sum and pointers l, r. Update builds new path copying nodes O(log n). Query uses version roots.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Node {
    ll sum; Node *l,*r;
    Node(ll s=0, Node*L=nullptr, Node*R=nullptr):sum(s),l(L),r(R){}
};
int N;
Node* build(int tl,int tr){
    if(tl==tr) return new Node(0);
    int tm=(tl+tr)>>1;
    return new Node(0, build(tl,tm), build(tm+1,tr));
}
Node* update(Node* v, int tl,int tr,int pos, ll val){
    if(tl==tr) return new Node(val);
    int tm=(tl+tr)>>1;
    if(pos<=tm) return new Node(v->sum - v->l->sum + val + v->r->sum, update(v->l, tl, tm, pos, val), v->r);
    else return new Node(v->sum - v->r->sum + val + v->l->sum, v->l, update(v->r, tm+1, tr, pos, val));
}
ll query(Node* v,int tl,int tr,int l,int r){
    if(l>r) return 0;
    if(l==tl && r==tr) return v->sum;
    int tm=(tl+tr)>>1;
    return query(v->l,tl,tm,l,min(r,tm)) + query(v->r,tm+1,tr,max(l,tm+1),r);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,q; if(!(cin>>n>>q)) return 0;
    N=n;
    vector<Node*> roots;
    roots.push_back(build(0,N-1));
    while(q--){
        int type; cin>>type;
        if(type==1){
            int ver,pos; long long val; cin>>ver>>pos>>val;
            Node* newroot = update(roots[ver], 0, N-1, pos, val);
            roots.push_back(newroot);
            cout<<"Version "<<roots.size()-1<<"\n";
        } else {
            int ver,l,r; cin>>ver>>l>>r;
            cout<<query(roots[ver], 0, N-1, l, r)<<"\n";
        }
    }
    return 0;
}

Pruebas
? Build initial zeros; update version 0 pos 2 = 5 -> version1; query version1 [0,3] => 5; query version0 [0,3] => 0.