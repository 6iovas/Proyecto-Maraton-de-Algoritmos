// Proyecto de Informatica
// Ejercicio 113
Ejercicio 111: Implementar un Trie (insert, search, startsWith) usando unordered_map
Análisis del Problema
 Construir una estructura Trie para almacenar palabras y permitir búsqueda exacta y prefijos.
Diseño de la Solución
 Nodo con unordered_map<char, Node*> y flag is_word. Operaciones: insert, search, startsWith.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> next;
    bool is_word = false;
};

struct Trie {
    TrieNode* root = new TrieNode();
    void insert(const string &s) {
        TrieNode* cur = root;
        for(char c : s) {
            if(!cur->next[c]) cur->next[c] = new TrieNode();
            cur = cur->next[c];
        }
        cur->is_word = true;
    }
    bool search(const string &s) {
        TrieNode* cur = root;
        for(char c : s) {
            if(!cur->next.count(c)) return false;
            cur = cur->next[c];
        }
        return cur->is_word;
    }
    bool startsWith(const string &p) {
        TrieNode* cur = root;
        for(char c : p) {
            if(!cur->next.count(c)) return false;
            cur = cur->next[c];
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Trie trie;
    trie.insert("hola");
    trie.insert("holanda");
    trie.insert("holi");
    cout << trie.search("hola") << '\n';      // 1
    cout << trie.search("hol") << '\n';       // 0
    cout << trie.startsWith("hol") << '\n';   // 1
    cout << trie.search("adios") << '\n';     // 0
    return 0;
}

Pruebas
? Inserta hola, holanda, holi. search("hola") -> 1, startsWith("hol") -> 1.