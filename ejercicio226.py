// Proyecto de Informatica
// Ejercicio 226
Ejercicio 20  Convex Hull Trick (CHT)  line container for min queries (Li Chao or deque trick)
Análisis del problema
 Implementar una estructura para mantener un conjunto dinámico de líneas y = m*x + b y responder consultas min y en valores x (offline x-queries or monotonic x). Dos implementaciones comunes: Li Chao tree (arbitrary x) o deque trick (if slopes monotonic). Aquí implementaremos Li Chao tree (segment tree over x-range) para soportar additions of lines and queries in O(log X) where X is coordinate range.
Diseño de la solución
? Discretizar rango de x (por ejemplo, [Xmin, Xmax]) y construir Li Chao segment tree storing best line in node.

? Each node store line best on that segment, swap/propagate as needed.

? Add line in O(log range), query point in O(log range).

Código (C++) (Li Chao over integer x in [XLo,XHi])
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Line { ll m, b; Line(ll _m=0, ll _b= (1LL<<60)) : m(_m), b(_b) {} ll eval(ll x) const { return m*x + b; } };
struct LiChao {
    struct Node { Line ln; Node *l=nullptr, *r=nullptr; Node(Line v=Line()):ln(v){} };
    Node* root = nullptr;
    ll L, R;
    LiChao(ll L, ll R): L(L), R(R), root(nullptr) {}
    void add_line(Line nw){ insert(root, L, R, nw); }
    void insert(Node*& node, ll l, ll r, Line nw){
        if(!node){ node = new Node(nw); return; }
        ll mid = (l + r) >> 1;
        bool left = nw.eval(l) < node->ln.eval(l);
        bool m = nw.eval(mid) < node->ln.eval(mid);
        if(m){ swap(nw, node->ln); }
        if(r==l) return;
        if(left != m) insert(node->l, l, mid, nw);
        else insert(node->r, mid+1, r, nw);
    }
    ll query(ll x){ return queryRec(root, L, R, x); }
    ll queryRec(Node* node, ll l, ll r, ll x){
        if(!node) return (1LL<<60);
        ll res = node->ln.eval(x);
        if(l==r) return res;
        ll mid = (l+r)>>1;
        if(x<=mid) return min(res, queryRec(node->l, l, mid, x));
        else return min(res, queryRec(node->r, mid+1, r, x));
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Example usage:
    // insert lines and query points (x in [0,1e6] for example)
    int q; if(!(cin>>q)) return 0;
    const ll XMIN = 0, XMAX = 1000000;
    LiChao lc(XMIN, XMAX);
    while(q--){
        int type; cin>>type;
        if(type==1){
            long long m,b; cin>>m>>b;
            lc.add_line(Line(m,b));
        } else {
            long long x; cin>>x;
            cout<<lc.query(x)<<"\n";
        }
    }
    return 0;
}

Prueba
? Add lines y query points; Li Chao will return minimal y among inserted lines for x.