// Proyecto de Informatica
// Ejercicio 131
Ejercicio 129: Rolling Hash (Rabin-Karp) para búsqueda de patrón
Análisis del Problema
 Encontrar ocurrencias de un patrón P en texto T eficientemente.
Diseño de la Solución
 Usar base B y modulo grande MOD, calcular hash de ventanas.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

vector<int> rabin_karp(const string &t, const string &p){
    int n=t.size(), m=p.size();
    if(m>n) return {};
    const ull B = 1315423911ULL; // use ull rolling (no modulo) or choose prime
    ull hp=0, ht=0, powB=1;
    for(int i=0;i<m;++i){ hp = hp*B + (unsigned char)p[i]; ht = ht*B + (unsigned char)t[i]; if(i) powB *= B; }
    vector<int> res;
    if(hp==ht) res.push_back(0);
    for(int i=m;i<n;++i){
        ht = ht - powB * (unsigned char)t[i-m];
        ht = ht*B + (unsigned char)t[i];
        if(ht==hp) res.push_back(i-m+1);
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string t,p; if(!(cin>>t>>p)) return 0;
    auto occ = rabin_karp(t,p);
    for(int i: occ) cout << i << ' ';
    cout << '\n';
    return 0;
}

Pruebas
? t="abracadabra", p="abra" -> positions 0 and 7.