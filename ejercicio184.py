// Proyecto de Informatica
// Ejercicio 184
Ejercicio 180: Longest Palindromic Substring (Manacher)
Análisis
 Encontrar palíndromo más largo en O(n).
Diseño
 Algoritmo de Manacher (implementación estándar).
Código
#include <bits/stdc++.h>
using namespace std;
string manacher(string s){
    string t = "@";
    for(char c:s){ t += '#'; t+=c; }
    t += "#$";
    int n=t.size();
    vector<int> p(n);
    int center=0, right=0;
    for(int i=1;i<n-1;++i){
        int mir = 2*center - i;
        if(i<right) p[i]=min(right-i, p[mir]);
        while(t[i+1+p[i]]==t[i-1-p[i]]) p[i]++;
        if(i+p[i]>right){ center=i; right=i+p[i]; }
    }
    int maxlen=0, centerIndex=0;
    for(int i=1;i<n-1;++i) if(p[i]>maxlen){ maxlen=p[i]; centerIndex=i; }
    int start = (centerIndex - maxlen -1)/2;
    return s.substr(start, maxlen);
}
int main(){ string s; if(!(cin>>s)) return 0; cout<<manacher(s)<<"\n"; }

Prueba
? babad ? bab or aba