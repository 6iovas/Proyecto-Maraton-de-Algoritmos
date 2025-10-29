// Proyecto de Informatica
// Ejercicio 178
Ejercicio 174: Construcción de suffix array (esqueleto O(n log n))
Análisis
 Construir SA para string dado.
Diseño
 Doubling algorithm.
Código (esqueleto, funcional)
#include <bits/stdc++.h>
using namespace std;
vector<int> build_sa(const string &s){
    int n=s.size(), k=1;
    vector<int> sa(n), r(n), tmp(n);
    for(int i=0;i<n;++i){ sa[i]=i; r[i]=s[i]; }
    auto cmp=[&](int a,int b){
        if(r[a]!=r[b]) return r[a]<r[b];
        int ra = a+k<n? r[a+k]: -1;
        int rb = b+k<n? r[b+k]: -1;
        return ra<rb;
    };
    for(k=1;;k<<=1){
        sort(sa.begin(), sa.end(), cmp);
        tmp[sa[0]]=0;
        for(int i=1;i<n;++i) tmp[sa[i]] = tmp[sa[i-1]] + cmp(sa[i-1], sa[i]);
        for(int i=0;i<n;++i) r[i]=tmp[i];
        if(r[sa[n-1]]==n-1) break;
    }
    return sa;
}
int main(){
    string s; if(!(cin>>s)) return 0;
    auto sa = build_sa(s);
    for(int i:sa) cout<<i<<" ";
    cout<<"\n";
}

Prueba
? banana ? SA e.g. 5 3 1 0 4 2 (one valid ordering)