// Proyecto de Informatica
// Ejercicio 127
Ejercicio 125: Skip List  idea y plantilla básica (conceptual)
Análisis del Problema
 Estructura probabilística similar a un balanced BST para operaciones O(log n) promedio.
Diseño de la Solución
 Proveer plantilla esquemática con nivel aleatorio; implementar insert, find, erase (versión minimal).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

// Minimal illustrative skip-list node (not production-grade)
struct Node {
    int val;
    vector<Node*> next;
    Node(int v, int lvl): val(v), next(lvl, nullptr) {}
};

struct SkipList {
    Node* head;
    int maxLevel;
    double p; // probability
    SkipList(int maxL=16, double prob=0.5): maxLevel(maxL), p(prob) {
        head = new Node(INT_MIN, maxLevel);
    }
    int randomLevel(){
        int lvl=1;
        while(((double)rand()/RAND_MAX) < p && lvl < maxLevel) lvl++;
        return lvl;
    }
    bool find(int x){
        Node* cur = head;
        for(int i=maxLevel-1;i>=0;--i){
            while(cur->next[i] && cur->next[i]->val < x) cur = cur->next[i];
        }
        cur = cur->next[0];
        return cur && cur->val == x;
    }
    void insert(int x){
        vector<Node*> update(maxLevel, nullptr);
        Node* cur = head;
        for(int i=maxLevel-1;i>=0;--i){
            while(cur->next[i] && cur->next[i]->val < x) cur = cur->next[i];
            update[i] = cur;
        }
        int lvl = randomLevel();
        Node* node = new Node(x, lvl);
        for(int i=0;i<lvl;++i){
            node->next[i] = update[i]->next[i];
            update[i]->next[i] = node;
        }
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    SkipList sl;
    sl.insert(10);
    sl.insert(20);
    sl.insert(15);
    cout << sl.find(15) << ' ' << sl.find(7) << '\n';
    return 0;
}

Pruebas
? Inserta 10,20,15 -> find(15)=1, find(7)=0.