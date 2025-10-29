// Proyecto de Informatica
// Ejercicio 180
Ejercicio 176: Rabin-Karp (búsqueda de patrón)
Análisis
 Buscar todas las ocurrencias de patrón P en texto T.
Diseño
 Rolling hash con base y modulo grande (uso ull to avoid modulo).
Código
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
vector<int> rabin_karp(const string &t,const string &p){
    int n=t.size(), m=p.size();
    if(m>n) return {};
    const ull B=1315423911ULL;
    ull hp=0, ht=0, powB=1;
    for(int i=0;i<m;++i){ hp = hp*B + (unsigned char)p[i]; ht = ht*B + (unsigned char)t[i]; if(i) powB *= B; }
    vector<int> res;
    if(hp==ht) res.push_back(0);
    for(int i=m;i<n;++i){
        ht = ht - powB*(unsigned char)t[i-m];
        ht = ht*B + (unsigned char)t[i];
        if(ht==hp) res.push_back(i-m+1);
    }
    return res;
}
int main(){ string t,p; if(!(cin>>t>>p)) return 0; auto r=rabin_karp(t,p); for(int i:r) cout<<i<<" "; cout<<"\n"; }

Prueba
? abracadabra y abra ? 0 7