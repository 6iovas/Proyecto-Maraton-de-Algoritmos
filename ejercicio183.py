// Proyecto de Informatica
// Ejercicio 183
Ejercicio 179: Minimal window substring (sliding window)
Análisis
 Dada string S y T, encontrar substring mínimo de S que contenga todas las letras de T (counts).
Diseño
 Sliding window con counts and formed counter.
Código
#include <bits/stdc++.h>
using namespace std;
string minWindow(string s, string t){
    vector<int> need(128,0);
    for(char c:t) need[c]++;
    int required = 0; for(int c=0;c<128;++c) if(need[c]>0) required++;
    vector<int> window(128,0);
    int formed=0, l=0, r=0, bestL=0, bestLen=INT_MAX;
    while(r<s.size()){
        char c=s[r++]; window[c]++;
        if(window[c]==need[c]) formed++;
        while(l<r && formed==required){
            if(r-l < bestLen){ bestLen=r-l; bestL=l; }
            char d=s[l++]; if(window[d]==need[d]) formed--; window[d]--;
        }
    }
    return bestLen==INT_MAX? string("") : s.substr(bestL,bestLen);
}
int main(){ string s,t; if(!(cin>>s>>t)) return 0; cout<<minWindow(s,t)<<"\n"; }

Prueba
? S=ADOBECODEBANC T=ABC ? output BANC