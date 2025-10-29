// Proyecto de Informatica
// Ejercicio 203
Ejercicio 199: Convert sorted array to balanced BST
Análisis
 Construir BST balanceado mínimo a partir de array ordenado.
Diseño
 Usar construcción recursiva mid -> root.
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ int v; Node* l; Node* r; Node(int x):v(x),l(nullptr),r(nullptr){} };
Node* build(vector<int>& a, int l, int r){
    if(l>r) return nullptr;
    int m = (l+r)/2;
    Node* root = new Node(a[m]);
    root->l = build(a, l, m-1);
    root->r = build(a, m+1, r);
    return root;
}
void inorder(Node* r){ if(!r) return; inorder(r->l); cout<<r->v<<" "; inorder(r->r); }
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n); for(int i=0;i<n;++i) cin>>a[i];
    Node* root = build(a,0,n-1);
    inorder(root); cout<<"\n";
}

Prueba
? a=[1,2,3,4,5] -> inorder prints sorted sequence.