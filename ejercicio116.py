// Proyecto de Informatica
// Ejercicio 116
Ejercicio 114: Uso de unique_ptr y shared_ptr (RAII, ownership)
Análisis del Problema
 Demostrar manejo de memoria con smart pointers; crear árbol simple con unique_ptr.
Diseño de la Solución
 unique_ptr para ownership exclusivo; shared_ptr para nodos con múltiples owners (ej. grafo simple).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    unique_ptr<Node> left;
    unique_ptr<Node> right;
    Node(int v): val(v) {}
};

int main(){
    auto root = make_unique<Node>(10);
    root->left = make_unique<Node>(5);
    root->right = make_unique<Node>(15);
    cout << root->left->val << ' ' << root->right->val << '\n';

    // shared_ptr example (multiple owners)
    auto a = make_shared<int>(42);
    auto b = a; // shared ownership
    cout << *a << ' ' << *b << '\n';
    cout << "use_count: " << a.use_count() << '\n';
    return 0;
}

Pruebas
? Imprime 5 15 y 42 42 y use_count: 2.