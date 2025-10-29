// Proyecto de Informatica
// Ejercicio 132
Ejercicio 130: Construcción de DFA mínimo a partir de un conjunto de patrones (Aho-Corasick skeleton + minimize idea)
Análisis del Problema
 Construir automata para múltiples patrones y buscar todas las ocurrencias en texto (Aho-Corasick). Minimización de DFA es más complejo; aquí implementamos Aho-Corasick.
Diseño de la Solución
 Trie + failure links + output lists.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Aho {
    struct Node {
        array<int,26> next;
        int link = -1;
        vector<int> out;
        Node(){ next.fill(-1); }
    };
    vector<Node> trie;
    Aho(){ trie.emplace_back(); }
    void add(const string &s, int id){
        int v = 0;
        for(char ch: s){
            int c = ch - 'a';
            if(trie[v].next[c] == -1){ trie[v].next[c] = trie.size(); trie.emplace_back(); }
            v = trie[v].next[c];
        }
        trie[v].out.push_back(id);
    }
    void build(){
        queue<int> q;
        trie[0].link = 0;
        for(int c=0;c<26;++c){
            int v = trie[0].next[c];
            if(v != -1){ trie[v].link = 0; q.push(v); }
            else trie[0].next[c] = 0;
        }
        while(!q.empty()){
            int v=q.front(); q.pop();
            for(int c=0;c<26;++c){
                int u = trie[v].next[c];
                if(u != -1){
                    trie[u].link = trie[trie[v].link].next[c];
                    for(int x: trie[trie[u].link].out) trie[u].out.push_back(x);
                    q.push(u);
                } else {
                    trie[v].next[c] = trie[trie[v].link].next[c];
                }
            }
        }
    }
    vector<vector<int>> searchAll(const string &t){
        vector<vector<int>> res;
        int v=0;
        for(int i=0;i<(int)t.size();++i){
            int c = t[i]-'a';
            v = trie[v].next[c];
            if(!trie[v].out.empty()){
                for(int id: trie[v].out) res.push_back({id, i});
            }
        }
        return res;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k; if(!(cin>>k)) return 0;
    Aho aho;
    for(int i=0;i<k;++i){ string s; cin>>s; aho.add(s,i); }
    aho.build();
    string text; cin>>text;
    auto occ = aho.searchAll(text);
    for(auto &v: occ) cout << "pattern_id=" << v[0] << " pos=" << v[1] << '\n';
    return 0;
}

Pruebas
? patterns he she his hers, text ushers should show matches accordingly (indexing and positions as implemented).