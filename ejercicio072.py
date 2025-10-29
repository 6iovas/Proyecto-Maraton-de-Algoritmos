// Proyecto de Informatica
// Ejercicio 72
Ejercicio 70: Word Ladder (transformación de palabras)  BFS en palabras
Análisis
 Encontrar mínimo pasos para transformar begin en end cambiando una letra y usando palabras del diccionario.
Diseño
 BFS: precompute adjacency via wildcard patterns or generate neighbors.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string beginWord, endWord; int n;
    if(!(cin>>beginWord>>endWord>>n)) return 0;
    vector<string> dict(n);
    unordered_set<string> wordSet;
    for(int i=0;i<n;++i){ cin>>dict[i]; wordSet.insert(dict[i]); }
    if(!wordSet.count(endWord)){ cout<<0<<"\n"; return 0; }
    queue<pair<string,int>> q; q.push({beginWord,1});
    unordered_set<string> vis; vis.insert(beginWord);
    while(!q.empty()){
        auto [word,steps] = q.front(); q.pop();
        if(word==endWord){ cout<<steps<<"\n"; return 0; }
        for(int i=0;i<(int)word.size();++i){
            string tmp = word;
            for(char c='a'; c<='z'; ++c){
                tmp[i]=c;
                if(wordSet.count(tmp) && !vis.count(tmp)){ vis.insert(tmp); q.push({tmp,steps+1}); }
            }
        }
    }
    cout<<0<<"\n";
    return 0;
}

Pruebas
? hit -> cog with dict includes hot dot dog lot log cog ? shortest length 5 (hit->hot->dot->dog->cog).
71. Mergesort