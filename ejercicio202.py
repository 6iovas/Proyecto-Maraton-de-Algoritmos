// Proyecto de Informatica
// Ejercicio 202
Ejercicio 198: Binary tree level order traversal (BFS)
Análisis
 Recorrer árbol por niveles y devolver listas por nivel.
Diseño
 Usar queue<Node*> y delimitar niveles por size.
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ int v; Node* l; Node* r; Node(int x):v(x),l(nullptr),r(nullptr){} };
int main(){
    Node* root = new Node(1);
    root->l = new Node(2); root->r = new Node(3);
    root->l->l = new Node(4); root->l->r = new Node(5);
    queue<Node*> q; q.push(root);
    while(!q.empty()){
        int sz = q.size();
        for(int i=0;i<sz;++i){
            Node* cur = q.front(); q.pop();
            cout<<cur->v<<" ";
            if(cur->l) q.push(cur->l);
            if(cur->r) q.push(cur->r);
        }
        cout<<"\n";
    }
}

Prueba
? Output levels: 1 then 2 3 then 4 5