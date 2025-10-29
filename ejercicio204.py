// Proyecto de Informatica
// Ejercicio 204
Ejercicio 200: Check if two binary trees are isomorphic (structure + values)
Análisis
 Determinar si dos árboles son idénticos (misma estructura y valores).
Diseño
 Recursión: check roots equal and left subtrees equal and right equal.
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ int v; Node* l; Node* r; Node(int x):v(x),l(nullptr),r(nullptr){} };
bool sameTree(Node* a, Node* b){
    if(!a && !b) return true;
    if(!a || !b) return false;
    if(a->v != b->v) return false;
    return sameTree(a->l, b->l) && sameTree(a->r, b->r);
}
int main(){
    Node* a = new Node(1); a->l = new Node(2); a->r = new Node(3);
    Node* b = new Node(1); b->l = new Node(2); b->r = new Node(3);
    cout << (sameTree(a,b) ? "SAME\n" : "DIFFERENT\n");
    b->r->v = 4;
    cout << (sameTree(a,b) ? "SAME\n" : "DIFFERENT\n");
}

Prueba
? Initially SAME; after change DIFFERENT.

Prueba
? For small complete graphs, produces a tour (not optimal but quick).