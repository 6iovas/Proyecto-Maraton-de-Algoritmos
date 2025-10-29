// Proyecto de Informatica
// Ejercicio 219
Ejercicio 14  KMP (Knuth-Morris-Pratt)  búsqueda de patrón con prefijo-función
Análisis del problema
 Implementar algoritmo KMP para encontrar todas las ocurrencias de un patrón P en texto T en O(|T|+|P|). Devolver índices de inicio (0-based).
? Importante: construir la prefix-function (pi) y usar para escanear T.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
vector<int> prefix_function(const string &s){
    int n=s.size();
    vector<int> pi(n);
    for(int i=1;i<n;++i){
        int j=pi[i-1];
        while(j>0 && s[i]!=s[j]) j=pi[j-1];
        if(s[i]==s[j]) ++j;
        pi[i]=j;
    }
    return pi;
}
vector<int> kmp(const string &t, const string &p){
    if(p.empty()) return {};
    vector<int> pi = prefix_function(p), res;
    int j=0;
    for(int i=0;i<(int)t.size();++i){
        while(j>0 && t[i]!=p[j]) j=pi[j-1];
        if(t[i]==p[j]) ++j;
        if(j==(int)p.size()){ res.push_back(i - j + 1); j = pi[j-1]; }
    }
    return res;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string T,P; if(!(cin>>T>>P)) return 0;
    auto occ = kmp(T,P);
    for(int i: occ) cout<<i<<" ";
    cout<<"\n";
    return 0;
}

Prueba
? T = "ababcababc", P = "ababc" ? ocurrencias en 0 y 5.