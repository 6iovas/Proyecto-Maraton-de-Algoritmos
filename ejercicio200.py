// Proyecto de Informatica
// Ejercicio 200
Ejercicio 196: Lowest Common Ancestor in BST (iterative)
Análisis
 Encontrar LCA de dos nodos en BST.
Diseño
 Iterar desde root: si ambos < root->v go left; if both > go right; else root is LCA.
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ int v; Node* l; Node* r; Node(int x):v(x),l(nullptr),r(nullptr){} };
Node* lcaBST(Node* root, int a, int b){
    while(root){
        if(a < root->v && b < root->v) root = root->l;
        else if(a > root->v && b > root->v) root = root->r;
        else return root;
    }
    return nullptr;
}
int main(){
    Node* root = new Node(6);
    root->l = new Node(2); root->r = new Node(8);
    root->l->l = new Node(0); root->l->r = new Node(4);
    int a=0,b=4;
    Node* res = lcaBST(root,a,b);
    if(res) cout<<res->v<<"\n"; else cout<<"NO\n";
}

Prueba
? LCA(0,4) ? 2