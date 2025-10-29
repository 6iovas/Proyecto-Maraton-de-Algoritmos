// Proyecto de Informatica
// Ejercicio 179
Ejercicio 175: Longest Common Prefix (LCP) array (Kasai)
Análisis
 Calcular LCP entre suffixes adyacentes en SA.
Diseño
 Algoritmo Kasai en O(n).
Código
#include <bits/stdc++.h>
using namespace std;
vector<int> build_sa(const string &s); // assume implemented (as above)
vector<int> build_lcp(const string &s, const vector<int>& sa){
    int n=s.size();
    vector<int> rank(n);
    for(int i=0;i<n;++i) rank[sa[i]]=i;
    vector<int> lcp(max(0,n-1));
    int h=0;
    for(int i=0;i<n;++i){
        if(rank[i]==0) continue;
        int j = sa[rank[i]-1];
        while(i+h<n && j+h<n && s[i+h]==s[j+h]) ++h;
        lcp[rank[i]-1]=h;
        if(h>0) --h;
    }
    return lcp;
}
int main(){
    string s; if(!(cin>>s)) return 0;
    auto sa = build_sa(s);
    auto lcp = build_lcp(s, sa);
    for(int v: lcp) cout<<v<<" ";
    cout<<"\n";
}

Prueba
? banana ? LCP array e.g. 1 3 0 0 2