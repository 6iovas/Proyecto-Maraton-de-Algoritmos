// Proyecto de Informatica
// Ejercicio 199
Ejercicio 195: Check if binary tree is BST (inorder traversal)
Análisis
 Verificar si un árbol binario es árbol de búsqueda válido.
Diseño
 Inorder traversal must be strictly increasing (or non-decreasing depends; here strict).
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ int v; Node* l; Node* r; Node(int x):v(x),l(nullptr),r(nullptr){} };
bool isBST(Node* root, long long minv=LLONG_MIN, long long maxv=LLONG_MAX){
    if(!root) return true;
    if(root->v <= minv || root->v >= maxv) return false;
    return isBST(root->l, minv, root->v) && isBST(root->r, root->v, maxv);
}
// Example building and test in main:
int main(){
    // Example: build simple tree: 2 / \ 1 3
    Node* root = new Node(2);
    root->l = new Node(1);
    root->r = new Node(3);
    cout << (isBST(root) ? "YES\n" : "NO\n");
    return 0;
}

Prueba
? Tree above ? YES; if right child 0 ? NO.