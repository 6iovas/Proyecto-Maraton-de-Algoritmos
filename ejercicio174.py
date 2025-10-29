// Proyecto de Informatica
// Ejercicio 174
Ejercicio 170: Implementar Trie con conteo de prefijos
Análisis
 Soportar insert y contar cuántas palabras tienen un prefijo dado.
Diseño
 Trie node con count de palabras en subárbol.
Código
#include <bits/stdc++.h>
using namespace std;
struct Node{ array<int,26> nxt; int cnt=0; Node(){ nxt.fill(-1); } };
int main(){
    vector<Node> trie(1);
    auto insert = [&](const string&s){
        int v=0; trie[v].cnt++;
        for(char ch:s){
            int c=ch-'a';
            if(trie[v].nxt[c]==-1){ trie[v].nxt[c]=trie.size(); trie.emplace_back(); }
            v=trie[v].nxt[c]; trie[v].cnt++;
        }
    };
    auto prefcnt = [&](const string&p){
        int v=0;
        for(char ch:p){ int c=ch-'a'; if(trie[v].nxt[c]==-1) return 0; v=trie[v].nxt[c]; }
        return trie[v].cnt;
    };
    insert("hello"); insert("hell"); insert("he");
    cout<<prefcnt("he")<<"\n"; // 3
}

Prueba
? prefcnt("he") ? 3