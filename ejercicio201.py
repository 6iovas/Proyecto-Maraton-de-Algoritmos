// Proyecto de Informatica
// Ejercicio 201
Ejercicio 197: Serialize / Deserialize binary tree (preorder with nulls)
Análisis
 Convertir árbol a string y reconstruirlo.
Diseño
 Preorder traversal, use # for nulls, separar con comas.
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ int v; Node* l; Node* r; Node(int x):v(x),l(nullptr),r(nullptr){} };
void serialize(Node* root, ostream &out){
    if(!root){ out << "#,"; return; }
    out << root->v << ",";
    serialize(root->l, out);
    serialize(root->r, out);
}
Node* deserialize(istringstream &in){
    string token;
    if(!getline(in, token, ',')) return nullptr;
    if(token=="#") return nullptr;
    Node* node = new Node(stoi(token));
    node->l = deserialize(in);
    node->r = deserialize(in);
    return node;
}
int main(){
    Node* root = new Node(1);
    root->l = new Node(2); root->r = new Node(3);
    root->r->l = new Node(4); root->r->r = new Node(5);
    ostringstream out;
    serialize(root, out);
    string s = out.str();
    cout << "Serialized: " << s << "\n";
    istringstream in(s);
    Node* root2 = deserialize(in);
    // Serialize again to verify
    ostringstream out2; serialize(root2, out2);
    cout << "Re-serialized: " << out2.str() << "\n";
}

Prueba
? Check serialized equals re-serialized.