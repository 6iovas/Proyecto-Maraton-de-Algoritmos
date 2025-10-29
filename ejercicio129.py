// Proyecto de Informatica
// Ejercicio 129
Ejercicio 127: Persistent Segment Tree (concepto sencillo  point update persistent)
Análisis del Problema
 Permitir versiones del segment tree después de updates (cada update crea nueva raíz compartir nodos inmutables).
Diseño de la Solución
 Nodo con left/right pointers; update returns new root copying path.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
struct Node {
    int val;
    Node *l, *r;
    Node(int v=0): val(v), l(nullptr), r(nullptr) {}
};
Node* build(int tl, int tr){
    Node* node = new Node();
    if(tl==tr) return node;
    int tm=(tl+tr)/2;
    node->l = build(tl, tm);
    node->r = build(tm+1, tr);
    return node;
}
Node* update(Node* v, int tl, int tr, int pos, int val){
    Node* node = new Node();
    *node = *v; // copy
    if(tl==tr){ node->val = val; return node; }
    int tm=(tl+tr)/2;
    if(pos<=tm) node->l = update(v->l, tl, tm, pos, val);
    else node->r = update(v->r, tm+1, tr, pos, val);
    node->val = (node->l?node->l->val:0) + (node->r?node->r->val:0);
    return node;
}
int query(Node* v, int tl, int tr, int l, int r){
    if(!v || r<tl || tr<l) return 0;
    if(l<=tl && tr<=r) return v->val;
    int tm=(tl+tr)/2;
    return query(v->l, tl, tm, l, r) + query(v->r, tm+1, tr, l, r);
}

int main(){
    int n = 5; // example fixed
    auto root0 = build(0,n-1);
    auto root1 = update(root0,0,n-1,2,10); // version 1 set pos2=10
    cout << query(root0,0,n-1,0,4) << '\n'; // 0
    cout << query(root1,0,n-1,0,4) << '\n'; // 10
    return 0;
}

Pruebas
? Builds base root0, root1 updated; query differences show persistence.